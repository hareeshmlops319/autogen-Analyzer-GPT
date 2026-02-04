from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constants import WORK_DIR, TIMEOUT_DOCKER

def getDockerCommandLineExecutor():
    docker= DockerCommandLineCodeExecutor(
    work_dir=WORK_DIR,
    timeout=TIMEOUT_DOCKER
)

    return docker

async def start_docker_container(docker):
    print('Starting docker container')
    await docker.start()
    print('Docker container started')

async def stop_docker_container(docker):
    print('Stopping docker container')
    await docker.stop()
    print('Docker container stopped')