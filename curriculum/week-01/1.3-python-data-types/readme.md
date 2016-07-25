---
title: Intro to Python 1
duration: "1:5"
creator:
    name: Dave Yerrington
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Intro to Python: Datatypes

Week 1 | Lesson 1.3

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Define integers, strings, tuples, lists, and dictionaries
- Demonstrate arithmetic operations and string operations
- Demonstrate variable assignment

### INSTRUCTOR PREP
- Review upcoming project deliverables, as needed
- Review what was covered yesterday and what is going to be covered tomorrow

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Describe/define Python data types

### LESSON GUIDE

| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Introduction](#introduction)   | Python Data Types  |
| 10 min  | [Demo / Codealong / Guided Practice](#demo)  | Integers  |
| 10 min  | [Demo / Codealong / Guided Practice](#demo)  | Strings  |
| 10 min  | [Demo / Codealong / Guided Practice](#demo)  | Tuples  |
| 10 min  | [Demo / Codealong / Guided Practice](#demo)  | Lists  |
| 10 min  | [Demo / Codealong / Guided Practice](#demo)  | Dictionaries  |
| 10 min  | [Demo / Codealong / Guided Practice](#demo)  | Arithmetic operations and String operations  |
| 10 min  | [Independent Practice](#ind-practice)  |   |
| 5 min  | [Conclusion](#conclusion)  |   |

### ALTERNATE LESSON GUIDE

Some students might already know Python quite well so we are offering this _optional_ code challenge to warm-up on while we go over Python fundamentals with the rest of the class.

| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Introduction](#introduction)   | Challenge  |
| 70 min  | [Code Challenge #1](code/starter-code/Alternate%20Code%20Challenges%20-%20Week%201%20Lesson%201.2.ipynb)  | Intense Coding  |
| 5 min  | [Conclusion](#conclusion)  |   |

---

<a name="introduction"></a>
## Introduction: Python Data Types (5 mins)

Integers: whole numbers from negative infinity to infinity, such as 1, 0, -5, etc.

Float: short for "floating point number," any rational number, usually used with decimals such as 2.8 or 3.14159.

Strings: a set of letters, numbers, or other characters.
"Frank Underwood, I am your father."

Tuples: a list with a fixed number of elements. ie x=(1,2,3) parentheses makes it a tuple.
x = ("Kirk", "Picard", "Spock")

Lists: a list without a fixed number of elements. ie x=[1,2,3] note the square brackets, a list
x = ["Lord", "of", "the", "Rings"]

Dictionaries: a type with multiple elements i.e. x = {1: 'a','b': 2,3: 3} where you address the elements with, e.g., a text.
x = {'key1':'value1', 'key2':'value2'}

[Python Basic data types](https://en.wikiversity.org/wiki/Python/Basic_data_types)


<a name="demo"></a>
## Demo / Codealong / Guided Practice: Integers (10 min)

#### Integers
Integers are numeric values and can be stored, manipulated, and expressed inside variables without quotes.
In iPython notebook type:
```bash
23
```
and it returns:
```bash
23
```


In iPython notebook type:
```bash
-44
```
and it returns:
```bash
-44
```

You can also perform basic math using integers as well. In iPython notebook type:
```bash
45-19
```
and it returns:
```bash
26
```

## Demo / Codealong / Guided Practice: Strings (10 min)

#### Strings
Strings are a type. They are the basic unit of text in Python and all the other types except integers may contain strings.
In iPython notebook type:
```bash
"I love Darth Vader"
```
and it returns:
```bash
'I love Darth Vader'
```

You can also make a variable refer to a string. In iPython notebook type:
```bash
x= "Luke, I am your father"
```
Now type:
```bash
x
```
and it returns:
```bash
'Luke, I am your father'
```
Now type:
```bash
print(x)
```
and it returns:
```bash
Luke, I am your father
```

The print command prints the value that 'x' stands for on the screen. It removes the quotations. Whenever you type something into a type that isn't an integer, syntax (the commands that you give python, such as print), or variable (such as x just was) you need to put it into quotations. You can use 'single' or "double" quotations.


## Demo / Codealong / Guided Practice: Tuples (10 min)
#### Tuples
A tuple is an unchangeable sequence of values.
When you typed ('I love Python') you only included one element.
In iPython notebook type:
```bash
x = ("Kirk", "Picard", "Spock")
```
When you do this you create a tuple with three elements. You can access these elements individually by typing the variable and the then inside brackets directly to the right of the variable type the number of the element to which you are referring.

Now type:
```bash
print(x[1])
```
and it returns:
```bash
Picard
```

You may think that it is odd that it returned element 2 instead of element 1. The reason that it did this is because Python starts numbering at 0. element 1 = 0, element 2= 1, element 3= 2. You can also call on the elements in reverse order.

Now type:
```bash
print(x[-1])
```
and it returns:
```bash
Spock
```

## Demo / Codealong / Guided Practice: Lists (10 min)
#### Lists
A list is a changeable sequence of data. A list is contained by square brackets i.e. [1,2,3]
In iPython notebook type:
```bash
x = ["Lord", "of", "the", "Rings"]
x[2] = "Frodo"
print(x)
```

and it returns:
```bash
['Lord', 'of', 'Frodo', 'Rings']
```

The code above changes element number 2 in x.


## Demo / Codealong / Guided Practice: Dictionaries (10 min)
#### Dictionaries
Dictionaries contain a key and a value. { } enclose dictionaries (Note, that you can also construct a set with curly brackets. The first input in a dictionary pair is the 'key'. The second input in a
dictionary pair is the 'value'. The general format looks like this:
key1:value1

In iPython notebook type:
```bash
x = {'key1':'value1', 'key2':'value2'}
```

Now type:
```bash
print(x)
```

These may not be in the exact order in which you typed them. The reason for the different order is because dictionaries have no order. You cannot type x[0] and be referring to 'key1':'value1' . What you do to refer to a value is type the key.

In iPython notebook type:
```bash
x[key1] = 'I love Python'
```

Now type:
```bash
print(x)
```

and it returns:
```bash
{'key2': 'value2', 'key1': 'value1', 'I love Python': 'I love Python'}
```

The keys stay the same but the values are changeable. You can also only have one occurrence of a key in a dictionary, but you may have the values all be the same.

Now type:
```bash
x = {'key':'value1', 'key':'value2'}
```

Then type:
```bash
print(x)
```

and it returns:
```bash
{'key': 'value2'}
```

The first key is overwritten by the second.

Now type:
```bash
x = {'key1':'value', 'key2':'value'}
```

Then type:
```bash
print(x)
```

and it returns:
```bash
{'key2': 'value', 'key1': 'value'}
```

This example shows that you can create two separate keys with the same value.

[Integers, Strings, Tuples, Lists, Dictionaries](https://en.wikiversity.org/wiki/Python/Basic_data_types)

**Check:** Define/describe: integer, string, tuple, list, dictionary


<a name="demo"></a>
## Demo / Codealong / Guided Practice: arithmetic operations and string operations (20 mins)

#### Simple Math
Math is very straightforward in Python. + adds, - subtracts, / divides, and believe it or not * multiplies. The main thing to comment on is %.  % performs a division and then returns the remainder. This is called the modulus operation.
In iPython notebook type:
```bash
9 % 3
```

and it returns:
```bash
0
```

Now type:
```bash
9 % 2
```

and it returns:
```bash
1
```

You can also use variables, and elements and values in simple arithmetic.
In iPython notebook type:
```bash
x = 1
y = 5
x + y
```

and it returns:
```bash
6
```
That is how the variable works.


Now type:
```bash
x = [1, 2, 3]
x[1] + x[2]
```

and it returns:
```bash
5
```

This is how you use elements from a list to perform arithmetic operations. It should be clarified that x[0] = 1, x[1] = 2, and x[2] = 3. You can also add and multiply strings, tuples, and lists.

In iPython notebook type:
```bash
x = {'a':1, 'b':2}
x['a'] + x['b']
```

and it returns:
```bash
3
```
That is how you do arithmetic with values from a dictionary. Don't forget to use quotations around the keys unless you use integers as the keys. Spend a couple of minutes messing around with this stuff, its fun and it'll help you remember it better. You may also add strings, tuples, and lists.

**Check:** What does % do?


#### Concatenating
To add two strings together - to do this you just type the first string, an addition sign, the second string.
In iPython notebook type:
```bash
"X Files" + " is awesome"
```

and it returns:
```bash
'X Files is awesome'
```

You can do the same with variables referring to strings.
In iPython notebook type:
```bash
x = "X Files"
y = " is awesome"
x + y
```

and it returns:
```bash
'X Files is awesome'
```

You can do the same with tuples.
In iPython notebook type:
```bash
x = ('I', 'Love')
y = ('True Detective Season 1',)
print(x + y)
```

and it returns:
```bash
('I', 'Love', 'True Detective Season 1')
```

It works the same with lists. What you cannot do is combine two different kinds of types.


#### Multiplying types
Multiplying is very easy and straight forward.
In iPython notebook type:
```bash
x = 'the americans '
x * 5
```

and it returns:
```bash
'the americans the americans the americans the americans the americans '
```

Now, try it with a tuple.
In iPython notebook type:
```bash
x = ('the americans',)
x * 5
```

and it returns:
```bash
('the americans',
 'the americans',
 'the americans',
 'the americans',
 'the americans')
```

You cannot do the same with dictionaries; that would make multiple keys with the same entry name, which isn't valid in Python.
In iPython notebook type:
```bash
x = {'the americans':1}
x * 5
```

and it returns:
```bash
TypeError                                 Traceback (most recent call last)
<ipython-input-16-f25efe1807bd> in <module>()
      1 x = {'the americans':1}
----> 2 x * 5

TypeError: unsupported operand type(s) for *: 'dict' and 'int'
```


#### Indexing
You have already learned how to index in lesson 2. When you typed x[3] you were indexing. You may also index a string without first making a variable represent it.
In iPython notebook type:
```bash
"I Love Spotify"[5]
```

and it returns:
```bash
'e'
```

#### Slicing
Slicing is used to access a range of elements the way that indexing accesses one element.
In iPython notebook type:
```bash
x = "Spotify and Netflix are awesome"
print(x[12:32])
```

and it returns:
```bash
Netflix are awesome
```
The numbers that you enter after the variable (the [12:32]) are called indices.


[arithmetic operations and string operations](https://en.wikiversity.org/wiki/Python/Basic_data_types)

**Check:** What is concatenating? indexing? slicing?


<a name="ind-practice"></a>
## Independent Practice: Topic (10 minutes)
Pair up, make up your own statements and see if your partner can tell you what will be returned BEFORE running it.


<a name="conclusion"></a>
## Conclusion (5 mins)
Let's check to see if we know what we learned about today:
- Define integers, strings, tuples, lists, and dictionaries
- Demonstrate arithmetic operations and string operations
- Demonstrate variable assignment
