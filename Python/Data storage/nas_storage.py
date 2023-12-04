import os
import shutil
import sys

from dotenv import load_dotenv

load_dotenv()

mount_path = os.getenv("DRIVE_MOUNT_PATH")


def get_all_files():
    try:
        files = [f for f in os.listdir(mount_path)]
        return files
    except FileNotFoundError:
        raise


def get_file(filename):
    try:
        files = get_all_files()
        if filename in files:
            return os.path.join(mount_path, filename)
    except FileNotFoundError:
        raise


def upload_file(filepath):
    try:
        destination_path = os.path.join(mount_path, os.path.basename(filepath))

        shutil.copy(filepath, destination_path)

        return True
    except FileNotFoundError:
        raise
    except IsADirectoryError:
        raise


if __name__ == '__main__':
    try:
        file_paths = sys.argv[1:]
        successful_uploads = []
        failed_uploads = []

        if not file_paths:
            print("No filepath specified")
            exit(1)

        for i, file in enumerate(file_paths):
            try:
                upload_file(file)
                successful_uploads.append(os.path.basename(file))
            except FileNotFoundError:
                print(f"File not found with filepath {file}")
                failed_uploads.append(os.path.basename(file))
            except IsADirectoryError:
                print(f"Specified file was a directory")
                failed_uploads.append(os.path.basename(file))
    finally:
        if successful_uploads:
            print("Succesful uploads:\n")
            for file in successful_uploads:
                print(f"File {file} upload successful")
        if failed_uploads:
            print("\nFailed uploads:\n")
            for file in failed_uploads:
                print(f"File {file} upload failed")
