#import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# generate normal distribution
mu, sigma = 0, 0.1 # mean and standard deviation
data_normal = np.random.normal(mu, sigma, 1000)

# binomial
n, p = 1000, .2  # number of trials, probability of each trial
data_binomial = np.random.binomial(n, p, 1000)

# pareto
a, m = 3., 2.  # shape and mode
data_pareto = (np.random.pareto(a, 1000) + 1) * m

shapiro_normal = stats.shapiro (data_normal)
shapiro_binomial = stats.shapiro (data_binomial)
shapiro_pareto = stats.shapiro (data_pareto)

anderson_normal = stats.anderson (data_normal, dist='norm')
anderson_binomial = stats.anderson (data_binomial, dist='norm')
anderson_pareto = stats.anderson (data_pareto, dist='norm')

print ("-------------------------------------")
print ("| Shapiro-Wilk test for normality   |")
print ("-------------------------------------")
print ("Normal: ", shapiro_normal)
print ("Binomial: ", shapiro_binomial)
print ("Pareto: ", shapiro_pareto)

print ("\n-------------------------------------")
print ("|Anderson-Darling test for normality|")
print ("-------------------------------------")
print ("Normal: ", anderson_normal)
print ("Binomial: ", anderson_binomial)
print ("Pareto: ", anderson_pareto)


# Plotting data
# count, bins, ignored = plt.hist(data_normal, 30, normed=True)
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *  np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
# plt.show()

# count, bins, _ = plt.hist(data_pareto, 100, normed=True)
# fit = a*m**a / bins**(a+1)
# plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')
# plt.show()



# TODO: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.anderson.html#scipy.stats.anderson
