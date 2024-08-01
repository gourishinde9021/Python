from flask import Flask

# create a flask application instance
app = Flask(__name__)

@app.route("/")            # Decorator
def hello():
    return 'Hello World!!'

app.run('0.0.0.0')