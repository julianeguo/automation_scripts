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
downloads_path = Path.home() / "Downloads"
print(downloads_path)

images_path = Path.home() / "Desktop" / "downloaded_files" / "images_downloaded"
pdfs_path = Path.home() / "Desktop" / "downloaded_files" / "pdfs_downloaded"
docs_path = Path.home() / "Desktop" / "downloaded_files" / "docs_downloaded"
other_formats_path = Path.home() / "Desktop" / "downloaded_files" / "other_formats_downloaded"
folders_path = Path.home() / "Desktop" / "downloaded_files" / "folders_downloaded"

image_extensions = [".png", ".jpg", ".jpeg", ".webp", ".avif", ".gif", ".heic"]
doc_extensions = [".docx", ".doc", ".xlsx"]

try:
    images_path.mkdir(parents=True, exist_ok=True)
    print(f"Directories created or already exist at '{images_path}'.")
    pdfs_path.mkdir(parents=True, exist_ok=True)
    print(f"Directories created or already exist at '{pdfs_path}'.")
    docs_path.mkdir(parents=True, exist_ok=True)
    print(f"Directories created or already exist at '{docs_path}'.")
    other_formats_path.mkdir(parents=True, exist_ok=True)
    print(f"Directories created or already exist at '{other_formats_path}'.")
    folders_path.mkdir(parents=True, exist_ok=True)
    print(f"Directories created or already exist at '{folders_path}'.")

except OSError as e:
    # This handles other OS-level errors like permission issues
    print(f"An OS error occurred: {e}")

for entry in downloads_path.iterdir(): # entry is the full path of every file in downloads
    if entry.is_file(): # images
        if entry.suffix.lower() in image_extensions:
            dest_path = collision_handle(images_path / entry.name, entry, images_path)
            print(f"Successfully moved {entry.name} to {images_path}")
            shutil.move(entry, dest_path)
        elif entry.suffix.lower() == ".pdf":
            dest_path = collision_handle(pdfs_path / entry.name, entry, pdfs_path)
            print(f"Successfully moved {entry.name} to {pdfs_path}")
            shutil.move(entry, dest_path)
        elif entry.suffix.lower() in doc_extensions:
            dest_path = collision_handle(docs_path / entry.name, entry, docs_path)
            print(f"Successfully moved {entry.name} to {docs_path}")
            shutil.move(entry, dest_path)
        else:
            dest_path = collision_handle(other_formats_path / entry.name, entry, other_formats_path)
            print(f"Successfully moved {entry.name} to {other_formats_path}")
            shutil.move(entry, dest_path)
    else: #folders
        dest_path = collision_handle(folders_path / entry.name, entry, folders_path)
        print(f"Successfully moved folder {entry.name} to {folders_path}")
        shutil.move(entry, dest_path)
