def create_free_job_object(client, dataset_name):
    # Configureate Pod template container
    job_name = "free"
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

    return job

def create_premium_job_object(client, dataset_name):
    # Configureate Pod template container
    job_name = "premium"
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

    return job