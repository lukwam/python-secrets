#!/usr/bin/env python
"""Example of managing secrets in a config file - better idea."""

import base64
from github import Github
from google.cloud import secretmanager_v1beta1

# import settings from config file
from config import repo_name, token
from config import project_id

def retrieve_token():
    """Retrieve the token from the github from Secret Manager."""
    # Parse the secret path to retrieve project and name
    _, _, secret_project, secret_name = token.split('/')

    # Initialize the Secret Manager client
    client = secretmanager_v1beta1.SecretManagerServiceClient()

    # Generate the name of the secret
    name = client.secret_version_path(secret_project, secret_name, 'latest')

    # Retrieve the secret version
    version = client.access_secret_version(name)
    
    return version.payload.data.decode('utf-8')

# decrypt the token
token = retrieve_token()

# First create a Github instance using an access token
g = Github(token)

# get the repo
repo = g.get_repo(repo_name)

# get the README.md content
content = repo.get_contents("README.md").content

# convert content to string
text = base64.b64decode(content).decode('utf-8')

# print content
print(text)
