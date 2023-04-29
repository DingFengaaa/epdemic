
import requests
import json
import pymysql

url = "https://gwpre.sina.cn/ncp/foreign?_=1585388721640"
response = requests.get(url)
data = json.loads(response.text)
print(data)
conn = pymysql.connect(
    host='localhost',
    port=3307,
    user='root',
    password='123456',
    db='user',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

for entry in data['result']['history']:
    certain = entry['certain']
    uncertain = entry['uncertain']
    die = entry['die']
    recure = entry['recure']
    date = entry['date']

    with conn.cursor() as cursor:
        sql = "INSERT INTO epidemic_history (certain, uncertain, die, recure, date) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (certain, uncertain, die, recure, date))
        conn.commit()

conn.close()
