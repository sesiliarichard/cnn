from PIL import Image
import math
from google.colab import files

def file_to_image(input_file, output_image):
    # Read the file's binary data
    with open(input_file, 'rb') as file:
        data = file.read()

    # Calculate the dimensions of the image
    size = int(math.ceil(math.sqrt(len(data))))
    image_size = (size, size)

    # Create a new image with the calculated size
    image = Image.new('L', image_size)  # 'L' mode for grayscale

    # Fill the image with pixel values from the file data
    image.putdata(list(data))

    # If the data is smaller than the image size, pad with zeros
    if len(data) < size * size:
        image.putdata(list(data) + [0] * (size * size - len(data)))

    # Save the image
    image.save(output_image)
    print(f"File converted to image and saved as {output_image}")

# Upload the file
uploaded = files.upload()

# Get the uploaded file name
input_file = list(uploaded.keys())[0]

# Specify the output image path
output_image = 'output.png'

# Call the function
file_to_image(input_file, output_image)
