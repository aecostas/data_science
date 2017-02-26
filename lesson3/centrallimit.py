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


def central_limit_theorem_OLD(iterations):
    samples = 1000;
    values = np.zeros(samples);

    # for i in range(iterations):
    #     values += np.random.uniform(low=-1, high=1, size=samples)
    #     print stats.shapiro(values)

    # reference = np.random.poisson(2, samples)
    # count, bins, ignored = plt.hist(reference, 100, normed=True)

    shapiro_W = []
    shapiro_p = []

    for i in range(iterations):
        tmp_W = []
        tmp_p = []

        for trial in range(100):
            valuesForTrial = np.array(values)
            valuesForTrial += np.random.uniform(low=-100, high=100, size=samples)
            shapiro_test = stats.shapiro(valuesForTrial)
            tmp_W.append(shapiro_test[0])
            tmp_p.append(shapiro_test[1])

        values = np.array(valuesForTrial)
        shapiro_W.append(np.array(tmp_W).mean())
        shapiro_p.append(np.array(tmp_p).mean())

    count, bins, ignored = plt.hist(values, 20, normed=True)
    plt.show()

    # P-Value trendline
    x = range(iterations)
    y = shapiro_p
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    fig = pylab.plot(x,p(x),'r--')

    plt.plot(y, 'ro')
    plt.title('Shapiro-Wilk test for central limit theorem evaluation')
    plt.ylabel('p-value')
    plt.xlabel('Number of random variables added')
    plt.show();

    # P-Value trendline
    x = range(iterations)
    y = shapiro_W
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    fig = pylab.plot(x,p(x),'r--')

    plt.plot(y, 'W')
    plt.title('Shapiro-Wilk test for central limit theorem evaluation')
    plt.ylabel('W')
    plt.xlabel('Number of random variables added')
    plt.show();

#    plt.savefig(filename+'_p.png', facecolor='#BABABA' , edgecolor='none', dpi=1200)

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
