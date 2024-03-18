# import os

# def organize_files(folder_name="basic"):
#     # Create a folder
#     os.makedirs(folder_name, exist_ok=True)

#     # Move all files to the folder
#     files = [f for f in os.listdir() if os.path.isfile(f)]
#     for file in files:
#         os.rename(file, os.path.join(folder_name, file))

# if __name__ == "__main__":
#     organize_files()

import os
from pathlib import Path

def list_files_by_creation_time():
    files = [(f, os.path.getctime(f)) for f in os.listdir() if os.path.isfile(f)]

    # If os.path.getctime() doesn't provide creation time, try pathlib.stat()
    if not files:
        files = [(f, Path(f).stat().st_ctime) for f in os.listdir() if os.path.isfile(f)]

    files.sort(key=lambda x: x[1], reverse=True)

    print("Files sorted by creation time:")
    for file, _ in files:
        print(file)

if __name__ == "__main__":
    list_files_by_creation_time()


