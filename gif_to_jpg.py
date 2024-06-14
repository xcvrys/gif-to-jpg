import os
import sys
from PIL import Image

def gif_to_jpg(gif_path, jpg_dir):
  """
  Function to convert a GIF file to a series of JPG images.

  :param gif_path: Path to the GIF file.
  :param jpg_dir: Directory to save the JPG images.
  
  :return: None
  """
  # Check if the GIF file exists
  try:
    gif = Image.open(gif_path)
    gif.seek(0)
  except Exception as e:
    print('\033[91mError:', e, '\033[0m')
    return

  frames = 0

  # Convert the GIF file to a series of JPG images
  while True:
    try:
      jpg = gif.convert('RGB')
      jpg_filename = os.path.join(jpg_dir, str(gif.tell()) + '.jpg')
      jpg.save(jpg_filename)
      gif.seek(gif.tell() + 1)
      frames += 1
    except EOFError:
      print(f'\033[92mSucces, {frames} created\033[0m')
      break
    except Exception as e:
      print('\033[91mError:', e, '\033[0m')
      break

if __name__ == '__main__':
  gif_path = sys.argv[1]
  jpg_dir = sys.argv[2]

  if not os.path.exists(jpg_dir):
    os.makedirs(jpg_dir)

  gif_to_jpg(gif_path, jpg_dir)
