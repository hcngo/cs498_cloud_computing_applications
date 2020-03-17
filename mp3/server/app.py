from flask import Flask
from flask import request
from kubernetes import client, config
from util import create_free_job_object, create_premium_job_object
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
def post():
    data = request.get_json(True, False, False)
    dataset = data["dataset"] if "dataset" in data else "mnist"
    free_job = create_free_job_object(client=client, dataset_name=dataset)
    api_response = batch_v1.create_namespaced_job(
        body=free_job,
        namespace="free-service"
    )
    return "Free Job created. status='%s'" % str(api_response.status)

# @app.route('/img-classification/premium', methods=['POST'])
# def post():
#     data = request.get_json(True, False, False)
#     dataset = data["dataset"] if "dataset" in data else "kmnist"
#     premium_job = create_premium_job_object(client=client, dataset_name=dataset)
#     api_response = batch_v1.create_namespaced_job(
#         body=premium_job,
#         namespace="default"
#     )
#     return "Premium Job created. status='%s'" % str(api_response.status)


  
if __name__ == '__main__':
  app.run()