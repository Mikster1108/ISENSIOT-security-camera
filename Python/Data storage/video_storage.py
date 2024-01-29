import os
import shutil
import sys
import logging

from dotenv import load_dotenv

load_dotenv()

mount_path = os.getenv("DRIVE_MOUNT_PATH")
local_video_directory = os.getenv("LOCAL_VIDEO_DIRECTORY")

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


def get_all_files():
    try:
        files = [f for f in os.listdir(local_video_directory)]
        return files
    except FileNotFoundError:
        raise


def get_file(filename):
    try:
        files = get_all_files()
        if filename in files:
            return os.path.join(local_video_directory, filename)
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        raise


def delete_file(filepath):
    try:
        os.remove(filepath)
    except FileNotFoundError:
        raise


def upload_file_to_nas():
    try:
        file_paths = get_all_files()
        successful_uploads = []
        failed_uploads = []

        if not os.path.exists(mount_path):
            logging.critical("Drive mount not found")
            exit(1)

        if not file_paths:
            logging.critical("No filepath specified")
            exit(1)

        for i, base_filename in enumerate(file_paths):
            try:
                file = get_file(base_filename)
                destination_path = os.path.join(mount_path, os.path.basename(file))

                shutil.copy(file, destination_path)
                successful_uploads.append(base_filename)

                delete_file(file)
            except FileNotFoundError:
                logging.error(f"File not found")
                failed_uploads.append(os.path.basename(base_filename))
            except IsADirectoryError:
                logging.error(f"Specified file was a directory")
                failed_uploads.append(os.path.basename(base_filename))
    finally:
        if successful_uploads:
            logging.info("Successful uploads:")
            for file in successful_uploads:
                logging.info(f"File {file} upload successful")
        if failed_uploads:
            logging.error("Failed uploads:")
            for file in failed_uploads:
                logging.error(f"File {file} upload failed")


if __name__ == '__main__':
    enable_logging = False

    if not enable_logging:
        logging.disable(logging.CRITICAL)

    upload_file_to_nas()
