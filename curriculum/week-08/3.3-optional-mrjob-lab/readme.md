---
title: MRJob lab
type: lab
duration: "1:25"
creator:
    name: Francesco Mosconi
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) MRJob Lab

## Introduction

![](https://raw.githubusercontent.com/Yelp/mrjob/master/docs/logos/logo_medium.png)

In the past lab we've used a Virtual Machine to run Map Reduce jobs on native hadoop. As you may have understood, it's quite cumbersome and complicated.

Luckily we don't have to do that, because our friends at Yelp developed a great open source python library that wraps around hadoop streaming called [MRJob](https://github.com/Yelp/mrjob).

This is already installed in your VM, but you can also install it locally if you prefer, using:

`pip install mrjob`.

## Exercise

This lab will teach you to use [MRJob](https://github.com/Yelp/mrjob), a very powerful python library for map reduce.

> **Instructor note**: this lab needs to be run on the VM they have installed in the previous hour. The VM is packaged with all the necessary data and libraries, so they should just connect to it using ssh and then run everything from inside the machine. If they are not familiar with VIM they can configure Sublime Text to access the VM via SFTP and modify the scripts there.

> Except for Exercise 1, all the other exercises can also be run on the laptop in local mode, if some of them have trouble connecting or using the VM. All they need is `pip install mrjob`.

#### Requirements
- Exercise 1: running map reduce locally and on hadoop cluster
- Exercise 2: add a combiner
- Exercise 3: multi step jobs
- Exercise 4: Setup and teardown of tasks
- Exercise 5: Counters

**Bonus:**

- Putting it all together: find top 15 most frequent words for all books
- Use NLTK to recognize a book from the most frequent words


#### Starter code

[Starter Code](./assets/code/starter-code/starter-code.ipynb)

> [Solution Code](./assets/code/solution-code/solution-code.ipynb)


Additional Resources

- [MRJob Documentation](https://pythonhosted.org/mrjob/)
- [MRJob Examples](https://github.com/Yelp/mrjob/tree/master/mrjob/examples)

