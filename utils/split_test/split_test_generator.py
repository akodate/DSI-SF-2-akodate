import numpy as np
import scipy.stats as stats

class SplitTestArm(object):

    def __init__(self, true_rate):
        self._true_rate = true_rate
        self._successes = 0
        self._failures = 0

    def __call__(self, users=1):
        outcomes = np.random.binomial(1, self._true_rate, size=users)
        self._successes += np.sum(outcomes)
        self._failures += (len(outcomes) - np.sum(outcomes))
        return outcomes


class SplitTest(object):

    def __init__(self, group_alpha=11, group_beta=51):
        self._group_beta = stats.beta(group_alpha, group_beta)
        self._total_users = 0

    def __getattr__(self, attr):
        if not attr in self.__dict__.keys():
            print 'Creating split test arm:', attr
            self.__dict__[attr] = SplitTestArm(self._group_beta.rvs())
            return self.__dict__[attr]
        else:
            return self.__dict__[attr]

    def __getitem__(self, attr):
        return self.__getattr__(attr)
