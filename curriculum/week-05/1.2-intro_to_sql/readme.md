---
title: Intro to SQL
duration: "1:25"
creator:
    name: Francesco Mosconi
    city: SF
    updated: David Yerringotn
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) More SQL
Week 5 | Lesson 1.2

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Connect to a local or remote database using Python or Pandas
- Connect to a local or remote database using SQLite Browser or Postico(for POSTGRES)
- Perform queries using SELECT
- Perform simple aggregations COUNT, MAX/MIN/SUM

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- connect to SQLite from command line
- connect to PostgreSQL from command line
- load data in Pandas

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 mins | [Opening](#opening) | Opening |
| 30 min | [Demo](#demo) | Interacting with SQLite from Python |
| 30 mins | [Guided-practice](#guided-practice) | SQL Syntax |
| 20 minutes | [Ind-practice](#ind-practice) | Querying a Local Database |
| 5 mins | [Conclusion](#conclusion) | Conclusion |

<a name="opening"></a>
## Opening (5 mins)
We have seen how to connect to a local sqlite database and to a remote postgresql database.

**Check:** What SQL commands have we learnt so far?
**Check:** What different commands have we learned for SQLite and PostgreSQL?


<a name="demo"></a>
## Interacting with SQLite from Python (30 min)

### The `sqlite3` package

The command line utility can be useful for basic SQL tasks, but since we're using python for the rest of code it will often be easier to access sqlite directly from within python.  We can use the python [`sqlite3`](https://docs.python.org/2.7/library/sqlite3.html) package for just this purpose.

Open a connection to an SQLite database file.  As before, if the file does not already exist it will automatically be created.


```python
import sqlite3
sqlite_db = './assets/datasets/test_db.sqlite'
conn = sqlite3.connect(sqlite_db)
c = conn.cursor()
```

The syntax to create a table is similar to the console, only now we use the `execute` method of the cursor object `c` that we just created:


```python
c.execute('CREATE TABLE houses (field1 INTEGER PRIMARY KEY, sqft INTEGER, bdrms INTEGER, age INTEGER, price INTEGER);')

# Save (commit) the changes
conn.commit()
```

With the database saved the table should now be viewable using SQLite Manager.

#### Adding data

Since we're back in python, we can now use regular programming techniques in conjunction with the sqlite connection.  In particular, the cursor's `execute()` method supports value substitutionusing the `?` character, which makes adding multiple records a bit easier.  See the [docs](https://docs.python.org/2.7/library/sqlite3.html) for more details.


```python
last_sale = (None, 4000, 5, 22, 619000)
c.execute('INSERT INTO houses VALUES (?,?,?,?,?)',last_sale)

# Remember to commit the changes
conn.commit()
```

Notice that in this syntax we use the python `None` value, rather than `NULL`, to trigger SQLite to auto-increment the Primary Key.

There is a related cursor method `executemany()` which takes an array of tuples and loops through them, substituting one tuple at a time.


```python
recent_sales = [
  (None, 2390, 4, 34, 319000),
  (None, 1870, 3, 14, 289000),
  (None, 1505, 3, 90, 269000),
]

c.executemany('INSERT INTO houses VALUES (?, ?, ?, ?, ?)', recent_sales)

conn.commit()
```

Once again, use SQLite Manager to verify the database contents.


![SQLite Manager](./assets/images/SQLiteManager.png)

#### Adding data from a csv file
Next let's load our housing.csv data into an array, and then `INSERT` those records into the database.  In this example we'll use the numpy `genfromtxt` function to read the file and parse the contents.


```python
from numpy import genfromtxt

# import into nparray of ints, then convert to list of lists
data = (genfromtxt('./assets/datasets/', dtype='i8',
                    delimiter=',', skip_header=1)).tolist()

# append a None value to beginning of each sub-list
for d in data:
    d.insert(0, None)
```


```python
data[0:3]
```




    [[None, 2104, 3, 70, 399900],
     [None, 1600, 3, 28, 329900],
     [None, 2400, 3, 44, 369000]]




```python
# loop through data, running an INSERT on each record (i.e. sublist)
for d in data:
    c.execute('INSERT INTO houses VALUES (?, ?, ?, ?, ?)', d)

conn.commit()
```

A reason for this example - remember that all elements in a numpy array must be the same data type, so if we want to 'add a None' to each row, we need to work around this.  Lists can contain mixed types, so that is one approach.

Still, in this case the value we're adding is the same for all records, so we could have simply used a 'None' in the INSERT statement directly.

**Check**how do you delete data?


```python
# similar syntax as before
results = c.execute("SELECT * FROM houses WHERE bdrms = 4")

# here results is a cursor object - use fetchall() to extract a list
results.fetchall()
```




    [(2, 2390, 4, 34, 319000),
     (9, 3000, 4, 75, 539900),
     (10, 1985, 4, 61, 299900),
     (15, 1940, 4, 7, 239999),
     (20, 2300, 4, 77, 449900),
     (23, 2609, 4, 5, 499998),
     (24, 3031, 4, 21, 599000),
     (28, 1962, 4, 53, 259900),
     (37, 2040, 4, 75, 314900),
     (39, 1811, 4, 24, 285900),
     (42, 2132, 4, 28, 345000),
     (43, 4215, 4, 66, 549000),
     (44, 2162, 4, 43, 287000),
     (47, 2567, 4, 57, 314000),
     (50, 1852, 4, 64, 299900)]



### Pandas connector

While databases provide many analytical capabilities, often it's useful to pull the data back into Python for more flexible programming. Large, fixed operations would be more efficient in a database, but Pandas allows for interactive processing.

For example, if you want to aggregate nightly log-ins or sales to present a report or dashboard, this operation is likely not changing and operating on a large dataset. This can run very efficiently in a database rather than by connecting to it with Python.

However, if we want to investigate login or sales data further and ask more interactive questions, then Python would be more practical.


```python
import pandas as pd
from pandas.io import sql
```

Pandas can connect to most relational databases. In this demonstration, we will create and connect to a SQLite database.

SQLite creates portable SQL databases saved in a single file. These databases are stored in a very efficient manner and allow fast querying, making them ideal for small databases or databases that need to be moved across machines.

### Writing data into a database

Data in Pandas can be loaded into a relational database. For the most part, Pandas can use column information to infer the schema for the table it creates. For the next demo we will use the Rossmann stores dataset.


```python
import pandas as pd

data = pd.read_csv('./assets/datasets/housing-data.csv', low_memory=False)
data.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sqft</th>
      <th>bdrms</th>
      <th>age</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2104</td>
      <td>3</td>
      <td>70</td>
      <td>399900</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1600</td>
      <td>3</td>
      <td>28</td>
      <td>329900</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2400</td>
      <td>3</td>
      <td>44</td>
      <td>369000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1416</td>
      <td>2</td>
      <td>49</td>
      <td>232000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3000</td>
      <td>4</td>
      <td>75</td>
      <td>539900</td>
    </tr>
  </tbody>
</table>
</div>



Data is moved to the database through the `to_sql` command, similar to the `to_csv` command.

`to_sql` takes as arguments:
    - `name`, the table name to create
    - `con`, a connection to a database
    - `index`, whether to input the index column
    - `schema`, if we want to write a custom schema for the new table
    - `if_exists`, what to do if the table already exists. We can overwrite it, add to it, or fail


```python
data.to_sql('houses_pandas',
            con=conn,
            if_exists='replace',
            index=False)
```

### Reading data from a database

If we already have data in our database, we can use Pandas to query it. Querying is done through the `read_sql` command in the `sql` module.


```python
sql.read_sql('select * from houses_pandas limit 10', con=conn)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sqft</th>
      <th>bdrms</th>
      <th>age</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2104</td>
      <td>3</td>
      <td>70</td>
      <td>399900</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1600</td>
      <td>3</td>
      <td>28</td>
      <td>329900</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2400</td>
      <td>3</td>
      <td>44</td>
      <td>369000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1416</td>
      <td>2</td>
      <td>49</td>
      <td>232000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3000</td>
      <td>4</td>
      <td>75</td>
      <td>539900</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1985</td>
      <td>4</td>
      <td>61</td>
      <td>299900</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1534</td>
      <td>3</td>
      <td>12</td>
      <td>314900</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1427</td>
      <td>3</td>
      <td>57</td>
      <td>198999</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1380</td>
      <td>3</td>
      <td>14</td>
      <td>212000</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1494</td>
      <td>3</td>
      <td>15</td>
      <td>242500</td>
    </tr>
  </tbody>
</table>
</div>



<a name="guided-practice"></a>
## SQL Syntax (30 mins)

### SQL Operators
> Instructor Note: Each of the following can be demoed in pandas using the data we've setup above. A demo and check are included for each, but it is up to the instructor whether to do these simultaneously or go through them one at a time.

#### SELECT
Every query should start with `SELECT`.  `SELECT` is followed by the names of the columns in the output.

`SELECT` is always paired with `FROM`, and `FROM` identifies the table to retrieve data from.

```sql
SELECT
<columns>
FROM
<table>
```

`SELECT *` denotes returns *all* of the columns.

Housing Data example:
```sql
SELECT
sqft, bdrms
FROM houses_pandas;
```

**Check:** Write a query that returns the `sqft`, `bdrms` and `price`.
>
```sql
SELECT
sqft, bdrms, price
FROM houses_pandas;
```

#### WHERE
`WHERE` is used to filter table to a specific criteria and follows the `FROM` clause.

```sql
SELECT
<columns>
FROM
<table>
WHERE
<condition>
```
Example:
```sql
SELECT
sqft, bdrms, age, price
FROM houses_pandas
WHERE bdrms = 2 and price < 250000;
```

The condition is some filter applied to the rows, where rows that match the condition will be in the output.

**Check:** Write a query that returns the `sqft`, `bdrms`, `age` for when houses older than 60 years.
>```sql
SELECT
sqft, bdrms, age
FROM houses_pandas
WHERE age > 60;
```

### AGGREGATIONS

Aggregations (or aggregate functions) are functions where the values of multiple rows are grouped together as input on certain criteria to form a single value of more significant meaning or measurement such as a set, a bag or a list.

Examples of aggregate functions:

- Average (i.e., arithmetic mean)
- Count
- Maximum
- Minimum
- Median
- Mode
- Sum

In SQL they are performed in a `SELECT` statement as follows.

```sql
SELECT COUNT(price)
FROM houses_pandas;
```

```sql
SELECT AVG(sqft), MIN(price), MAX(price)
FROM houses_pandas
WHERE bdrms = 2;
```

<a name="ind-practice"></a>
## Querying a Database (20 minutes)

Practice querying the SQLite database we've created using any of the methods you've learnt so far:

- console connection
- python `sqlite3` package
- pandas
- firefox browser extension [SQLite Manager](https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager/?src)

Practice querying the PostgreSQL database you can find at [add url here](http://) using:
- console connection
- python `sqlite3` package
- pandas
- [Postico](https://eggerapps.at/postico/)


Questions:
1. What's the average price per room for 1 bedroom apartments?
1. What's the average price per room for 2 bedrooms apartments?
1. What's the most frequent apartment size (in terms of bedrooms)?
1. How many are there of that apartment kind?
1. What fraction of the total number are of that kind?
1. How old is the oldest 3 bedrooms apartment?
1. How old is the youngest apartment?
1. What's the average age for the whole dataset?
1. What's the average age for each bedroom size?

Try to answer all these in SQL.

If you finish, try completing the first sections of [SQL zoo](http://www.sqlzoo.net).

<a name="conclusion"></a>
## Conclusion (5 mins)
We have learnt how to connect to a local database and how to execute simple queries.

***
### ADDITIONAL RESOURCES

- [sqlite3 home](http://www.sqlite.org)  
- [SQLite - Python tutorial](http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html)  
- [SQL zoo](http://www.sqlzoo.net)
