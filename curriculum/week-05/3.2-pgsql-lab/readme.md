---
title: SQL Lab
type: lab
duration: "1:25"
creator:
    name: Francesco Mosconi
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) SQL Lab

In this lab we will learn how to execute SQL from the ipython notebook and practice some queries on the  [Northwind sample database](https://northwinddatabase.codeplex.com/) that we used in Lesson 3.1.

We have imported this database into our PostgreSQL which you can access as follows:

    psql -h dsi.c20gkj5cvu3l.us-east-1.rds.amazonaws.com -p 5432 -U dsi_student northwind
    password: gastudents

## Introduction

Use your new SQL skills to query the Northwind database and extract some interesting information.

## Exercise

#### Requirements

- Inspect the database (what tables, what schemas)
- Inspect the products table (what columns, what data types)
- Inspect the orders table (what columns, what data types)

**Bonus:**
- Explore other tables in the database (employees, suppliers, etc.)


#### Starter code

[Starter code](code/starter-code/starter-code-3_2.ipynb)

> [Solution code](code/solution-code/solution-code-3_2.ipynb)


## Additional Resources

- [Ipython-SQL extension](https://github.com/catherinedevlin/ipython-sql).
- [Pandas Merge doc](http://pandas.pydata.org/pandas-docs/stable/merging.html)
