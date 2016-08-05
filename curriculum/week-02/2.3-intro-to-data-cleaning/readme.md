---
title: Intro to Data Cleaning
duration: "1:5"
creator:
    name: Lucy Williams
    city: DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Intro to Data Cleaning
Week 2 | Lesson 2.3

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Inspect data types
- Clean up a column using df.apply()
- Know what situations to use .value_counts() in your code


### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck
- 

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Introduction](#introduction)   | Inpsect data types, df.apply(), .value_counts()  |
| 20 min  | [Demo /Guided Practice](#demo)  | Inpsect data types |
| 20 min  | [Demo /Guided Practice](#demo)  | df.apply() |
| 20 min  | [Demo /Guided Practice](#demo)  | .value_counts() |
| 20 min  | [Independent Practice](#ind-practice)  |   |
| 5 min  | [Conclusion](#conclusion)  |   |

---

<a name="introduction"></a>
## Introduction: Topic (5 mins)

Since we're starting to get pretty comfortable with using pandas to do EDA, let's add a
couple more tools to our toolbox. 

The main data types stored in pandas objects are float, int, bool, datetime64, datetime64, timedelta, 
category, and object. 

df.apply() will apply a function along any axis of the DataFrame. We'll see it in action below. 

pandas.Series.value_counts returns Series containing counts of unique values. The resulting 
Series will be in descending order so that the first element is the most frequently-occurring 
element. Excludes NA values.

[dtypes](http://pandas.pydata.org/pandas-docs/stable/pandas.pdf)
[value_counts](http://nullege.com/codes/search/pandas.Series.value_counts)



<a name="Inpsect data types "></a>
## Demo /Guided Practice: Inspect data types  (20 mins)

Let's create a small dictionary with different data types in it. 

> [demo code](https://github.com/generalassembly-studio/dsi-course-materials/blob/W2-L2.3/curriculum/04-lessons/week-02/2.3-lesson/code/W2%20L2.3%20Intro%20to%20Data%20Cleaning%20demo%20code.ipynb)
can be found in the code folder and contains all the code in this lesson in a Jupyter
notebook. May be easier to use...

in iPython notebook type: 
```Python
import pandas as pd
import numpy as np
dft = pd.DataFrame(dict(A = np.random.rand(3),
                        B = 1,
                        C = 'foo',
                        D = pd.Timestamp('20010102'),
                        E = pd.Series([1.0]*3).astype('float32'),
                                F = False,
                                G = pd.Series([1]*3,dtype='int8')))
dft
```

There is a really easy way to see what kind of dtypes are in each column. 
```Python
dft.dtypes
```

If a pandas object contains data multiple dtypes IN A SINGLE COLUMN, the dtype of the 
column will be chosen to accommodate all of the data types (object is the most general).

```Python
# these ints are coerced to floats
pd.Series([1, 2, 3, 4, 5, 6.])
```
```Python
# string data forces an ``object`` dtype
pd.Series([1, 2, 3, 6., 'foo'])
```

The method get_dtype_counts() will return the number of columns of each type in a DataFrame:
```Python
dft.get_dtype_counts()
```

You can do a lot more with dtypes that you can check out 
[here](http://pandas.pydata.org/pandas-docs/stable/pandas.pdf)

**Check:** Why do you think it might be important to know what kind of dtypes youre'
working with? 



<a name=" df.apply()"></a>
## Demo /Guided Practice:  df.apply() (20 mins)

Let's create a small data frame. 
```Python
df = pd.DataFrame(np.random.randn(5, 4), columns=['a', 'b', 'c', 'd'])
df
```

Use df.apply to find the square root of all the values. 
```Python
df.apply(numpy.sqrt)
```

Find the mean of all of the columns.
```Python
df.apply(np.mean, axis=0)
```

Find the mean of all of the rows.
```Python
df.apply(np.mean, axis=1)
```

[df.apply](https://gist.github.com/why-not/4582705)
[df.apply](http://chrisalbon.com/python/pandas_apply_operations_to_dataframes.html)

**Check:** How would find the std of the columns and rows? 



<a name=".value_counts()"></a>
## Demo /Guided Practice: .value_counts() (20 mins)

Let's create a random array with 50 numbers, ranging from 0 to 7.
```Python
data = np.random.randint(0, 7, size = 50)
```

Convert the array into a series.
```Python
s = pd.Series(data)
```

How many of each number is there in the series? Enter value_counts()
```Python
pd.value_counts(s)
```


<a name="ind-practice"></a>
## Independent Practice: Topic (20 minutes)
- Use the sales.csv data set, we've seen this a few times in previous lessons
- Inspect the data types
- You've found out that all your values in column 1 are off by 1. Use df.apply 
    to add 1 to column 1 of the dataset
- Use .value_counts to count the values of 1 column of the dataset

**Bonus** 
- Add 3 to column 2
- Use .value_counts for each column of the dataset


<a name="conclusion"></a>
## Conclusion (5 mins)
So far we've used pandas to look at the head and tail of a data set. We've also taken a look at summary stats and different
types of data types. We've selected and sliced data too. Today we added inspecting data types, df.apply, .value_counts to
our pandas arsenal. Nice!

