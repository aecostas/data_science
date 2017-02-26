import matplotlib.pyplot as plt
from decimal import Decimal
import numpy as np
import pylab
from scipy import stats


def uniform_dependent(samples, iterations, low, high):
    '''
    Sum of 'iterations' uniform dependent variables 
    '''
    values = np.zeros(samples)
    shapiro_W = []
    shapiro_p = []
    base_uniform = np.random.uniform(low=-low, high=high, size=samples)

    for i in range(iterations):
        values += base_uniform*np.random.uniform(low=-1, high=1, size=1)
        shapiro_test = stats.shapiro(values)
        shapiro_W.append(shapiro_test[0])
        shapiro_p.append(shapiro_test[1])
        print shapiro_test

    return values

def uniform(samples, iterations, low, high):
    '''
    Sum of 'iterations' uniform independent variables 
    '''
    values = np.zeros(samples)
    shapiro_W = []
    shapiro_p = []

    for i in range(iterations):
        values += np.random.uniform(low=-low, high=high, size=samples)
        shapiro_test = stats.shapiro(values)
        shapiro_W.append(shapiro_test[0])
        shapiro_p.append(shapiro_test[1])
        print shapiro_test
    return values

if __name__ == "__main__":
    uniformDependent = uniform_dependent(1000, 30, 100, 100)
    uniformIndependent = uniform(1000, 30, 100, 100)

    fig, ax = plt.subplots(2,2)

    # dependant values
    count, bins, ignored = ax[0,0].hist(uniformDependent, 20, normed=True)
    stats.probplot(uniformDependent, dist="norm", plot=ax[0,1])
    ax[1,1].set_title("")
    ax[0,1].set_title("")
    ax[1,1].set_ylabel("")
    ax[0,1].set_ylabel("")
    ax[1,1].tick_params(axis='both', which='major', labelsize=9)
    ax[0,1].tick_params(axis='both', which='major', labelsize=9)

    # independant values
    count, bins, ignored = ax[1,0].hist(uniformIndependent, 20, normed=True)
    stats.probplot(uniformIndependent, dist="norm", plot=ax[1,1])
    ax[1,0].set_title("")
    ax[1,1].set_title("")
    ax[1,0].set_ylabel("")
    ax[1,1].set_ylabel("")
    ax[1,0].tick_params(axis='both', which='major', labelsize=9)
    ax[1,1].tick_params(axis='both', which='major', labelsize=9)

    pylab.suptitle("Normal probability plot")
    pylab.savefig('prueba.png',facecolor=fig.get_facecolor(), edgecolor='none', dpi=120)
