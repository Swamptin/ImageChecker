# ImageChecker
  
This is a repo that currently has two files:
checksum_images.py and image_checksum_compare.py

To run these files you must have python3.6 or greater installed on your system. To install python3 please go to https://www.python.org/downloads/ and install the
latest version of Python3 that is available.  
Once you have python installed the scripts can be called in the following way  
python3 script.py input1 input2  
  
For example:  
python3 checksum_images.py C:\Users\swamptin\Images\
or  
python3 image_checksum_compare.py image.jpg HashedImages.txt

You must run checksum_images.py first to create the HashedImages.txt file. Once that has been done, you run image_checksum_compare.py to see if a sample image
is present in the HashedImages.txt file. Any re-running of the first script will append to hashedImages.txt rather than replace it. If you do not wish to append,
simply rename HashedImages.txt before re-running checksum_images.py. 

### Please Note, these scripts assume you have a local copy of images to hash. Currently they do not work against remote copies. 

