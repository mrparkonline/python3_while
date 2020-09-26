---
title: ""
draft: false
weight:
lesson: true
descriptor: ""
---

# Flag Based While Loop
---

To control when to exit a while loop, we can also a flag like variable to make the condition become False based on user input.

```python
    
    flag = True
    
    while flag:
        
        Your Code Here
        
        user_input = input('Do you want an exit? (y/n): ')
        if user_input in 'yY':
            flag = False
   # end of while
```

This type of formatting a while loop help us to potentially loop forever, but at the end of the code block we get to choose if we want to iterate again.
