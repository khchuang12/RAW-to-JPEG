import os
import rawpy
import imageio

def convert_raw_to_jpeg(raw_folder):
    # Create an 'JPEG' folder inside the raw folder if it doesn't exist
    jpeg_folder = os.path.join(raw_folder, 'JPEG')
    os.makedirs(jpeg_folder, exist_ok=True)

    # List all files in the raw folder with supported RAW extensions
    raw_files = [f for f in os.listdir(raw_folder) if any(f.lower().endswith(ext) for ext in ['.arw', '.cr2', '.dng', '.nef', '.raw'])]

    for raw_file in raw_files:
        raw_path = os.path.join(raw_folder, raw_file)

        # Create an output file path with the same name but a .jpg extension
        output_path = os.path.join(jpeg_folder, os.path.splitext(raw_file)[0] + '.jpg')

        # Convert RAW to JPEG
        convert_raw_to_jpeg_single(raw_path, output_path)

def convert_raw_to_jpeg_single(raw_path, output_path):
    try:
        # Open the RAW image using rawpy
        with rawpy.imread(raw_path) as raw:
            # Convert to RGB
            rgb = raw.postprocess()

            # Save the image as JPEG using imageio
            imageio.imsave(output_path, rgb)

            print(f'Converted {raw_path} to {output_path}')

    except Exception as e:
        # Handle any exceptions that might occur during the conversion
        print(f'Error converting {raw_path}: {e}')

if __name__ == "__main__":
    # Replace 'raw_folder' with the actual path to your RAW images
    raw_folder = r'your/local/folder/path'

    # Call the main conversion function
    convert_raw_to_jpeg(raw_folder)
