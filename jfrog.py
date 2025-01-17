#!/usr/bin/env python3

import requests
import os

# JFrog Artifactory details
artifactory_url = 'http://13.57.254.36:8082/artifactory'
repository_name = 'example-repo-local'
username = 'admin'
password = 'Sanjeeva@123'

# Path to the JAR file you want to upload
jar_file_path = '/var/lib/jenkins/workspace/jfrog/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'

# Construct the URL for uploading
upload_url = f'{artifactory_url}/{repository_name}/example-repo-local/repository/{os.path.basename(jar_file_path)}'

# Set up basic authentication
auth = (username, password)

# Create a session
session = requests.Session()
session.auth = auth

# Upload the JAR file
try:
    with open(jar_file_path, 'rb') as jar_file:
        response = session.put(upload_url, data=jar_file)
        response.raise_for_status()
        print(f"JAR file uploaded successfully to {upload_url}")
except Exception as e:
    print(f"Error uploading JAR file: {str(e)}")
finally:
    session.close()
