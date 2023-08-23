import subprocess
from pymongo import MongoClient

def connect_mongo():
    cmd = "docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mongo"
    result = subprocess.run(cmd, 
                            shell=True, 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE, 
                            universal_newlines=True)
    
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        docker_container_ip = result.stdout.strip()

    connection = MongoClient(f'mongodb://{docker_container_ip}:27017/')
    return connection