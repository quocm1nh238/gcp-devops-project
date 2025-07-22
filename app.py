from flask  import Flask
app = Flask(__name__)  

@app.route('/')
def hello_world():
    return 'bro Minh, First Step into CLOUD'