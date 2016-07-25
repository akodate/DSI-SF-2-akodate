---
title: Intro to Git
duration: "1:5"
creator:
    name: Lucy Williams
    city: DC
---


# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Intro to Git
Week 1 | Lesson 1.2

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Use/explain git commands like init, add, commit, push, pull, and clone
- Distinguish between local and remote repositories
- Create, copy, and delete repositories locally, or on Github
- Clone remote repositories

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Have completed [Code Academy: Learn Git](https://www.codecademy.com/learn/learn-git)
- Install [Homebrew](http://brew.sh/)
- Install git (after installing Homebrew, type "brew install git")
- Setup a GitHub account
- Setup [SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)


### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 20 min  | [Introduction](#introduction)   | Git vs GitHub and version control  |
| 15 min  | [Codealong](#demo)  | Let's use Git  |
| 15 min  | [Codealong](#demo)  | Making and cloning repositories  |
| 10 min  | [Codealong](#demo)  | Create a pull request on GitHub  |
| 25 min  | [Independent Practice](#ind-practice)  
| 5 min  | [Conclusion](#conclusion)

---
<a name="introduction"></a>
## Git vs GitHub and version control - Intro (20 mins)


First things first - Git is not Github. This is a common mistake that people make.


#### What is Git?

[Git](https://git-scm.com/) is:

- A program you run from the command line
- A distributed version control system

Programmers use Git so that they can keep the history of all the changes to their code. This means that they can rollback changes (or switch to older versions) as far back int time as they started using Git on their project.

A codebase in Git is referred to as a **repository**, or **repo**, for short.

Git was created by [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds), the principal developer of Linux.

#### What is Github?

[Github](https://github.com/) is:

- A hosting service for Git repositories
- A web interface to explore Git repositories
- A social network of programmers
- We all have individual accounts and put our codebases on our Github account
- You can follow users and star your favorite projects
- Developers can access codebases on other public accounts
- GitHub uses Git

#### Can you use git without Github?

Think about this quote: “Git is software. GitHub is a company that happens to use Git software.”  So yes, you can certainly use Git without GitHub!

Your local repository consists of three "trees" maintained by Git.

- **Working Directory**: which holds the actual files.
- **Index**: which acts as a staging area
- **HEAD**: which points to the last commit you've made.

![workflow](https://cloud.githubusercontent.com/assets/40461/8221736/f1f7e972-1559-11e5-9dcb-66b44139ee6f.png)

#### So many commands?!

There are also a lot of commands you can use in git. You can take a look at a list of the available commands by running:

```bash
$ git help -a
```

Even though there are lots of commands, on the course we will really only need about 10.

<a name="demo"></a>
## Let's use Git - Codealong (15 mins)

First, create a directory on your Desktop:

```bash
$ cd ~/Desktop
$ mkdir hello-world
```

You can place this directory under Git revision control using the command:

```bash
$ git init
```

Git will reply:

```bash
Initialized empty Git repository in <location>
```

You've now initialized the working directory.

#### The .git folder

If we look at the contents of this empty folder using:

```bash
ls -A
```

We should see that there is now a hidden folder called `.git` this is where all of the information about your repository is stored. There is no need for you to make any changes to this folder. You can control all the git flow using `git` commands.

#### Add a file

Let's create a new file:

```bash
$ touch a.txt
```

If we run `git status` we should get:

```bash
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	a.txt

nothing added to commit but untracked files present (use "git add" to track)
```

This means that there is a new **untracked** file. Next, tell Git to take a snapshot of the contents of all files under the current directory (note the .)

```bash
$ git add .
```

This snapshot is now stored in a temporary staging area which Git calls the "index".

#### Commit

To permanently store the contents of the index in the repository, (commit these changes to the HEAD), you need to run:

```bash
$ git commit -m "Please remember this file at this time"
```

You should now get:

```bash
[master (root-commit) b4faebd] Please remember this file at this time
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt
```

#### Checking the log

If we want to view the commit history, we can run:

```bash
git log
```

You should see:

```bash
* b4faebd (HEAD, master) Please remember this file at this time
```

<a name="demo"></a>
#### Making and cloning repositories - Codealong (10 mins)

Let's do this together:

1. Go to your Github account
2. In the right hand side, hit the green + button for `New repository`
3. Name your repository `hello-world`
4. **Initialize this repository with a README** (So that we can `git pull`)
4. Click the big green Create Repository button

We now need to connect our local Git repo with our remote repository on GitHub. We have to add a "remote" repository, an address where we can send our local files to be stored.

```bash
git remote add origin git@github.com:github-name/hello-world.git
```

Alternatively, you can clone this repo from your Github link to have this automatically configured in a new directory.

```
git clone https://github.com/github-username/hello-world.git
```

#### Pushing to Github

In order to send files from our local machine to our remote repository on Github, we need to use the command `git push`. However, you also need to add the name of the remote, in this case we called it `origin` and the name of the branch, in this case `master`.

```bash
git push origin master
```

This should fail due to new files on the remote repo.

#### Pulling from Github

As we added the README.md in our repo, we need to first `pull` that file to our local repository to check that we haven't got a 'conflict'.

```bash
git pull origin master
```

```bash
git status
```

```bash
git add .
```

```bash
git commit -m "README.md"
```

Once we have done this, you should see the README file on your computer.

```bash
ls
```

Open it up and type some kind of modification/addition.


```bash
git add .
```

Now you can push your changes:

```bash
git push origin master
```

Refresh your GitHub webpage, and the files should be there.


#### Cloning your first repository

Now that everyone has their first repository on GitHub, let's clone our first repository!

Cloning allows you to get a local copy of a remote repository.

Navigate back to your Desktop and **delete your hello-world repository**:

```bash
cd ~/Desktop
rm -rf hello-world
```

Now ask the person sitting next to you for their github name and navigate to their repository on github:

```bash
https://www.github.com/<github-username>/hello-world
```

On the right hand side you will see:


#### Clone their repo!

To retrieve the contents of their repo, all you need to do is:

```bash
$ git clone git@github.com:alexpchin/hello-world.git
```

Git should reply:

```bash
Cloning into 'hello-world'...
remote: Counting objects: 3, done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
Checking connectivity... done.
```

You now have cloned your first repository!


<a name="demo"></a>
## Create a pull request on GitHub - Codealong (5 mins)

Before you can open a pull request, you must create a branch in your local repository, commit to it, and push the branch to a repository or fork on GitHub.

1. Visit the repository you pushed to
2. Click the "Compare, review, create a pull request" button in the repository ![pr](https://cloud.githubusercontent.com/assets/40461/8229344/d344aa8e-15ad-11e5-8578-08893bcee335.jpg)
3. You'll land right onto the compare page - you can click Edit at the top to pick a new branch to merge in, using the Head Branch dropdown.
4. Select the target branch your branch should be merged to, using the Base Branch dropdown
5. Review your proposed change
6. Click "Click to create a pull request" for this comparison
7. Enter a title and description for your pull request
8. Click 'Send pull request'

<a name="ind-practice"></a>
## Assess - Independent Practice (10 mins)
- Show a partner how to use to:  init, add, commit, push, pull, and clone

<a name="conclusion"></a>
## Conclusion (5 mins)
Feel comfortable with Git and GitHub? Since we'll be using it a lot of coursework, let's get
comfortable!

<a name="bonus"></a>
## Bonus Challenges

Once you've mastered the basics, further your understanding of Python by attempting ["Bonus Challenges #1"](code/starter-code/w1-1.2-bonus-starter.ipynb).  Challenge 1 deals with types, counting, and control flows.  

_These challenges are optional!_
