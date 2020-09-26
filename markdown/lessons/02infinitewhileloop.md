---
title: ""
draft: false
weight:
lesson: true
descriptor: ""
---

# Infinite While Loop
---

An infinite loop is an iteration that never ends. It may seem like a bad idea to have an infinite loop; however, there are scenarios that may require an infinite loop.

The most common scenario is when a program __needs to be on always__.

```python

    # Infinite While Loop on Python Example Format
    
    while True:
        
        Your Code Here
    
    # end of while
```

In the code above, since the while loop's condition cannot ever be ```False```, the code block inside the loop will continue to run unless there is forceful intervention: _Force Quit_.

### ```break``` keyword

**WARNING:** It is not recommended for beginner programmers to rely upon infinite while loops and the ```break``` keyword. 

**It is better to write sound conditions on while loops to write loops that terminate on their own.**

```break``` is a built-in keyword in Python that allows us to exit an iteration when needed. It is often used within a conditional statement such that we exit the loop prematurely when a condition is met.

```python

    while True:
        
        Some Code
        
        if _boolean_condition_:
            break
            
    # end of while
```


```python
# Example 1: Using Break

num = 10

while True:
    print(num)
    num -= 1
    
    if num == 4:
        break
# end of while loop
```

    10
    9
    8
    7
    6
    5


This code is an infinite loop; however, we wrote a conditional check inside the loop that allow us to exit the loop if the condition is True ```num == 4```.

### ```continue``` keyword

The ```continue``` keyword is very similar to ```break```. 

However, ```continue``` allows us to end the code block prematurely, but go back to the top of the iteration to go to the next iteration.


```python
# Example 2: Using Continue

num = 10

while True:
    num -= 1
    
    if num == 4:
        continue # once this code is executed, it ignores all the code below in the code block.
    
    print(num)
    
    if num == 1:
        break
# end of while
```

    9
    8
    7
    6
    5
    3
    2
    1


Notice that the number **4** does not get outputted.


#### Real World Application of an Infinite Loop: ```Game Loop```

"The **game loop** is the **overall flow control** for the entire game program. It’s a loop because the game keeps doing a series of actions over and over again until the user quits. _Each iteration of the game loop_ is known as a **frame**. Most real-time games update several times per second: 30 and 60 are the two most common intervals. If a game runs at 60 FPS (frames per second), this means that the game loop completes 60 iterations every second.

There can be many variations of the game loop, depending on a number of factors, most notably the target hardware. Let’s first discuss the traditional game loop before exploring a more advanced formulation that’s designed for more modern hardware"

[Source](https://www.informit.com/articles/article.aspx?p=2167437&seqNum=2)
