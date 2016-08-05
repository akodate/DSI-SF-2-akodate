---
title: Practicing Joins
type: lab
duration: "1:5"
creator:
    name: Lucy Williams
    city: DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Practicing Joins

## Introduction

Inner, outer, left, and right joins can help us to combine data in ways that
can make analysis a lot easier. Let's get some more practice. 

#### Requirements

Using these two DataFrames:
```Python
df_a = pd.DataFrame([{"a": 1, "b": 4}, {"a": 2, "b": 5}, {"a": 3, "b": 6}])
df_a
```
```Python
df_b = pd.DataFrame([{"c": 2, "d": 7}, {"c": 3, "d": 8}])
df_b
```
and do: 
- an inner join
- an outer join
- a left join
- a right join

**Bonus:**
Using these two DataFrames, do all of the above. 
```Python
left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                  'key2': ['one', 'two', 'one'],
                  'lval': [1, 2, 3]})
```
```Python
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                   'key2': ['one', 'one', 'one', 'two'],
                   'rval': [4, 5, 6, 7]})
```
