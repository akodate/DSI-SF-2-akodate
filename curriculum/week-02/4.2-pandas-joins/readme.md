---
title: Joins & Pandas
duration: "1:5"
name: Lucy Williams
city: DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Joins & Pandas
Week 2 | Lesson 4.3

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Join data via concat
- Do left, right, inner, and outer joins

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Introduction](#introduction)   | Concatenate & Join  |
| 10 min  | [Demo / Guided Practice](#demo)  | Concatenate  |
| 25 min  | [Demo / Guided Practice](#demo)  | Left and right joins  |
| 25 min  | [Demo / Guided Practice](#demo)  | Outer and inner joins  |
| 20 min  | [Independent Practice](#ind-practice)  |   |
| 5 min  | [Conclusion](#conclusion)  |  |

---

<a name="Concatenate & Join"></a>
## Introduction: Concatenate & Joins (5 mins)

Concatenation is taking two or more separately located things and placing them
side-by-side next to each other so that they can now be treated as one thing. In
computer programming and data processing, two or more character strings are sometimes
concatenated for the purpose of saving space or so that they can be addressed as a
single item.

Joins using pandas happen when columns of two DataFrames are joined either on index
or on a key column. Here is a representation of left, right, inner, and outer joins
using Venn diagrams.

![](https://github.com/generalassembly-studio/dsi-course-materials/blob/W2-L4.3/curriculum/04-lessons/week-02/4.3-lesson/assets/images/Joins.png)

**Check:** In pairs draw a left, right, inner, and outer join. Then, show the other person and explain it to them.

[concatenation](http://whatis.techtarget.com/definition/concatenation-concatenate-concatenating)
[venn of joins](http://www.bogotobogo.com/php/images/mysql-join/Joins.png)



<a name="Concatenate"></a>
## Demo / Guided Practice: Left joins (12 mins)

Let's look at a simple example of concatenation. No need to do this yourself,
just follow along.

> [demo code](https://github.com/generalassembly-studio/dsi-course-materials/blob/W2-L4.3/curriculum/04-lessons/week-02/4.3-lesson/code/W2%20L4.3%20demo%20code.ipynb)

```Python
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])
```
```Python
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7])
```

Define the two frames as one variable, frames.
```Python
frames = [df1, df2]
```

Concatenate.
```Python
result = pd.concat(frames)
result
```

[concat](http://pandas.pydata.org/pandas-docs/stable/pandas.pdf)




<a name="Left and right joins"></a>
## Demo / Guided Practice: Left joins (25 mins)

Let's create a small DataFrame to and try a left, right, inner, and outer join.
```Python
import pandas as pd
from IPython.display import display
from IPython.display import Image
```
```Python
raw_data = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
df_a = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
df_a
```

Create a 2nd DataFrame
```Python
raw_data = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
df_b = pd.DataFrame(raw_data, columns = ['subject_id', 'first_name', 'last_name'])
df_b
```

Create a 3rd DataFrame
```Python
raw_data = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
df_n = pd.DataFrame(raw_data, columns = ['subject_id','test_id'])
df_n
```

Merge with a left join produces a complete set of records from
df_a, with the matching records (where available) in df_b. If there is no
match, the right side will contain null.
```Python
pd.merge(df_a, df_b, on='subject_id', how='left')
```

**Check** What do you think a right join will result in?

Merge with a right join produces a complete set of records from
df_b, with the matching records (where available) in df_a. If there is no
match, the left side will contain null.
```Python
pd.merge(df_a, df_b, on='subject_id', how='right')
```

[left and right join](http://chrisalbon.com/python/pandas_join_merge_dataframe.html)





<a name="Outer and inner joins"></a>
## Demo / Guided Practice: Outer and inner joins (25 mins)

An outer join produces the set of all records in df_a and df_b, with
matching records from both sides where available. If there is no match, the
missing side will contain null.
```Python
pd.merge(df_a, df_b, on='subject_id', how='outer')
```

**Check** What do you think an inner join will produce?

An inner join produces only the set of records that match in both df_a and df_b.
```Python
pd.merge(df_a, df_b, on='subject_id', how='inner')
```

[outer and inner join](http://chrisalbon.com/python/pandas_join_merge_dataframe.html)




<a name="ind-practice"></a>
## Independent Practice: Topic (20 minutes)

Here are two simple DataFrames:

```Python
df1 = pd.DataFrame([[1, 2, 3]])
df1
```
```Python
df2 = pd.DataFrame([[1, 7, 8],[4, 9, 9]], columns=[0, 3, 4])
df2
```

Do a left, right, inner, and outer join.

**Bonus**  If you've used SQL before, joins are probably old hat to you. If so and you finish
early, how is your neighbor doing? Remember, you might be quiz at joins, but
they might be a whiz at linear regression. Sharing knowledge will make you
both smarter...

<a name="conclusion"></a>
## Conclusion (5 mins)
Pair up and explain a left, a right, an inner, and an outer join to a partner. 
