---
title: Feature Extraction from Text
duration: "1:25"
creator:
    name: Francesco Mosconi
    city: SF
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Feature Extraction from Text
Week 6| Lesson 4.1

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Extract features from free form text using Scikit Learn
- Identify Parts of Speech using NLTK
- Remove stop words
- Describe how TFIDF works

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Familiarize yourself with [nltk.download()](http://www.nltk.org/data.html) in case you need to download additional corpuses
- Describe what a transformer is in Scikit Learn and use it
- Recognize basic principles of English language syntax

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Read in / Review any dataset(s) & starter/solution code
- Generate a brief slide deck
- Prepare any specific materials
- Provide students with additional resources

### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 10 min | [Opening](#opening) | Opening |
| 10 min | [Introduction](#introduction) | Feature Extraction from Text |
| 10 min | [Demo](#demo) | Demo: Scikit Learn Count Vectorizer |
| 10 min | [Guided](#guided_practice) | Scikit Learn Hashing Vectorizer |
| 15 mins | [Introduction](#introduction_2) | Intro: Natural Language Processing |
| 15 mins | [Demo](#demo_2) | Demo: Advanced NLP with NLTK |
| 10 mins | [Guided-practice](#guided-practice_2) | Term frequency - Inverse document Frequency |
| 5 mins | [Conclusion](#conclusion) | Conclusion |


<a name="opening"></a>
## Opening (10 min)

All the models we have learned so far accept a 2D table of real numbers as input (we called it `X`) and output a vector of classes or numbers (we called it `y`). Very often though, our starting point data is not given in the form of a table of numbers, rather it's unstructured, for example in the case of text documents. In this case we need a way to go from unstructure data to a table of numbers, so that we can then apply the usual methods. This is called _feature extraction_ and this lesson is dedicated to it.

**Check:** Take a couple of minutes to think of real-world applications of Natural Language Processing and share them with the class.
> Examples:
- speech recognition
- machine translation
- question answering
- topic modeling
- sentiment analysis

<a name="introduction"></a>
## Feature Extraction from Text (10 min)

### A Simple Example
Suppose we are building a spam/ham classifier. Input are emails, output is a binary classification.

Here's an example of an input email:


```python
spam = """
Hello,\nI saw your contact information on LinkedIn. I have carefully read through your profile and you seem to have an outstanding personality. This is one major reason why I am in contact with you. My name is Mr. Valery Grayfer Chairman of the Board of Directors of PJSC "LUKOIL". I am 86 years old and I was diagnosed with cancer 2 years ago. I will be going in for an operation later this week. I decided to WILL/Donate the sum of 8,750,000.00 Euros(Eight Million Seven Hundred And Fifty Thousand Euros Only etc. etc.
"""

ham = """
Hello,\nI am writing in regards to your application to the position of Data Scientist at Hooli X. We are pleased to inform you that you passed the first round of interviews and we would like to invite you for an on-site interview with our Senior Data Scientist Mr. John Smith. You will find attached to this message further information on date, time and location of the interview. Please let me know if I can be of any further assistance. Best Regards.
"""
print spam
print
print ham
```

    
    Hello,
    I saw your contact information on LinkedIn. I have carefully read through your profile and you seem to have an outstanding personality. This is one major reason why I am in contact with you. My name is Mr. Valery Grayfer Chairman of the Board of Directors of PJSC "LUKOIL". I am 86 years old and I was diagnosed with cancer 2 years ago. I will be going in for an operation later this week. I decided to WILL/Donate the sum of 8,750,000.00 Euros(Eight Million Seven Hundred And Fifty Thousand Euros Only etc. etc.
    
    
    
    Hello,
    I am writing in regards to your application to the position of Data Scientist at Hooli X. We are pleased to inform you that you passed the first round of interviews and we would like to invite you for an on-site interview with our Senior Data Scientist Mr. John Smith. You will find attached to this message further information on date, time and location of the interview. Please let me know if I can be of any further assistance. Best Regards.
    


**Check:** Can you think of a simple heuristic rule to catch email like this?
> Answer: We could check for the presence of the words Donate, WILL, sum, cancer, LinkedIn and similar.

By defining a simple rule that parses the text we have performed one of the simplest feature extraction from text: _binary word counting_.

### Bag of words / Word Counting

The bag-of-words model is a simplifying representation used in natural language processing. In this model, a text (such as a sentence or a document) is represented as the bag (multiset) of its words, disregarding grammar and even word order but keeping multiplicity.


```python
from collections import Counter
print Counter(spam.lower().split())
print
print Counter(ham.lower().split())
```

    Counter({'i': 7, 'of': 4, 'and': 3, 'is': 2, 'etc.': 2, 'am': 2, 'an': 2, 'have': 2, 'in': 2, 'your': 2, 'to': 2, 'years': 2, 'with': 2, 'this': 2, 'contact': 2, 'the': 2, 'major': 1, 'old': 1, 'cancer': 1, 'outstanding': 1, 'seven': 1, 'decided': 1, 'through': 1, 'carefully': 1, 'euros(eight': 1, 'seem': 1, 'saw': 1, 'information': 1, 'for': 1, 'euros': 1, 'fifty': 1, '86': 1, 'sum': 1, '"lukoil".': 1, 'only': 1, 'pjsc': 1, 'mr.': 1, '2': 1, 'linkedin.': 1, 'will/donate': 1, 'you': 1, 'hundred': 1, 'was': 1, 'personality.': 1, 'chairman': 1, 'profile': 1, 'you.': 1, 'hello,': 1, 'ago.': 1, 'read': 1, 'going': 1, 'thousand': 1, 'million': 1, 'grayfer': 1, 'reason': 1, 'be': 1, 'one': 1, 'why': 1, 'on': 1, 'name': 1, 'week.': 1, '8,750,000.00': 1, 'later': 1, 'board': 1, 'operation': 1, 'will': 1, 'directors': 1, 'diagnosed': 1, 'valery': 1, 'my': 1})
    
    Counter({'to': 5, 'you': 4, 'of': 4, 'the': 3, 'and': 2, 'we': 2, 'scientist': 2, 'data': 2, 'i': 2, 'further': 2, 'this': 1, 'regards.': 1, 'find': 1, 'information': 1, 'am': 1, 'an': 1, 'at': 1, 'in': 1, 'our': 1, 'message': 1, 'pleased': 1, 'best': 1, 'if': 1, 'will': 1, 'would': 1, 'with': 1, 'interviews': 1, 'please': 1, 'writing': 1, 'application': 1, 'mr.': 1, 'location': 1, 'passed': 1, 'interview': 1, 'for': 1, 'john': 1, 'date,': 1, 'be': 1, 'hello,': 1, 'x.': 1, 'invite': 1, 'that': 1, 'any': 1, 'interview.': 1, 'regards': 1, 'let': 1, 'know': 1, 'hooli': 1, 'on-site': 1, 'me': 1, 'on': 1, 'your': 1, 'like': 1, 'assistance.': 1, 'attached': 1, 'senior': 1, 'inform': 1, 'smith.': 1, 'can': 1, 'time': 1, 'position': 1, 'first': 1, 'round': 1, 'are': 1})


In the above example we counted the number of times each word appeared in the text. Note that since we included all the words in the text, we created a dictionary that contains many words with only one appearance.

<a name="demo"></a>
## Demo: Scikit Learn Count Vectorizer (10 min)

Scikit-learn offers a `CountVectorizer` with many configurable options:


```python
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
```


```python
cvec = CountVectorizer()
cvec.fit([spam])
```




    CountVectorizer(analyzer=u'word', binary=False, decode_error=u'strict',
            dtype=<type 'numpy.int64'>, encoding=u'utf-8', input=u'content',
            lowercase=True, max_df=1.0, max_features=None, min_df=1,
            ngram_range=(1, 1), preprocessor=None, stop_words=None,
            strip_accents=None, token_pattern=u'(?u)\\b\\w\\w+\\b',
            tokenizer=None, vocabulary=None)




```python
df  = pd.DataFrame(cvec.transform([spam]).todense(),
             columns=cvec.get_feature_names())

df.transpose().sort_values(0, ascending=False).head(10).transpose()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>of</th>
      <th>and</th>
      <th>your</th>
      <th>contact</th>
      <th>is</th>
      <th>in</th>
      <th>have</th>
      <th>euros</th>
      <th>the</th>
      <th>this</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



Note that there are several parameters to tweak.

**Check:** Spend a couple of minutes scanning the documentation to figure out what those parameters do. Take 5 minutes, then share a few takeaways from the documentation in groups. What features stand out to you?

[Count Vectorizer Documentation](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)

> Instructor: they should at least notice that you can set:
    - max_df
    - min_df
    - max_features
> You can prompt them by asking if they noticed any parameter that would reduce or control the number of features.

<a name="guided_practice"></a>
## Scikit-Learn Hashing Vectorizer (10 min)

### Hashing Vectorizer

As you have seen we can set the `CountVectorizer` dictionary to have a fixed size, only keeping words of certain frequencies, however, we still have to compute a dictionary and hold the dictionary in memory. This could be a problem when we have a large corpus or in streaming applications where we don't know which words we will encounter in the future.

These problems can be solved using the `HashingVectorizer`, which converts a collection of text documents to a matrix of occurrences, calculated with the [hashing trick](https://en.wikipedia.org/wiki/Feature_hashing). Each word is mapped to a feature with the use of a [hash function](https://en.wikipedia.org/wiki/Hash_function) that converts it to a hash. If we encounter that word again in the text, it will be converted to the same hash, allowing us to count word occurence without retaining a dictionary in memory. This is very convenient!

The main drawback of the this trick is that it's not possible to compute the inverse transform, and thus we lose information on what words the important features correspond to. The hash function employed is the signed 32-bit version of Murmurhash3.

**Check:** What characteristics should feature extraction from text satisfy?
> Answer: It should return a vector of fixed size, regardless of the length of a text.

**Check:** Using the code above as example, let's repeat the vectorization using a _HashingVectorizer_.

> Answer:
>
    from sklearn.feature_extraction.text import HashingVectorizer
    hvec = HashingVectorizer()
    hvec.fit([spam])
    
> Instructor note: have them say what code they need to write in order to import and initialize the HashingVectorizer


```python
# your code here


```


```python
df  = pd.DataFrame(hvec.transform([spam]).todense())
```


```python
df.transpose().sort_values(0, ascending=False).head(10).transpose()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>479532</th>
      <th>144749</th>
      <th>174171</th>
      <th>832412</th>
      <th>828689</th>
      <th>994433</th>
      <th>1005907</th>
      <th>170062</th>
      <th>675997</th>
      <th>959146</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.338062</td>
      <td>0.169031</td>
      <td>0.169031</td>
      <td>0.169031</td>
      <td>0.169031</td>
      <td>0.169031</td>
      <td>0.169031</td>
      <td>0.169031</td>
      <td>0.169031</td>
      <td>0.084515</td>
    </tr>
  </tbody>
</table>
</div>



**Check:** What new parameters does this vectorizer offer?
> Answer:
- n_features

<a name="introduction_2"></a>
## Intro: Natural Language Processing (15 mins)

Bag of word approaches like the one outlined before completely ignore the structure of a sentence, they merely assess presence of specific words or word combinations.

Besides, the same word can have multiple meanings in different contexts. Consider for example the following two sentences:

- There's wood floating in the **sea**
- Mike's in a **sea** of trouble with the move

In the first case the word "sea" indicates a large body of water, while in the second case it indicates "a lot of".

How do we teach a computer to disambiguate? Here are some additional techniques that may come to help.

### Segmentation

_Segmentation_ is a technique to identify sentences within a body of text. Language is not a continuous uninterrupted stream of words: punctuation serves as a guide to group together words that convey meaning when contiguous.


```python
easy_text = "I went to the zoo today. What do you think of that? I bet you hate it! Or maybe you don't"

easy_split_text = ["I went to the zoo today.",
                   "What do you think of that?",
                   "I bet you hate it!",
                   "Or maybe you don't"]
```


```python
def simple_sentencer(text):
    '''take a string called `text` and return
    a list of strings, each containing a sentence'''
    
    sentences = []
    substring = ''
    for c in text:
        if c in ('.', '!', '?'):
            sentences.append(substring + c)
            substring = ''
        else:
            substring += c
    return sentences

simple_sentencer(easy_text)
```




    ['I went to the zoo today.',
     ' What do you think of that?',
     ' I bet you hate it!']



The sentencer above doesn't work perfectly. In the lab you will learn how to improve it. On the other hand, the NLTK library offers an easy to use sentencer.


```python
from nltk.tokenize import PunktSentenceTokenizer
sent_detector = PunktSentenceTokenizer()
sent_detector.sentences_from_text(easy_text)
```




    ['I went to the zoo today.',
     'What do you think of that?',
     'I bet you hate it!',
     "Or maybe you don't"]



**Check:** Does NLTK offer other Tokenizers? Use nltk.download() to explore the available packages.

<a name="demo_2"></a>
## Demo: Advanced NLP with NLTK (15 mins)

_Normalization_ is when slightly different version of a word exist. For example: LinkedIn sees 6000+ variations of the title "Software Engineer" and 8000+ variations of the word "IBM".

**Check:** What are other common cases of text that could need normalization?
> Answer:
- Person titles (Mr. MR. DR etc.)
- Dates (10/03, March 10 etc.)
- Numbers
- Plurals
- Verb conjugations
- Slang
- SMS abbreviations

It would be wrong to consider the words "MR." and "mr" to be different features, thus we need a technique to normalize words to a common root. This technique is called _Stemming_.

- Science, Scientist => Scien
- Swimming, Swimmer, Swim => Swim

As we did above we could define a Stemmer based on rules:


```python
def stem(tokens):
    '''rules-based stemming of a bunch of tokens'''
    
    new_bag = []
    for token in tokens:
        # define rules here
        if token.endswith('s'):
            new_bag.append(token[:-1])
        elif token.endswith('er'):
            new_bag.append(token[:-2])
        elif token.endswith('tion'):
            new_bag.append(token[:-4])
        elif token.endswith('tist'):
            new_bag.append(token[:-4])
        elif token.endswith('ce'):
            new_bag.append(token[:-2])
        elif token.endswith('ing'):
            new_bag.append(token[:-2])
        else:
            new_bag.append(token)

    return new_bag

stem(['Science', 'Scientist'])
```




    ['Scien', 'Scien']



Luckily for us, NLTK contains several robust stemmers.


```python
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print stemmer.stem('Swimmed')
print stemmer.stem('Swimming')
```

    Swim
    Swim


**Check:** There are other stemmers available in NLTK. Let's split the class in 2 teams and have a look at [this article](https://www.elastic.co/guide/en/elasticsearch/guide/current/choosing-a-stemmer.html). One team will focus on the pros of the Porter Stemmer, the other team will focus on the pros of the Snowball Stemmer. You have 5 minutes to read, then each side will have 2 minutes to convince the other side about their stemmer.

> Instructor notes:
> First Stemmer is Lovins in 1968
> Porter Stemmer written in 1980 and became de-facto in 2000, many versions, some buggy
> Snowball Stemmer is a Framework to build stemmers, written by Porter too
> See [here](http://stackoverflow.com/questions/10554052/what-are-the-major-differences-and-benefits-of-porter-and-lancaster-stemming-alg) for more info on stemmers.

### Stop Words

Some words are very common and provide no information on the text content.
**Check:** Can you give some examples?
> Answer: the, a, of etc.

We should remove these _stop words_. Note that each language has different stop words.


```python
from nltk.corpus import stopwords
stop = stopwords.words('english')
sentence = "this is a foo bar sentence"
print [i for i in sentence.split() if i not in stop]
```

    ['foo', 'bar', 'sentence']


### Parts of Speech

Each word has a specific role in a sentence (Verb, Noun etc.) Parts-of-speech tagging (POS) is a feature extraction technique that attaches a tag to each word in the sentence, in order to provide a more precise context for further analysis. This is often a resource intensive process, but it can sometimes improve the accuracy or our models.




```python
from nltk.tag import pos_tag
from nltk.tokenize import WordPunctTokenizer
tok = WordPunctTokenizer()
pos_tag(tok.tokenize("today is a great day to learn nlp"))
```




    [('today', 'NN'),
     ('is', 'VBZ'),
     ('a', 'DT'),
     ('great', 'JJ'),
     ('day', 'NN'),
     ('to', 'TO'),
     ('learn', 'VB'),
     ('nlp', 'NN')]



<a name="guided-practice_2"></a>
## Term frequency - Inverse document Frequency (10 mins)

More interesting than stop-words is the tf-idf score. This tells us which words are most discriminating between documents. Words that occur a lot in one document but doesn't occur in many documents will tell you something special about the document.

Let's see how it is calculated.

Term frequency tf is the frequency of a certain term in a document:
$$
\mathrm{tf}(t,d) = \frac{N_\text{term}}{N_\text{terms in Document}}
$$
Inverse document frequency is defined as the frequency of documents that contain that term over the whole corpus.
$$
\mathrm{idf}(t, D) = \log\frac{N_\text{Documents}}{N_\text{Documents that contain term}}
$$

Term frequency - Inverse Document Frequency is calculated as:

$$
\mathrm{tfidf}(t,d,D) = \mathrm{tf}(t,d) \cdot \mathrm{idf}(t, D)
$$

This enhances terms that are highly specific of a particular document, while suppressing terms that are common to most documents.

**Check:** Can you think of situations where the definition above may be problematic?
> The definition above is problematic with rare terms, because the idf will be big. There are several normalization schemes, the interested reader is referred to [this link](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).

Scikit Learn introduces a TFIDF vectorizer that works similarly to the other vectorizers. Notice that now we can also eliminate stop words to improve our analysis.

**Check:** As you did above, import and initialize the TfidfVectorizer, then fit the spam and ham data. 

> Answer:
>
    from sklearn.feature_extraction.text import TfidfVectorizer
    tvec = TfidfVectorizer(stop_words='english')
    tvec.fit([spam, ham])


```python

```


```python
df  = pd.DataFrame(tvec.transform([spam, ham]).todense(),
                   columns=tvec.get_feature_names(),
                   index=['spam', 'ham'])

df.transpose().sort_values('spam', ascending=False).head(10).transpose()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>years</th>
      <th>euros</th>
      <th>contact</th>
      <th>personality</th>
      <th>linkedin</th>
      <th>lukoil</th>
      <th>major</th>
      <th>million</th>
      <th>old</th>
      <th>operation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>spam</th>
      <td>0.287128</td>
      <td>0.287128</td>
      <td>0.287128</td>
      <td>0.143564</td>
      <td>0.143564</td>
      <td>0.143564</td>
      <td>0.143564</td>
      <td>0.143564</td>
      <td>0.143564</td>
      <td>0.143564</td>
    </tr>
    <tr>
      <th>ham</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.transpose().sort_values('ham', ascending=False).head(10).transpose()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>interview</th>
      <th>regards</th>
      <th>scientist</th>
      <th>data</th>
      <th>let</th>
      <th>position</th>
      <th>john</th>
      <th>invite</th>
      <th>interviews</th>
      <th>inform</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>spam</th>
      <td>0.00000</td>
      <td>0.00000</td>
      <td>0.00000</td>
      <td>0.00000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>ham</th>
      <td>0.31039</td>
      <td>0.31039</td>
      <td>0.31039</td>
      <td>0.31039</td>
      <td>0.155195</td>
      <td>0.155195</td>
      <td>0.155195</td>
      <td>0.155195</td>
      <td>0.155195</td>
      <td>0.155195</td>
    </tr>
  </tbody>
</table>
</div>



**Check:** What is TFIDF? describe with your own words.

<a name="conclusion"></a>
## Conclusion (5 mins)

In this lesson we learned about Natural Language Processing and about two very powerful toolkits:
- Scikit Learn Feature Extraction Text
- Natural Language Tool Kit

**Check:** Discussion: what are some real world applications of these techniques?

### ADDITIONAL RESOURCES

- [Count Vectorizer Documentation](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html)
- [Choosing a Stemmer](https://www.elastic.co/guide/en/elasticsearch/guide/current/choosing-a-stemmer.html)
- [Feature Hashing](https://en.wikipedia.org/wiki/Feature_hashing)
- [Term Frequency Inverse Document Frequency](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
- [TFIDF Vectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
