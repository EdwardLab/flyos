# The FlyOS Project by: DigitalPlat Team(Edward Hsing)
# main.py Created by: Edward Hsing(xingyujie50@gmail.com)
from flask import Flask, render_template, request, redirect, url_for, session, make_response, Response, jsonify
from flask_login import LoginManager, current_user, login_required, UserMixin, login_user, logout_user
from urllib.parse import urlparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_babel import Babel, gettext, ngettext, pgettext, lazy_gettext
from tools import *
from datetime import timedelta
import secrets
import string
import os
import subprocess
import sqlite3
import requests
from config import *
from datetime import datetime
import random
import shutil
from flask_login.config import USE_SESSION_FOR_NEXT
def get_locale():
    cookie = request.cookies.get('locale')
    if cookie in ['en', 'es', 'zh']:
        return cookie
    return request.accept_languages.best_match(['en', 'es', 'zh'])
def restore_config():
    try:
        import config
        config.server_port
        config.hostname
        config.boot_ssh
        config.boot_vnc
        config.boot_dashboard
        config.boot_code_server
        config.log_message
        config.show_motd
    except:
        config_path = '/flyos/config.py'
        backup_path = '/flyos/files/backup/config.py'
        shutil.copy(backup_path, config_path)
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id
        self.username = ""

app = Flask(__name__)
babel = Babel(app)
app.secret_key = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=5)
app.config['USE_SESSION_FOR_NEXT'] = True
babel.init_app(app, locale_selector=get_locale)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

command_thread = None
app.config['LANGUAGES'] = {
    'en': 'English',
    'es': 'Spanish',
    'zh': 'Chinese'
}
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = '/flyos/translations'

@app.route('/change_language/<language>', methods=['GET'])
def change_language(language):
    if language in ['en', 'es', 'zh']: 
        response = make_response("Language set to: " + language)
        response.set_cookie('locale', language)
        return response
    else:
        return "Invalid language code"
no_pwd_login_alert_command = f'adb shell "su -lp 2000 -c \\"cmd notification post -S bigtext -t \'FlyOS Login Security Alert\' \'{random.randint(10000, 100000)}\' \'A device logged into the dashboard using the no_pwd_login flag. The device has disabled protection. For security, please disable this flag.\'\\""'
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

@app.route('/language/<lang_code>')
def set_language(lang_code):
    session['lang'] = lang_code
    return redirect(request.referrer or url_for('panel'))

@app.route('/')
def redirectmain():
    if setup_check() == False:
        return redirect(url_for('setup_default_login'))
    if no_pwd_login == True:
        user_id = 1
        user = User(user_id)
        login_user(user)
        
        os.system(no_pwd_login_alert_command)
        return redirect(url_for('panel'))
    return redirect(url_for('panel'))

@app.route('/dashboard')
@login_required
def panel():
    if setup_check() == False:
        return redirect(url_for('setup_default_login'))
    current_date = datetime.now()
    formatted_date = current_date.strftime('%b %d %Y %H:%M')
    battery_remaining = battery_status()
    desktop_opt = request.args.get('desktop_mode')
    ip_addr = get_local_ip()
    if desktop_opt == "true":
        desktop_mode = ''
    else:
        desktop_mode = '<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">'
    
    if check_country() == 'false':
        offline_notice = 'Offline mode'
    else:
        offline_notice = ''
    hostname = request.host.split(':')[0]
    return render_template('./panel.html',
    desktop_mode=desktop_mode, 
    offline_notice=offline_notice, 
    run_system=run_system, 
    formatted_date=formatted_date,
    battery_remaining=battery_remaining,
    ip_addr=ip_addr,
    hostname=hostname,
    terminal_port=terminal_port,
    dashboard_menu_timeout=dashboard_menu_timeout
    )

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

@app.route('/dashboard/androidmgr/usb_tethering')
@login_required
def androidmgr_usb_tethering():
    return render_template('./manager/usb_tethering.html')

