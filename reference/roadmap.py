#### Roadmap for Statistical Modeling
"""
Made for General Assembly's Data Science Immersive Cohort 2
Roadmap/Cheatsheet for Data Input, Learning, Munging, Exploring and Modeling
"""





### Uploading the CSV file
#=====================================================================================================
import pandas as pd
import numpy as np

df = pd.read_csv('../../../example.csv')
#=====================================================================================================





### Learn about the data
#=====================================================================================================
df.info() # Tells you the shape and the types
df.shape # Tells you the shape of the dataframe
df.dtypes # Tells you the data type for each column
df.head() # Prints out first 5 rows
df.tail() # Prints out last 5 rows
df.columns # Prints out all column names
df['col1'].unique() # Prints out all unique values in col1
df['col1'].value_counts() # Prints out each unique value and # of instances
#=====================================================================================================





### Clean the data
#=====================================================================================================
## Change Yes/No, True/False into 0 and 1
df['col1'].map(lambda x: 1 if x == 'Yes' else 0)

## Remove all $ signs, or any strings, in dataframes and change to a float, if needed, with .apply
def remove_dollar_sign(x):
	if '$' in x:
		return float(x.replace('$', ''))
	else:
		return x

df['col'].apply(remove_dollar_sign)

# Simple way to change all values in column to different type with .apply
df['col'].apply(float)

## Rename columns
df.rename(columns={'col1':'new_col1', 'col2':'new_col2'}, inplace=True)

# Another way
update_columns = ['new_col1', 'new_col2']
new_df = pd.DataFrame[data=df, columns=update_columns]

## Drop/Edit Nan Values
# Drop rows with NaN values
df.dropna()
df['col1'].dropna()

# Edit NaN Values
df.fillna('new_value')
df['col1'].fillna('new_value')

## Create new column
df['new_col'] = np.mean(df['col1']) / np.mean(df['col2'])

## Masking
# new_col has to be True AND col1 has to be 0 OR col2 does not equal to 'you'
new_mask = (df['new_col'] == True) & (df['col1'] == 0) | (df['col2'] != 'you')
df[new_mask]

## Quick way to create new dataframe with select columns from another dataset
new_df = df[['col1', 'col2', 'col3']]

## Dealing with outliers
# Removing
def reject_outliers(data, m=1.5):
    data[abs(data - np.mean(data)) > m * np.std(data)]

# Removing Outliers by Replacing with Mean

# Removing Outliets by Removing Row

## Indexing
"""
.loc - indexes with the labels for rows and columns
.iloc - indexes with the integer positions for rows and columns
.ix - indexes with both lebals and integer positions
"""
#=====================================================================================================





### Hypothesis, EDA and Graphing
#=====================================================================================================
## Hypothesis
# This is where you setup your null hypothesis for testing.
# A preferable null hypothesis would be:
	# In the winter season, whiskey sales are sold 20% higher than any other alcohol.


#-----------------------------------------------------------------------------------------------------


## EDA
from scipy import stats
stats.mode(a)

# correlation matrix
df.corr() # method='pearson' / 'spearman' / 'kendall'
# covariance matrix
df.cov()
# displays all descriptive statistics
df.describe()
# displays all unique values in 1 column and counts them
df['col'].value_counts()
# displays all unique values in 1 column
df['col'].unique()

x = [1,2,3,4,5]
# returns the mean of the array
np.mean(x)
# returns the median of the array
np.median(x)
# returns the sum of the array
np.sum(x)
# returns the size/shape of the array
np.size(x)
# returns the variance of the array
np.var(x)
# returns the standard deviation of the array
np.std(x)
# returns the square root of the array
np.sqrt(x)
# returns the count occurance of the array 
.count(x)

## Groupby
new_df = df.groupby(['col1'])[['col2', 'col3']].mean().reset_index()
new_df.sort_values('col2', axis=1)
# Groupby col1 with the mean values of col2 and col3, reset the index and sorted by col2
# Must have .size() .mean() .sum() etc... for groupby to work

