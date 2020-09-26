---
title: ""
draft: false
weight:
lesson: true
descriptor: ""
---

# While Loop and Numbers
---

We can manipulate variables to represent a range of numbers by repetitively applying arithmetic operators.

### Recall: Assignment Operators

```python
    a = b   # (Assignment)
    a += b  # (Add & Assign)
    a -= b  # (Subtract & Assign)
    a *= b  # (Multiply & Assign)
    a /= b  # (Divide & Assign)
    a //= b # (Floor Divide & Assign)
    a **= b # (Exponentiate & Assign)
    a %= b  # (Modulo & Assign)
```

These operators will manipulate/update the left variable with the result of the arithmetic operation with the right operand.

If we can use these inside a while loop code block, we can repetitively change the variable to make a condition become False to end the while loop.


```python
# Counting from 1 to 10

num = 1
while num <= 10:
    print(num)
    num += 1
# end of while
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10



```python
# Counting down from 10 to 1:

num = 10
while num > 0:
    print(num)
    num -= 1
# end of while
```

    10
    9
    8
    7
    6
    5
    4
    3
    2
    1



```python
# Collatz Sequence
# The conjecture of the collatz sequence is that any number following the set of rules will always end up at 1

# Rule:
# If N is even, divide it by 2
# If N is odd, multiply by 3 then add 1

num = 13 # a random starting value

while num != 1:
    print(num)
    
    if num % 2 == 0:
        num //= 2
    else:
        num *= 3
        num += 1
# end of while
print(num)
```

    13
    40
    20
    10
    5
    16
    8
    4
    2
    1

