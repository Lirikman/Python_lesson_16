from flask import Flask, render_template, request

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


@app.route('/result.html', methods=['POST'])
def result():
    city = request.form['city']
    vac = request.form['vac']
    print(city, vac)
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
