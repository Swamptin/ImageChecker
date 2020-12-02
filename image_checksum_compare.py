# This script is used to parse a list of known hashes created by
# checksum_images.py. Please run that script first if you have not been provided
# with a 'Hashed_Images.txt' file.
#
# This file will output if there is a match for your input image in the
# Hashed_Images.txt file.
# Known Limitations:
#       1) Images must be identical to match
#       2) Images may not match if format is changed
#       3) Images will not match if someone has defaced the image
#
import sys
import os
import hashlib

def usage():
    print("This file checks an image against a list of known hashed values.")
    print("Please call it in the form:")
    print("python3  image_check image.jpg HashedImages.txt \n")
    sys.exit()

def hashfile(image):
    sha256_hash = hashlib.sha256()
    with open(image,"rb") as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def main(image, hashedinput):
    hashed_file = hashfile(image)
    if os.path.isfile(hashedinput):
        try:
            f = open(hashedinput, "r")
            line = f.readline()
            while line:
                if hashed_file in line:
                    print("The image "+image+" was found here:")
                    print(line)
                line = f.readline()
            f.close
        except IOError:
            print("Error opening " + hashedinput)
    else:
        print("Please place the "+hashedinput+" file in the same location as this script.\n")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()
    else:
        image = sys.argv[1]
        hashedinput = sys.argv[2]
        main(image, hashedinput)
