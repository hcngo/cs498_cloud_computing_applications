from flask import Flask
from flask import request
app = Flask(__name__)

SEED = 0

@app.route('/', methods=['GET', 'POST'])
def default():
    global SEED
    res = ""
    if request.method == 'POST':
        data = request.get_json(True, False, False)
        if "num" in data:
            SEED = data["num"]
            res = f'Seed is set to {SEED}'
        else:
            res = f'invalid request data'
    else:
        res = f'{SEED}'
    response = app.make_response(res)
    response.headers['Content-type'] = 'text/plain; charset=utf-8'
    return response
  
if __name__ == '__main__':
  app.run()