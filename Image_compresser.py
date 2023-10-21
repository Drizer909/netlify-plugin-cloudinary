import numpy as np
from PIL import Image

def image_compression(image, quality=75):
  """
  Compresses an image using the JPEG algorithm.

  Args:
    image: A PIL Image object.
    quality: The quality of the compressed image, from 0 to 100.

  Returns:
    A compressed PIL Image object.
  """

  # Convert the image to a NumPy array.
  image_array = np.array(image)

  # Compress the image using the JPEG algorithm.
  compressed_image_array = Image.fromarray(image_array).compress(quality)

  # Convert the compressed NumPy array back to a PIL Image object.
  compressed_image = Image.fromarray(compressed_image_array)

  return compressed_image


# Example usage:

# Load the image.
image = Image.open("image.jpg")

# Compress the image.
compressed_image = image_compression(image)

# Save the compressed image.
compressed_image.save("compressed_image.jpg")