## Pivot Tables - Long to Wide
df_wide = pd.pivot_table(df_long, # The Data frame you want to convert
                        columns=['col'], # The values in the long df you want to assign for the wide dataframe
                        values='value', # The values in the long df you want to pivot to the wide dataframe
                        index=['subject_id'], # The columns in the long df you want to become the index for the wide dataframe
                        aggfunc=np.mean, # Aggregate function that defaults to the mean, can put own function in, works like .apply 
                        fill_value=np.nan) # Fills in all empty values as assigned value

# Pivot Table example
   A   B   C      D
0  foo one small  1
1  foo one large  2
2  foo one large  2
3  foo two small  3
4  foo two small  3
5  bar one large  4
6  bar one small  5
7  bar two small  6
8  bar two large  7

table = pivot_table(df, values='D', index=['A', 'B'], columns=['C'], aggfunc=np.sum, fill_value='hi')

# Output:
          small  large
foo  one  1      4
     two  6      'hi'
bar  one  5      4
     two  6      7

## Melt() - Wide to Long
df_long = pd.melt(df_wide, # The Data frame you want to convert
                  id_vars=['col1','col2'], # The identifiers for the other columns
                  value_vars=, # The value that identifies to each id_vars
                  var_name=, # The column name for value_vars
                  value_name=) # The column name for the values for each value_vars

# Melt example
df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})

   A  B  C
0  a  1  2
1  b  3  4
2  c  5  6

pd.melt(df, id_vars=['A'], value_vars=['B'], var_name='myVarname', value_name='myValname')

# Output:
   A myVarname  myValname
0  a         B          1
1  b         B          3
2  c         B          5


## Merging
new_df = df1.merge(df2, on='Id', how='left')
new_df = pd.merge(df1, df2, on='Id', how='right')
# Multiple merges in 1 line
new_df = df1.merge(df2, on='Id', how='left').merge(df3, on='Name', how='inner').merge(df4, on='Password', how='outer')


#-----------------------------------------------------------------------------------------------------


### Graphing
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('fivethirtyeight')

# Plot within the jupyter notebook
%matplotlib inline
# Basically, the HD version
%config InlineBackend.figure_format = 'retina'

# Create a figure size
fig = plt.figure(figsize=(7,7))
ax = fig.gca()

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Scatterplot
# Seaborn
ax = sns.regplot(x=x, y=y, data=df, color='green', marker='+', ci=68, x_estimater=x, y_jitters=0.1, 
                 x_bins=5, truncate=True, logistic=False)
# Matplotlib
ax.scatter(x, y, s=150, c='blue', label='accepted')
ax.scatter(x, y, s=100, c='orange', label='rejected')

ax.set_ylabel('y label', fontsize=16)
ax.set_xlabel('x label', fontsize=16)
ax.set_title('I am title', fontsize=20)

ax.set_xlim([2.,5.])
ax.set_ylim([-0.1, 1.1])

plt.legend(loc='upper left')
plt.show()
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Histogram
# Seaborn
ax = sns.distplot(x, name='x variable', fit=norm, kde=False, vertical=False, color='yellow')
# Matplotlib
ax.hist(x, bin=5, alpha=0.7) # Hist for 2 datasets, input [x,y]
ax.set_ylabel('frequency', fontsize=16)
ax.set_xlabel('something', fontsize=16)
ax.set_title('I am title', fontsize=20)

ax.set_xlim([0.,50.])
ax.set_ylim([0, 100])

plt.show()

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Lineplot
# Seaborn
ax = sns.pointplot(x=x, y=y, hue='gender',data=df, marker=['o','x'], linestyle=['-','--'], join=True, 
                   color='#bb3f3f', order=['Dinner','Lunch'], estimator=np.median, capsize=.2)
# Matplotlib
ax = sns.plot(x,y)
ax.set_ylabel('y', fontsize=16)
ax.set_xlabel('x', fontsize=16)
ax.set_title('title', fontsize=20)

ax.set_xlim([0.,50.])
ax.set_ylim([0, 100])

plt.show()

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Heatmap (Correlate)
# Seaborn
corr = df.corr
ax = sns.heatmap(corr, vmin=0, vmin=1, annot=False, square=True, linewidths=.5, cmap="YlGnBu", cbar=True)
# Matplotlib
## It's difficult, use seaborn pls

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Barplot
# Seaborn
ax = sns.barplot(x=x, y=y, data=df, hue='gender', order=['Dinner', 'Lunch'], estimator=np.median, color='b')
# Matplotlib
ax.bar(x, y, width=1.5, color='blue')
ax.set_ylabel('y', fontsize=16)
ax.set_xlabel('x', fontsize=16)
ax.set_title('title', fontsize=20)

