import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np
import pandas as pd
import seaborn as sns

from ipywidgets import *

from pprint import pprint

from sklearn.datasets import make_moons, make_classification, make_gaussian_quantiles
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score



class EnsemblePlotter(object):

    def __init__(self, N=200, scaling=20,
                 mesh_granularity=400, n_estimators=100,
                 point_size=100, figsize=(18,8), rf_maxdepth=None,
                 gb_maxdepth=2):

        self.N = N
        self.scaling = scaling
        self.mesh_granularity = mesh_granularity
        self.n_estimators = n_estimators
        self.point_size = point_size
        self.figsize = figsize
        self.rf_maxdepth = rf_maxdepth
        self.gb_maxdepth = gb_maxdepth

        self.light_colors = {'blue': '#729ECE',
                             'brown': '#A8786E',
                             'green': '#67BF5C',
                             'grey': '#A2A2A2',
                             'orange': '#FF9E4A',
                             'pink': '#ED97CA',
                             'purple': '#AD8BC9',
                             'red': '#ED665D',
                             'teal': '#6DCCDA',
                             'yellow': '#CDCC5D'}

        self.dark_colors = dict(blue='#1F77B4',
                                orange='#FF7F0E',
                                green='#2CA02C',
                                red='#D62728',
                                purple='#9467BD',
                                brown='#8C564B',
                                pink='#E377C2',
                                grey='#7F7F7F',
                                yellow='#BCBD22',
                                teal='#17BECF')


    def make_moon_data(self):
        X, y = make_moons(self.N, noise=0.15)
        X = X*self.scaling
        return X, y


    def make_cls_data(self):
        X, y = make_classification(n_samples=self.N,
                                   n_features=2,
                                   n_informative=2,
                                   n_redundant=0,
                                   n_classes=2,
                                   n_clusters_per_class=2,
                                   flip_y=0.35,
                                   scale=1.,
                                   class_sep=1.25)
        X = X*self.scaling
        return X, y


    def make_gaussian_data(self):

        X1, y1 = make_gaussian_quantiles(cov=0.75,
                                         n_samples=self.N/2,
                                         n_features=2,
                                         n_classes=2)
        X2, y2 = make_gaussian_quantiles(mean=(3, 3),
                                         cov=0.75,
                                         n_samples=self.N/2,
                                         n_features=2,
                                         n_classes=2)
        X = np.concatenate((X1, X2))
        y = np.concatenate((y1, - y2 + 1))

        yinds = np.random.choice(range(len(y)), size=int(round(len(y)/6)), replace=False)
        yshuff = np.random.choice(y[yinds], size=len(yinds), replace=False)
        y[yinds] = yshuff



        X = X*self.scaling
        return X, y


    def make_meshgrid(self, X):
        x_min, x_max = X[:, 0].min() - 3, X[:, 0].max() + 3
        y_min, y_max = X[:, 1].min() - 3, X[:, 1].max() + 3
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, self.mesh_granularity),
                             np.linspace(y_min, y_max, self.mesh_granularity))
        return xx, yy


    def predict_onto_meshgrid(self, X, y, Xtest, ytest, xx, yy):

        rfZs = {}
        gbZs = {}

        rfscores = {}
        gbscores = {}

        for ne in range(1, self.n_estimators+1):

            if (ne % 10) == 0:
                print 'n_estimators:', ne

            rf = RandomForestClassifier(max_depth=self.rf_maxdepth,
                                        n_estimators=ne)

            #learning_rate = 1. - ((ne**1.05 - 1.) / (1. + ne**1.05))
            gb = GradientBoostingClassifier(n_estimators=ne,
                                            max_depth=self.gb_maxdepth,
                                            learning_rate=0.1)

            rf.fit(X, y)
            gb.fit(X, y)

            rfZ = rf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:,1]
            gbZ = gb.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:,1]

            rfZs[ne] = rfZ
            gbZs[ne] = gbZ

            rf_yhat = rf.predict(Xtest)
            gb_yhat = gb.predict(Xtest)

            rfscores[ne] = accuracy_score(ytest, rf_yhat)
            gbscores[ne] = accuracy_score(ytest, gb_yhat)

        return rfZs, gbZs, rfscores, gbscores


    def initialize_data(self):

        self.data = {}


        Xclass, yclass = self.make_cls_data()
        Xgauss, ygauss = self.make_gaussian_data()


        for data_type in ['moon','class','gauss']:
            print data_type

            if data_type == 'moon':
                X, y = self.make_moon_data()
            elif data_type == 'class':
                X, y = self.make_cls_data()
            elif data_type == 'gauss':
                X, y = self.make_gaussian_data()

            xx, yy = self.make_meshgrid(X)

            Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.50)

            rfZs, gbZs, rfs, gbs = self.predict_onto_meshgrid(Xtrain, ytrain,
                                                              Xtest, ytest,
                                                              xx, yy)

            self.data[data_type] = {
                'X':X,
                'y':y,
                'Xtrain':Xtrain,
                'Xtest':Xtest,
                'ytrain':ytrain,
                'ytest':ytest,
                'xx':xx,
                'yy':yy,
                'rfZs':rfZs,
                'gbZs':gbZs,
                'rfs':rfs,
                'gbs':gbs
            }


    def plot_bagging_boosting(self, data_type, estimators, test_data=False):

        d = self.data[data_type]

        if not test_data:
            X = d['Xtrain']
            y = d['ytrain']
        else:
            X = d['Xtest']
            y = d['ytest']

        xx = d['xx']
        yy = d['yy']
        rfZs = d['rfZs'][estimators]
        gbZs = d['gbZs'][estimators]
        rfs = d['rfs'][estimators]
        gbs = d['gbs'][estimators]

        fig, axarr = plt.subplots(1, 2, figsize=self.figsize)

        pp_cm = LinearSegmentedColormap.from_list('pp_cm',
                                                  [self.light_colors['blue'],
                                                   self.light_colors['orange']])

        if test_data:
            point_alpha = 1.0
            point_cm = ListedColormap([self.light_colors['blue'], self.light_colors['orange']])
        else:
            point_alpha = 1.0
            point_cm = ListedColormap([self.dark_colors['blue'], self.dark_colors['orange']])

        for a, Z, clf_name, s in zip([axarr[0], axarr[1]],
                                     [rfZs, gbZs],
                                     ['Random Forest','Gradient Boosted Trees'],
                                     [rfs, gbs]):


            a.scatter(X[:, 0], X[:, 1], c=y, cmap=point_cm, s=self.point_size,
                      alpha=point_alpha)

            a.set_xlim(xx.min(), xx.max())
            a.set_ylim(yy.min(), yy.max())

            Z = Z.reshape(xx.shape)
            a.contourf(xx, yy, Z, cmap=pp_cm, alpha=0.4)

            a.set_xlabel('X1', fontsize=16)
            a.set_ylabel('X2', fontsize=16)

            a.set_title(clf_name+' (Acc. = '+"{0:.3f}".format(s)+')\n', fontsize=20)

        plt.show()


    def plot_wrapper(self, n_estimators=1, problem='moon', test_data=False):
        self.plot_bagging_boosting(problem, n_estimators, test_data=test_data)


    def ensemble_interact(self):

        ne = widgets.IntSlider(min=1, max=self.n_estimators,
                               step=1, value=1, continuous_update=False)
        ne.width = '600px'
        ne.description = 'base trees:'

        prob = widgets.Dropdown(description='problem', width=200)
        prob.options = ['moon','class','gauss']

        test = widgets.Checkbox(value=False)
        test.description = 'test data:'


        widgets.interact(self.plot_wrapper,
                         n_estimators=ne,
                         problem=prob,
                         test_data=test)
