import os
import json

walk = [(root if root.endswith("/") else root + "/", files) for root, _, files in os.walk("./data/")]