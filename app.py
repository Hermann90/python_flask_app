import random
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name.capitalize()}! Welcome to the Exciting Flask App.'

@app.route('/quote')
def quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Innovation distinguishes between a leader and a follower. - Steve Jobs",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "You only live once, but if you do it right, once is enough. - Mae West"
    ]
    return random.choice(quotes)

@app.route('/random')
def random_number():
    min_val = request.args.get('min', default=1, type=int)
    max_val = request.args.get('max', default=100, type=int)
    return str(random.randint(min_val, max_val))

if __name__ == '__main__':
    app.run(debug=True)