ax.set_xlim([0.,50.])
ax.set_ylim([0, 100])

plt.show()

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Pairplot
# Seaborn
ax = sns.pairplot(df, hue='gender', markers=['x','o'], size=3, vars=['Height', 'Weight'], kind='reg')

#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>

## Boxplot
# Seaborn
ax = sns.boxplot(x=x, y=y, data=df, hue='gender', orient='h', fliersize=2)
ax = sns.swarmplot(x=x, y=y, data=df, color='.25')
# Matplotlib
ax.barplot(data)

#=====================================================================================================





### Modeling
#=====================================================================================================
## Setting up Patsy
import patsy

formula = 'target ~ predictor1 + predictor2 + predictor3 + predictor4 ... + predictor100 - 1'
y, X    = patsy.dmatrices(formula, df=df, return_type='dataframe')

# Since patsy makes y into a 2D array/dataframe with the index, have to change y into a 1D array/List
y = y.values
# or
y = np.ravel(y)
# or
y = df['target']


#-----------------------------------------------------------------------------------------------------


## Setting up train-test split
from sklearn.cross_validation import train_test_split

trainX, testX, trainY, testY = train_test_split(X, y, train_size=0.7, stratify=y) # Can also use test_size
print trainX.shape, testX.shape
print trainY.shape, trainY.shape
# trainX and testX should be a data from like (1000,15)
# trainY and testY should be a 1D array or list like (1000,)


#-----------------------------------------------------------------------------------------------------


## GridSearch
# Gridsearch is used for searching for the best parameters
from sklearn.grid_search import GridSearchCV

# Setup our GridSearch Parmaters
search_parameters = {
    'fit_intercept':  [True, False], 
    'normalize':      [False, True]
}

# Intialize a blank model object
lm = LinearRegression()

# Initialize gridsearch
estimator = grid_search.GridSearchCV(lm, search_parameters, cv=5)

# Fit some data!
results = estimator.fit(trainX, trainY)

results.param_grid			#Displays parameters used
results.best_score_			#Best score achieved
results.best_estimator_		#Reference to model with best score. Is usable / callable.
results.best_params_		#The parameters that have been found to perform with the best score.
results.grid_scores_		#Display score attributes with cooresponding parameters


#-----------------------------------------------------------------------------------------------------


## Normalization, Standardization, Lasso, Ridge, Elastic Net
# Normalization
from sklearn.preprocessing import MinMaxScaler, StandardScaler

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)


#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Standardization
from sklearn.preprocessing import MinMaxScaler, StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)


#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Lasso (Complete with GridSearch)
from sklearn.linear_model import Lasso
lasso = Lasso()
parameters
	(alpha=1.0, fit_intercept=True, normalize=False, precompute=False, copy_X=True, 
	max_iter=1000, tol=0.0001, warm_start=False, positive=False, random_state=None, selection='cyclic')

from sklearn.linear_model import LassoCV

parameters
	(eps=0.001, n_alphas=100, alphas=None, fit_intercept=True, normalize=False, precompute='auto', 
	max_iter=1000, tol=0.0001, copy_X=True, cv=None, verbose=False, n_jobs=1, positive=False, 
	random_state=None, selection='cyclic')


