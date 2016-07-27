---
title: Intro to Python 3
duration: "1:5"
creator:
    name: Lucy Williams
    city: DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Intro to Python 3
Week 1 | Lesson 1.4

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Explain if/else and if/elif/else
- Explain for loop
- Demonstrate how to define functions

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Have a cursory explanation/idea of if/else, if/elif/else, loops, and functions.

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 10 min  | [Introduction](#introduction)   | Control Flow  |
| 15 min  | [Demo](#demo)  | if, if/else  |
| 15 min  | [Demo](#demo)  | if/elif/else  |
| 15 min  | [Demo](#demo)  | loops  |
| 15 min  | [Demo](#demo)  | functions  |
| 15 min  | [Independent Practice](#ind-practice)  
| 5 min  | [Conclusion](#conclusion)
---

<a name="Control Flow"></a>
## Introduction: Topic (10 mins)

It is very important to control program execution because in real situations are full of conditions and if you want your program to mimic the real world you need to transform those real world situations into your program . For this, you need to control the execution of your program statements. Controlling the program execution sequence is commonly known as control flow.

[control flow](http://www.codeproject.com/Articles/663666/Python-Basics-Understanding-The-Flow-Control-State)


<a name="if, if/else"></a>
## Demo / Codealong / Guided Practice: if, if/else (15 mins)
The general Python syntax for a simple if statement is:
```bash
        if condition :
            indentedStatementBlock

```

If the condition is true, then do the indented statements. If the condition
is not true, then skip the indented statements.

> Instructor Note: code also in [demo code folder](https://github.com/generalassembly-studio/dsi-course-materials/blob/Week-1-Lesson-1.4/curriculum/04-lessons/week-01/1.4-lesson/code/Week%201%20Lesson%201.4%20%20demo%20code.ipynb)

In iPython notebook type:
```bash
weight = float(input("How many pounds does your suitcase weigh? "))
if weight > 50:
        print("There is a $25 charge for luggage that heavy.")
print("Thank you for your business.")
```

then type:
```bash
43
```

and it returns:
```bash
Thank you for your business.
```

Do it again, but this time put in a number > 50.

and it returns:
```bash
There is a $25 charge for luggage that heavy.
Thank you for your business.
```


The general Python if-else syntax is

        if condition :
            indentedStatementBlockForTrueCondition
        else:
            indentedStatementBlockForFalseCondition

These statement blocks can have any number of statements, and can include
about any kind of statement.

In iPython notebook type:
```bash
temperature = float(input('What is the temperature? '))
```

Input a temp.

then type:
```bash
if temperature > 70:
    print('Wear shorts.')
else:
    print('Wear long pants.')
print('Get some exercise outside.')
```
The middle four lines are an if-else statement. There are two indented
blocks: One, like in the simple if statement, comes right after the
if heading and is executed when the condition in the if heading is true.
In the if-else form this is followed by an else: line, followed by
another indented block that is only executed when the original condition is false.
In an if-else statement exactly one of two possible indented blocks is executed.

Play around inputting numbers that are < 70 or > 70.

[control flow statements](http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html)

**Check**: What is the general syntax for an if statement? an if/else?


<a name="if/elif/else"></a>
## Demo / Codealong / Guided Practice: if/elif/else (15 mins)
The syntax for an if-elif-else statement is indicated in general below:

        if condition1 :
            indentedStatementBlockForTrueCondition1
        elif condition2 :
            indentedStatementBlockForFirstTrueCondition2
        elif condition3 :
            indentedStatementBlockForFirstTrueCondition3
        elif condition4 :
            indentedStatementBlockForFirstTrueCondition4
        else:
            indentedStatementBlockForEachConditionFalse

In iPython notebook type:
```bash
x = int(raw_input("Please enter an integer: "))
```

Type in an integer.

then type:
```bash
if x < 0:
    x = 0
    print 'Negative changed to zero'
elif x == 0:
    print 'Zero'
elif x == 1:
    print 'Single'
else:
    print 'More'
```
The if, each elif, and the final else line are all aligned. There can be any number
of elif lines, each followed by an indented block. With this construction exactly
one of the indented blocks is executed. It is the one corresponding to the first
True condition.

[control flow statements](http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html)

**Check**: How many indented blocks in an if/elif/else are executed?


<a name="loops"></a>
## Demo / Codealong / Guided Practice: loops (15 mins)

Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.

The syntax for loop is indicated in general below:

    for iterator_name in iterating_sequence:
        …statements…

In iPython notebook type:
```bash
words = ['cat', 'window', 'defenestrate']
for w in words:
    print w, len(w)
```

and it returns:
```bash
cat 3
window 6
defenestrate 12
```

Knowledge check: what's happening here? Explain how the code returns what it does.

[for statements](https://docs.python.org/2/tutorial/controlflow.html#if-statements)
[for loop](http://www.codeproject.com/Articles/663666/Python-Basics-Understanding-The-Flow-Control-State)


<a name="functions"></a>
## Demo / Codealong / Guided Practice: functions (15 mins)

- You can define functions to provide the required functionality. Here are simple rules to define a function in Python.
    - Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).
    - Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside            these parentheses.
    - The first statement of a function can be an optional statement - the documentation string of the function or                  docstring.
    - The code block within every function starts with a colon (:) and is indented.
    - The statement return [expression] exits a function, optionally passing back an expression to the caller. A return             statement with no arguments is the same as return None.

The syntax for a function is indicated in general below:
```bash
def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]
```

Let's create a function called printme
In iPython notebook type:
```bash
def printme( str ):
   "This prints a passed string into this function"
   print str
   return
```

now, let's call the function:
```bash
printme("Beltway traffic makes my head hurt.")
printme("It looks like a parking lot out there!")
```

and it returns:
```bash
Beltway traffic makes my head hurt.
It looks like a parking lot out there!
```

[defining a function](http://www.tutorialspoint.com/python/python_functions.htm)

**Check** What’s the general syntax for a function? Why do you think functions might be useful?

<a name="ind-practice"></a>
## Independent Practice: Topic (10 minutes)
- What is the general syntax/format of:  
        -  if/else?
        -  if/elif/else?
        -  loop?
        - function?
- Define and explain each to a partner

<a name="conclusion"></a>
## Conclusion (5 mins)
Today we learned about if/else, if/elif/else, loops, and functions. Practice coding each until you
feel comfortable. If you understand basic control flow concepts, you're on your way to writing
fantastic executable programs!

## Bonus Challenges
Once you've mastered the basics, further your understanding of Python by attempting "[Alternate Code Challenges 3](code/starter-code/Bonus%20Code%20Challenges%203%20Starter%20Code%20-%20Week%201%20Lesson%202.2.ipynb#)", involving recursive functions.
