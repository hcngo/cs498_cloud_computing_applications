from flask import Flask
from flask import request
app = Flask(__name__)

SEED = 0

@app.route('/', methods=['GET', 'POST'])
def default():
    if request.method == 'POST':
        return request.data
    else:
        return SEED
  
if __name__ == '__main__':
  app.run()