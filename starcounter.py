import urllib.request
import os
import json
import pandas
import yaml
import time
from collections import Counter

CACHE_DIR = 'cache_stars_json'

os.makedirs(CACHE_DIR, exist_ok=True)

def load_known_users(filename="known-users.yml"):
	with open(filename, 'rt') as f:
		known_users = yaml.safe_load(f)
	return known_users

def cache_know