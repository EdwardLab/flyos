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
from datetime import datetime
import random
import shutil

def restore_config():
    try:
        import config
        config.server_port
        config.hostname
        config.boot_app
    except:
        config_path = '/flyos/config.py'
        backup_path = '/flyos/files/backup/config.py'
        shutil.copy(backup_path, config_path)
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
command_thread = None
app.config['LANGUAGES'] = {
    'en': 'English',
    'zh-cn': 'Chinese'
}
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
# load user config
from config import *
PASSWORDS_FILE = "/flyos/files/pwd.conf"

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

# Required user_loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Function to check the password
def check_password(password):
    with open(PASSWORDS_FILE, "r") as file:
        stored_password_hash = file.read().strip()
        if check_password_hash(stored_password_hash, password):
            return True
    return False

@app.route('/')
@login_required
def redirectmain():
    return redirect(url_for('panel'))

@app.route('/dashboard')
@login_required
def panel():
    current_date = datetime.now()
    formatted_date = current_date.strftime('%b %d %Y %H:%M')
    battery_remaining = battery_status()
    desktop_opt = request.args.get('desktop_mode')
    ip_addr = get_local_ip()
    if desktop_opt == "true":
        desktop_mode = ''
    else:
        desktop_mode = '<meta name="viewport" content="width=device-width, initial-scale=1">'
    
    if check_country() == 'false':
        offline_notice = 'Offline mode'
    else:
        offline_notice = ''
    return render_template('./panel.html',
    desktop_mode=desktop_mode, 
    offline_notice=offline_notice, 
    run_system=run_system, 
    formatted_date=formatted_date,
    battery_remaining=battery_remaining,
    ip_addr=ip_addr)

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

    return render_template('./overview.html', notice=notice, storage=storage, ssh=ssh, vnc=vnc, kernel=kernel, framework_status=framework_status, run_system=run_system, battery_remaining=battery_remaining, not_available=not_available)
@app.route('/dashboard/vnc/view')
@login_required
def vnc_page():
    
    vnc = check_vnc_process()
    if vnc == 'Stopped':
        return 'VNC Service not started'
    hostname = request.host.split(':')[0]
    return redirect(f'http://{hostname}:{vnc_port}/vnc.html')
@app.route('/dashboard/codeserver/view')
@login_required
def codeserver_page():
    
    code = check_codeserver_process()
    if code == 'Stopped':
        return 'Code Server Service not started'
    hostname = request.host.split(':')[0]
    return redirect(f'http://{hostname}:{code_server_port}/')
@app.route('/dashboard/terminal/view')
@login_required
def terminal_android_page():
    
    ttyd = check_ttyd_process()
    if ttyd == 'Stopped':
        return 'Web Terminal Service not started'
    hostname = request.host.split(':')[0]
    return redirect(f'http://{hostname}:{terminal_port}/')
@app.route('/dashboard/terminal_android/view')
@login_required
def terminal_page():
    
    ttyd = check_ttyd_process()
    if ttyd == 'Stopped':
        return 'Web Terminal Service not started'
    hostname = request.host.split(':')[0]
    return redirect(f'http://{hostname}:{android_terminal_port}/')
@app.route('/dashboard/androidmgr/view')
@login_required
def android_mgr():
    
    hostname = request.host.split(':')[0]
    return render_template('androidmgr.html')
@app.route('/dashboard/notebook/view')
@login_required
def jupyter_notebook():
    
    hostname = request.host.split(':')[0]
    return redirect(f'http://{hostname}:{jupyter_notebook_port}/')
@app.route('/dashboard/about')
@login_required
def about():
    return render_template('about.html', run_system=run_system)
@app.route('/dashboard/settings', methods=['GET', 'POST'])
@login_required
def settings_view():
    if request.method == 'POST':
        newconf = request.form.get('conf')
        configfile_write = open('/flyos/config.py', 'w')
        configfile_write.write(newconf)
        return '''
<script>
    alert('Saved! Please re-login')
</script>
<meta http-equiv="refresh" content="0;url=/dashboard/settings"> 
        '''
    configfile_read = open('/flyos/config.py')
    configfile_read = configfile_read.read()
    return render_template('settings.html', run_system=run_system, configfile_read=configfile_read)
@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if log_message:
            current_time = datetime.now()
            formatted_time = current_time.strftime("%b %d %H:%M")
            alert_command = f'adb shell "su -lp 2000 -c \\"cmd notification post -S bigtext -t \'FlyOS Login Security Alert\' \'{random.randint(10000, 100000)}\' \'A device has successfully logged into the FlyOS dashboard at {formatted_time}, if you are not operating, please change the password (If you want to disable this notification, you can modify the configuration file: /flyos/config.py)\'\\""'
            os.system(alert_command)
        password = request.form.get('password')
        if password == '':
            return render_template('./oops.html', info='Incorrect password')
        if check_password(password):
            user_id = 1  # You can set any user ID or use a more complex logic here
            user = User(user_id)
            login_user(user)
            return redirect(url_for('panel'))
        else:
            return render_template('./oops.html', info='Incorrect password')
    return render_template('./login.html')
@app.route('/dashboard/settings/updatepwd', methods=['POST'])
@login_required
def settings_updatepwd_view():
    if request.method == 'POST':
        passwd = request.form.get('passwd')
        hashpwd = generate_password_hash(passwd)
        file_path = '/flyos/files/pwd.conf'
        try:
            os.remove(file_path)
        except:
            pass
        try:
            with open(file_path, 'w') as pwd_file:
                pwd_file.write(hashpwd)
            return render_template('info.html', info='Password changed!')
        except Exception as e:
            return render_template('info.html', info=f'system error: {e}, please try again')
@app.route('/auth/login/otplogin', methods=['GET', 'POST'])
def otpcode_login():
    if request.method == 'POST':
        getcode = request.form.get('password')
        read_otp = open('/flyos/files/temp/otp', 'r')
        read_otp = read_otp.read()    
        if getcode == read_otp:
            user_id = 1
            user = User(user_id)
            login_user(user)
            return redirect(url_for('panel'))
        else:
            return render_template('./oops.html', info='Incorrect one-time password, Please regenerate and try again')
    else:
        otp_code = random.randint(10000, 100000)
        save_otp = open('/flyos/files/temp/otp', 'w')
        save_otp.write(str(otp_code))
        send_android_msg('FlyOS Login OTP', f'Your one-time login password is: {otp_code}, valid for this page session', 5000)
        return render_template('otplogin.html')
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
if __name__ == '__main__':
    restore_config()
    app.run(host=dashboard_host_addr, port=server_port, debug=True)