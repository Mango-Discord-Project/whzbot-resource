from common_data import *


def load(path, encoding) -> dict:
    with open(path, encoding=encoding) as file:
        return json.load(file)

error_files = []

for root, files in walk:
    for file in files:
        path = root + file
        try:
            data = load(path, "gbk")
        except UnicodeEncodeError:
            data = load(path, "utf-8")
        except json.decoder.JSONDecodeError:
            error_files.append(path)
        with open(path, encoding="utf8") as file:
            data = json.dump(data, file, indent=2, ensure_ascii=False)

print(error_files)