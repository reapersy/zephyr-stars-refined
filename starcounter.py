import urllib.request
import os
import json
import pandas
import yaml
import time
from collections import Counter

CACHE_DIR = 'cache_stars_json'

os.make