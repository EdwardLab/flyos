# The FlyOS Project by: DigitalPlat Team(Edward Hsing)
# main.py Created by: Edward Hsing(xingyujie50@gmail.com)
from flask import Flask, render_template, request, redirect, url_for, session, make_response, Response
from flask_login import LoginManager, current_user, login_required, UserMixin, login_user, logout_user
from urllib.parse import urlparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_babel import Babel, gettext, ngettext, pgettext, lazy_gettext
from tools import *
from datetime import timedelta
import os
import subprocess
import sqlite3
import requests
from config import *
os.system('hostname ' + hostname)
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id
        self.username = ""

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=5)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
# SQLite database file path
db_path = '/flyos/flyos.db'
command_thread = None
app.config['LANGUAGES'] = {
    'en': 'English',
    'zh-cn': 'Chinese'
}
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
# load user config
from config import *
@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM user WHERE user_id = ?;", (user_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row is not None:
        user = User(user_id)
        user.username = row[0]
        return user
    else:
        return None

def checkuser(username, password):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, password FROM user WHERE username = ?;", (username,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row is not None:
        user_id, getpassword = row
        if check_password_hash(getpassword, password):
            return user_id
    return None

def userload():
    username = session.get('username')
    if username is None:
        return redirect(url_for('login'))
    return username

@app.route('/')
@login_required
def redirectmain():
    return redirect(url_for('domainpanel'))

@app.route('/dashboard')
@login_required
def domainpanel():
    username = userload()
    desktop_opt = request.args.get('desktop_mode')
    if desktop_opt == "true":
        desktop_mode = ''
    else:
        desktop_mode = '<meta name="viewport" content="width=device-width, initial-scale=1">'
    
    if check_country() == 'false':
        offline_notice = 'Offline mode'
    else:
        offline_notice = ''
    return render_template('./panel.html', username=username, desktop_mode=desktop_mode, offline_notice=offline_notice)

@app.route('/query_files', methods=['POST'])
@login_required
def query_files():
    try:
        path = request.json['path']
        result = subprocess.check_output(f'ls {path}', shell=True).decode()
        return result
    except:
        return 'No such file or directory'
@app.route('/dashboard/home/view')
@login_required
def overview():
    battery_remaining = battery_status()
    username = userload()
    try:
        url = "https://raw.githubusercontent.com/xingyujie/flyos/master/notices.txt"
        response = requests.get(url)
        notice = response.text
    except:
        notice = 'Failed to load notice: No network connection or System Error'
    storage = get_device_storage()
    ssh = check_ssh_process()
    vnc = check_vnc_process()
    kernel = get_kernel_version()
    framework_status = flyos_framework_status()
    if framework_status:
        framework_status =  'Running'
    else:
        framework_status = 'Stopped'

    try:
        if check_country() == 'false':
            not_available = '''
<div class="alert alert-danger" role="alert">
    WARNING! FlyOS Cloud service is currently not available in your country or region. As a result, offline mode will be enabled, which means you will not have access to system updates, networking services, or FlyOS framework services, etc.<br>
    However, FlyOS is an open source software distributed under the GPL-3.0 LICENSE. This means you are free to use, modify, and distribute the software according to the terms of the license.<br>
    Please note that the availability of FlyOS Cloud service and offline mode may vary based on your location and future updates. For the most accurate and up-to-date information, refer to our official documentation or contact our support team.<br>
</div>
            '''
        else:
            not_available = ''
    except Exception as e:
        print("Exception in overview:", str(e))
        not_available = ''

    return render_template('./overview.html', username=username, notice=notice, storage=storage, ssh=ssh, vnc=vnc, kernel=kernel, framework_status=framework_status, run_system=run_system, battery_remaining=battery_remaining, not_available=not_available)
@app.route('/dashboard/vnc/view')
@login_required
def vnc_page():
    username = userload()
    vnc = check_vnc_process()
    if vnc == 'Stopped':
        return 'VNC Service not started'
    hostname = request.host.split(':')[0]
    return redirect(f'http://{hostname}:{vnc_port}/vnc.html')
@app.route('/dashboard/codeserver/view')
@login_required
def codeserver_page():
    username = userload()
    code = check_codeserver_process()
    if code == 'Stopped':
        return 'Code Server Service not started'
    hostname = request.host.split(':')[0]
    return redirect(f'http://{hostname}:{code_server_port}/')
@app.route('/dashboard/terminal/view')
@login_required
def terminal_android_page():
    username = userload()
    ttyd = check_ttyd_process()
    if ttyd == 'Stopped':
        return 'Web Terminal Service not started'
    hostname = request.host.split(':')[0]
    return redirect(f'http://{hostname}:{terminal_port}/')
@app.route('/dashboard/terminal_android/view')
@login_required
def terminal_page():
    username = userload()
    ttyd = check_ttyd_process()
    if ttyd == 'Stopped':
        return 'Web Terminal Service not started'
    hostname = request.host.split(':')[0]
    return redirect(f'http://{hostname}:{android_terminal_port}/')
@app.route('/dashboard/androidmgr/view')
@login_required
def android_mgr():
    username = userload()
    hostname = request.host.split(':')[0]
    return render_template('androidmgr.html')
@app.route('/dashboard/notebook/view')
@login_required
def jupyter_notebook():
    username = userload()
    hostname = request.host.split(':')[0]
    return redirect(f'http://{hostname}:{jupyter_notebook_port}/')
@app.route('/dashboard/about')
@login_required
def about():
    username = userload()
    hostname = request.host.split(':')[0]
    return render_template('about.html')
@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == '':
            return render_template('./oops.html', info='Incorrect username or password')
        if password == '':
            return render_template('./oops.html', info='Incorrect username or password')
        user_id = checkuser(username, password)
        if user_id is not None:
            user = User(user_id)
            user.username = username
            login_user(user)
            session['username'] = username  # Store username in session
            return redirect(url_for('domainpanel'))
        else:
            return render_template('./oops.html', info='Incorrect username or password')
    return render_template('./login.html')
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=server_port, debug=True)