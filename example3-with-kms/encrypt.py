#!/usr/bin/env python

#
# example from:
# https://cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python
#

import base64
import sys

# Imports the Google APIs client library
from google.cloud import kms_v1

from config import project_id, location_id, key_ring_id, crypto_key_id

# Check the command line arguments for the plaintext string
if not sys.argv[1:]:
    sys.exit('ERROR: Input string required.')
plaintext = sys.argv[1].encode('utf-8')

#
# from example:
# https://cloud.google.com/kms/docs/encrypt-decrypt#encrypt
#

# Creates an API client for the KMS API.
client = kms_v1.KeyManagementServiceClient()

# The resource name of the CryptoKey.
name = client.crypto_key_path_path(
    project_id, 
    location_id, 
    key_ring_id,
    crypto_key_id
)

# Use the KMS API to encrypt the data.
response = client.encrypt(name, plaintext)
# print(response.ciphertext)
print(base64.b64encode(response.ciphertext).decode('utf-8'))
