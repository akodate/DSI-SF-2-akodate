---
title: 1.3 Intro to Stats Models & SKLearn
duration: "1:25"
creator:
    name: Marc Harper
    city: LA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Stats Models & SKLearn
Week 3 | Lesson 1.3

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Perform a linear regression in scikit-learn
- Perform a linear regression in statsmodels
- Do linear regression on boston housing dataset with statsmodels, just using a few of the columns, then try again with all of them - does the model get better?


### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Use matplotlib for making scatter plots
- Extract data from pandas DataFrames
- Fit a linear regression for one variable


### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck
- Prepare any specific materials
- Provide students with additional resources

> This lesson will be heavily code-driven since we're introducing how to use
two new modules.

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Opening](#opening)  | Topic description  |
| 10 min  | [Introduction](#introduction)   | Topic description  |
| 30 min  | [Demo](#demo)  | Topic description  |
| 25 min  | [Guided Practice](#guided-practice<a name="opening"></a>)  | Topic description  |
| 10 min  | [Independent Practice](#ind-practice)  | Topic description  |
| 5 min  | [Conclusion](#conclusion)  | Topic description  |

---

<a name="opening"></a>
## Opening (5 mins)
- Review prior labs/homework, upcoming projects, or exit tickets, when applicable
- Review lesson objectives
- Discuss real world relevance of these topics
- Relate topics to the [Data Science Workflow](https://drive.google.com/file/d/0Bx2SHQGVqWasOGY4dE95OFVvZjQ/view?usp=sharing) - i.e. are these concepts typically used to acquire, parse, clean, mine, refine, model, present, or deploy?

**Check:** Ask students to define, explain, or recall any relevant prework concepts.

<a name="introduction"></a>
## Introduction: Topic (10 mins)

> Instructor Note: Review the concepts behind linear regression from the eariler
lesson and touch on multilinear regression as described below.

In the earlier lesson we went through several fits for models that have one
independent variable. Usually we have more than one independent variable in
our datasets. The way we fit for multiple independent variables is often called
_multilinear regression_ and is conceptually the same. Instead of an equation like

```
y = a + b x
```

where `x` is the independent variable, we instead fit a matrix equation

```
y = X B
```

where `X` is a we have a matrix of independent variables and `B` is a vector
of coefficients like `b`. It's far too tedious to do this by hand so we rely on
one of many software packages to find the best fit coefficients.

Using multiple variables allows us to fit higher dimensional shapes:

```
y = b_0 + b_1 x_1 + b_2 x_2
```

and also more complex curves, like parabolas:

```
y = a  + b x + c x^2
```

What matters is that the relationship between the variables are linear, not the
shape itself. So for the parabola we really have that `x_1 = x` and `x_2 = x^2`.

> For equations and images use the [wikipedia page](https://en.wikipedia.org/wiki/Linear_regression):
section "Introduction to linear regression", which lays things out nicely.

**Check:** Translate `y^2 = a x^3 + b x` into a linear regression using three new variables `y_1`, `x_1`, and `x_2`.

> Solution: y_1 = a x_1 + b x_2` where `y_1 = y^2`, `x_1 = x^3`, and `x_2 = x`

**Check:** Can any curve be made into a linear regression?
> No. For example, `y = a sin(x)` is linear between `y` and `x_1 = sin(x)`, but
we can't rewrite `y = sin(a x)` as a linear relationship between `y` and `x`

<a name="demo"></a>
## Demo: Topic (20 mins)

> Use the included [Starter Code](code/starter-code/W3 L1.3.ipynb) This is a code-
heavy lesson since we are introducing two new python packages, so think of it
as a combination of lesson and lab.

> One issue to look out for -- when students try to fit all the data they may
forget to remove the target variable, ending up with a perfect model fit. This
could be very confusing, but it's also an opportunity to discuss how linear
regression works. In this case the model will fit completely on the target
and the other coefficients will be zero.

<a name="guided-practice"></a>
## Guided Practice: Statsmodels (25 mins)

[Demo / Starter Code](code/starter-code/W3 L1.3.ipynb)

> At the end of the Jupyter notebook, students are asked to recreate the models
built in scikit-learn with statsmodels. They can work in small groups if
desired.

> [Solution Code](code/solution-code/W3 L1.3-Solution.ipynb)

<a name="ind-practice"></a>
## Independent Practice: Topic (15 minutes)

Continue with the starter notebook and practice more model fits.

> The next lesson (1.4) is largely independent practice. Since this lesson is
very content heavy, spend more time on guided practice and the demo as needed.

> Students can explore other combinations of variables in the time remaining, looking for a good fit with a small number of variables. Explain that less complex models are better in general if asked why.

> [Demo / Starter Code](code/starter-code/W3 L1.3.ipynb)

> [Solution Code](code/solution-code/W3 L1.3-Solution.ipynb)


<a name="conclusion"></a>
## Conclusion (# mins)
- Review the two modules introduced and explain that we'll use both for many more
models as the course progresses

***

### UPCOMING ASSIGNMENTS
|   |   |  |
|---|---|---|
| **HOMEWORK** | [Example Assignment](#)  | Session Due |
| **PROJECTS**  | [Project Title](#)  | Session Due |

