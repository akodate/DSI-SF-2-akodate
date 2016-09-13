import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy

from sklearn.linear_model import LinearRegression

from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib.cm as cm
import matplotlib.colors as cl

from ipywidgets import *



class BootstrapPlotter(object):

    def __init__(self, reg_figsize=(18,7), hist_figsize=(18,7), pointsize=60):

        self.reg_figsize = reg_figsize
        self.hist_figsize = hist_figsize
        self.pointsize = pointsize

        self.colors = dict(blue='#1F77B4',
                           orange='#FF7F0E',
                           green='#2CA02C',
                           red='#D62728',
                           purple='#9467BD',
                           brown='#8C564B',
                           pink='#E377C2',
                           grey='#7F7F7F',
                           yellow='#BCBD22',
                           teal='#17BECF')

        self.model = LinearRegression()


    def initialize_reg_data(self, N=55):
        x = np.linspace(0., 40., N)+np.random.normal(0, 3, size=N)
        y = ((np.linspace(0., 40., N)**3.1)/1000.)
        y = y + np.random.normal(np.random.normal(10,20,1), 7, size=N)/2.2

        rinds = np.random.choice(range(len(y)), size=int(round(N/3.)), replace=False)
        y[rinds] = y[rinds]+(np.random.normal(-55,40,size=len(rinds)))

        self.regN = N
        self.regmat = pd.DataFrame(np.array([x, y]).T, columns=['x','y'])

        self.bootstrap_regression()


    def bootstrap_regression(self):

        self.reg_bootmax = 100
        self.reg_bootmin = 5
        self.xvalues = np.linspace(np.min(self.regmat.x.values)-10,
                                   np.max(self.regmat.x.values)+10,
                                   200)

        self.reg_bootstraps = {}

        for i in range(self.reg_bootmin, self.reg_bootmax+1):
            r = np.random.choice(range(self.regmat.shape[0]),
                                 size=self.regmat.shape[0], replace=True)
            sample_regmat = self.regmat.iloc[r, :]

            y = sample_regmat.y.values
            X = sample_regmat[['x']].values
            self.model.fit(X, y)

            self.reg_bootstraps[i] = {
                'b0':self.model.intercept_,
                'b1':self.model.coef_[0],
                'r2':self.model.score(X,y)
            }




    def reg_plots(self, bootstraps):

        fig, axarr = plt.subplots(1, 2, figsize=self.reg_figsize)

        ax0 = axarr[0]
        ax1 = axarr[1]

        b0s = [self.reg_bootstraps[i]['b0'] for i in range(self.reg_bootmin, bootstraps+1)]
        b1s = [self.reg_bootstraps[i]['b1'] for i in range(self.reg_bootmin, bootstraps+1)]
        r2s = [self.reg_bootstraps[i]['r2'] for i in range(self.reg_bootmin, bootstraps+1)]

        b0_mean = np.mean(b0s)
        b1_mean = np.mean(b1s)

        yvalues = [b0_mean + b1_mean*x for x in self.xvalues]

        b0_pctl_low, b0_pctl_high = np.percentile(b0s, 5), np.percentile(b0s, 95)
        b1_pctl_low, b1_pctl_high = np.percentile(b1s, 5), np.percentile(b1s, 95)

        yvalues_pctl_low = [b0_pctl_low + b1_pctl_low*x for x in self.xvalues]
        yvalues_pctl_high = [b0_pctl_high + b1_pctl_high*x for x in self.xvalues]


        ax0.scatter(self.regmat.x.values, self.regmat.y.values,
                    color=self.colors['blue'], s=self.pointsize,
                    label='observations')

        ax0.plot(self.xvalues, yvalues, color=self.colors['red'],
                 lw=4, label='mean regression')

        ax0.plot(self.xvalues, yvalues_pctl_low, color=self.colors['yellow'],
                 lw=2.5, ls='dashed', label='5th pctl regression',
                 alpha=0.7)

        ax0.plot(self.xvalues, yvalues_pctl_high, color=self.colors['yellow'],
                 lw=2.5, ls='dashed', label='95th pctl regression',
                 alpha=0.7)

        ax0.set_ylabel('y', fontsize=16)
        ax0.set_xlabel('x', fontsize=16)
        ax0.set_title('bootstrapped regression with confidence interval',
                      fontsize=20)
        ax0.legend(loc='lower right')

        r2_pctl_low, r2_pctl_high = np.percentile(r2s, 5), np.percentile(r2s, 95)

        ax1bins = min(int(round(len(r2s)/4.))+1, 50)
        ax1.hist(r2s, color=self.colors['grey'], alpha=0.8,
                 bins=ax1bins, label='bootstrapped R2s')

        ax1.axvline(r2_pctl_low, color=self.colors['teal'], lw=3.5, alpha=1.0,
                   ls='dashed', label='5th percentile R2')

        ax1.axvline(r2_pctl_high, color=self.colors['teal'], lw=3.5, alpha=1.0,
                   ls='dashed', label='95th percentile R2')

        ax1.axvline(np.mean(r2s), color=self.colors['teal'], lw=6, alpha=1.0,
                    label='mean R2')

        ax1.set_ylabel('count', fontsize=16)
        ax1.set_xlabel('R2', fontsize=16)
        ax1.set_title('bootstrapped regression R2s', fontsize=20)
        ax1.legend(loc='upper right')

        plt.show()


    def initialize_hist_data(self, N=100):
        distribution = scipy.stats.gamma(3.5, N)

        points = ((distribution.rvs(N)+np.random.gamma(1.2,5,size=N))/10.)
        points = points*np.logspace(0,1.1,N)
        points = sorted(points)

        back_set = int(round(N/6.))
        points[-back_set:] = points[-back_set:]+np.random.normal(10,4,size=back_set)

        addN = int(round(N/2.))
        addpoints = points[:addN]
        points = np.concatenate([points, addpoints+(np.random.normal(0, 25, size=addN)+np.mean(points)+2*np.std(points))])

        points = points + np.random.normal(10,6,size=len(points))
        self.histN = len(points)
        self.histpoints = points

        self.bootstrap_hist_stats()


    def bootstrap_hist_stats(self):

        self.hist_bootmax = 1000
        self.hist_bootmin = 10

        self.hist_bootstraps = {}

        for i in range(self.hist_bootmin, self.hist_bootmax+1):
            r = np.random.choice(range(self.histN), size=self.histN, replace=True)
            hist_samp = self.histpoints[r]
            self.hist_bootstraps[i] = np.median(hist_samp)


    def hist_plots(self, bootstraps):

        fig, axarr = plt.subplots(1, 2, figsize=self.hist_figsize)

        ax0 = axarr[0]
        ax1 = axarr[1]

        stats = [self.hist_bootstraps[i] for i in range(self.hist_bootmin, bootstraps+1)]
        mean_stat = np.mean(stats)
        pctl_low = np.percentile(stats, 5)
        pctl_high = np.percentile(stats, 95)

        ax0bins = min(int(round(self.histN/4.))+1, 50)
        ax0.hist(self.histpoints, color=self.colors['blue'],
                bins=ax0bins, label='sample distribution')

        ax0.axvline(mean_stat, color=self.colors['red'], lw=4,
                   label='bootstrapped mean')

        ax0.axvline(pctl_low, color=self.colors['yellow'], lw=2.5, alpha=1.0,
                   ls='dashed', label='5th percentile')

        ax0.axvline(pctl_high, color=self.colors['yellow'], lw=2.5, alpha=1.0,
                   ls='dashed', label='95th percentile')

        ax0.set_ylabel('count', fontsize=16)
        ax0.set_xlabel('value', fontsize=16)
        ax0.set_title('sample with bootstrapped median')
        ax0.legend(loc='upper right')


        ax1bins = min(int(round(len(stats)/4.))+1, 50)
        ax1.hist(stats, color=self.colors['red'], alpha=0.8,
                 bins=ax1bins, label='bootstrapped medians')

        ax1.axvline(pctl_low, color=self.colors['yellow'], lw=3.5, alpha=1.0,
                   ls='dashed', label='5th percentile')

        ax1.axvline(pctl_high, color=self.colors['yellow'], lw=3.5, alpha=1.0,
                   ls='dashed', label='95th percentile')

        ax1.set_ylabel('count', fontsize=16)
        ax1.set_xlabel('median', fontsize=16)
        ax1.set_title('bootstrapped medians with confidence intervals',
                      fontsize=20)
        ax1.legend(loc='upper right')

        plt.show()


    def reg_plotter(self, bootstraps=30):
        self.reg_plots(bootstraps)

    def reg_interact(self):
        boots = widgets.IntSlider(min=5, max=100, step=1,
                                  continuous_update=False, value=3)
        boots.width = '600px'
        boots.description = 'iters:'

        widgets.interact(self.reg_plotter,
                         bootstraps=boots)


    def hist_plotter(self, bootstraps=30):
        self.hist_plots(bootstraps)

    def hist_interact(self):
        boots = widgets.IntSlider(min=10, max=1000, step=1,
                                  continuous_update=False, value=10)
        boots.width = '600px'
        boots.description = 'iters:'

        widgets.interact(self.hist_plotter,
                         bootstraps=boots)
