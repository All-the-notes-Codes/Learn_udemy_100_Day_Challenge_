Below is a cleaned-up, more readable version of both scripts. I’ve kept your original logic and code alongside each “improved” version so you can compare and understand exactly what changed and why.

---

## Code 1: **Treasure Island**

### Your Original Code
```python
print("Welcome to Treasure Island. Your mission is to find the treasure.")
step1 = ((input(" LEFT or RIGHT : Type 'L' or 'R' ")).lower()[0])

if step1 == 'l':
   step2 = ((input(" Swim or Wait : Type Swim or Wait ")).lower()[0])    
   if step2 == "w":
      step3 = ((input(" Which Door ? : Red, Blue, or Yello ")).lower()[0])
      if step3 == 'y':
         print(" Winner !! ")
      else:
         print("Game Over !!")   
   else:
      print(" Game Over !!")
else:
   print(" Game Over !! ")
```

### Improved Version
```python
print("Welcome to Treasure Island. Your mission is to find the treasure.")

# First choice
choice1 = input("LEFT or RIGHT? (Type 'L' or 'R'): ").lower()
if not choice1.startswith('l'):
    print("Game Over!!")
    exit()

# Second choice
choice2 = input("Swim or Wait? (Type 'S' or 'W'): ").lower()
if not choice2.startswith('w'):
    print("Game Over!!")
    exit()

# Final choice
choice3 = input("Which Door? (Red, Blue, or Yellow): ").lower()
if choice3.startswith('y'):
    print("Winner!! You found the treasure.")
else:
    print("Game Over!!")
```

#### **What Changed & Why**
1. **Immediate Checks**: Instead of deeply nested `if` statements, we immediately check each choice. If the input is wrong, we end the game and exit the program. This makes the code flow simpler and easier to read.
2. **Use of `startswith()`**: Instead of `[0]`, using `startswith()` handles partial inputs more robustly (e.g., someone types `"Left"` vs `"l"`).
3. **Spelling Fix**: Corrected `"Yello"` to `"Yellow"`.
4. **Consistent Messages**: Standardized `"Game Over!!"` and `"Winner!!"` messages.
5. **Exit Early**: `exit()` stops the program immediately when a losing choice is made.

#### **Best Practices & Techniques**
- **Validate Input**: If you want to prevent the game from crashing on empty input, you could wrap each input in a loop that keeps asking until a valid answer is given.
- **Avoid Hard-coded Strings**: You could store valid directions, prompts, or results in dictionaries or lists to keep logic organized.
- **Consistent Style**: Use consistent naming (e.g., `choice1`, `choice2`, `choice3`) so that other developers can follow the code more easily.

---

## Code 2: **Pizza Python**

### Your Original Code
```python
print("Welcome to Python Deliveries")
size = (input("What size Pizza do you want? S, M, or L : ")).lower()
pepporoni = (input("Do you want pepporoni on your Pizza? Y or N : ")).lower()
extra_cheese = (input("Do you want extra cheese? Y or N: ")).lower()

bill = 0

# Price => Size
if size == 's':
  bill += 15
elif size == 'm':
  bill += 20
elif size == 'l':
  bill += 25
else:
   print("You typed the wrong input. ")

# Pepporoni
if pepporoni == 'y':
   if size == 's':
      bill += 2
   else:
      bill +=3

# Cheeze
if extra_cheese == 'y':
   bill +=1

print(f"Total Bill is : {bill} ")
```

### Improved Version
```python
print("Welcome to Python Deliveries")

# Dictionary for pizza size prices
size_prices = {
    's': 15,
    'm': 20,
    'l': 25
}

size = input("What size pizza do you want? (S, M, L): ").lower()
if size not in size_prices:
    print("Invalid pizza size. Exiting program.")
    exit()

bill = size_prices[size]

pepperoni = input("Do you want pepperoni on your pizza? (Y/N): ").lower()
if pepperoni == 'y':
    # Extra charge based on size
    bill += 2 if size == 's' else 3

extra_cheese = input("Do you want extra cheese? (Y/N): ").lower()
if extra_cheese == 'y':
    bill += 1

print(f"Your total bill is: ${bill}")
```

#### **What Changed & Why**
1. **Dictionary for Size Prices**: Instead of multiple `if/elif` lines, we use a dictionary (`size_prices`). This avoids repetition and makes the code more scalable.
2. **Exit Early if Invalid**: If a user types a size that doesn’t exist (e.g., `"x"`), we immediately notify them and `exit()`.
3. **Pepperoni Spelling**: Changed `pepporoni` to `pepperoni` for clarity.
4. **Clearer Inputs**: The prompts explicitly show `(S, M, L)` and `(Y/N)` to guide the user.
5. **Single Bill Calculation**: All charges accumulate in the `bill` variable in one place.

#### **Best Practices & Techniques**
- **Use Dictionaries**: Great for mapping items (like pizza sizes) to their prices without cluttering your logic with repetitive conditionals.
- **Clear Variable Names**: `pepperoni` is spelled correctly and is easier to read.
- **Input Validation**: If you want to handle “invalid” answers for pepperoni or cheese, you could do more checks or even re-prompt the user instead of ignoring it.

---

### Additional Tips for Both Scripts
- **Input Validation**: Consider re-prompting the user if they provide invalid input rather than immediately calling `exit()`. This can make the user experience smoother.
- **Functions**: If these scripts get longer, you can break the logic into functions (e.g., `def get_pizza_size()` or `def choose_direction()`) to keep them organized.
- **Comments & Docstrings**: Add brief comments about what each block does, especially if you plan to revisit or share the code.
- **Consistent Naming & Case**: Keep your variable names in a consistent style (e.g., all lowercase with underscores) to make the code more professional and uniform.

By adopting these improvements, you’ll reduce redundancy, handle edge cases more gracefully, and make your code more modular and maintainable.