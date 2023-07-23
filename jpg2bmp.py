from PIL import Image

import os

def crop_center(image, width, height):
    img_width, img_height = image.size
    left = (img_width - width) // 2
    top = (img_height - height) // 2
    right = (img_width + width) // 2
    bottom = (img_height + height) // 2
    return image.crop((left, top, right, bottom))

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
                # Crop the image to 800x480 from the center
                cropped_img = crop_center(img, 800, 480)

                # Convert and save as BMP
                cropped_img.save(output_path)

if __name__ == "__main__":
    input_folder = "images"  # Replace "images" with your input folder path
    output_folder = "bmp_images"  # Replace "bmp_images" with the desired output folder path

    convert_jpg_to_bmp(input_folder, output_folder)