#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Ridge (Complete with GridSearch)
from sklearn.linear_model import Ridge
ridge = Ridge()
parameters
	(alpha=1.0, fit_intercept=True, normalize=False, copy_X=True, max_iter=None, 
	tol=0.001, solver='auto', random_state=None

from sklearn.linear_model import RidgeCV

parameters
	(alphas=(0.1, 1.0, 10.0), fit_intercept=True, normalize=False, scoring=None, 
	cv=None, gcv_mode=None, store_cv_values=False)


#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Elastic Net (Complete with GridSearch)
from sklearn.linear_model import ElasticNet
en = ElasticNet()
parameters
	(alpha=1.0, l1_ratio=0.5, fit_intercept=True, normalize=False, precompute=False, max_iter=1000, 
	copy_X=True, tol=0.0001, warm_start=False, positive=False, random_state=None, selection='cyclic')

from sklearn.linear_model import ElasticNetCV

parameters	
	(l1_ratio=0.5, eps=0.001, n_alphas=100, alphas=None, fit_intercept=True, normalize=False, 
	precompute='auto', max_iter=1000, tol=0.0001, cv=None, copy_X=True, verbose=0, n_jobs=1, 
	positive=False, random_state=None, selection='cyclic')


#-----------------------------------------------------------------------------------------------------


## Modeling - this is where you decide which model to use
# The parameters found in GridSearch can be used for regression analysis
#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Linear Regression
from sklearn.linear_model import LinearRegression

# Assign lm as the LinearRegression function
lm = LinearRegression()
# Fits trainX and trainY with the lm model and assigns to a variable
model = lm.fit(trainX, trainY)
# Returns Predicted Y values
predictions = model.predict(testX)
# Plots your True Y with Predicted Y
plt.scatter(testY, predictions)
# R-squared
score = model.score(testX, testY)


#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# K-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier

# Assign knn as a KNeighborsClassifier function
knn = KNeighborsClassifier(n_neighbors=5, weights='uniform') # uniform or distance
# Fits trainX and trainY with the knn model and assigns to a variable
model = knn.fit(trainX, trainY)
# ?
predictions = model.predict(testX)
# ?
score = model.score(testX, testY)


#<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>


# Logistic Regression
import patsy
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
%matplotlib inline

def logistic_regression_calculation(predictors, target, title='Your Prediction'):
    
    ### Test-Train split 70-30
    trainX, testX, trainY, testY = train_test_split(predictors, target, train_size=0.7, stratify=target)
    print 'trainX shape: ', trainX.shape, '\ntestX shape:', testX.shape
    print 'trainY shape: ', trainY.shape, '\ntestY shape:', testY.shape
    
    ### Setup LogisticRegression modeling
    # Create LogisticRegression function cross validated 5 times
    logreg = LogisticRegressionCV(cv=5)
    # Fit the data points into the LogisticRegression model
    model = logreg.fit(trainX, trainY)
    # Predict Probability
    probabilities = model.predict_proba(testX)
    # Score the model
    score = model.score(testX, testY)
    print 'Model Score: ', score
    
    ### Plot the data
    # Creating a blank set of objects to store my confusion matrix metrics here
    FPR = dict()
    TPR = dict()
    ROC_AUC = dict()

    # I am assigning the 1st offsets to my FPR / TPR from the 2nd set of probabiliies from my
    # .predict_proba() predictions
    # This data is what will be plotted once we throw it to our figure
    FPR[1], TPR[1], _ = roc_curve(testY, probabilities[:, 1])
    ROC_AUC[1] = auc(FPR[1], TPR[1])

    # 1. Initialize a blank plot, aspect 11x9
    plt.figure(figsize=[11,9])
    # 2. Plot my false and true rates (returned from roc_curve function)
    plt.plot(FPR[1], TPR[1], label='ROC curve (area = %0.2f)' % ROC_AUC[1], linewidth=4)
    # 3. Plotting a dotted line diagonally, representing the .5
    plt.plot([0, 1], [0, 1], 'k--', linewidth=4)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=18)
    plt.ylabel('True Positive Rate', fontsize=18)
    plt.title('Receiver operating characteristic for %s' %title, fontsize=18)
    plt.legend(loc="lower right")
    plt.show()

logistic_regression_calculation(X, y, title='over 200k predictions')


#-----------------------------------------------------------------------------------------------------


## Cross Validation
from sklearn.cross_validation import cross_val_score, cross_val_predict
from sklearn import metrics

# Perform 6-fold cross validation
scores = cross_val_score(model, X, y, cv=6) #parameters (model, predictor/dataset, target, folds)
print 'Cross-validated scores:', scores

# Make cross validated predictions
predictions = cross_val_predict(model, X, y, cv=6) #parameters same as cross_val_score
plt.scatter(y, predictions)

# Calculated accuracy
accuracy = metrics.r2_score(y, predictions)
print 'Cross-predicted Accuracy:', accuracy
#=====================================================================================================





### Definitions
#=====================================================================================================
# Correlation (matrix) vs Covariance (matrix)

# Pearson vs Spearman

# Bias vs Variance

# 










