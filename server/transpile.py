from typing import Union
from shutil import rmtree
from os.path import exists
from threading import Thread
from os import system, unlink
from zipper import zip_file_and_folder
from logging import basicConfig, DEBUG, info, error
from java_to_python_transpiler import java_to_python_from_file, TranspilerFailure


# Basic configuration for logging to the console
basicConfig(level=DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


class Transpiler:
    def __init__(self, java_file: Union[str, None] = None, python_file: Union[str, None] = None) -> None:
        # Dynamic file name generator
        if java_file and exists(java_file) and java_file.split(".")[-1] == "java":
            self.java_file: str = java_file
            self.py_file: str = f".{self.java_file.split('.')[-2].lower()}.py"
            self.zip_filename: str = f".{self.java_file.split('.')[-2].lower()}.zip"
            self.file_to_zip: str = self.py_file
        if python_file and exists(python_file) and python_file.split(".")[-1] == "py":
            self.py_file: str = python_file
            self.html_file: str = f".{self.py_file.split('.')[-2].lower()}.html"
            self.temp: list[str] = self.py_file.split('.')[-2].lower().split("/")[2:]
            self.temp.insert(0, "__target__")
            self.js_file: str = f"./{'/'.join(self.temp)}.js"
            self.zip_filename: str = f".{self.py_file.split('.')[-2].lower()}.zip"
            self.file_to_zip: str = self.html_file
            self.temp = self.py_file.split(".")[-2].lower().split("/")[:2]
            self.temp.append("__target__")
            self.folder_to_zip: str = f".{'/'.join(self.temp)}"
            

    def java2py(self) -> None:
        py_data: Union[list[str], TranspilerFailure] = java_to_python_from_file(self.java_file).split("\n")

        if isinstance(py_data, TranspilerFailure):
            error(f" ⚠️ Transpiler-Failure ⚠️\nReason: {py_data}")
            return

        try:
            with open(self.py_file, "w") as python_file:
                for row in py_data:
                    python_file.write(row + "\n")
            zip_file_and_folder(zip_filename=self.zip_filename, file_to_zip=self.file_to_zip)
            # Cleaning up unnecessary files
            unlink(self.py_file)
            unlink(self.java_file)
            info(" ℹ️ Py2Js Process Completed! ℹ️")
            
        except Exception as e:
            error(f" Failed to write to file. Reason: {e}")

    def py2js(self) -> None:
        try:
            with open(self.html_file, "w") as web_file:
                web_file.write(f'<script type="module" src="{self.js_file}"></script>' + "\n")
            
            def tscrypt() -> None: 
                system(f"transcrypt -b -m -n {self.py_file}")
                zip_file_and_folder(zip_filename=self.zip_filename, file_to_zip=self.file_to_zip, folder_to_zip=self.folder_to_zip)
                # Cleaning up unnecessary files
                unlink(self.py_file)
                unlink(self.html_file)
                rmtree(self.folder_to_zip)

            # Running transcrypt in a separate thread
            info(" ℹ️ Starting Async Conversion! ℹ️")
            Thread(target=tscrypt).start()

        except Exception as e:
            error(f" Failed to write to file. Reason: {e}")

