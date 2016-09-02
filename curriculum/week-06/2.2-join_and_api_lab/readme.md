---
title: APIs and SQL Joins Lab
type: lab
duration: "1:25"
creator:
    name: Francesco Mosconi
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) APIs and SQL Joins Lab
The city of San Francisco wants to assess the quality of restaurants in the city. Their data is scattered across multiple sources and incomplete.

They tasked you to help them assess it.

They would like to know where are there more violations in order to better manage their inspections.

## Introduction

To answer the prompt we will need to retrieve and merge data from multiple sources.

> Note: We can do this with SQLite or PostgreSQL locally

## Exercise

The starter code will guide you through the next points.

#### Requirements

1. Open the files and look at their content
-  Import the files to a local database
    1. Display the first few lines of each table
    - Investigate violations using SQL and Pandas
    - Investigate Inspections using SQL and Pandas
- Zipcode analysis
Final recommendation

**Bonus:**
- Neighborhood data
    - Google Geocoding API
    - Fast requests with Pycurl
    - Polygons and points with Shapely
    - Further exploration: PostGIS, Postgres with GIS

#### Starter code

[Starter code](./code/starter-code/starter-code-3_2.ipynb)

> [Solution code](./code/solution-code/solution-code-3_2.ipynb)


## Additional Resources

- [Ipython-SQL extension](https://github.com/catherinedevlin/ipython-sql).
- [PostgreSQL](http://www.postgresql.org/)
- [Google Geocoding API](https://developers.google.com/maps/documentation/geocoding/intro)
