---
title: Intro to Pandas & Time Series Data
duration: "1:25"
creator:
    name: Robby Grodin
    city: Boston
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Intro to Time Series
Week 9 | Lesson 1.3

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Understand what time series analysis is and what it is used for
- Use Pandas to model and manipulate a Time Series
- Explain the functionality afforded to the DateTime object

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Load data into a Pandas DataFrame
- Access data in a DataFrame object
- Use Pandas' built in descriptive statistics functions

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Review the GOOG data set from week 2 for familiarity
- Review both .ipynb notebooks. You will be live-coding the Introduction, Demo, and part of the Discussion sections in these notebooks. **Feel free to diverge from the provided solution code, these are just suggestions. Also, feel free to add more exercises. You know your students best!**

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening)  | What Is Time Series Analysis? |
| 15 min  | [Introduction](#introduction)   | The DateTime Object |
| 20 min  | [Demo](#demo)  | Time Series In Pandas  |
| 15 min  | [Discussion](#discussion)  | Date Ranges and Frequencies |
| 25 min  | [Independent Practice](#ind-practice)  | Manipulating a Time Series  |
| 5 min  | [Conclusion](#conclusion)  | Recapitulation  |

---

<a name="opening"></a>
## What Is Time Series Analysis? (5 mins)
- Statistical modeling of time ordered data observations
- Two main goals:
  * Identifying the underlying mechanisms represented by the sequence of observations
  * Forecasting: predicting the future values of a variable described in the time series
- Examining multiple time series to model dynamic relationships

> Instructor Note: Have the students list the possible business uses for time series analysis, i.e.: Financial Analysis/Forecasting, retail inventory planning, CDC predictions, neuroscience, signal processing, etc.

**Check:** Recall the `np.correlate` function from Week 2, which we used to analyse the relationship between GOOG and AAPL stocks.

<a name="introduction"></a>
## The DateTime Object (15 mins)

As our data will be ordered by time, we will need a powerful library for dealing with timestamps. Luckily, Python provides a module that gives us both simple and complex methods of manipulating dates and times. The cornerstone of the datetime module is the DateTime object, a container representing a time that is either aware or naive. Aware DateTimes have information regarding time zone and daylight savings time, a naive DateTime does not.

Let's check out the [DateTime Documentation](https://docs.python.org/2/library/datetime.html).

```python
from datetime import datetime

# Time this lesson plan was written
lesson_date = datetime(2016, 3, 5, 23, 31, 1, 844089)
```

The DateTime object has all kinds of descriptive methods. Let's try some!

```python
lesson_date.day
lesson_date.month
lesson_date.year
lesson_date.hour
```

**NOTE:** See [Reference A](#ref-a) below for all components that can be extracted from a DateTime object.

We can also use a `timedelta` object to shift a DateTime object. Here's an example:

```python
from datetime import timedelta
offset = timedelta(days=1, seconds=20)
offset.days
offset.seconds
offset.microseconds

now = datetime.now()
now

now + offset
now - offset
```

**Code:** Open the datetime.ipynb notebook and complete the 4 exercises

<a name="demo"></a>
## Time Series In Pandas (20 mins)

Let's load switch over to the timeseries.ipynb notebook, and I'll walk you through loading a time series into Pandas. We'll also go over applying the DateTime functionality to the time series.

<a name="discussion"></a>
## Date Ranges and Frequencies (15 mins)

Using the Pandas documentation, take a few minutes to read about the `asfreq` and `resample` methods.

> Instructor's Note: Give the students a few minutes to read about these methods. Have a brief discussion about the implications of both.

Let's go back to our timeseries.ipynb notebook and implement the two functions to get a better idea of what they do.

Note that `asfreq` gives us a `method` keyword argument. Backfill, or bfill, will propogate the last valid observation forward. In other words, it will use the value preceding a range of unknown indices to fill in the unknowns. Inversely, pad, or ffill, will use the first value succeeding a range of unknown indices to fill in the unknowns.

Now, let's discuss the following points:
- What does `asfreq` do?
- What does `resample` do?
- What is the difference?
- When would we want to use each?

We can also create our own date ranges using a built in function, `date_range`. The `periods` and `freq` keyword arguments grant the user fine-grained control over the resulting values. To reset the time data, use the `normalize=True` directive.

**NOTE:** See [Reference B](#ref-b) below for all of the possible

We are also given a Period object, which can be used to represent a time interval. The Period object consists of a start time and an end time, and can be created by providing a start time and a given frequency.

<a name="ind-practice"></a>
## Manipulating a Time Series (25 mins)

Let's break up into groups and look at the different ways we can manipulate our time series.

Try the following to mutate `df_goog` to represent a daily, weekly, and monthly granularity.
When you have data on a daily level, use the Period and date_range functionalities to practice retrieving data from a DataFrame for a given range or frequency.
- `asfreq`
- `resample`
- `Period`
- `date_range`


**BONUS:**
- Create a new DataFrame with the daily change for each column in df_goog (hint: you'll need to reset the index to a daily timeframe)
- Apply models studied previously to gauge the relationship between a random sampling of columns from df_goog
- Create an Aware DateTime object with Boston's UTC offset.

<a name="conclusion"></a>
## Recapitulation (5 mins)
- Recap the objects and methods discussed
- Discuss how these techniques will help with the Kaggle challenge
- Repeat the importance of reading the documentation (does it do what you think it does, are you re-inventing the wheel, etc.)

### ADDITIONAL RESOURCES

**Reference**

<a name="ref-a"></a>
A) Time/Date components that can be accessed from a DateTime object ([source](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#time-date-components))

| Alias | Description |
|---|---|
| year	| The year of the datetime |
| month	| The month of the datetime |
| day	| The days of the datetime |
| hour	| The hour of the datetime |
| minute	| The minutes of the datetime |
| second	| The seconds of the datetime |
| microsecond	| The microseconds of the datetime |
| nanosecond	| The nanoseconds of the datetime |
| date	| Returns datetime.date |
| time	| Returns datetime.time |
| dayofyear	| The ordinal day of year |
| weekofyear	| The week ordinal of the year |
| week	| The week ordinal of the year |
| dayofweek	| The day of the week with Monday=0, Sunday=6 |
| weekday	| The day of the week with Monday=0, Sunday=6 |
| quarter	| Quarter of the date: Jan=Mar = 1, Apr-Jun = 2, etc. |
| days_in_month	| The number of days in the month of the datetime |
| is_month_start	| Logical indicating if first day of month (defined by frequency) |
| is_month_end	| Logical indicating if last day of month (defined by frequency) |
| is_quarter_start	| Logical indicating if first day of quarter (defined by frequency) |
| is_quarter_end	| Logical indicating if last day of quarter (defined by frequency) |
| is_year_start	| Logical indicating if first day of year (defined by frequency) |
| is_year_end	| Logical indicating if last day of year (defined by frequency) |

<a name="ref-b"></a>
B) Time offset aliases ([source](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases))

| Alias | Description |
|---|---|
| B | business day frequency |
| C | custom business day frequency (experimental) |
| D | calendar day frequency |
| W | weekly frequency |
| M | month end frequency |
| BM | business month end frequency |
| CBM | custom business month end frequency |
| MS | month start frequency |
| BMS | business month start frequency |
| CBMS | custom business month start frequency |
| Q | quarter end frequency |
| BQ | business quarter endfrequency |
| QS | quarter start frequency |
| BQS | business quarter start frequency |
| A | year end frequency |
| BA | business year end frequency |
| AS | year start frequency |
| BAS | business year start frequency |
| BH | business hour frequency |
| H | hourly frequency |
| T, min | minutely frequency |
| S | secondly frequency |
| L, ms | milliseonds |
| U, us | microseconds |
| N | nanoseconds |
