# This file reads an input of a directory. It then checks that directory and all
# subfolders for images of various types. Once it has a full list of all images
# it will create a file 'HashedImages.txt' and save it to disk. 
#
# To make use of the output you can then run image_checksum_compare.py with a
# sample image. If there is a match, you are notified.
# To extend this functionality you can change the file types that are searched
# for when calling run_fast_scandir().
#
import sys
import os
import hashlib

def usage():
    print("This program creates a list of hashes of files and stores them in a new file.")
    print("Please call it in the form:")
    print("python3  image_check /Path/To/Files/To/Hash \n")
    sys.exit()

def run_fast_scandir(dir, ext):    # dir: str, ext: list
    subfolders, files = [], []

    for f in os.scandir(dir):
        if f.is_dir():
            subfolders.append(f.path)
        if f.is_file():
            if os.path.splitext(f.name)[1].lower() in ext:
                files.append(f.path)


    for dir in list(subfolders):
        sf, f = run_fast_scandir(dir, ext)
        subfolders.extend(sf)
        files.extend(f)
    return subfolders, files

def hashfile(image):
    sha256_hash = hashlib.sha256()
    with open(image,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def main(path):
    subfolders, files = run_fast_scandir(path, [".jpg",".jpeg",".png",".gif"])
    for image in files:
        filename = os.path.basename(image)
        hashed_file = hashfile(image)
        if os.path.isfile("HashedImages.txt"):
            try:
                f = open("HashedImages.txt", "a")
                f.write(hashed_file + " : " + filename + "\n")
                f.close
            except IOError:
                print("Error opening HashedImages.txt")
        else:
            f = open("HashedImages.txt", "w+")
            f.write(hashed_file + " : " + image + "\n")
            f.close
    print("Script completed successfully")
    print("Please use the checker script to search for a specific file.\n")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
    else:
        path = sys.argv[1]
        main(path)