@app.route('/dashboard/androidmgr/usb_tethering/launch')
@login_required
def androidmgr_usb_tethering_launch():
    results = os.popen('adb shell svc usb setFunctions rndis').read()
    return render_template('./success.html', info=f'USB Tethering is enabled {results}')

@app.route('/dashboard/androidmgr/android_screen')
@login_required
def androidmgr_android_screen():
    return render_template('./manager/android_screen.html')

@app.route('/dashboard/androidmgr/android_screen/launch')
@login_required
def androidmgr_android_screen_launch():
    hostname = request.host.split(':')[0]
    os.system(f'nohup vncserver :{android_screen_port_vnc} {android_screen_vnc_conf} >> /flyos/logs/android_screen_vnc.log 2>&1 &')
    os.system(f'nohup /flyosext/novnc/utils/novnc_proxy --vnc localhost:590{android_screen_port_vnc} --listen 0.0.0.0:{android_screen_port_web} >> /flyos/logs/android_screen_novnc.log 2>&1 &')
    time.sleep(3)
    return redirect(f'http://{hostname}:{android_screen_port_web}/vnc.html')

@app.route('/dashboard/androidmgr/android_screen/redirect')
@login_required
def androidmgr_android_screen_launch_redirect():
    hostname = request.host.split(':')[0]
    return redirect(f'http://{hostname}:{android_screen_port_web}/vnc.html')

@app.route('/dashboard/androidmgr/android_screen/stop')
@login_required
def androidmgr_android_screen_launch_stop():
    results = os.popen(f'vncserver -kill :{android_screen_port_vnc}').read()
    return render_template('./success.html', info=f'Stopped Android Screen Mirroring Service {results}')


@app.route('/dashboard/androidmgr/launch_desktop')
@login_required
def androidmgr_linuxmode():
    return render_template('./manager/linuxmode.html')

@app.route('/dashboard/androidmgr/launch_desktop/launch')
@login_required
def androidmgr_linuxmode_launch():
    return render_template('./manager/linuxmode_launch.html', launch_linux_mode=launch_linux_mode())

@app.route('/dashboard/androidmgr/launch_desktop/launch/view_logs')
@login_required
def androidmgr_linuxmode_launch_viewlog():
    hostname = request.host.split(':')[0]
    logs_path = '/flyos/logs/launch_linux.log'

    with open(logs_path, 'r') as logs:
        logs_read = logs.read()

    text_response = Response(
        response=logs_read,
        status=200,
        mimetype='text/plain'
    )

    return text_response
    
@app.route('/dashboard/notebook/view')
@login_required
def jupyter_notebook():
    hostname = request.host.split(':')[0]
    return redirect(f'http://{hostname}:{jupyter_notebook_port}/')
@app.route('/dashboard/about')
@login_required
def about():
    return render_template('about.html', 
        run_system=run_system,
        os_ver=os_ver,
        os_build_channel=os_build_channel,
        cust_build=cust_build)
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
    with open('/flyos/files/token/token', 'r') as read_token:
        readtoken = read_token.read()
    return render_template('settings.html', run_system=run_system, configfile_read=configfile_read, readtoken=readtoken)
@app.route('/settings/update_timezone')
@login_required
def update_timezone_view():
    timezone = request.args.get("timezone")
    next = request.args.get("next")
    os.system(f"sudo ln -sf /usr/share/zoneinfo/{timezone} /etc/localtime")
    os.system("dpkg-reconfigure -f noninteractive tzdata")
    if next is not None:
        return redirect(next)
    return render_template('./success.html', info='You have successfully changed the time zone. If it has not changed, please check the "/etc/timezone" file!')
@app.route('/settings/updateuserpwd')
@login_required
def updateuserpwd():
    username = request.args.get("username")
    passwd = request.args.get("passwd")
    command = f'echo {username}:{passwd} | chpasswd'
    results = subprocess.getoutput(command)

    if results.strip() != '':
        return render_template('./oops.html', info=f'Update password failed, {results}')
    else:
        return render_template('./success.html', info=f'User: {username} password: {passwd} updated successfully! {results}')
