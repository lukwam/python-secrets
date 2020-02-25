#!/usr/bin/env python
"""Example of managing secrets in code - BAD IDEA."""

#
# example from googling "simple github api python example":
# https://gist.github.com/mxmader/8281851a99d0cfb53a363286246c08d8
#

import base64
from github import Github

# First create a Github instance:

# using username and password
# g = Github("user", "password")

# or using an access token
g = Github('****************************************')

# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
# for repo in g.get_user().get_repos():
#     print(repo.name)

# get the repo
repo = g.get_repo('lukwam/python-secrets')

# get the README.md content
content = repo.get_contents("README.md").content

# convert content to string
text = base64.b64decode(content).decode('utf-8')

# print content
print(text)
