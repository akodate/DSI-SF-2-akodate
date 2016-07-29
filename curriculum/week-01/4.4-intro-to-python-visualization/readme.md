---
title: Data Viz Principles
duration: "1:5"
creator:
    name: Lucy Williams 
    city: DC
updated:
    name: David Yerrington
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Data Viz Principles
Week 1 | Lesson 4.4


### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Describe the characteristics of a great data visualization


### STUDENT PRE-WORK
*Before this lesson, you should/might already be able to:*
- Open up Tableau and take a look around


### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Slide prep


### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Introduction](#introduction)   | Why use data visualizations?  |
| 10 min  | [Demo](#demo)  | Anscomb's Quartet  |
| 25 min  | [Demo](#demo)  | Visualization attributes   |
| 25 min  | [Demo](#demo)  | Choosing the right chart   |
| 20 min  | [Independent Practice](#ind-practice)  |   |
| 5 min  | [Conclusion](#conclusion)  |   |

---

<a name="Why use data visualizations?"></a>
## Introduction: Why use data visualizations? (5 mins)

Because of the way the human brain processes information, using charts or graphs to 
visualize large amounts of complex data is easier than poring over spreadsheets or 
reports. Data visualization is a quick, easy way to convey concepts in a universal 
manner – and you can experiment with different scenarios by making slight adjustments.

[data viz](http://www.sas.com/en_us/insights/big-data/data-visualization.html)



<a name="Anscombe's Quartet"></a>
## Demo: Anscomb's Quartet (10 mins)

Here is the summary statistics for four plots. What do you think the visualization for 
each of these plots would look like? 

![summary statistics for four different plots](https://github.com/generalassembly-studio/dsi-course-materials/blob/master/curriculum/04-lessons/week-01/4.4-lesson/assets/images/anscombs%20quartet.png)

You can probably already guess that the answer is, although the four plots have the same summary statistics, 
they actually are completely different and this can be seen when we visualize them together. 

![anscomb's quartet](https://github.com/generalassembly-studio/dsi-course-materials/blob/master/curriculum/04-lessons/week-01/4.4-lesson/assets/images/anscombs%20quartert%20visualization.png)

Anscomb's quartet reminds us not to rely completely on just the summary stats of our data. 
And that, especially during exploratory data analysis (EDA), which we will get to in Week 2, 
making some exploratory visual plots could keep us from making some incorrect assumptions 
about our data.



<a name="Visualization attributes"></a>
## Demo: Visualization attributes (25 mins)

What do you think might be impotant attributes that a data visualization should have? 

Let's take a look at what Jeffrey Shaffer, who teaches data visualization at the 
University of Cincinnati, thinks is important. 

![](https://github.com/generalassembly-studio/dsi-course-materials/blob/master/curriculum/04-lessons/week-01/4.4-lesson/assets/images/data%20attributes.png)

Something really interesting, is that some attributes have more of an effect on our brains. 
The one we tend to focus on most is position, then color and size. 

Let's take a look at three visualizations. Which one of the three catches your attention 
the most and why?
![](https://github.com/generalassembly-studio/dsi-course-materials/blob/master/curriculum/04-lessons/week-01/4.4-lesson/assets/images/mixed%20shapes.png)

![](https://github.com/generalassembly-studio/dsi-course-materials/blob/master/curriculum/04-lessons/week-01/4.4-lesson/assets/images/squares%20and%20circles.png)

![](https://github.com/generalassembly-studio/dsi-course-materials/blob/master/curriculum/04-lessons/week-01/4.4-lesson/assets/images/color.png)

Let's focus on color for a minute. Generally, in data visualizations, you’re going to 
use color in one of three ways: sequential, diverging, or categorical. 

Sequential colors are used to show values ordered from low to high.

![sequential](https://github.com/generalassembly-studio/dsi-course-materials/blob/master/curriculum/04-lessons/week-01/4.4-lesson/assets/images/sequential.png)

Divergent colors are used to show ordered values that have a critical midpoint, like an 
average or zero.

![divergent](https://github.com/generalassembly-studio/dsi-course-materials/blob/master/curriculum/04-lessons/week-01/4.4-lesson/assets/images/divergent.png)

Categorical colors are used to distinguish data that falls into distinct groups.

![categorical](https://github.com/generalassembly-studio/dsi-course-materials/blob/master/curriculum/04-lessons/week-01/4.4-lesson/assets/images/categorical.png)

[shaffer: data viz attributes](http://mediashift.org/2016/02/checklist-does-your-data-visualization-say-what-you-think-it-says/)



<a name="Choosing the right chart "></a>
## Demo: Choosing the right chart  (25 mins)

In addition to taking visualization attributes into consideration, you should also 
consider carefully, which kind of chart or graph to use. Let's look at a few commonly 
used charts and graphs. 

Bar chart
Bar charts are one of the most common ways to visualize data. Why? Because it's easy 
to compare information, revealing highs and lows quickly. Bar charts are
most effective when you have numerical data that splits neatly into different
categories.

![](https://github.com/generalassembly-studio/dsi-course-materials/blob/master/curriculum/04-lessons/week-01/4.4-lesson/assets/images/bar%20chart.png)


Pie chart
The only time that pie charts should be used is to show relative proportions 
or percentages of information. Pie charts are the most commonly mis-used chart type.
If you want to compare data, leave it to bars or stacked bars. If your viewer
has to work to translate pie wedges into relevant data or compare pie charts, key points
you might be trying to convey may be missed. 

![](https://github.com/generalassembly-studio/dsi-course-materials/blob/master/curriculum/04-lessons/week-01/4.4-lesson/assets/images/pie%20chart.jpg)
[pie chart](http://www.tv.com/news/learning-about-the-2013-pilot-season-through-pie-charts-136243394841/)

Scatter plot
Scatter plots are a great way to give you a sense of trends, concentrations 
and outliers. This will give you a good idea of where you may want to investigate
further. 

![](https://github.com/generalassembly-studio/dsi-course-materials/blob/master/curriculum/04-lessons/week-01/4.4-lesson/assets/images/scatter%20plot.png)
[scatter plot](https://en.wikibooks.org/wiki/Statistics/Displaying_Data/Scatter_Graphs)

Histogram chart
Histograms are useful when you want to see how your data are distributed across groups.

![](https://github.com/generalassembly-studio/dsi-course-materials/blob/master/curriculum/04-lessons/week-01/4.4-lesson/assets/images/histogram%20chart.png)

This is not an all inclusive list of the kinds of charts and graphs that one 
could use, but the point is, there are several types. Consideration should be
given to which one is most appropriate to represent a particular data set. 

[charts and graphs](https://drive.google.com/file/d/0Bx2SHQGVqWasT1l4NWtLclJJcWM/view)



<a name="ind-practice"></a>
## Independent Practice: Topic (20 minutes)
- Create a Tableau visualization. Try to keep in mind all the points that were made above. 
- Share it with a partner. What's the first question they ask you? 


<a name="conclusion"></a>
## Conclusion (5 mins)
- Why is visualization so important? 
- What are some things to keep in mind when creating a visualization? 
- Describe when you would use particular types of charts or graphs. 
    - bar chart?
    - pie chart? 
    - scatter plot?
    - histogram chart? 
