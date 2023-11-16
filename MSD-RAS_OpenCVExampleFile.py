# import libraries used in the script
# in this case we will import cv2 - the opencv module and argparse for command line argument inputs

import cv2
import argparse


# Review of argparse documentation shows us the syntax for adding command line arguments

parser = argparse.ArgumentParser()

# In this function we add a nickname to be used in the command line (-f) and a name to be used in the script (File)
parser.add_argument("-f", "--File")
args = parser.parse_args()
filename = args.File

# Now we write our openCV Methods here ---------

# Read an Image
img = cv2.imread(args.File)
src_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

max_binary_value = 255
threshold_type = cv2.THRESH_BINARY

for i in range(0,255,10):
  threshold_value = i
  _, dst = cv2.threshold(src_gray, threshold_value, max_binary_value, threshold_type)

  # Write an Image
  cv2.imwrite('output_' + str(i) + '.jpg',dst)
