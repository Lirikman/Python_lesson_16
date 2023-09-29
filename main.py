from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/parsing.html')
def parsing():
    return render_template('parsing.html')

@app.route('/resume.html')
def resume():
    return render_template('resume.html')


if __name__ == '__main__':
    app.run(debug=True)
