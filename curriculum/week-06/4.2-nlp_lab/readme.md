
---
title: Natural Language Processing Lab
type: lab
duration: "1:25"
creator:
    name: Francesco Mosconi
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Natural Language Processing Lab

## Introduction

In this lab we will further explore Scikit's and NLTK's capabilities to process text. We will use the [20 Newsgroup dataset](http://qwone.com/~jason/20Newsgroups/), which is provided by Scikit-Learn. This is a collection of approximately 20,000 newsgroup documents, partitioned (nearly) evenly across 20 different newsgroups. The 20 newsgroups collection has become a popular data set for experiments in text applications of machine learning techniques, such as text classification and text clustering.

We will restrict the analysis to 4 groups and will attempt to classify them starting from the corresponding text.

This is a typical example of text classification, where a data scientist's task is to train a model that can partition text in pre-defined categories. Other examples include sentiment analysis and topic assignment.

## Exercise

### Requirements

1. Data inspection: let's first explore the data and see how it is organized
- Bag of Words model: let's build a simple model
- Hashing and TF-IDF: let's beef-up our model with some more powerful techniques
- Classifier comparison: what's our best model?

**Bonus:**
- Other Classifiers: What's the performance of other classifiers?
- Explore NLTK in more detail

### Code

[Starter Code](./code/starter-code/starter-code-4_2.ipynb)

>[Solution Code](./code/solution-code/solution-code-4_2.ipynb)

## Additional resources
- [Text Feature Extraction](http://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
- [20 Newsgroups](http://qwone.com/~jason/20Newsgroups/)
