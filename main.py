from typing import Union
from os.path import exists
from os import system, name
from threading import Thread
from sys import exit as sys_exit
from logging import basicConfig, DEBUG, info, error
from java_to_python_transpiler import java_to_python_from_file, TranspilerFailure

# Clear Terminal Screen
system("cls" if name == "nt" else "clear")


# Basic configuration for logging to the console
basicConfig(level=DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


class Transpiler:
	def __init__(self, java_file: Union[str, None] = "./Calculator.java") -> None:
		self.java_file: Union[str, None] = java_file
		if self.java_file and exists(self.java_file) and self.java_file.split(".")[-1] == "java":
			self.py_file: str = f".{self.java_file.split('.')[-2].lower()}.py"
			self.html_file: str = f".{self.java_file.split('.')[-2].lower()}.html"
			self.js_file: str = f"./__target__{self.java_file.split('.')[-2].lower()}.js"
		else: 
			sys_exit(error(" ⚠️ Invalid File! ⚠️"))

	def run(self):
		system("python -m http.server 8000 --bind 127.0.0.1")

	def java2py(self) -> None:
		py_data: Union[list[str], TranspilerFailure] = java_to_python_from_file(self.java_file).split("\n")

		if isinstance(py_data, TranspilerFailure):
			error(f" ⚠️ Transpiler-Failure ⚠️\nReason: {py_data}")
			return

		try:
			with open(self.py_file, "w") as python_file:
				for row in py_data:
					python_file.write(row + "\n")
			info(" ℹ️ Py2Js Process Completed! ℹ️")
			self.py2js()
			
		except Exception as e:
			error(f" Failed to write to file. Reason: {e}")

	def py2js(self) -> None:
		try:
			with open(self.html_file, "w") as web_file:
				web_file.write(f'<script type="module" src="{self.js_file}"></script>' + "\n")
			
			def tscrypt() -> None: 
				system(f"transcrypt -b -m -n {self.py_file}")

				# Running http.server in a separate thread
				info(" ℹ️ Initializing HTTP.Server! ℹ️")
				Thread(target=self.run).start()

			# Running transcrypt in a separate thread
			info(" ℹ️ Starting Async Conversion! ℹ️")
			Thread(target=tscrypt).start()

		except Exception as e:
			error(f" Failed to write to file. Reason: {e}")


if __name__ == "__main__":
	transpiler: Transpiler = Transpiler()
	transpiler.java2py()
