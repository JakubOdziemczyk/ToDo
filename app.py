from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')

tasks = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title', '').strip()
    if not title:
        flash('Podaj nazwę zadania.')
        return redirect(url_for('index'))
    tasks.append(title)
    flash('Dodano zadanie.')
    return redirect(url_for('index'))

@app.route('/delete/<int:idx>', methods=['POST'])
def delete(idx):
    if 0 <= idx < len(tasks):
        tasks.pop(idx)
        flash('Usunięto zadanie.')
    else:
        flash('Nieprawidłowy indeks zadania.')
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
