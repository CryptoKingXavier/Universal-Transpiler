from os import walk
from typing import Union
from zipfile import ZipFile, ZIP_DEFLATED
from os.path import isfile, relpath, dirname, join

def zip_file_and_folder(zip_filename, file_to_zip: Union[str, None] = None, folder_to_zip: Union[str, None] = None):
    with ZipFile(zip_filename, 'w', ZIP_DEFLATED) as zipf:
        # Zip the individual file and maintain its directory structure
        if file_to_zip:
            if isfile(file_to_zip):
                zipf.write(file_to_zip, relpath(file_to_zip, dirname(file_to_zip)))

        # Zip the folder, maintaining folder structure
        if folder_to_zip:
            for root, dirs, files in walk(folder_to_zip):
                for file in files:
                    file_path = join(root, file)
                    # Write the file to the zip, maintaining its relative path inside the zip
                    zipf.write(file_path, relpath(file_path, dirname(folder_to_zip)))
    
    print(f"Zipped {file_to_zip} and {folder_to_zip} into {zip_filename}, preserving file hierarchy.")
