from PIL import Image, ImageOps
import os

def crop_center(image, width, height):
    img_width, img_height = image.size
    left = (img_width - width) // 2
    top = (img_height - height) // 2
    right = (img_width + width) // 2
    bottom = (img_height + height) // 2
    return image.crop((left, top, right, bottom))

def convert_jpg_to_bmp(input_folder, output_folder, mode='scale', dither=Image.FLOYDSTEINBERG):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Create a palette object for e-paper display (black, white, green)
    pal_image = Image.new("P", (1,1))
    pal_image.putpalette((0,0,0,  255,255,255,  0,255,0,   0,0,255,  255,0,0,  255,255,0, 255,128,0) + (0,0,0)*249)

    # Get a list of all files in the input folder
    file_list = os.listdir(input_folder)

    for filename in file_list:
        # Check if the file is a JPEG image
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".bmp")

            # Open the JPEG image
            with Image.open(input_path) as img:
                # Check if image aspect ratio matches 800x480
                target_ratio = 800 / 480
                current_ratio = img.width / img.height
                
                if abs(current_ratio - target_ratio) > 0.01:  # Allow small floating point differences
                    # Crop to 800x480 aspect ratio
                    if current_ratio > target_ratio:
                        # Image is wider than target
                        new_width = int(img.height * target_ratio)
                        final_img = crop_center(img, new_width, img.height)
                    else:
                        # Image is taller than target
                        new_height = int(img.width / target_ratio)
                        final_img = crop_center(img, img.width, new_height)
                else:
                    final_img = img

                if mode == 'scale':
                    # Scale the image while maintaining aspect ratio
                    scale_ratio = max(800 / final_img.width, 480 / final_img.height)
                    new_width = int(final_img.width * scale_ratio)
                    new_height = int(final_img.height * scale_ratio)
                    resized_img = final_img.resize((new_width, new_height))
                    
                    # Create a new white background
                    final_img = Image.new('RGB', (800, 480), (255, 255, 255))
                    # Paste the resized image in the center
                    left = (800 - new_width) // 2
                    top = (480 - new_height) // 2
                    final_img.paste(resized_img, (left, top))
                else:  # mode == 'cut'
                    # Crop from center to exact 800x480
                    final_img = crop_center(final_img, 800, 480)

                # Apply color quantization and dithering
                quantized_img = final_img.quantize(dither=dither, palette=pal_image).convert('RGB')
                
                # Save as BMP
                quantized_img.save(output_path)
                print(f'Converted {filename} to {output_path}')

if __name__ == "__main__":
    input_folder = "images"  # Replace "images" with your input folder path
    output_folder = "bmp_images"  # Replace "bmp_images" with the desired output folder path
    
    # You can choose between 'scale' or 'cut' mode
    convert_jpg_to_bmp(input_folder, output_folder, mode='scale')
