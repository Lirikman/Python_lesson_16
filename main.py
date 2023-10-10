import requests
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


@app.route('/result.html', methods=['POST', 'GET'])
def result():
    #    city = request.form['city']
    #    vac = request.form['vac']
    #    print(city, vac)
    #    return render_template('result.html', city=city, vac=vac)
    area = request.form['city']
    vac_text = request.form['vac']
    url = 'https://api.hh.ru/vacancies'
    params = {'text': f'NAME:({vac_text})', 'area': area}
    result = requests.get(url, params=params).json()
    total_pages = result['pages']
    vac_json = []
    for i in range(total_pages):
        url = 'https://api.hh.ru/vacancies'
        params = {'text': f'NAME:({vac_text})', 'area': area, 'page': i, 'per_page': 20}
        vac_json.append(requests.get(url, params=params).json())
    all_salary = 0
    all_vac = 0
    for i in vac_json:
        items = i['items']
        count_vac = 0
        summ_salary = 0
        for j in items:
            if j['salary'] is not None:
                s = j['salary']
                if s['from'] is not None:
                    count_vac += 1
                    summ_salary += s['from']
        all_salary += summ_salary
        all_vac += count_vac
    average_salary = all_salary // all_vac
    return render_template('result.html', salary=average_salary)


if __name__ == '__main__':
    app.run(debug=True)
