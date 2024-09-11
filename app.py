# Importing required libraries
from re import search
from logging import error
from os.path import exists
from typing import Mapping
from java_to_python_transpiler import java_to_python_from_file


# Program Entry
def main() -> None:
  transpiler: Java2PyTranspiler = Java2PyTranspiler(utf_file="./test.utf")
  if transpiler.validate_file():
    transpiler.codebase_to_file()
    transpiler.java_to_python(file_path="./Calculator.java")


class Java2PyTranspiler:
  def __init__(self, utf_file: str) -> None:
    self.utf_file = utf_file
    self.data: list[str] | None = None
    self.code_segments: list[list[str]] | None = None
    self.codebase: Mapping[str, list[str]] | None = None
    self.code_headers: list[tuple[str, str]] | None = None
  
  # Function to validate file format and check existence
  def validate_file(self) -> bool:
    if self.utf_file.split(".")[-1] == "utf" and exists(self.utf_file):
      # Opening UTF -> Universal Transpilable File and splitting file per line, Removing all `\n` -> newlines
      with open(self.utf_file, "r") as file:
        self.data = [row for row in file.read().split("\n")]
      
      # List of all extracted code segments per HLL
      if self.data:
        self.code_headers = [
          (row, f"</{row.split('<')[-1]}") for row in self.data \
            if search("^<code-[a-zA-Z]+>$", row)
        ]
        
        if self.code_headers:
          print(f"\nCode Headers: {self.code_headers}\n")
          self.extract_code_segments(self.data, self.code_headers)
          return True
        else:
          error("ERROR: No valid code headers found in the file.")
          return False
        
      else: 
        error(f"ERROR: Reading Empty File in `{self.utf_file}`")
        return False
    
    else:
      error(f"ERROR: Invalid file format or file does not exist: `{self.utf_file}`")


  # Function to extract code segments between headers
  def extract_code_segments(self, rows: list[str], code_headers: list[tuple[str, str]]) -> None:
    # Extract code segments between identified headers
    self.code_segments = [
      rows[rows.index(header[0]) + 1 : rows.index(header[1])] \
        for header in code_headers
    ]

    # Updating code base mapping
    self.codebase = dict(zip([header[0] for header in code_headers], self.code_segments))


  # Code Base Viewer
  def codebase_viewer(self, key: str = str()) -> None:
    if key in self.codebase:
      for row in self.codebase.get(key):
        print(row)
    else:
      error(f"ERROR: Codebase key `{key}` not found.")


  # Code Base To File
  def codebase_to_file(self) -> None:
    for header, segment in self.codebase.items():
      try:
        with open("./main.py", "w") if header == "<code-python>" else \
          open(f"./{self.codebase.get('<code-java>')[0].split(' ')[-2]}.java", "w") as file:
            for row in segment:
              file.write(row + "\n")
      except Exception as e:
        error(f"ERROR: Failed to write to file. Reason: {e}")


  # Optionally Convert Java -> Python
  def java_to_python(self, file_path: str | None = None) -> None:
    if file_path:
      try:
        print(java_to_python_from_file(file_path))
      except Exception as e:
        error(f"ERROR: Java to Python conversion failed. Reason: {e}")


main()
