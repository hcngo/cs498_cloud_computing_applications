import uuid

def create_free_job(client, batch_client, dataset_name):
    # Configureate Pod template container
    job_name = "free-%s" % str(uuid.uuid4())
    job_namespace = "free-service"

    resources = client.V1ResourceRequirements(
        limits={"cpu": "0.9"},
        requests={"cpu": "0.9"}
    )
    container_env = [
        client.V1EnvVar(name="DATASET", value=dataset_name),
        client.V1EnvVar(name="TYPE", value="ff")
    ]
    container = client.V1Container(
        name=job_name,
        image="hieungo91/mp3-cloud-computing-applications:latest",
        resources=resources,
        env=container_env)
    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": job_name}),
        spec=client.V1PodSpec(restart_policy="Never", containers=[container]))
    # Create the specification of deployment
    spec = client.V1JobSpec(
        template=template,
        backoff_limit=4)
    # Instantiate the job object
    job = client.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=client.V1ObjectMeta(name=job_name, namespace=job_namespace),
        spec=spec)

    # Api call to create the job
    api_response = batch_client.create_namespaced_job(
        body=job,
        namespace=job_namespace
    )

    # Need to read the info rightaway
    job_status_info = batch_client.read_namespaced_job_status(
        name=job_name,
        namespace=job_namespace
    )

    return job_status_info

def create_premium_job(client, batch_client, dataset_name):
    # Configureate Pod template container
    job_name = "premium-%s" % str(uuid.uuid4())
    job_namespace = "default"

    container_env = [
        client.V1EnvVar(name="DATASET", value=dataset_name),
        client.V1EnvVar(name="TYPE", value="cnv")
    ]
    container = client.V1Container(
        name=job_name,
        image="hieungo91/mp3-cloud-computing-applications:latest",
        env=container_env)
    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": job_name}),
        spec=client.V1PodSpec(restart_policy="Never", containers=[container]))
    # Create the specification of deployment
    spec = client.V1JobSpec(
        template=template,
        backoff_limit=4)
    # Instantiate the job object
    job = client.V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=client.V1ObjectMeta(name=job_name, namespace=job_namespace),
        spec=spec)

    # Api call to create the job
    api_response = batch_client.create_namespaced_job(
        body=job,
        namespace=job_namespace
    )

    # Need to read the info rightaway
    job_status_info = batch_client.read_namespaced_job_status(
        name=job_name,
        namespace=job_namespace
    )

    return job_status_info

def get_pods_info(core_client):
    original_pod_list = core_client.list_pod_for_all_namespaces()
    pod_list = [{
        "node": p.spec,
        "ip": p.status.pod_ip,
        "namespace": p.metadata.namespace,
        "name": p.metadata.name,
        "status": p.status.phase
        }
        for p in original_pod_list.items
    ]
    return pod_list