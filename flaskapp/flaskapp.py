from flask import Flask
from flask import request
app = Flask(__name__)

SEED = 0

@app.route('/', methods=['GET'])
def get():
    global SEED
    return f'{SEED}'

@app.route('/', methods=['POST'])
def post():
    global SEED
    data = request.get_json(True, False, False)
    if "num" in data:
        SEED = data["num"]
  
if __name__ == '__main__':
  app.run()