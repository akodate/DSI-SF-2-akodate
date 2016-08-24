---
title: Classification Case Studies
duration: "1:25"
creator:
    name: Francesco Mosconi
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Classification Case Studies
Week 5 | Lesson 2.1

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Walk through real world dataset case studies
- Map out the analytics/data science workflow used
- Discuss pros/cons of the methods involved

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Perform EDA
- Perform classification
- Demonstrate proficiency with basic SQL syntax


### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck
- Prepare any specific materials
- Provide students with additional resources


### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 10 mins | [Opening](#opening) | Opening |
| 25 mins | [Case](#case_1) | Default of Credit Card clients / Calling Emergency Medical Services |
| 25 mins | [Case](#case_2) | Chronic Kidney Disease / A fall detection system using k-nearest neighbor classifier |
| 25 mins | [Case](#case_3) | Student Alcohol Consumption / Machine-learning prediction of cancer survival:|
| 5 mins | [Conclusion](#conclusion) | Conclusion |

<a name="opening"></a>


## Opening (10 mins)
In this class we will review several case studies in order to demonstrate how messy real data can be.

**Check:** Can anyone explain what steps are involved in data cleaning and preparation?

> Answer:
Answers can include any of the following:
- filling missing data
- normalization
- scaling

**Check:** Can anyone explain what classification is and how it is performed? What methods have we learned so far?

> Answer:
- KNN
- Logistic Regression

<a name="case_1"></a>
## Default of Credit Card clients (25 mins)

For this lesson you will be working in pairs. Take 10 minutes to have a look at the paper and dataset.

[Credit Cards](http://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients)

[Dataset](default_of_credit_card_clients.xls)

[Paper](DefaultCreditCardClients_yeh_2009.pdf)

See if you can answer the following questions:
- What is the goal of the study? (hint: this is usually described in the abstract)
> Compare the predictive accuracy of probability of default among six data mining methods.

- What is the target variable (hint: look at the website and dataset)
> a binary variable – default payment (Yes = 1, No = 0)

- What models do they compare? (hint: although you have not yet seen all of them, try to grasp the differences)
- How do they judge the goodness of a model? Do they use accuracy? if not, what do they use?
> the study uses area ratio, instead of the error rate, to examine the classification accuracy among the six data mining techniques.

- What validation method do they use? Simple train/test split? Cross Validation?
> Train/test split

- **Bonus:** Which model performs best?
> Neural Networks

## Calling emergency medical services during drug overdose: an examination of individual, social and setting correlates 

For this lesson you will be working in pairs. Take 10 minutes to have a look at the paper (dataset no available).

[Paper](Calling_emergency.pdf)

- What is the goal of the study? (hint: this is usually described in the abstract)

- What is the target variable (hint: look at the website and dataset)

- What models do they compare? (hint: although you have not yet seen all of them, try to grasp the differences)

- How do they judge the goodness of a model? Do they use accuracy? if not, what do they use?

- What validation method do they use? Simple train/test split? Cross Validation?


## Chronic Kidney Disease (25 mins)

This case study is an example of a poorly written study. Many papers have been written about the Chronic Kidney Disease Dataset on UCI. The one we've chosen is particularly simple and not very good in quality. See if you can come up with observations on how to improve it.

Spend 10 minutes to review the paper and the dataset, then answer the questions below.


[Chronic Kidney Disease](http://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease)

[Dataset](chronic_kidney_disease_full.csv)

[Paper](chronic_kidney_disease.pdf)

Discuss:
- What is the goal of the study? (hint: this is usually described in the abstract)
> Compare KNN and SVM

- What is the target variable? (hint: look at the website and dataset)
> binary variable

- What models do they compare? (hint: although you have not yet seen all of them, try to grasp the differences)
> KNN and SVM

- How do they judge the goodness of a model? Do they use accuracy? if not, what do they use?
> Accuracy, Precision, Recall, F1-score

- What validation method do they use? Simple train/test split? Cross Validation?
> Train/test

- How could the paper be improved? Consider:
    - is the text well organized?
    - are the methods clear?
    - are the results clear?
    - are the graphs easy to understand?
    
## A fall detection system using k-nearest neighbor classifier

[Paper](falling.pdf)
Discuss:
- What is the goal of the study? (hint: this is usually described in the abstract)

- What is the target variable? 

- What models do they compare? (hint: although you have not yet seen all of them, try to grasp the differences)

- How do they judge the goodness of a model? Do they use accuracy? if not, what do they use?

- What validation method do they use? Simple train/test split? Cross Validation?


- How could the paper be improved? Consider:
    - is the text well organized?
    - are the methods clear?
    - are the results clear?
    - are the graphs easy to understand?
    

<a name="case_3"></a>
## Student Alcohol Consumption (25 mins)

[Student Alcohol Consumption](http://archive.ics.uci.edu/ml/datasets/STUDENT+ALCOHOL+CONSUMPTION)

[Dataset1](student-mat.csv)

[Dataset2](datasets/student-mat.csv)

[Paper](STUDENT ALCOHOL CONSUMPTION.pdf)

Discuss:
- What is the goal of the study? (hint: this is usually described in the abstract)
> Predicting the alcohol consumption of high school students

- What is the target variable? (hint: look at the website and dataset)
> categorical variable with 5 classes (1 very low - 5 very high)

- What models do they compare? (hint: although you have not yet seen all of them, try to grasp the differences)
> Decision trees and Random forests

- How do they judge the goodness of a model? Do they use accuracy? if not, what do they use?
> Accuracy

- What validation method do they use? Simple train/test split? Cross Validation?
> Cross Validation

- Do they have missing data? Which pre-processing techniques do they use?
> They check and there is no missing data.


## Machine-learning prediction of cancer survival: a retrospective study using electronic administrative records and a cancer registry
[Paper](BMJ_Open-2014-Gupta.pdf)
Discuss:
- What is the goal of the study? (hint: this is usually described in the abstract)

- What is the target variable? 

- What models do they compare? (hint: although you have not yet seen all of them, try to grasp the differences)

- How do they judge the goodness of a model? Do they use accuracy? if not, what do they use?

- What validation method do they use? Simple train/test split? Cross Validation?

- Do they have missing data? Which pre-processing techniques do they use?


<a name="conclusion"></a>

## Conclusion (5 mins)
We have reviewed few classification studies and explored the issues of data preparation, model building and model selection.

***

### ADDITIONAL RESOURCES

- [UCI Datasets](http://archive.ics.uci.edu/ml/datasets.html)
