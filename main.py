from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parsing.html')
def parsing():
    return 'Pasring vacancy python'

@app.route('/resume.html')
def resume():
    return 'Python the best language programming'


if __name__ == '__main__':
    app.run(debug=True)
