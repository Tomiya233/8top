import re
import requests
from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def top():
  urls = {
      "新加坡centos7": "https://fk1.8top.top/buy/2",
      "新加坡debian11": "https://fk1.8top.top/buy/3",
      "日本centos7": "https://fk1.8top.top/buy/39",
      "日本debian11": "https://fk1.8top.top/buy/40",
      "美西centos7": "https://fk1.8top.top/buy/5",
      "美西debian11": "https://fk1.8top.top/buy/6",
  }

  data = {}
  for key, url in urls.items():
    response = requests.get(url)
    response.encoding = 'utf-8'
    content = response.text
    match = re.search(r'库存\((\d+)\)', content)
    if match:
      data[key] = match.group(1)
    else:
      data[key] = "无库存"

  return jsonify(data)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
