__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import shutil



def clean_cache():
   
    if not os.path.exists(".\cache"):
       os.mkdir(".\cache")
    else:
        shutil.rmtree(".\cache")
        os.mkdir(".\cache")

def cache_zip(zip_file, cache_dir):
    shutil.unpack_archive(zip_file, extract_dir=cache_dir)

def cached_files():
    file_paths = []

    for folder, subs, files in os.walk(os.path.join(os.getcwd(), 'cache')):
        for filename in files:
            file_paths.append(os.path.abspath(os.path.join(folder, filename)))
    return file_paths

def find_password(file_paths):
    for path in file_paths:
        for line in open(path):
            phrase = "password"
            if phrase in line:
                password = line.split(" ")[1]
                return password.strip()