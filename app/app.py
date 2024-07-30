from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

    
@app.route("/home")
def home():
    return "<p>welcome to my world!</p>"


@app.route("/contact")
def contact():
    phone_no="07063460231"
    email="preye@gmail.com"
    r=str(phone_no + email)
    return "<p>r</p>"

if __name__=='__main__':
    app.run(host="127.0.0.1",port=5005,debug=True)