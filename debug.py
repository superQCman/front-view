from flask import Flask, jsonify,render_template,request
import random
from datetime import datetime, timedelta
app = Flask(__name__)
def random_date(start, end):
    return start + timedelta(minutes=random.randint(0, int((end - start).total_seconds() / 60)))

@app.route('/get_data', methods=['GET'])
def get_data():
    # 这里你可以定义要返回的数据
    today = datetime.now()
    
    # 数据
    data = [
        { 'id': 1, 'title': "成功Meeting with Ben's agent.", 'date': random_date(today - timedelta(days=5), today + timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S'), 'href': "#" },
        { 'id': 2, 'title': 'Papers review with Tonny.', 'date': random_date(today - timedelta(minutes=60), today + timedelta(minutes=60)).strftime('%Y-%m-%d %H:%M:%S'), 'href': "#" },
        { 'id': 3, 'title': "Annual party at Eric's house.", 'date': random_date(today - timedelta(days=5), today + timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S'), 'href': "#" },
        { 'id': 4, 'title': 'Last day to pay off auto credit.', 'date': random_date(today - timedelta(days=5), today + timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S'), 'href': "#" },
        { 'id': 5, 'title': 'Call and schedule another meeting with Amanda.', 'date': random_date(today - timedelta(minutes=360), today + timedelta(minutes=360)).strftime('%Y-%m-%d %H:%M:%S'), 'href': "#" },
        { 'id': 6, 'title': "Don't forget to send in financial reports.", 'date': random_date(today - timedelta(days=5), today + timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S'), 'href': "#" }
    ]
    return jsonify(data)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # 获取多选的值，返回的是一个列表
        selected_provinces = request.form.getlist('multyselect')
        # 获取单选的值
        selected_time = request.form.get('choose_one')
        
        # 处理接收到的值
        print('Selected Provinces:', selected_provinces)
        print('Selected Time:', selected_time)
        return 'Form submitted successfully'
    return render_template('客户主界面.html')

if __name__ == '__main__':
    app.run(debug=True)
