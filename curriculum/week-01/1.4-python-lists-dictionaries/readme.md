---
title: Intro to Python 2
duration: "1:30"
creator:
    name: Lucy Williams & Kiefer Katovich
    city: DC & SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Intro to Python 2: Lists & Dictionaries
Week 1 | Lesson 1.4

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Create lists and operate on them
- Create dictionaries and operate on them

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Define/describe/explain a list and a dictionary

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 10 min  | [Introduction](#introduction)   | Lists and dictionaries  |
| 25 min  | [Demo / Codealong / Guided Practice](#demo)  | Lists  |
| 10 min  | [Independent Practice](#ind-practice)  | Lists  |
| 25 min  | [Demo / Codealong / Guided Practice](#demo)  | Dictionaries  |
| 10 min  | [Independent Practice](#ind-practice)  | Dictionaries  |
| 10 min  | [Conclusion](#conclusion)  |  |


<a name="introduction"></a>
## Introduction: Lists and dictionaries (10 mins)

**Lists** are lists of arbitrary items in python.

Lists are:

- expressed with square brackets: **[ ]**
- indexed starting at 0
- "mutable", meaning they can be modified such as appended to
- can contain any type of python type
- can contain a mixture of types

Examples:
```python
numbers = [1, 2, 3, 4, 5]
letters = ['a','b','c','d']
mixture = ['hi',12.13,1,(1,2),['a','b','c']]
```

**Dictionaries** contain multiple items, like lists, but are organized in key:value pairs

Dictionaries are:

- expressed with curly brackets: **{ }**
- follow the pattern: {key1:value1, key2:value2, ...}
- indexed by their keys rather than numeric index
- are mutable
- can contain mixtures of key and value types

Examples:
```python
telephone_nums = {'john':5103315523, 'andrew':4156678890}
lists = {0:[1,2,3], 1:[4,5,6]}
mixture = {'animals':['dog','cat'], 1:2, empty_dicts:{'a':{}, 'b':{}}}
```

[Lists and Dictionaries](http://sthurlow.com/python/lesson06/)


<a name="demo"></a>
## Demo / Codealong / Guided Practice: Lists (25 mins)

In nearly all cases lists are preferable to tuples because we can change their values. Let's practice creating and modifying python lists

---

##### Creating lists

Lists are defined like tuples.
Say you have 5 friends called Curly, Moe, Larry, Tweedle Dee and Tweedle Dumb. Create a list named "friends" with the 5 friends.

Lists can be assigned to variables. Make the list of friends and assign it to a variable named "friends"
<details><summary> L-1: make a list with the 5 friends
</summary>
```python
friends = ['Curly', 'Moe', 'Larry', 'Tweedle Dee', 'Tweedle Dumb']
print(friends)
['Curly', 'Moe', 'Larry', 'Tweedle Dee', 'Tweedle Dumb']
```
</details>

Recall that lists are indexed with integers.

<details><summary> L-2: print the 3rd item of the friends list
</summary>
```python
print(friends[2])
Larry
```
</details>

You can use two indices separated by a colon to access a range of elements within a list. For example: **my_list[0:5]** would print out the first 5 elements of my_list.

<details><summary> L-3: print the 3rd thru 5th elements of the friends list
</summary>
```python
print(friends[2:5])
['Larry', 'Tweedle Dee', 'Tweedle Dumb']
```
</details>

---

##### Modifying lists

Lists have pre-defined functions which are very useful for manipulating them. The build in functions of list work _in place_, meaning that you do not have to assign the result to a new variable.

The **.append()** function will add an element to the end of a list. Use the function like: **[...].append(item)**

<details><summary> L-4: add 'Samwise' to the end of the friends list using .append()
</summary>
```python
friends.append('Samwise')
print(friends)
['Curly', 'Moe', 'Larry', 'Tweedle Dee', 'Tweedle Dumb', 'Sam']
```
</details>

You can also combine lists by simply adding them together with the **+** operator.

<details><summary> L-5: add the list ['Bob', 'Joe'] to the friends list
</summary>
```python
friends = friends + ['Bob', 'Joe']
print(friends)
['Curly', 'Moe', 'Larry', 'Tweedle Dee', 'Tweedle Dumb', 'Sam', 'Bob', 'Joe']
```
</details>

The **.remove()** function can remove an specific element of a list, and the **del** command will remove the item of a list at a specific index. For example, **del my_list[2]** removes the 3rd element of my_list.

<details><summary> L-6: remove 'Sam' from the list with the .remove() function
</summary>
```python
friends.remove(3)
print(friends)
['Curly', 'Moe', 'Larry', 'Tweedle Dumb', 'Bob', 'Joe']
```
</details>

<details><summary> L-7: remove the first element of friends using del
</summary>
```python
del friends[0]
print(friends)
['Moe', 'Larry', 'Tweedle Dumb', 'Bob', 'Joe']
```
</details>

[More information about lists](http://sthurlow.com/python/lesson06/)


<a name="ind-practice"></a>
## Independent Practice: Lists (10 minutes)
Explore the built in functions of lists:

- use **.append(item)** to add item to a list
- use **.extend([item1, item2])** to join another list to the end of the list
- use **.insert(index, item)** to add an item to a list at an index
- use **.remove(item)** to remove an item from a list
- use **.sort()** to sort a list
- use **.count(item)** to count the number of times an item appears in a list
- use **.index(item)** to find the index of an element in a list
- use **.pop()** to extract (and remove) the last element of a list
- use **.reverse()** to reverse a list


<a name="demo"></a>
## Demo / Codealong / Guided Practice: Dictionaries (25 mins)

Dictionaries are useful when you want to associate items with a specific reference, or **key**. An example of this would be storing phone numbers of your friends with the key values as your friends' names.

Remember that dictionaries are created with curly brackets, using **{key:value, key2:value2}** syntax.

One potentially confusing aspect of dictionaries is that although they are created with the curly brackets **{ }**, accessing a value with a key is done using square brackets **[ ]**, for example: **my_dict['key']** returns the value for "key" in my_dict.

---

##### Making and using dictionaries

Dictionaries are created the same as lists, with assignment to a variable. Create a dictionary called "zipcodes" with the following district:zip code pairs:

'sunset':94122
'presidio':94129
'soma':94105
'marina':94123

<details><summary> D-1: Create the SF district dictionary
</summary>
```python
zipcodes = {'sunset':94122, 'presidio':94129, 'soma':94105, 'marina':94123}
print(zipcodes)
{'soma': 94105, 'presidio': 94129, 'sunset': 94122, 'marina': 94123}
```
</details>

As you can see, when you print the dictionary, the key:value pairs are not guaranteed to be ordered the way you entered them like a list.

Values for a key can be accessed using the square bracket **[ ]** syntax or with the **.get()** method.

<details><summary> D-2: access the zip code for soma and assign it to a variable
</summary>
```python
soma = zipcodes['soma']
print(soma)
94105
```
</details>

You can list the current keys in a dictionary with the **.keys()** function. The keys will be returned in a list.

<details><summary> D-3: print out a list of the keys in zipcodes using .keys()
</summary>
```python
zipcodes.keys()
['soma', 'presidio', 'sunset', 'marina']
```
</details>

The **.items()** function will create a list of tuples, where each of the tuples in the list is a key:value pair in the dictionary.

<details><summary> D-4: print out a list of the key:value pairs in zipcodes using .items()
</summary>
```python
zipcodes.items()
[('soma', 94105), ('presidio', 94129), ('castro', 94114), ('marina', 94123)]
```
</details>

---

##### Modifying dictionaries

Adding new key:value pairs to a dictionary is similar to how you access an existing entry. The syntax for adding a new entry is: **my_dict['new_key'] = new_value**.

<details><summary> D-5: add 'castro':94114 to the zipcodes dictionary
</summary>
```python
zipcodes['castro'] = 94114
print(zipcodes)
{'soma': 94105, 'presidio': 94129, 'sunset': 94122, 'castro': 94114, 'marina': 94123}
```
</details>

Removing a dictionary key:value pair can be done with the **del** command, like with a list, or with the **.pop()** function which will remove a key from the dictionary and return the value for that key.

<details><summary> D-6: remove the sunset zipcode with .pop() and assign it to a variable
</summary>
```python
sunset = zipcodes.pop('sunset')
print(sunset)
94122
```
</details>

<a name="ind-practice"></a>
## Independent Practice: Dictionaries (10 minutes)

Build your own dictionary with key:value pairs of your choosing.

Explore some of the built in functions for dictionaries:

- use **.pop(key)** to remove a key:value pair from the dictionary and return the value
- use **.get(key)** to get the value for a key
- use **.has_key(key)** to check if a key is in the dictionary
- use **.keys()** to get a list of the keys in the dictionary
- use **.items()** to get a list of the key:value pairs in the dictionary
- use **.update(other_dictionary)** to merge a 2nd dictionary into the current dictionary
- use **.clear()** to remove all key:value pairs from the dictionary

<a name="conclusion"></a>
## Conclusion (10 mins)
- Partner up and explain what a list and a dictionary are to your partners
- What are the differences between a list and a dictionary?
- What are the two things you need for a dictionary?

## Bonus Challenges
Once you've mastered the basics, further your understanding of Python by attempting "[Alternate Code Challenges 2](code/starter-code/Alternate%20Code%20Challenges%20-%20Week%201%20Lesson%201.2.ipynb)".
