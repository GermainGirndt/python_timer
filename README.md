# :clock2: Python Timer
A timer for measuring and comparing different functions' execution time. (working on 13th Jun 2020)

## :mag_right: Preview

![preview](https://github.com/GermainPereira/python_timer/blob/master/2020-06-13-preview-python-timer.gif?raw=true)

## :star2: Features

Python Timer executes **any number of functions** set as parameter a given number of times and uses decorators for automaticaly alternating between the function been executed and measuring individually each function's runtime. 

In the end, Python Timer prints on the terminal a message containing the average runtime for each function.

## :notebook: Notes
Python Timer was just an experiment made by me while learning about decorators. It has surelly many weak points, like depending on the computer's current state, which normally influences considerably the function's runtime.  

I've tried to reduce this external condition by testing the algorithm using tests functions which had a pretty low average runtime. Since the functions being compared are ran in turns, this could theorically contribute for just increasing execution time in both functions, in a way that the final result (better/worse function) wouldn't be affected at all by the computer. 

**Still, on my experiments this theory has been proved wrong. I guess mathematical models are still a better option hehehe**
