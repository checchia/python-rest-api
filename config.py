import os
import json

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))

with open("package-config.json", 'r') as f:
    pkg_dict = json.load(f)

