#!/usr/bin/env python
"""Example of managing secrets in a config file - better idea."""

import base64
from github import Github

# import settings from config file
from config import repo_name, token

# First create a Github instance using an access token
g = Github(token)

repo = g.get_repo(repo_name)
contents = repo.get_contents("README.md")
text = base64.b64decode(contents.content).decode('utf-8')
print(text)