@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if no_pwd_login == True:
            user_id = 1
            user = User(user_id)
            login_user(user)
            
            os.system(no_pwd_login_alert_command)
            return redirect(url_for('panel'))
        if log_message:
            current_time = datetime.now()
            formatted_time = current_time.strftime("%b %d %H:%M")
            alert_command = f'adb shell "su -lp 2000 -c \\"cmd notification post -S bigtext -t \'FlyOS Login Security Alert\' \'{random.randint(10000, 100000)}\' \'A device has successfully logged into the FlyOS dashboard at {formatted_time}, if you are not operating, please change the password in settings, (This message can be disabled in advanced settings)\'\\""'
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
    if setup_check() == False:
        return redirect(url_for('setup_default_login'))
    if no_pwd_login == True:
        user_id = 1
        user = User(user_id)
        login_user(user)
        
        os.system(no_pwd_login_alert_command)
        return redirect(url_for('panel'))
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

@app.route('/dashboard/settings/sysupdate/main')
@login_required
def settings_sysupdate_main():
    response = requests.get(sys_update_check_server)
    if response.status_code == 200:
        latest_ver = response.text
    else:
        latest_ver = f"No internet or unable to connect to update server, Status code: {response.status_code}"
    return render_template('./settings/system_update.html',
    os_ver=os_ver,
    os_build_channel=os_build_channel,
    cust_build=cust_build,
    latest_ver=latest_ver
    )

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
        if setup_check() == False:
            return redirect(url_for('setup_default_login'))
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

# first setup
setup_lock_text = 'You have already done the setup, to do it again, delete the file "/flyos/files/setup/setup_lock"'
@app.route("/setup/login")
def setup_default_login():
    if setup_check() == False:
        user_id = 1
        user = User(user_id)
        login_user(user)
        return redirect(url_for('setup_welcome'))
    else:
        return render_template('./oops.html', info=setup_lock_text)

@app.route("/setup/welcome")
@login_required
def setup_welcome():
    if setup_check() == False:
        return render_template('./setup/welcome.html')
    else:
        return render_template('./oops.html', info=setup_lock_text)
@app.route("/setup/timezone")
@login_required
def setup_timezone():
    if setup_check() == False:
        return render_template('./setup/timezone.html')
    else:
        return render_template('./oops.html', info=setup_lock_text)
def logout():
    logout_user()
    return redirect(url_for('login'))


# service api
def require_token(func):
    with open('/flyos/files/token/token', 'r') as tokenfile:
        valid_token = tokenfile.read().strip() 

    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        if token != valid_token:
            return jsonify({"status": 401, "error": "Unauthorized", "message": "Invalid token"}), 401
        return func(*args, **kwargs)

    return wrapper

@app.route("/api/get_service_code_server")
def api_get_service_code_server():
    return check_codeserver_process()

@app.route("/api/get_service_ssh")
def api_get_service_ssh():
    return check_ssh_process()

@app.route("/api/get_service_jupyter")
def api_get_service_jupyter():
    return check_jupyter_process()

@app.route("/api/send_msg")
@require_token
def api_send_android_msg():
    title = request.args.get('title')
    msg = request.args.get('msg')
    msgid = request.args.get('msgid')
    send_android_msg(title, msg, msgid)

    response_data = {
        "status": 200,
        "message": "ok",
        "title": title,
        "msg": msg,
        "msgid": msgid
    }

    return jsonify(response_data), 200
# reset token
def generate_random_token(length=16):
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for _ in range(length))
    return token
@app.route("/api/token/reset")
def api_token_reset():
    random_token = generate_random_token(20)
    with open('/flyos/files/token/token', 'w') as tokenfile:
        tokenfile.write(random_token)
    return render_template('./success.html', info=f'API has been reset: {random_token}, please use new Token')
    

def generate_random_token(length=16):
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for _ in range(length))
    return token

if __name__ == '__main__':
    restore_config()
    app.run(host=dashboard_host_addr, port=server_port, debug={dev_server_debug})