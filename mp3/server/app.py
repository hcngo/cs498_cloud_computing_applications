from flask import Flask
from flask import request
from kubernetes import client, config
from util import create_free_job, create_premium_job
app = Flask(__name__)
SEED = 0
# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
batch_v1 = client.BatchV1Api()

@app.route('/', methods=['GET'])
def get():
    global SEED
    return f'{SEED}'

@app.route('/img-classification/free', methods=['POST'])
def free_job():
    data = request.get_json(True, False, False)
    dataset = data["dataset"] if "dataset" in data else "mnist"
    free_job = create_free_job(client=client, batch_client=batch_v1, dataset_name=dataset)
    return "Free Job created. status='%s'" % str(free_job.status)

@app.route('/img-classification/premium', methods=['POST'])
def premium_job():
    data = request.get_json(True, False, False)
    dataset = data["dataset"] if "dataset" in data else "kmnist"
    premium_job = create_premium_job(client=client, batch_client=batch_v1, dataset_name=dataset)
    return "Premium Job created. status='%s'" % str(premium_job.status)

if __name__ == '__main__':
  app.run()