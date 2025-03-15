Your functions are straightforward, but they can be slightly improved for flexibility and best practices. Here’s a cleaner version with improvements:

### **Improved Version**
```python
def greet(name="Guest"):
    """Prints a greeting message. Defaults to 'Guest' if no name is provided."""
    print(f"Hello, {name}!")

def goodbye(name="Guest"):
    """Prints a farewell message. Defaults to 'Guest' if no name is provided."""
    print(f"Goodbye, {name}!")

full_name = "Jaskaran Singh"
```

### **Improvements & Best Practices**
1. **Added default value**  
   - Instead of an empty string `""`, I set a default name `"Guest"`, making it more user-friendly.
   - Example:
     ```python
     greet()  # Output: Hello, Guest!
     ```

2. **Added Docstrings**  
   - This provides clarity on what each function does.

3. **Kept the `full_name` variable**  
   - If it's a constant, consider renaming it to `FULL_NAME` as per Python naming conventions.

This version keeps your functionality intact while improving readability and usability. 🚀
