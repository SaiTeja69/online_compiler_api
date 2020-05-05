from flask import Flask,request,jsonify,render_template
import os
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api', methods=["POST"])
def main_interface():
    response = request.get_json()
    print(response)
    message=response['message']
    with open('file.py','w') as f:
      f.write(message)
      f.close()
    os.system("python file.py > op.txt")
    with open('op.txt','r') as f:
      data=f.read()
      f.close()
    response['message']=data
    return jsonify(response)
@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response