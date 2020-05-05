from flask import Flask,request,jsonify,render_template
import os
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api', methods=["POST"])
def main_interface():
    message = request.form['message']
    print(message)
    result=message
    with open('file.py','w') as f:
      f.write(result)
      f.close()
    os.system("python file.py > op.txt")
    with open('op.txt','r') as f:
      result=f.read()
      f.close()
    return jsonify({'message': result})

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response