from flask import Flask, render_template, request, Response
from queue import Queue
from threading import Thread
import subprocess

app = Flask(__name__)
app.secret_key = 'your_secret_key'

output_queue = Queue()


def execute_command(command):
    process = subprocess.Popen(
        command.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True
    )
    for line in iter(process.stdout.readline, ''):
        output_queue.put(line.rstrip())
    process.stdout.close()
    process.wait()

    output_queue.put(None)


def generate_output():
    for output in iter(output_queue.get, None):
        yield "{}\n".format(output)
        output_queue.task_done()


@app.route('/system/cmd')
def index():
    command = request.args.get('command')
    if command:
        command_thread = Thread(target=execute_command, args=(command,))
        command_thread.start()

    return Response(generate_output(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
