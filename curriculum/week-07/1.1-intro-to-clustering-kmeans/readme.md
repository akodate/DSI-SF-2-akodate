---
title: Intro to Clustering
duration: "1:25"
creator:
    name: Patrick Smith
    city: DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Intro to Clustering
Week 7 | Lesson 1.1

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Format and preprocess data for cluster
- Perform a K-Means Clustering Analysis
- Evaluate clusters for fit 


### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Write functions in Python
- Have a working knowledge of Pandas and Scikit-Learn

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Prepare the starter and solution code on their local machine

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening)  | Topic description  |
| 10 min  | [Introduction](#introduction)   | What is Clustering?  |
| 15 min  | [Demo](#demo)  | Example of Clustering  |
| 25 min  | [Guided Practice](#guided-practice<a name="opening"></a>)  | Format your data for clustering |
| 25 min  | [Independent Practice](#ind-practice)  | Perform a k-means cluster analysis |
| 5 min  | [Conclusion](#conclusion)  | Conclusion  |

---

<a name="opening"></a>
## Opening (5 mins)
> Instructor Note: 
- Review pre-work, projects, or exit ticket, if applicable
- Review current lesson objectives
- Reference general course content or topics (e.g. code or concepts that have been used across multiple lessons)
- Include Hook / Real-world Relevance (why the content from this lesson is useful or important)

<a name="introduction"></a>
## Introduction: Intro to Clustering (5 mins)


#### What is Clustering? 

Clustering is one of the most ubiquitous and widespread methods for understanding a dataset. In clustering, we group points in a dataset together so that the members of that group are more similar to each other than they are to members of other groups. In this sense, we're creating groups to understand our data. 

For instance; Your employer gives you a dataset of voter preferences from a local poll and they want you to figure out just exactly how these voters are grouping based on their preferences. The answer: clustering!

#### How is Clustering Different from Classification? 

You may be thinking: How is clustering different from classification? If we're just creating groups, aren't the two one and the same?
There exists an important distinction between classification and clustering: In classification, we are grouping data according to a set of predefined groups; We know what the characteristics of a mammal are, and humans have the characteristics of that predefined group. In clustering, however, we set out to figure out *if* the points in our dataset have relationships with each other, and we group those with similar characteristics in a cluster. In other words, we need to discover the classes themselves.

**Check:** How is clustering different from classification? When might we use one over the other? 

<a name="demo"></a>
## How Does Clustering Work? - Demo (10 mins)

The are numerous algorithms for clustering a dataset; today we're going to look at one of the most commonly used algorithms: k-means.

#### K-Means Clustering

K-Means is a clustering algorithm that assumes *k* clusters, and then computes these clusters based on the attributes of the available data. The algorithm takes your entire dataset, let's call it *df*, and iterates over its attributes to determine clusters based around centers, known as **centroids**. Unlike many statistical methods, there is no finite way to determine what "k" is; for our methods, we're going to approximate *k* based on distribution of our data. 

#### K-Means in Python

Implementing k-means in python is as simple as calling a function from the Scikit-Learn toolbox:

```python
sklearn.cluster.KMeans(n_clusters=k)
```

Getting to this point takes a good deal of preprocessing - however we'll touch on that in a bit. To find *k* in python, we can use an approximation using a graph of the dataset.

We can also test the accuracy of our k-means test by computing the **Silhouette Coefficient**, a metric to test how well each of the data points lies within the cluster

```python
metrics.silhouette_score(test, labels, metric='euclidean')
plt.plot(s)
plt.ylabel("Silouette")
plt.xlabel("k")
sns.despine()
```

**Check:** What is a centroid? How does it relate to clustering? .

<a name="guided-practice"></a>
## Guided Practice: Preparing your analysis & Handling Data (15 mins)

Let's say that you're asked to perform a k-means clustering analysis on the classic Iris dataset - how would you go about it?

First; Let's setup out imports: 

```python
%matplotlib inline 

import pandas as pd
import numpy as np
from sklearn import cluster
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn import cluster, datasets
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
```

We're going to be using **Scikit-Learn** for our analysis; let's load in the [Iris](./assets/datasets/iris.csv) dataset using Pandas ```read.csv``` and check the head to see it's structure:

```python
iris = pd.read_csv(".../iris.csv")
iris.head(n=5)
```
Now that we have our data; let's convert it to a Pandas dataframe for our analysis: 

```python
df = pd.DataFrame(data=iris, columns=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Name'])
```

Our dataset has the categorical column **Name** in it, so we'll to convert this columns to numeric data for the k-means algorithm to accept it. Typically, that would take a simple **if** statement to for all of the values in the categorical column. For this dataset, the name column has *Iris-setosa*, *Iris-virginica*, and *Iris-versicolor* as attributes. 

Let's write a definition: 

```python
def name_to_numeric(x):
    if x=='Iris-setosa':
        return 1
    if x=='Iris-virginica':
        return 2
    if x=='Iris-versicolor':
        return 3
```

and apply: 

```python
df['name_num'] = df['name'].apply(name_to_numeric)
del df['name']


```

Now let's plot the data to see the distributions:

```python
df.plot(kind='SepalLength',x='_num',y='name_num')
```
If we run this plot multiple times using different factor combinations -  we can see that regardless of what factors we plot, there seems to be two distinct clusters emerging - this will help us with the next portion of our analysis: running the k-means test.  

**Check:** Were students able to successfully run their own code? Does is match the instructors results? 


<a name="guided-practice"></a>
## Guided Practice: Perform K-Means Clustering (15 mins)

Before you perform your k-means test - there are still some transformations to do: 

We convert our data into a Numpy Array:

```python
dn = df.as_matrix(columns=None)
```
and we're ready to go!

Now that we've formatted our data and understand it's structures, we can finally go ahead and cluster.

We're going to set *k* at two given behavior we were seeing above in our graphs. 

```python
k = 2
kmeans = cluster.KMeans(n_clusters=k)
kmeans.fit(dn1)
```

We can use Scikit's built-in functions to determine the locations of the centroids and their labels: 

```python
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
```

And to compute the clusters' silhouette coefficient:

```python
metrics.silhouette_score(dn1, labels, metric='euclidean')
```

...and we're done! You've completed your first clustering analysis.

**Check:** Were students able to successfully run their own code? Does it match the instructors results?


<a name="ind-practice"></a>
## Independent Practice: Perform a K-Means Analysis (15 minutes)

> Instructor Note: This can be a pair programming activity or done indpendently.

Now that we've walked through the process of clustering, it's time to try it on your own. We're going to be working with the mtcars data set, and your job is to cluster these cars to understand their various attributes.

The dataset contains a listing of 33 different cars from a used car dealership - your task is the cluster the cars to discover their groupings. For each car, you have a variety of technical information related to the car's performance. 

Open the [data](./assets/datasets/mtcars.csv) and [starter code](./code/starter-code/starter-code.ipynb) and try to work through both exercises with a partner. Do your best!

**Check:** Were you able to complete the starter code? Discuss the two variables you chose and explain how your plots demonstrate the data.

<a name="conclusion"></a>
## Conclusion (5 mins)
-  Check: What is Clustering?
- Check: How is Clustering Different from Classification?


***

### ADDITIONAL RESOURCES

- An [Introductory Tutorial on Clustering](http://home.deib.polimi.it/matteucc/Clustering/tutorial_html/)
- A [Deep Dive from Wikipedia](https://en.wikipedia.org/wiki/K-means_clustering)
- A Blog From [Galvanize on Clustering](http://www.galvanize.com/blog/introduction-k-means-cluster-analysis/#.VzzxhGPqNFI)
