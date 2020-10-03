from flask import *
import logging

app = Flask(__name__)

#ログ出力設定
LOGFILE = "flask.log"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(LOGFILE)
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
app.logger.addHandler(fh)

@app.route("/")
def index():
    return render_template('index.html', msg='Hello, ', additional_msg="from Python")

@app.route('/good')
def good():
    name = "Good"
    return name


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)