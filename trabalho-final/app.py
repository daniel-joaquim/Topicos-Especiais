from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

# Variáveis globais para o cronômetro
start_time = 0
elapsed_time = 0
running = False

# Rota para servir o arquivo HTML
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_timer():
    global start_time, running
    if not running:
        start_time = time.time() - elapsed_time
        running = True
    return jsonify({'status': 'started'})

@app.route('/pause', methods=['POST'])
def pause_timer():
    global elapsed_time, running
    if running:
        elapsed_time = time.time() - start_time
        running = False
    return jsonify({'status': 'paused'})

@app.route('/reset', methods=['POST'])
def reset_timer():
    global start_time, elapsed_time, running
    start_time = 0
    elapsed_time = 0
    running = False
    return jsonify({'status': 'reset'})

@app.route('/time', methods=['GET'])
def get_time():
    global start_time, elapsed_time, running
    if running:
        elapsed_time = time.time() - start_time
    hours, rem = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(rem, 60)
    time_str = "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))
    return jsonify({'time': time_str})

if __name__ == '__main__':
    app.run(debug=True)
