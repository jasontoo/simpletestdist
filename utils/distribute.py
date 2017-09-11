"""
Distribution Mode implementation
"""
import docker

def _get_docker_arguments():
    """
    Retrieve docker container arguments
    """
    return {
        'image': 'simpletestdist',
        'command': 'python /root/testrunner.py',
        'environment': {'DISPLAY': ':99', 'DBUS_SESSION_BUS_ADDRESS': '/dev/null'},
        'ports': {'8888/tcp': None, '5904/tcp': None},
        'detach': True,
        'tty': True,
        'stdin_open': True
    }

def _show_vnc_ports(client):
    network = client.networks.get('bridge')
    containers = network.attrs['Containers']
    for i in containers:
        container = client.containers.get(i)
        print(container.attrs['NetworkSettings']['Ports']['5904/tcp'][0]['HostPort'])

def get_container_arguments():
    """
    Returns list of IPv4 Addresses of Docker Containers
    in the pytest argument format
    """
    container_args = []
    client = docker.from_env()
    network = client.networks.get('bridge')
    containers = network.attrs['Containers']
    for i in containers:
        tx_arg = ['--tx', 'socket={}:8888'.format(containers[i]['IPv4Address'][:-3])]
        container_args.extend(tx_arg)
    return container_args

def create_docker_containers(count):
    """
    Create test runners

    :Args:
     - count - Number of containers to create
    """
    docker_client = docker.from_env()
    docker_args = _get_docker_arguments()
    for i in range(count):
        docker_client.containers.run(**docker_args)

def check(client):
    """
    Debug function for checking existing containers
    in bridge network

    :Args:
     - client - Docker client
    """
    network = client.networks.get('bridge')
    containers = network.attrs['Containers']
    print(containers)

def cleanup():
    """
    Remove all running Docker Containers
    """
    client = docker.from_env()
    network = client.networks.get('bridge')
    containers = network.attrs['Containers']
    for i in containers:
        container = client.containers.get(i)
        if container.status == 'running':
            container.kill()
        container.remove()
