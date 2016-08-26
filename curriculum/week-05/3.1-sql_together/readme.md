---
title: More SQL
duration: "1:25"
creator:
    name: Francesco Mosconi
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) More SQL
Week 5 | Lesson 3.1

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Sort results by a column using `ORDER BY`
- Simplify our syntax using aliases (`AS`)
- Match patterns using `LIKE`
- Select distinct items using `DISTINCT`
- Aggregate values using `GROUP BY`
- Filter on aggregations using `HAVING`


### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Connect to a local or remote relational database
- Add and remove data, create new tables, alter table schemas
- Perform simple queries using SQL language

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck
- Prepare any specific materials
- Provide students with additional resources
- Make sure the GA copy of the northwind database is available at:
        psql -h dsi.c20gkj5cvu3l.us-east-1.rds.amazonaws.com -p 5432 -U dsi_student northwind
        password: gastudents


### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 mins | [Opening](#opening) | Opening |
| 10 mins | [Introduction](#introduction) | More SQL |
| 10 mins | [Guided-practice](#guided-practice_1) | Guided Practice: ORDER BY |
| 10 mins | [Guided-practice](#guided-practice_2) | Guided Practice: Aliases |
| 10 mins | [Guided-practice](#guided-practice_3) | Guided Practice: SQL LIKE Operator |
| 10 mins | [Guided-practice](#guided-practice_4) | Guided Practice: DISTINCT and LIMIT Operators |
| 10 mins | [Guided-practice](#guided-practice_5) | Guided Practice: GROUP BY Operator |
| 10 mins | [Guided-practice](#guided-practice_6) | Guided Practice: HAVING Operator |
| 10 mins | [Ind-practice](#ind-practice) | Independent Practice |
| 5 mins | [Conclusion](#conclusion) | Conclusion |

<a name="opening"></a>
## Opening (5 mins)
We have seen how to connect to a local sqlite database and to a remote postgresql database.

**Check:** What SQL commands have we learned so far?

> Answer:
- CREATE
- INSERT
- DELETE
- UPDATE
- SELECT

**Check:** What different commands have we learned for SQLite and PostgreSQL?

> Answer:
- how to list schema and tables


<a name="introduction"></a>
## More SQL (10 mins)

In this lecture we'll learn a few more useful `SQL` commands that will give us the ability to perform more complex queries.

In particular we will learn to:
- Sort results by a column using `ORDER BY`
- Simplify our syntax using aliases
- Match patterns using `LIKE`
- Select distinct items using `DISTINCT`
- Aggregate values using `GROUP BY`
- Filter on aggregations using `HAVING`

For all the following example we will use the well-known [Northwind sample database](https://northwinddatabase.codeplex.com/).

We have imported this database into our PostgreSQL instance that you can connect to as follows:

    psql -h dsi.c20gkj5cvu3l.us-east-1.rds.amazonaws.com -p 5432 -U dsi_student northwind
    password: gastudents

We will use a few tables from this database:

`customers`:

|CustomerID |CompanyName |ContactName | ContactTitle |Address|City | Region | PostalCode | Country |Phone | Fax|
|---|
|ALFKI| Alfreds Futterkiste| Maria Anders | Sales Representative | Obere Str. 57 | Berlin|| 12209| Germany | 030-0074321| 030-0076545|
|ANATR| Ana Trujillo Emparedados y helados | Ana Trujillo | Owner| Avda. de la Constitución 2222 | México D.F. || 05021| Mexico| (5) 555-4729 | (5) 555-3745|
|ANTON| Antonio Moreno Taquería| Antonio Moreno | Owner| Mataderos2312 | México D.F. || 05023| Mexico| (5) 555-3932 |
|...|...|...|...|...|...|...|...|...|...|...|

`orders`:

|OrderID | CustomerID | EmployeeID | OrderDate| RequiredDate | ShippedDate | ShipVia | Freight | ShipName|ShipAddress |ShipCity| ShipRegion | ShipPostalCode | ShipCountry |
|----|
|10248 | VINET|5 | 1996-07-04 | 1996-08-01 | 1996-07-16| 3 | 32.38 | Vins et alcools Chevalier | 59 rue de l'Abbaye | Reims|| 51100| France|
|10249 | TOMSP|6 | 1996-07-05 | 1996-08-16 | 1996-07-10| 1 | 11.61 | Toms Spezialitäten| Luisenstr. 48| Münster|| 44087| Germany|
|10250 | HANAR|4 | 1996-07-08 | 1996-08-05 | 1996-07-12| 2 | 65.83 | Hanari Carnes | Rua do Paço, 67| Rio de Janeiro | RJ | 05454-876| Brazil|
|...|...|...|...|...|...|...|...|...|...|...|

`order_details`:

| OrderID |  ProductID |  UnitPrice | Quantity | Discount |
| ----- |
|10248|11|14|12|0|
|10248|42|9.8|10|0|
|10248|72|34.8|5|0|
|10249|14|18.6|9|0|
|10249|51|42.4|40|0|
|10250|41|7.7|10|0|
|...|...|...|...|...|


**Check:** Let's come up with a few queries you'd be curious to run on these tables.


<a name="guided-practice_1"></a>
## Guided Practice: ORDER BY (10 mins)

The `ORDER BY` keyword is used to sort the result-set by one or more columns. It sorts the records in ascending order by default. To sort the records in a descending order, you can use the `DESC` keyword.

### SQL ORDER BY Syntax

```sql
SELECT _column_name_,_ column_name_  
FROM _table_name_  
ORDER BY _column_name _ASC|DESC,_ column_name_ ASC|DESC;
```

#### Example

The following SQL statement selects all customers from the "Customers" table,  sorted by the "Country" column:

```sql
SELECT "CustomerID", "CompanyName", "Country" FROM customers
ORDER BY "Country";
```

|CustomerID|CompanyName|Country|
|----|
|OCEAN|Océano Atlántico Ltda.|Argentina|
|CACTU|Cactus Comidas para llevar|Argentina|
|RANCH|Rancho grande |Argentina|
|...|...|...|


#### ORDER BY DESC Example

The following SQL statement selects all customers from the "Customers" table, sorted DESCENDING by the "Country" column:


```sql
SELECT "CustomerID", "CompanyName", "Country" FROM customers
ORDER BY "Country" DESC;
```

|CustomerID|CompanyName|Country|
|----|
|GROSR|GROSELLA-Restaurante |Venezuela|
|LILAS|LILA-Supermercado|Venezuela|
|HILAA|HILARION-Abastos |Venezuela|
|...|...|...|



#### ORDER BY Several Columns Example

The following SQL statement selects all customers from the `customers` table, sorted by the "Country" and the "CompanyName" columns:

```sql
SELECT "CustomerID", "CompanyName", "Country" FROM customers
ORDER BY "Country", "CompanyName";
```

|CustomerID|CompanyName|Country|
|----|
|CACTU|Cactus Comidas para llevar|Argentina|
|OCEAN|Océano Atlántico Ltda.|Argentina|
|RANCH|Rancho grande |Argentina|
|...|...|...|

**Check:** run a few queries on the provided database and try using the `ORDER BY` command.

<a name="guided-practice_2"></a>
## Guided Practice: Aliases (10 mins)

SQL aliases are used to give a database table, or a column in a table, a temporary name. Aliases are often created to make column names more readable.

### SQL Alias Syntax for Columns

```sql
SELECT _column_name_ AS _alias_name_  
FROM _table_name;_
```
### SQL Alias Syntax for Tables
```sql
SELECT _column_name(s)_  
FROM _table_name _AS _alias_name;_
```

#### Alias Examples for Table Columns

The following SQL statement specifies two aliases, one for the `CompanyName`  column and one for the `ContactName` column:

```sql
SELECT "CompanyName" AS "Customer", "ContactName" AS "[Contact Person]"
FROM customers;
```

|Customer|[Contact Person]|
|----|
|Alfreds Futterkiste| Maria Anders|
|Ana Trujillo Emparedados y helados| Ana Trujillo|
|Antonio Moreno Taquería| Antonio Moreno|
|...|...|


In the following SQL statement we combine four columns (Address, City, PostalCode and Country) and create an alias named `Address`:

```sql
SELECT "CompanyName" AS "Customer",
    CONCAT("Address",', ',"City",', ', "PostalCode",', ',"Country") AS "Address"
FROM customers;
```

|Customer|Address|
|----|
|Alfreds Futterkiste| Obere Str. 57, Berlin, 12209, Germany|
|Ana Trujillo Emparedados y helados| Avda. de la Constitución 2222, México D.F., 05021, Mexico|
|Antonio Moreno Taquería Mataderos| 2312, México D.F., 05023, Mexico|
|...|...|


#### Alias Example for Tables

The following SQL statement selects all the orders from the customer with  CustomerID=4 (Around the Horn). We use the `customers` and `orders` tables, and  give them the table aliases of `c` and `o` respectively. (This time we used aliases to make the SQL shorter.)


```sql
SELECT o."OrderID", o."OrderDate", c."CompanyName"
FROM customers AS c, orders  AS o  
WHERE c."CompanyName" = 'Around the Horn' AND c."CustomerID"=o."CustomerID";
```

|CustomerID|OrderDate|CompanyName|
|----|
|10355|1996-11-15|Around the Horn|
|10383|1996-12-16|Around the Horn|
|10453|1997-02-21|Around the Horn|
|10558|1997-06-04|Around the Horn|
|...|...|...|

**Check** what would be the same SQL statement without aliases?

Aliases can be useful when:

- More than one table is involved in a query
- Functions are used in the query
- Column names are long or not very readable
- Two or more columns are combined together

**Check:** Try running the same queries as above with aliases. Are they more readable?

<a name="guided-practice_3"></a>
## Guided Practice: SQL LIKE Operator (10 mins)

The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

### SQL LIKE Syntax
```sql
SELECT _column_name(s)_  
FROM _table_name_  
WHERE _column_name_ LIKE _pattern_;
```

#### SQL LIKE Operator Examples

The following SQL statement selects all customers with a City starting with  the letter "S":

```sql
SELECT * FROM customers
WHERE "City" LIKE 'S%';
```

|CustomerID |CompanyName |ContactName | ContactTitle |Address|City | Region | PostalCode | Country |Phone | Fax|
|---|
|BLONP| Blondesddsl père et fils|Frédérique Citeaux|Marketing Manager| 24, place Kléber|Strasbourg||67000| France|88.60.15.31|88.60.15.32|
|COMMI| Comércio Mineiro|Pedro Afonso|Sales Associate|Av. dos Lusíadas, 23|Sao Paulo| SP|05432-043| Brazil|(11) 555-7647| 
|FAMIA| Familia Arquibaldo|Aria Cruz| Marketing Assistant | Rua Orós, 92|Sao Paulo| SP|05442-030| Brazil|(11) 555-9857| 
|...|...|...|...|...|...|...|...|...|...|...|

**Tip:** The "%" sign is used to define wildcards (missing letters) both before and after the pattern. Also notice that `PostgreSQL` is case sensitive.

The following SQL statement selects all customers with a City ending with the  letter "s":

```sql
SELECT * FROM customers
WHERE "City" LIKE '%s';
```

|CustomerID |CompanyName |ContactName | ContactTitle |Address|City | Region | PostalCode | Country |Phone | Fax|
|---|
|CACTU| Cactus Comidas para llevar|Patricio Simpson|Sales Agent|Cerrito 333 |Buenos Aires||1010|Argentina| (1) 135-5555|(1) 135-4892|
|DUMON| Du monde entier|Janine Labrune|Owner| 67, rue des Cinquante Otages|Nantes||44000| France|40.67.88.88| 40.67.89.89|
|FRANR| France restauration|Carine Schmitt|Marketing Manager| 54, rue Royale|Nantes||44000| France|40.32.21.21| 40.32.21.20|
|...|...|...|...|...|...|...|...|...|...|...|

Using the NOT keyword allows you to select records that do NOT match the pattern. The following SQL statement selects all customers with Country NOT  containing the pattern "land":

```sql
SELECT * FROM customers
WHERE "Country" NOT LIKE '%land%';
```
|CustomerID |CompanyName |ContactName | ContactTitle |Address|City | Region | PostalCode | Country |Phone | Fax|
|---|
|ALFKI| Alfreds Futterkiste|Maria Anders|Sales Representative|Obere Str. 57| Berlin||12209| Germany|030-0074321| 030-0076545|
|ANATR| Ana Trujillo Emparedados y helados|Ana Trujillo|Owner| Avda. de la Constitución 2222| México D.F.|| 05021| Mexico|(5) 555-4729|(5) 555-3745|
|ANTON| Antonio Moreno Taquería|Antonio Moreno|Owner| Mataderos|2312 México D.F.|| 05023| Mexico|(5) 555-3932|
|...|...|...|...|...|...|...|...|...|...|...|

**Check:** Run a few queries on the provided database and try using the `LIKE` command.

<a name="guided-practice_4"></a>
## Guided Practice: DISTINCT and LIMIT Operators (10 mins)

The SELECT DISTINCT statement is used to return only distinct (different) values. In a table, a column may contain many duplicate values; and sometimes you only want to list the different (distinct) values.

### SQL SELECT DISTINCT Syntax
```sql
SELECT DISTINCT _column_name_,_column_name_  
FROM _table_name_;
```

#### SELECT DISTINCT Example

The following SQL statement selects only the distinct values from the "City"  columns from the "Customers" table:

```sql
SELECT DISTINCT "City" FROM customers;
```

| City|
|---|
|Leipzig|
|London|
|Nantes|
|...|

The `DISTINCT` operator is equivalent to the `numpy.unique` command.

### SQL SELECT LIMIT Syntax
Sometimes we may want to only retrieve a fixed number of records from the database. This is where the `LIMIT` operator comes in.

```sql
SELECT _column_name_,_column_name_  
FROM _table_name_
LIMIT _number_of_records;
```

#### SELECT LIMIT Example

The following SQL statement selects only the first 3 values from the "City"  columns from the "Customers" table:

```sql
SELECT DISTINCT "City"
FROM customers
LIMIT 3;
```

| City|
|---|
|Leipzig|
|London|
|Nantes|

The `LIMIT` operator is equivalent to the `pandas.Dataframe.head` command.

**Check:** Try running the same queries using `DISTINCT` and `LIMIT`

<a name="guided-practice_5"></a>
## Guided Practice: GROUP BY Operator (10 mins)

A table may contain several records that have a common key. Consider for example the following `order_details` table:


| OrderID |  ProductID |  UnitPrice | Quantity | Discount |
| ----- |
|10248|11|14|12|0|
|10248|42|9.8|10|0|
|10248|72|34.8|5|0|
|10249|14|18.6|9|0|
|10249|51|42.4|40|0|
|10250|41|7.7|10|0|
|...|...|...|...|...|


The _GROUP BY_ statement is used in conjunction with the aggregate functions to group the result-set by one or more columns. For example we may want to know the total number of items purchased in each order.

#### SQL GROUP BY Syntax

The syntax to perform a _GROUP BY_ operation is the following:

```sql
SELECT column_name, aggregate_function(column_name)  
FROM table_name  
WHERE column_name operator value  
GROUP BY column_name;
```
We select the column we want to aggregate on and the function.


#### Example

In order to calculate the total amount of items in a specific order we can use the following query:

```sql
SELECT "OrderID", SUM("Quantity")
FROM order_details
GROUP BY "OrderID"
```

Note that in `PostgreSQL` unquoted names are case-insensitive. Thus `SELECT * FROM hello` and `SELECT * FROM HELLO` are equivalent.

However, quoted names are case-sensivite. `SELECT * FROM "hello"` is not equivalent to `SELECT * FROM "HELLO"`.

To make a "bridge" between quoted names and unquoted names, unquoted names are implicitly lowercased, thus hello, HELLO and HeLLo are equivalent to "hello", but not to "HELLO" or "HeLLo".

Thus, when creating entities (tables, views, procedures, etc) in PostgreSQL, you should specify them either unquoted, or quoted-but-lowercased.

<a name="guided-practice_6"></a>
## Guided Practice: HAVING Operator (10 mins)

The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions. Let's consider the previous example where we aggregated the `Quantity` of an order. What if we would like to filter the results for orders where the Maximum discount applied on any item is lower than 10%?

#### SQL HAVING Syntax

```sql
SELECT column_name, aggregate_function(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name
HAVING aggregate_function(column_name) operator value;
```

##### Example

```sql
SELECT "OrderID", SUM("Quantity"), MAX("Discount")
FROM order_details
GROUP BY "OrderID"
HAVING MAX("Discount") <= 0.1;
```

|OrderID|sum|max|
|---|
|10501|20|0|
|10295|4|0|
|10827|36|0|

<a name="ind-practice"></a>
## Independent Practice (10 minutes)

Now that you've learned a lot more commands, try combining them:

- Retrieve the top 3 orders by number of items ordered
- Retrieve the oldest 5 orders
- Retrieve the 5 most recent orders. Nest that query into another one that ranks these 5 orders by shipping country (alphabetical order)
- Try some queries on your own

> Answers:
```sql
SELECT "OrderID", SUM("Quantity") AS "Sum"
FROM order_details
GROUP BY "OrderID"
ORDER BY "Sum" DESC
LIMIT 3;
```
```sql
SELECT "OrderID", "OrderDate"
FROM orders
ORDER BY "OrderDate"
LIMIT 5;
```
```sql
SELECT * FROM (
    SELECT "OrderID", "OrderDate", "ShipCountry"
    FROM orders
    ORDER BY "OrderDate" DESC
    LIMIT 5
    ) AS fivemostrecent
ORDER BY "ShipCountry";
```

<a name="conclusion"></a>
## Conclusion (5 mins)
In this lesson we have learned many more new commands to make our SQL queries more powerful.


In particular we learned how to:
- Sort results by a column using `ORDER BY`
- Simplify our syntax using aliases
- Match patterns using `LIKE`
- Select distinct items using `DISTINCT`
- Aggregate values using `GROUP BY`
- Filter on aggregations using `HAVING`

**Check:** can you think of a few more business cases where these are useful?

***

### ADDITIONAL RESOURCES

- [PostgreSQL Documentation](http://www.postgresql.org/docs/)
- [Sqlite Documentation](https://www.sqlite.org/docs.html)
