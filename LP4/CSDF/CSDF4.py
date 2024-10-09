import pytsk3
import sys
import os


# Function to list deleted files in a filesystem
img_path = 'captcha_image.png'
def list_deleted_files(img_path):
    try:
        # Open the disk image
        img = pytsk3.Img_Info(img_path)

        # Open the filesystem (change to your filesystem type)
        fs = pytsk3.FS_Info(img)

        # Traverse the filesystem
        directory = fs.open_dir("/")

        print("Deleted files:")
        for entry in directory:
            # Check if the entry is deleted
            if entry.info.name.name.decode("utf-8").startswith(
                    ".") or entry.info.meta.type == pytsk3.TSK_FS_META_TYPE_UNALLOC:
                print(f"Deleted: {entry.info.name.name.decode('utf-8')} (Inode: {entry.info.meta.addr})")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python recover.py <image_file>")
        sys.exit(1)

    img_path = sys.argv[1]
    list_deleted_files(img_path)
