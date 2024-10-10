import hashlib
import imghdr
from PIL import Image
import exifread
import os

# Function to extract metadata (EXIF data)
def extract_metadata(image_path):
    print(f"Extracting metadata for {image_path}...")
    try:
        with open(image_path, 'rb') as img_file:
            tags = exifread.process_file(img_file, details=False)
            for tag in tags:
                print(f"{tag}: {tags[tag]}")
    except Exception as e:
        print(f"Error extracting metadata: {e}")

# Function to calculate image hash (SHA-256)
def calculate_image_hash(image_path):
    print(f"Calculating SHA-256 hash for {image_path}...")
    try:
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
            return hashlib.sha256(img_data).hexdigest()
    except Exception as e:
        print(f"Error calculating hash: {e}")
        return None

# Function to validate file format
def validate_image_format(image_path):
    print(f"Validating file format for {image_path}...")
    file_type = imghdr.what(image_path)
    if file_type:
        print(f"File format detected: {file_type}")
        return file_type
    else:
        print("Unknown file format or corrupted file.")
        return None

# Function to check image integrity (basic error level analysis placeholder)
def check_image_integrity(image_path):
    print(f"Checking image integrity for {image_path}...")
    try:
        with Image.open(image_path) as img:
            img.show()  # Display the image to verify it's viewable.
            print("Image opened successfully. No basic corruption detected.")
    except Exception as e:
        print(f"Error in image integrity: {e}")

# Main forensic tool function
def digital_forensic_tool(image_path):
    # Check if file exists
    if not os.path.isfile(image_path):
        print(f"File not found: {image_path}")
        return

    # Step 1: Extract metadata (EXIF)
    extract_metadata(image_path)

    # Step 2: Calculate image hash (SHA-256 for integrity)
    image_hash = calculate_image_hash(image_path)
    if image_hash:
        print(f"SHA-256 hash: {image_hash}")

    # Step 3: Validate file format
    validate_image_format(image_path)

    # Step 4: Check image integrity
    check_image_integrity(image_path)

# Usage example
if __name__ == "__main__":
    # Replace with the path of the image you want to analyze
    image_path = 'img.png'
    digital_forensic_tool(image_path)
