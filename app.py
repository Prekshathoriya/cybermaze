from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # change this for production

SCORES_FILE = 'scores.json'

# Helper to load scores
def load_scores():
    if not os.path.exists(SCORES_FILE):
        return []
    with open(SCORES_FILE, 'r') as f:
        return json.load(f)

# Helper to save scores
def save_scores(scores):
    with open(SCORES_FILE, 'w') as f:
        json.dump(scores, f, indent=2)

@app.route('/', methods=['GET'])
def home():
    # Reset session on home
    session.clear()
    return render_template('home.html')

# Level 1 - Brute Force
@app.route('/level1', methods=['GET', 'POST'])
def level1():
    correct_pin = '431'
    attempts_left = session.get('attempts_left', 5)
    message = ''
    success = False

    if request.method == 'POST':
        pin = request.form.get('pin')
        if pin == correct_pin:
            success = True
            session['score'] = session.get('score', 0) + 10
            return redirect(url_for('level2'))
        else:
            attempts_left -= 1
            session['attempts_left'] = attempts_left
            if attempts_left <= 0:
                message = 'No attempts left. Restart to try again.'
            else:
                message = f'Incorrect. Attempts left: {attempts_left}'

    return render_template('level1.html', message=message, attempts_left=attempts_left)

# Level 2 - Caesar Cipher
@app.route('/level2', methods=['GET', 'POST'])
def level2():
    encrypted_msg = "khoor"
    correct_answer = "hello"
    message = ''
    if request.method == 'POST':
        answer = request.form.get('answer', '').lower()
        if answer == correct_answer:
            session['score'] = session.get('score', 0) + 10
            return redirect(url_for('level3'))
        else:
            message = 'Incorrect. Try again.'

    return render_template('level2.html', encrypted_msg=encrypted_msg, message=message)

# Level 3 - Simple Password Check (Example)
@app.route('/level3', methods=['GET', 'POST'])
def level3():
    secret_word = "cybermaze"
    message = ''
    if request.method == 'POST':
        answer = request.form.get('answer', '').lower()
        if answer == secret_word:
            session['score'] = session.get('score', 0) + 10
            # Save final score to scoreboard
            scores = load_scores()
            scores.append({"player": "Agent", "score": session.get('score', 0)})
            save_scores(scores)
            return redirect(url_for('success'))
        else:
            message = 'Incorrect. Try again.'

    return render_template('level3.html', message=message)

@app.route('/success')
def success():
    score = session.get('score', 0)
    return render_template('success.html', score=score)

@app.route('/leaderboard')
def leaderboard():
    scores = load_scores()
    # Sort scores descending by score
    scores = sorted(scores, key=lambda x: x['score'], reverse=True)
    return render_template('leaderboard.html', scores=scores)

if __name__ == '__main__':
    app.run(debug=True)
