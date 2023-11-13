# RAW to JPEG Converter

A simple Python script to convert RAW image files (ARW, CR2, DNG, NEF, RAW) to JPEG format. This tool creates a 'JPEG' folder within the specified RAW image folder, processes each RAW file, and saves the resulting JPEG images in the created folder.

## Features

- **RAW to JPEG Conversion:** Converts supported RAW image formats to JPEG.
- **Folder Organization:** Creates a 'JPEG' subfolder to store the converted JPEG images.
- **Supported Formats:** Handles RAW formats including ARW, CR2, DNG, NEF, and RAW.

## Dependencies

- **rawpy:** Used for reading and processing RAW image files.
- **imageio:** Enables saving images in JPEG format.

## Usage

1. **Clone Repository:**
   ```bash
   git clone https://github.com/your-username/raw-to-jpeg-converter.git
2. **Navigate to Project Folder**
   ```bash
   cd raw-to-jpeg-converter
3. **Install Dependencies**
   ```bash
   pip install rawpy imageio
5. **Run the Script**
   ```bash
   python raw_to_jpeg_converter.py
6. **Specify RAW Image Folder**
   Replace 'raw_folder' with the actual path to your folder containing RAW images in the script.

## Example

- Consider running the script on a folder containing RAW images:
   ```bash
  python raw_to_jpeg_converter.py

## Contributing

- Contributions are welcome! Feel free to open issues, submit feature requests, or create pull requests to enhance the functionality of the script.
