from flask import Flask
print("asda")
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'chenzhuo Hello, World!'

if __name__ == '__main__':
    print("nihio")
    app.run()