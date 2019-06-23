# Create iOS AppIcon.appiconset from an image file.
#
# References:
# - https://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/app-icon/

import sys
import os
import shutil

from PIL import Image

OUTPUT_DIR = 'output'
RESOURCE_DIR = 'resource'
APPICON_DIR = 'AppIcon.appiconset'
ICON_SIZE_ARRAY = [
  29,
  40,
  50,
  57,
  58,
  72,
  76,
  80,
  87,
  100,
  114,
  120,
  144,
  152,
  180,
  1024,
]


if __name__ == '__main__':
  if len(sys.argv) < 2:
    sys.exit('Please specify an image file.')

  srcImage = Image.open(sys.argv[1])
  srcImage = srcImage.convert("RGB")
  width, height = srcImage.size
  if width < ICON_SIZE_ARRAY[-1] or height < ICON_SIZE_ARRAY[-1]:
    sys.exit('The width and height must be least 1024 px.')

  if os.path.isdir(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)

  shutil.copytree(RESOURCE_DIR, OUTPUT_DIR)

  for elm in ICON_SIZE_ARRAY:
    dstPath = os.path.join(OUTPUT_DIR, APPICON_DIR)
    dstPath = os.path.join(dstPath, str(elm) + '.png')

    dstImage = srcImage.resize((elm, elm), Image.BICUBIC)
    dstImage.save(dstPath)
