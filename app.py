from flask import Flask,request,jsonify,render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api', methods=["POST"])
def main_interface():
    message = request.form['message']
    result=eval(message)
    return jsonify({'message': result})
