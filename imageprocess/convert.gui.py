import sys
import os
from PIL import Image, ImagePalette, ImageOps
import argparse

def convert_images(input_folder, output_folder, display_direction=None, display_mode='scale', display_dither=Image.FLOYDSTEINBERG):
    # Get the absolute path of the current script
    current_script_path = os.path.abspath(os.path.dirname(__file__))

    # Construct the absolute path for the input folder
    input_folder = os.path.abspath(os.path.join(current_script_path, input_folder))

    # Get the absolute path for the output folder
    output_folder = os.path.abspath(os.path.join(current_script_path,output_folder))

    # Create the input and output folders if they don't exist
    os.makedirs(output_folder, exist_ok=True)

    
    file_list = os.listdir(input_folder)

    # Filter only JPEG files
    jpg_files = [filename for filename in file_list if filename.lower().endswith('.jpg')]

    for input_filename in jpg_files:
        # Check whether the input file exists
        input_filepath = os.path.join(input_folder, input_filename)
        if not os.path.isfile(input_filepath):
            print(f'Error: file {input_filepath} does not exist')
            continue

        # Read input image
        input_image = Image.open(input_filepath)

        # Get the original image size
        width, height = input_image.size

        # Specified target size
        if display_direction:
            if display_direction == 'landscape':
                target_width, target_height = 800, 480
            else:
                target_width, target_height = 480, 800
        else:
            if width > height:
                target_width, target_height = 800, 480
            else:
                target_width, target_height = 480, 800

        if display_mode == 'scale':
            # Computed scaling
            scale_ratio = max(target_width / width, target_height / height)

            # Calculate the size after scaling
            resized_width = int(width * scale_ratio)
            resized_height = int(height * scale_ratio)

            # Resize image
            output_image = input_image.resize((resized_width, resized_height))

            # Create the target image and center the resized image
            resized_image = Image.new('RGB', (target_width, target_height), (255, 255, 255))
            left = (target_width - resized_width) // 2
            top = (target_height - resized_height) // 2
            resized_image.paste(output_image, (left, top))
        elif display_mode == 'cut':
            # Calculate the fill size to add or the area to crop
            if width / height >= target_width / target_height:
                # The image aspect ratio is larger than the target aspect ratio, and padding needs to be added on the left and right
                delta_width = int(height * target_width / target_height - width)
                padding = (delta_width // 2, 0, delta_width - delta_width // 2, 0)
                box = (0, 0, width, height)
            else:
                # The image aspect ratio is smaller than the target aspect ratio and needs to be filled up and down
                delta_height = int(width * target_height / target_width - height)
                padding = (0, delta_height // 2, 0, delta_height - delta_height // 2)
                box = (0, 0, width, height)

            resized_image = ImageOps.pad(input_image.crop(box), size=(target_width, target_height), color=(255, 255, 255), centering=(0.5, 0.5))

        # Create a palette object
        pal_image = Image.new("P", (1,1))
        pal_image.putpalette( (0,0,0,  255,255,255,  0,255,0,   0,0,255,  255,0,0,  255,255,0, 255,128,0) + (0,0,0)*249)

        # The color quantization and dithering algorithms are performed, and the results are converted to RGB mode
        quantized_image = resized_image.quantize(dither=display_dither, palette=pal_image).convert('RGB')

        # Save output image
        output_filename = os.path.splitext(input_filename)[0] + '_' + display_mode + '_output.bmp'
        output_filepath = os.path.join(output_folder, output_filename)
        quantized_image.save(output_filepath)

        print(f'Successfully converted {input_filepath} to {output_filepath}')

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Process some images.')

    # Add orientation parameter
    parser.add_argument('--dir', choices=['landscape', 'portrait'], help='Image direction (landscape or portrait)')
    parser.add_argument('--mode', choices=['scale', 'cut'], default='scale', help='Image conversion mode (scale or cut)')
    parser.add_argument('--dither', type=int, choices=[Image.NONE, Image.FLOYDSTEINBERG], default=Image.FLOYDSTEINBERG, help='Image dithering algorithm (NONE(0) or FLOYDSTEINBERG(3))')
    parser.add_argument('--input_folder', type=str, default='jpg', help='Input folder containing JPEG images')
    parser.add_argument('--output_folder', type=str, default='bmp', help='Output folder for BMP images')

    # Parse command line arguments
    args = parser.parse_args()

    # Convert images using the specified arguments
    convert_images(args.input_folder, args.output_folder, args.dir, args.mode, args.dither)

if __name__ == "__main__":
    #to convert files in jpg to bmp files
    main()
