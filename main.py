from flask import Flask
from config import DevConfig

app = Flask(__name__)

# Get the config from object of DecConfig
app.config.from_object(DevConfig)

@app.route('/')
def home():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()
