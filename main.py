Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, render_template, request, url_for
import similarity

app = Flask(__name__, template_folder='Templates')

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')

@app.route('/report',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['text']
      return (similarity.returnTable(similarity.report(str(result))))

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0', port=5555)