---
title: Intro to Pandas 1
duration: "1:5"
creator:
    name: Lucy Williams
    city: DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Intro to Pandas 1
Week 2 | Lesson 1.1

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Read a csv file using pandas
- Viewing data: head, columns, values, describe
- Selection: a single column, slicing by row, by position


### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Since we're using Anaconda, pandas should already be installed. But, 
make sure you have all the dependencies installed as well: 
    - setuptools
    - NumPy: 1.7.1 or higher
    - python-dateutil: 1.5 or higher
    - pytz: needed for time zone support

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck


### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Introduction](#introduction)   | Pandas, no not Mei Xiang, Tian Tian, or Tai Shan  |
| 10 min  | [Demo / Guided Practice](#demo)  | Read csv  |
| 25 min  | [Demo / Guided Practice](#demo)  | Viewing data: head/tail, describe |
| 25 min  | [Demo / Guided Practice](#demo)  | Selection: a single column, slicing by row, by position |
| 20 min  | [Independent Practice](#ind-practice)  |   |
| 5 min  | [Conclusion](#conclusion)  |   |

---

<a name="Pandas"></a>
## Introduction: Topic (5 mins)

Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data 
structures and data analysis tools for the Python programming language. 

[pandas](http://pandas.pydata.org/)



<a name="Read csv"></a>
## Demo / Guided Practice: Topic (10 mins)

[demo code](https://github.com/generalassembly-studio/dsi-course-materials/blob/W2-L1.1/curriculum/04-lessons/week-02/1.1-lesson/code/Demo%20Code%20-%20W2%20L1.1%20Intro%20to%20Pandas%201.ipynb)

in iPython notebook type: 
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

Let's read in a csv file and create a pandas dataframe. 

```python
df = pd.read_csv('sales.csv')
```

**Check:** This looks familiar...didn't we already learn how to read in csv files? 
Yes, but that was using Python without any libraries or packages. It took 5 lines of 
Python [W1 L3.2](https://github.com/generalassembly-studio/dsi-course-materials/blob/master/curriculum/04-lessons/week-01/3.2-lesson/code/Demo%20Code%20-%20Week%201%20Lesson%203.2%20-%20iPython%20Notebooks%2C%20Data%20Values%2C%20CSV%20Library.ipynb), but using Pandas it only takes one line. Nice!



<a name="Viewing data: head/tail, describe"></a>
## Demo / Guided Practice: Viewing data: head/tail, describe (25 mins)

Let's take a summary look at our data. First, let's look at the head and tail. 
```python
df.head(df)
```

```python
df.tail(df)
```

**Check:** What can looking at the head and tail of a dataset tell us? 


Let's take a look at summary statistics.
```python
df.describe
```

This gives us: count, mean, std, min, 25%, 50%, 75%, and max. Awesome!

**Check:** What was the cautionary tale about relying too heavily on summary stats again?



<a name="Selection: a single column, slicing by row, by position"></a>
## Demo / Guided Practice: Selection: a single column, slicing by row, by position (25 mins)

Let's select a single column. 
```python
df['Account']
```
**Check:** How would you select the 'Quantity' and 'Price' columns separately?


Now, let's slice and select for certain rows. 
```python
df[0:3]
```
**Check:** How would you slice for rows 9 to 14? 


Now, let's try selecting by position. First, let's slice some rows. 
```Python
df.iloc[1:3, :]
```
**Check:** How would you slice for rows 9 to 14? 


Now, let's slice some columns. 
```Python
df.iloc[:,1:3]
```
**Check:** How would you slice for the 'Manager' and 'Product' columns? 


Now, let's get an explicit value only. 
```Python
df.iloc[1,1]
```



<a name="ind-practice"></a>
## Independent Practice: Topic (20 minutes)
- Read in this [star wars survey csv](https://github.com/fivethirtyeight/data/blob/master/star-wars-survey/StarWars.csv)
- Look at its head, tail, and summary stats, what does this tell you about the dataset? 
- Select a certain column
- Slice for a set of rows
- Select a data point based on position


**Bonus** 
- Convert one data type to another in the star wars survey csv
- Create a dummy variable for the yes and no answers


<a name="conclusion"></a>
## Conclusion (5 mins)
We read a csv file into a pandas dataframe with just one line of code. Compared to last week, when 
we used just used Python to read in a csv file, it took about 5 lines of code. Pandas is already making 
our data lives easier. We also took a look at how easy pandas makes it to get some general information 
about our dataset by looking at the head, tail, and summary stats. Lastly, we started to select and 
slice our dataset. 


### ADDITIONAL RESOURCES

- [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/pandas.pdf)
- [pandas website](http://pandas.pydata.org/)

