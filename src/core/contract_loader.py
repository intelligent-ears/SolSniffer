import os

def get_solidity_files(directory: str):
    files = []
    for root, _, filenames in os.walk(directory):
        for file in filenames:
            if file.endswith(".sol"):
                files.append(os.path.join(root, file))
    return files