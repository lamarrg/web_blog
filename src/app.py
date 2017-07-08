from flask import Flask

app = Flask(__name__) # '__main__'


@app.route('/')  # www.mysite.com/api/
def hello_method():
    return "Hello, world!"

if __name__ == '__main__':
    # app.run()  -- this is the default
    app.run(port=4995)  # set a custom port

