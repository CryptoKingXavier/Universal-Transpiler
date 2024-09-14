# Transcrypt - Py2Js

**Transcrypt** is a Python-to-JavaScript transpiler, meaning it allows you to write Python code that can be converted into JavaScript. This is useful for web development because it enables developers to use Python, a popular and versatile language, for client-side web applications that traditionally require JavaScript.

### Key Features of Transcrypt

1. **Python Syntax**: You can write code in idiomatic Python, and Transcrypt will convert it into efficient, readable JavaScript. It supports Python 3.x syntax, including modern features like list comprehensions, decorators, and generator functions.

2. **Seamless Integration with JavaScript**: Transcrypt allows for easy integration with existing JavaScript libraries and frameworks. You can import and use JavaScript modules directly from Python and vice versa.

3. **Optimized for Performance**: The transpiled JavaScript code is optimized for size and speed, making it suitable for production environments. Transcrypt compiles Python code into JavaScript that is comparable in performance to handwritten JavaScript.

4. **Source Maps**: It generates source maps for debugging, allowing you to debug the Python source code in your browser's developer tools instead of the transpiled JavaScript.

5. **Static Type Checking**: Transcrypt supports optional static type checking using type hints (annotations), making it easier to catch errors early in development.

6. **Built-in Libraries**: Transcrypt includes a small, built-in JavaScript library that mimics the behavior of Python's standard library, allowing you to use Python's built-in functions and types (like `list`, `dict`, `set`, etc.) in your JavaScript code.

7. **Support for Classes and Modules**: It supports object-oriented programming features like classes, inheritance, and modules, allowing for a more structured approach to JavaScript development.

### How Transcrypt Works

1. **Write Python Code**: You write your web application code in Python.
2. **Transpile to JavaScript**: Use the Transcrypt command-line tool to convert the Python code into JavaScript.
   ```bash
   transcrypt -b yourscript.py
   ```
3. **Integrate with Web Application**: Include the transpiled JavaScript file in your HTML like any other JavaScript file.
4. **Run in Browser**: Your Python code, now converted to JavaScript, runs natively in the browser.

### Use Cases for Transcrypt

- **Web Development**: Developers who prefer Python can use it for front-end development instead of JavaScript.
- **Prototyping**: Quickly prototype web applications using Python.
- **Code Sharing**: Reuse code between server-side (Python) and client-side (JavaScript) environments.

### Example

Here's a simple Python code snippet using Transcrypt:

**Python Code (example.py):**
```python
class Calculator:
    def add(self, num1, num2):
        return num1+num2

    def subtract(self, num1, num2):
        return num1-num2

    def multiply(self, num1, num2):
        return num1*num2

    def divide(self, num1, num2):
        if num2 == 0:
            return 0
        else:
            return num1/num2

    def main(self):
        print(self.add(3, 4))
        print(self.subtract(3, 4))
        print(self.multiply(3, 4))
        print(self.divide(3, 4))

calc = Calculator()
calc.main()
```

After transpiling with Transcrypt, it will generate a corresponding JavaScript file (`example.js`), which you can include in your web page.

### Conclusion

Transcrypt is a powerful tool for Python developers looking to leverage their skills in web development by writing client-side code in Python instead of JavaScript. It is particularly useful for those who want to maintain a consistent programming language across the full stack.

### Compiling a Python File

```bash
transcrypt -b -m -n yourscript.py
```