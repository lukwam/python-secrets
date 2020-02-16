#!/usr/bin/env python
"""Example of managing secrets in a config file - better idea."""

import base64
from github import Github
from google.cloud import kms_v1

# import settings from config file
from config import repo_name, token
from config import project_id, location_id, key_ring_id, crypto_key_id


def decrypt_token():
    """Decrypt the token from the config file."""
    #
    # from example:
    # https://cloud.google.com/kms/docs/encrypt-decrypt#decrypt
    #
    
    # base64 decode the encrypted token
    ciphertext = base64.b64decode(token.encode('utf-8'))

    # Creates an API client for the KMS API.
    client = kms_v1.KeyManagementServiceClient()

    # The resource name of the CryptoKey.
    name = client.crypto_key_path_path(
        project_id, 
        location_id, 
        key_ring_id,                                       
        crypto_key_id
    )

    # Use the KMS API to decrypt the data.
    response = client.decrypt(name, ciphertext)
    return response.plaintext.decode('utf-8')

# decrypt the token
token = decrypt_token()

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
