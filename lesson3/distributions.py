import matplotlib.pyplot as plt
import numpy as np
import pylab
from scipy import stats

trial_count = 10

normal = []
normal.append({'mu':0, 'sigma':0.1})  # 0
normal.append({'mu':0, 'sigma':0.3})  # 1
normal.append({'mu':0, 'sigma':0.9})  # 2
normal.append({'mu':3, 'sigma':0.1})  # 3
normal.append({'mu':3, 'sigma':0.3})  # 4
normal.append({'mu':3, 'sigma':0.9})  # 5

noise = np.random.normal(0, 0.1, 1000)

#
# Normality shapiro tests with different
# distributions
#
# for params in normal:
#     params['trials'] = []
#     for trial in range(trial_count):
#         # generate normal distribution
#         data = np.random.normal(params['mu'], params['sigma'], 1000)
#         params['data'] = data
#         shapiro = stats.shapiro(data)
#         anderson = stats.anderson(data, dist='norm')
#         print ('Normal (%.3f,%.2f): %.2f  %.2f' % (params['mu'], params['sigma'], shapiro[0], shapiro[1]))

#     count, bins, ignored = plt.hist(normal[0]['data'], 30, normed=True)
#     count, bins, ignored = plt.hist(normal[1]['data'], 30, normed=True)
#     count, bins, ignored = plt.hist(normal[2]['data'], 30, normed=True)
#     count, bins, ignored = plt.hist(normal[3]['data'], 30, normed=True)
#     count, bins, ignored = plt.hist(normal[4]['data'], 30, normed=True)
#     count, bins, ignored = plt.hist(normal[5]['data'], 30, normed=True)

#     plt.show()
        

def normal_sum():
    #
    # Sum of normal distributions
    #
    fig, ax = plt.subplots(1,1)
    
    data = normal[0]['data'] + normal[0]['data']
    count, bins, ignored = plt.hist(normal[0]['data'],
                                    30,
                                    normed=True,
                                    label="(%d, %.2f)" % (normal[0]['mu'],  normal[0]['sigma']))
    count, bins, ignored = plt.hist(data,
                                    30,
                                    normed=True,
    label="sum")
    plt.legend()
    plt.show()
    print stats.shapiro(data)


def shapiro_study(mu, sigma, iterations, trials):
    normal_noisy = []
    scale = 0.01
    shapiro_W = []
    shapiro_p = []
    normal = np.random.normal(mu, sigma, 1000)
    
    for i in range(iterations):
        tmp_trials = []
        tmp_W = []
        tmp_p = []
        for trial in range(trials):
            normal_noisy = [x + np.random.uniform(low=-scale*i, high=scale*i) for x in normal]
            shapiro_test = stats.shapiro(normal_noisy)
            tmp_W.append(shapiro_test[0])
            tmp_p.append(shapiro_test[1])
        shapiro_W.append(np.array(tmp_W).mean())
        shapiro_p.append(np.array(tmp_p).mean())

    # trendline
    x = range(iterations)
    y = shapiro_p
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    pylab.plot(x,p(x),'r--')

    plt.plot(y, 'ro')
    plt.show()

    
def noisy_normal(mu, sigma):
    #
    # Noisy normal distribution
    #
    trials = 10
    normal = np.random.normal(mu, sigma, 1000)

    normal_noisy_1 = [x + np.random.uniform(low=-0.5, high=0.5) for x in normal]
    normal_noisy_2 = [x + np.random.uniform(low=-1, high=1) for x in normal]
    normal_noisy_3 = [x + np.random.uniform(low=-1.5, high=1.5) for x in normal]

    # normality tests
    print stats.shapiro(normal)
    print stats.shapiro(normal_noisy_1)
    print stats.shapiro(normal_noisy_2)
    print stats.shapiro(normal_noisy_3)

    fig = plt.figure()
    ax1 = fig.add_subplot(221)
    stats.probplot(normal, dist="norm", plot=pylab)

    ax2 = fig.add_subplot(222)
    stats.probplot(normal_noisy_1, dist="norm", plot=pylab)

    ax3 = fig.add_subplot(223)    
    stats.probplot(normal_noisy_2, dist="norm", plot=pylab)

    ax4 = fig.add_subplot(224)
    stats.probplot(normal_noisy_3, dist="norm", plot=pylab)
    
    pylab.show()


    

        

# exit(0)



# # binomial
# n, p = 1000, .2  # number of trials, probability of each trial
# data_binomial = np.random.binomial(n, p, 1000)

# # pareto
# a, m = 3., 2.  # shape and mode
# data_pareto = (np.random.pareto(a, 1000) + 1) * m

# shapiro_normal = stats.shapiro (normal[0]['data'])
# shapiro_binomial = stats.shapiro (data_binomial)
# shapiro_pareto = stats.shapiro (data_pareto)

# anderson_normal = stats.anderson (normal[0]['data'], dist='norm')
# anderson_binomial = stats.anderson (data_binomial, dist='norm')
# anderson_pareto = stats.anderson (data_pareto, dist='norm')

# print ("-------------------------------------")
# print ("| Shapiro-Wilk test for normality   |")
# print ("-------------------------------------")
# print ("Normal: ", shapiro_normal)
# print ("Binomial: ", shapiro_binomial)
# print ("Pareto: ", shapiro_pareto)

# print ("\n-------------------------------------")
# print ("|Anderson-Darling test for normality|")
# print ("-------------------------------------")
# print ("Normal: ", anderson_normal)
# print ("Binomial: ", anderson_binomial)
# print ("Pareto: ", anderson_pareto)


# exit(0)

# # Plotting data
# count, bins, ignored = plt.hist(data_normal, 30, normed=True)
# #plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *  np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
# plt.show()

# count, bins, _ = plt.hist(data_pareto, 100, normed=True)
# fit = a*m**a / bins**(a+1)
# plt.plot(bins, max(count)*fit/max(fit), linewidth=2, color='r')
# plt.show()



# TODO: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.anderson.html#scipy.stats.anderson

if __name__ == "__main__":
#    noisy_normal(0, 0.2)
    shapiro_study(0, 0.2, 50, 100)

   
