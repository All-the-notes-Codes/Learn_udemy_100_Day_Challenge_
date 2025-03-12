### **String Manipulation**
#### **Subscripting using Indexing**
- Strings are indexed starting from **0** for positive indexing and **-1** for negative indexing.
```python
print("Hello"[1])     # 'e'
print("Karan"[-1])    # 'n' (last character)
print("Jason"[-2])    # 'o' (2nd last character)
```

#### **String Concatenation**
- Strings can be concatenated using `+`.
```python
print("123" + "456")  # Output: 123456
```

---

### **Numeric Data Types**
#### **Integer**
```python
print(20 + 40)  # Output: 60
```

#### **Large Integers (Readable format)**
- Use `_` (underscore) to separate digits for better readability.
```python
print(123_456_789)  # Output: 123456789
```

#### **Float (Decimal Numbers)**
```python
print(3.14321)  # Output: 3.14321
```

#### **Boolean Values**
```python
print(True)
print(False)
```

---

### **Checking Data Type (Type Checking)**
- Use `type()` to check the data type of a variable.
```python
print(type("Some text"))  # <class 'str'>
print(type(34223))        # <class 'int'>
print(type(False))        # <class 'bool'>
print(type(89.32))        # <class 'float'>
```

---

### **Type Conversion (Type Casting)**
- Convert one data type to another.
```python
print(int("897234"))   # Converts string to integer
print(float("425.5434"))  # Converts string to float
print(bool("False"))   # Any non-empty string returns True (even "False" as a string)
```

---

### **User Input**
- Prompt the user for input.
```python
email = input("Enter the Email here: ")
print(email)
```

---

### **String Functions**
#### **Length of a String (`len()`)**
- `len()` function only accepts string, bytes, tuple, list, or range.
```python
print(len("Jaskaran Singh"))  # Output: 14
```

---

### **Mathematical Operators**
#### **Division & Floor Division**
```python
print(10 / 2)  # Output: 5.0 (Float division)
print(10 // 2) # Output: 5 (Integer division)
```

#### **Exponentiation**
```python
print(2 ** 3)  # Output: 8 (2^3)
```

#### **Rounding Numbers**
- `round(number, decimal_places)`
```python
print(round(8.8))     # Output: 9
print(round(8.5))     # Output: 8 (Python follows Bankers' rounding)
print(round(22 / 7, 3)) # Output: 3.143 (Rounded to 3 decimal places)
```

---

### **Assignment Operators**
- Shortcuts for performing operations and assigning values.
```python
x = 10
x += 2  # x = x + 2
x -= 1  # x = x - 1
x *= 3  # x = x * 3
x /= 2  # x = x / 2
```

---

### **Formatted Strings (`f-strings`)**
- Used for inserting variables inside strings.
```python
name = "Jaskaran"
age = 25
print(f"My name is {name} and I am {age} years old.")
```

---

This version simplifies the notes, removes redundancy, and ensures clarity. Let me know if you'd like further refinements! 🚀
