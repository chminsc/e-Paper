# pip3 install pillow
from PIL import Image

import os

def convert_jpg_to_bmp(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    file_list = os.listdir(input_folder)

    for filename in file_list:
        # Check if the file is a JPEG image
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".bmp")

            # Open the JPEG image
            with Image.open(input_path) as img:
                # Convert and save as BMP
                img.save(output_path)

if __name__ == "__main__":
    input_folder = "images"  # Replace "images" with your input folder path
    output_folder = "bmp_images"  # Replace "bmp_images" with the desired output folder path

    convert_jpg_to_bmp(input_folder, output_folder)
