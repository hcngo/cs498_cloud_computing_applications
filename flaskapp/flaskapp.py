from flask import Flask
from flask import request
app = Flask(__name__)

global SEED
SEED = 0

@app.route('/', methods=['GET', 'POST'])
def default():
    if request.method == 'POST':
        data = request.get_json(True)
        if "num" in data:
            SEED = data["num"]
            return f'Seed is set to {SEED}'
        else:
            return f'invalid request data'
    else:
        return f'{SEED}'
  
if __name__ == '__main__':
  app.run()