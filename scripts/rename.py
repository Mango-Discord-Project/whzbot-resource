from common_data import *

for root, files in walk:
    for file in files:
        os.rename(root + file, root + file.split(".")[0] + ".json")
