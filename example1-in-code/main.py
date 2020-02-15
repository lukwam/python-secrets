#!/usr/bin/env python
"""Example of managing secrets in code - BAD IDEA."""

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

repo = g.get_repo('lukwam/python-secrets')
contents = repo.get_contents("README.md")
text = base64.b64decode(contents.content).decode('utf-8')
print(text)
