from flask import Flask, render_template, jsonify
import pymysql
from mysqlupdate import generate_and_update_data
import threading

app = Flask(__name__)

# Database connection details
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '1234',
    'db': 'db'
}


def execute_query(query):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def fetch_data(query, field_names):
    results = execute_query(query)
    data = []
    for row in results:
        item = {}
        for i, field_name in enumerate(field_names):
            item[field_name] = row[i]
        data.append(item)
    return data


@app.route('/')
def serve_template():
    return render_template('index.html')


@app.route('/get_interests_data', methods=['GET'])
def get_interests_data():
    query = "SELECT interest_name, interest_value FROM interest_distribution"
    field_names = ['name', 'value']
    interests_data = fetch_data(query, field_names)
    return jsonify(interests_data)


@app.route('/get_echarts_data', methods=['GET'])
def get_echarts_data():
    query = "SELECT category, value FROM echarts_data"
    field_names = ['category', 'value']
    echarts_data = fetch_data(query, field_names)
    return jsonify(echarts_data)


@app.route('/get_charts_data', methods=['GET'])
def get_charts_data():
    query = "SELECT region, value FROM chart_data"
    field_names = ['region', 'value']
    charts_data = fetch_data(query, field_names)
    return jsonify(charts_data)


@app.route('/get_as_ios_data', methods=['GET'])
def get_as_ios_data():
    as_query = "SELECT id, category, value FROM as_data"
    ios_query = "SELECT id, category, value FROM ios_data"
    field_names = ['id', 'category', 'value']
    as_data = fetch_data(as_query, field_names)
    ios_data = fetch_data(ios_query, field_names)
    return jsonify({'as_data': as_data, 'ios_data': ios_data})


@app.route('/get_pie_data', methods=['GET'])
def get_pie_data():
    query = "SELECT name, value FROM pie_data"
    field_names = ['name', 'value']
    pie_data = fetch_data(query, field_names)
    return jsonify(pie_data)


@app.route('/get_age_data', methods=['GET'])
def get_age_data():
    query = "SELECT age_group, value FROM age_data"
    field_names = ['age_group', 'value']
    age_data = fetch_data(query, field_names)
    return jsonify(age_data)


@app.route('/get_fb_data', methods=['GET'])
def get_fb_data():
    fb_query = "SELECT name, value FROM fb_data"
    field_names = ['name', 'value']
    fb_data = fetch_data(fb_query, field_names)
    return jsonify({'fb_data': fb_data})


def update_data_thread():
    generate_and_update_data()


if __name__ == '__main__':
    # 在单独的线程中启动更新过程
    update_thread = threading.Thread(target=update_data_thread)
    update_thread.start()

    # 运行Flask应用程序
    app.run(host='0.0.0.0')
