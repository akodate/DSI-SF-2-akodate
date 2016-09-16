---
title: AWS Amazon Web Services
duration: "1:25"
creator:
    name: Francesco Mosconi
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) AWS: Amazon Web Services
Week 10| Lesson 2.1

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- explain what services AWS offers and which ones are relevant to data science
- start and terminate an EC2 instance in the cloud
- store and download data from an S3 bucket

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- set up an account on AWS, using 2-Factor authentication for security
- connect to a remote computer via ssh
- students should have a credit card to sign up for AWS or have an AWS account

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck
- Prepare any specific materials
- Provide students with additional resources
- This week requires some additional preparation. You'll need to check with your local team about buying, accessing, or reimbursing AWS credits for your students to use S3, EC2, and EMR.
- make sure students keep receipts in case local teams want to either reimburse or give AWS credits

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min | [Opening](#opening) | Opening |
| 10 min | [Introduction](#introduction) | Intro to AWS |
| 5 min | [Demo](#demo) | Demo: Elastic Compute Cloud [EC2] |
| 15 min | [Ind-practice](#ind-practice) | Elastic Compute Cloud [EC2] |
| 5 min | [Demo](#demo) | Simple Storage Service [S3] |
| 5 min | [Ind-practice](#ind-practice) | Simple Storage Service [S3] |
| 5 min | [Demo](#demo) | AWS Command Line [AWSCLI] |
| 15 min | [Ind-practice](#ind-practice) | AWS Command Line [AWSCLI] |
| 15 min | [Guided](#guided_practice) | EC2 from the command line |
| 5 min | [Conclusion](#conclusion) | Conclusion |


<a name="opening"></a>
## Opening (5 min)

Today we are going to discover Amazon Web Services. In particular we will focus on those services that are mostly used in Data Science. AWS are cloud computing services, essentially virtual machines somewhere in a datacenter that you can access and pay only for the time you need them.


**Check:** What is a server?
> Answer: A server is a computer or software that performs administration or coordination functions within a network.

**Check:** What did the world look like before AWS and Google cloud?
> Answer: computation was expensive to set up, to access and to maintain => only large companies, governments and institutions had access to it. Now anyone can rent it for pennies.

<a name="introduction"></a>
## Intro to AWS (10 min)
_Amazon Web Services (AWS)_, is a subsidiary of Amazon.com, which offers a suite of cloud computing services that make up an on-demand computing platform. These services operate from 12 geographical regions across the world. The most central and best-known of these services arguably include Amazon Elastic Compute Cloud, also known as "EC2", and Amazon Simple Storage Service, also known as "S3". AWS now has more than 70 services that span a wide range including compute, storage, networking, database, analytics, application services, deployment, management, mobile, developer tools and tools for the Internet of things. Amazon markets AWS as a service to provide large computing capacity quicker and cheaper than a client company building an actual physical server farm. _(from wikipedia)_

Today we will explore two services that are relevant to a lot of big-data scenarios.

1. EC2 (Elastic Compute Cloud)
- S3 (Simple Storage Service)

By the end of today you will be able to start and stop a computer in the cloud and to store data in the cloud. How cool is that!?

> Instructor Note: in the absence of amazon credits have the students sign up with a new account so they can get free-tier usage for 1 year.

**Check:** What could be some advantages of using a server in the cloud instead of managing our own data center?
>
- Cost reduction: don't pay infrastructure costs when you don't need it
- Reliability: Servers are maintained and guaranteed by a company whose only job is to make sure they are available for you
- Scalability: Can add more computing power when necessary


<a name="demo"></a>
## Demo: Elastic Compute Cloud [EC2] (5 min)

> Instructor note: All the following guided practices could be done as pair-programming exercises or as guided practices. You can decided to pair up students if you feel the class may benefit from it.

The first service we will discover is _Elastic Compute Cloud_ or _EC2_. This service forms a central part of Amazon.com's cloud-computing platform by allowing users to rent virtual computers on which to run their own computer applications. Let's learn some terms first:

- **Instance**: virtual machine hosted in Amazon Cloud running the software we want
- **Amazon Machine Image (AMI)**: a snapshot of a configured machine that we can use as starting point to boot an instance. We can also save a running instance to a new AMI so that in the future we can boot a new machine with identical configuration.
- **SSH Key**: [pair of keys](https://en.wikipedia.org/wiki/Public-key_cryptography) necessary to connect to an instance remotely. The private key will be downloaded to our laptop, the matching public key will be automatically configured on the instance.


The main conceptual shift from using a laptop to running an instance in the cloud is that we should think of computing power as ephemeral. We can request computing power when we need it, do a calculation and dismiss that power as we are done. Input and output will not be stored on the machine, rather stored somewhere else in the cloud (hint: S3). In this sense, computing power is a commodity that we purchase and use in the amount and time that we need.

Let's see how it works.

1) Create a new account on AWS [here](https://aws.amazon.com/)

It will ask you for contact information and credit card. Do not worry, most of the thing we will do are free for first time users and when we will use paying services it won't likely cost more than 10$.

Here are some screenshots of the process:

![](./assets/images/aws1.png)

![](./assets/images/aws2.png)

![](./assets/images/aws3.png)

Once you're done you should get to this page:

![](./assets/images/aws4.png)

Let's sign in to the console, you should get to this page:

![](./assets/images/services1.png)


<a name="ind-practice"></a>
## Elastic Compute Cloud [EC2] (15 min)

Let's go ahead and follow the [tutorial for EC2](https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/).

### Steps to complete:

#### Step1: Launch an Amazon EC2 Instance

![](./assets/images/launch-instance.png)


#### Step2: Configure your Instance

Follow the suggested steps until you see your image booting up:

![](./assets/images/launched1.png)

Notice that we can have a lot of information about the instance, in particular:

- it's DNS name and IP address
**Check:** What is an IP address?
> Answer: It's the address at which we can reach our machine
- They type of instance
- The key necessary to connect


#### Step 3: Connect to your Instance

Go ahead and follow the instructions on how to connect to the instance. In particular:

1. (optional) download a bash shell
- copy the SSH key you downloaded to the appropriate location
- use the SSH key to connect as explained in the tutorial

![](./assets/images/connected.png)

Congratulations!! You've just connected to an instance in the cloud!! How awesome is that!!

Try launching python from the shell and do something with it.

![](./assets/images/python.png)

#### Step 4: Terminate Your Instance

Once you're done with your calculation and you no longer need the instance, you can go ahead and terminate it. NB: this will kill the instance and it will no longer be available to you. You should make sure you have saved all the data and the code you needed somewhere else.

![](./assets/images/terminate.png)

![](./assets/images/terminated.png)

Unless you are using your machine to serve a live application (like a web app or an api) it's very important that you terminate your instance if you don't use it so that you don't incur in additional unnecessary costs.

> Instructor note: make sure everyone has terminated their instance, destroyed any EBS allocated storage and emptied their S3 space, so that they don't get charged for anything unknowingly.

### Additional remarks

We've seen the simplest way to launch and terminate an instance in the cloud.

There's a lot more to it, that you'll discover in time, here are some pointers you may find useful:

- [Pricing](https://aws.amazon.com/ec2/pricing/): EC2 pricing depends on the type of instance and on the chosen region. Make sure you understand the cost of the instance you request in order to avoid surprise bills. If you're in doubt you can use the convenient [Cost Calculator](http://calculator.s3.amazonaws.com/index.html) to get an exact forecast of your costs.

![](./assets/images/costcalculator.png)

- [Spot instances](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html): spot instances are even more ephemeral than normal instances. They only live till their cost is lower than the price you agreed to pay. They are a great way to save money when using more powerful machines.
- [AMIs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) AMIs are shapshot of our machine. They are great if we installed a lot of software on our machine and want to save that particular configuration.

![](./assets/images/createimage.png)

**Check:** can you give an example of when AMIs could be useful?
> Answer: e.g. if we have downloaded and installed Anaconda Python

- [Security Groups](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html): security groups are ways to open ports to the services running on our machine.
**Check:** can you give an example of a practical case?
> Answer: e.g. if we are running IPython notebook on the instance and want to reach it from a browser.

- [Elastic IPs](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html): we can rent a fixed IP address and associate it to our instance. This way we can configure tools to always connect to the same address, independently of which machine is behind it.
**Check:** can you give a practical use case?
> Answer: e.g. if we want to automate ssh connection with a configuration file.

<a name="demo"></a>
## Simple Storage Service [S3] (5 min)

We have learned how to start and stop an instance in the cloud. That's great, because it gives us "computing power as a service". Now let's learn how we can store data in the cloud too.

Amazon S3 (Simple Storage Service) is an online file storage. It provides storage through web services interfaces (REST, SOAP, and BitTorrent) using an _object storage architecture_. According to Amazon, S3's design aims to provide scalability, high availability, and low latency at commodity costs.

Objects are organized into buckets (each owned by an Amazon Web Services account), and identified within each bucket by a unique, user-assigned key. Buckets and objects can be created, listed, and retrieved using either a REST-style HTTP interface or a SOAP interface. Additionally, objects can be downloaded using the HTTP GET interface and the BitTorrent protocol.


<a name="ind-practice"></a>
## Simple Storage Service [S3] (5 min)

In pairs: go ahead and follow the [tutorial for S3](https://aws.amazon.com/getting-started/tutorials/backup-files-to-amazon-s3/).

The steps should be super simple to follow. Any questions?

**Check:** what's a practical case you can envision using S3 for?
> Answer: storing input dataset, storing result tables. It's like Dropbox


<a name="demo"></a>
## AWS Command Line [AWSCLI] (5 min)

Wow, great! We have learned to request and access computing power and storage as a service through AWS. Wouldn't it be nice to be able to do this in a quick way from the command line? Yeah! Let's introduce AWSCLI!

[AWSCLI](https://github.com/aws/aws-cli) is a unified command line interface to Amazon Web Services. It allows us to control most of AWS services from the same command line interface.

**Check:** Why is that useful? Why is that powerful? Can you give some examples?
> e.g. to be able to programatically turn instances on and off or to create complex architectures or to provision clusters in response to a demand


<a name="ind-practice"></a>
## AWS Command Line [AWSCLI] (15 min)

Let's go ahead and follow the [tutorial for AWSCLI](https://aws.amazon.com/getting-started/tutorials/backup-to-s3-cli/)


### Steps to complete

#### Step 1: Create an AWS IAM User

In order to use the command line we will have to configure a set of access credentials on our laptop. It's very important to create a separate identity with limited permissions instead of using our root account credentials.

**Check:** why is this so important?
> Answer: so that we can limit the damage a user could do if he/she were to obtain our credentials

![](./assets/images/identitymanager.png)

**Note:** It's also probably a very good idea to set up 2-Factor Authentication!

**Note:** When attaching a Policy you can be more restrictive and only give the user permission to use the services you intend him/her to use.


#### Step 2: Install and Configure the AWS CLI


http://docs.aws.amazon.com/cli/latest/userguide/installing.html

Note that one of the method is to simply use `pip` to install the AWSCLI.

**Note:** If you already have AWSCLI configured and you would like to have multiple roles, you can do that as explained [here](http://docs.aws.amazon.com/cli/latest/userguide/cli-roles.html).

#### Step 3: Using the AWS CLI with Amazon S3

Now you can go ahead and copy files back and forth from your command line, without ever having to click on the web interface. How cool is that?


Here's a [Cheat Sheet](https://github.com/toddm92/aws/wiki/AWS-CLI-Cheat-Sheet) for the AWSCLI.

<a name="guided_practice"></a>
## EC2 from the command line (15 min)

Empowered with a well configured AWSCLI, we can now start and stop EC2 instances from the command line! Let's use it to spin up a spot instance.

#### 1. Check prices

Let's check the price for an `m3.medium` spot instance:

```bash
aws ec2 describe-spot-price-history \
    --start-time $(date -u +"%Y%m%dT%H0000") \
    --product "Linux/UNIX" \
    --instance-type "m3.medium" \
    --region us-west-2 \
    --output table
```

**Note:** you may have to set the region to the same region you used when opening your account.

```bash
-------------------------------------------------------------------------------------------------------
|                                      DescribeSpotPriceHistory                                       |
+-----------------------------------------------------------------------------------------------------+
||                                         SpotPriceHistory                                          ||
|+------------------+---------------+---------------------+------------+-----------------------------+|
|| AvailabilityZone | InstanceType  | ProductDescription  | SpotPrice  |          Timestamp          ||
|+------------------+---------------+---------------------+------------+-----------------------------+|
||  us-west-2b      |  m3.medium    |  Linux/UNIX         |  0.009700  |  2016-05-30T00:48:11.000Z   ||
||  us-west-2b      |  m3.medium    |  Linux/UNIX         |  0.009800  |  2016-05-30T00:45:56.000Z   ||
||  us-west-2a      |  m3.medium    |  Linux/UNIX         |  0.011100  |  2016-05-30T00:40:35.000Z   ||
||  us-west-2a      |  m3.medium    |  Linux/UNIX         |  0.011000  |  2016-05-30T00:35:39.000Z   ||
||  us-west-2b      |  m3.medium    |  Linux/UNIX         |  0.009900  |  2016-05-30T00:35:39.000Z   ||
||  us-west-2b      |  m3.medium    |  Linux/UNIX         |  0.010000  |  2016-05-30T00:30:46.000Z   ||
||  us-west-2b      |  m3.medium    |  Linux/UNIX         |  0.009800  |  2016-05-30T00:25:24.000Z   ||
||  us-west-2a      |  m3.medium    |  Linux/UNIX         |  0.011100  |  2016-05-30T00:22:38.000Z   ||
||  us-west-2a      |  m3.medium    |  Linux/UNIX         |  0.011200  |  2016-05-30T00:17:14.000Z   ||
||  us-west-2b      |  m3.medium    |  Linux/UNIX         |  0.009900  |  2016-05-30T00:14:46.000Z   ||
||  us-west-2a      |  m3.medium    |  Linux/UNIX         |  0.011100  |  2016-05-30T00:14:46.000Z   ||
||  us-west-2a      |  m3.medium    |  Linux/UNIX         |  0.010900  |  2016-05-30T00:11:47.000Z   ||
||  us-west-2a      |  m3.medium    |  Linux/UNIX         |  0.011000  |  2016-05-30T00:09:35.000Z   ||
||  us-west-2a      |  m3.medium    |  Linux/UNIX         |  0.010900  |  2016-05-30T00:06:52.000Z   ||
||  us-west-2a      |  m3.medium    |  Linux/UNIX         |  0.011000  |  2016-05-30T00:02:05.000Z   ||
||  us-west-2b      |  m3.medium    |  Linux/UNIX         |  0.009800  |  2016-05-29T23:49:30.000Z   ||
||  us-west-2a      |  m3.medium    |  Linux/UNIX         |  0.011100  |  2016-05-29T23:49:30.000Z   ||
||  us-west-2c      |  m3.medium    |  Linux/UNIX         |  0.013500  |  2016-05-29T01:14:22.000Z   ||
|+------------------+---------------+---------------------+------------+-----------------------------+|
```

#### 2. Get the Security group id

In the previous activity we launched an instance and created a security group that allows SSH access. Let's use the same security group.

```bash
aws ec2 describe-security-groups --region us-west-2
```
(or the region you chose)

This will return a json string. You want to copy the id of the security group that has port 22 open.

#### 3. Get the AMI id

Get the AMI id of the Ubuntu Linux 14.04 Image. You can find by checking the name in the [launch instance window](https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#LaunchInstanceWizard). At the time of writing it's: `ami-9abea4fb`.

You can check it by typing:

```bash
aws ec2 describe-images --image-ids ami-9abea4fb --region us-west-2
```


#### 4. Launch spot instance

You're now ready to sumbit the spot instance request:

```bash
aws ec2 request-spot-instances \
    --region us-west-2 \
    --spot-price 0.02 \
    --launch-specification "{
        \"KeyName\": \"MyFirstKey\",
        \"ImageId\": \"<MOST RECENT UBUNTU AMI ID>\",
        \"InstanceType\": \"m3.medium\" ,
        \"SecurityGroupIds\": [\"<YOUR SECURITY GROUP ID>\"]
    }"
```

If working this should return a json description of the instance request.

You can check that the instance request has been opened:

![](./assets/images/instancerequest.png)

or by command line:

```bash
aws ec2 describe-spot-instance-requests --region us-west-2
```

When the request has been accepted, an instance is spawned:

![](./assets/images/spotinstance.png)

Let's retrieve the DNS name:
```bash
aws ec2 describe-instances --region us-west-2 --output json | grep PublicDnsName | head -n 1
```

#### 4. Connect to the spot instance

```bash
ssh -i ~/.ssh/MyFirstKey.pem ubuntu@<YOUR INSTANCE DNS>
```

#### 5. Terminate the spot instance

Let's retrieve the instance id and kill it:

```bash
aws ec2 describe-instances --region us-west-2 --output json | grep InstanceId

aws ec2 terminate-instances --instance-ids i-0aa55cd3363b0f187
```

![](./assets/images/terminatedspot.png)

Et Voilà!


<a name="conclusion"></a>
## Conclusion (5 min)

In this lesson we have learned about 2 fundamental Amazon web services: Elastic Cloud Compute and Simple Storage Service. These 2 services are so common because they provide on demand computation and storage at a very affordable cost.

We have learned how to use them both from the web interface and from the command line.

**Check:** can you think of a situation where this could be useful?
> Have them reflect on availability of data from multiple terminals, and availability of much greater computing power and storage capacity than a laptop.


### ADDITIONAL RESOURCES

- [EC2](https://aws.amazon.com/ec2/?nc2=h_m1)
- [S3](https://aws.amazon.com/s3/?nc2=h_m1)
- [Tutorials](https://aws.amazon.com/getting-started/tutorials/)
- [AWS CLI Tutorial](http://www.joyofdata.de/blog/guide-to-aws-ec2-on-cli/)

