from pathlib import Path
import shutil

# creates empty folder called "screenshots" on desktop if it doesn't exist
# creates empty folder called "images" on desktop if it doesn't exist
# creates empty folder called "pdfs" on desktop if it doesn't exist
# detects which files are labeled as screenshots in metadata -> puts in "screenshots" folder
    # if file with same name exists, rename new file
# detects which remaining files are labeled as .png, .jpeg., .webp -> puts in "images" folder
    # if file with same name exists, rename new file

# helper
def collision_handle(orig_dest_path, file, folder_path):
    if orig_dest_path.is_file():
        print("collision found!")
        # finds correct file name
        cur_dest_path = orig_dest_path
        counter = 1
        while cur_dest_path.is_file():
            cur_dest_path = folder_path / (file.stem + " " + str(counter) + file.suffix)
            counter += 1
        return cur_dest_path
    else:
        return orig_dest_path


# main code
desktop_path = Path.home() / "Desktop"
print(desktop_path)

screenshots_path = Path.home() / "Desktop" / "screenshots"
images_path = Path.home() / "Desktop" / "images"
pdfs_path = Path.home() / "Desktop" / "pdfs"

image_extensions = [".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif"]

try:
    screenshots_path.mkdir(parents=True, exist_ok=True)
    print(f"Directories created or already exist at '{screenshots_path}'.")
    images_path.mkdir(parents=True, exist_ok=True)
    print(f"Directories created or already exist at '{images_path}'.")
    pdfs_path.mkdir(parents=True, exist_ok=True)
    print(f"Directories created or already exist at '{pdfs_path}'.")

except OSError as e:
    # This handles other OS-level errors like permission issues
    print(f"An OS error occurred: {e}")

for entry in desktop_path.iterdir(): # entry is the full path of every file in desktop
    if entry.is_file():
        # screenshots
        if str(entry.name).startswith("Screenshot") and entry.suffix.lower() == ".png":
            dest_path = collision_handle(screenshots_path / entry.name, entry, screenshots_path)
            print(f"Successfully moved screenshot {entry.name} to {screenshots_path}")
            shutil.move(entry, dest_path)
        # images
        elif entry.suffix.lower() in image_extensions:
            dest_path = collision_handle(images_path / entry.name, entry, images_path)
            print(f"Successfully moved image {entry.name} to {images_path}")
            shutil.move(entry, dest_path)
        elif entry.suffix.lower() == ".pdf":
            dest_path = collision_handle(pdfs_path / entry.name, entry, pdfs_path)
            print(f"Successfully moved image {entry.name} to {pdfs_path}")
            shutil.move(entry, dest_path)

