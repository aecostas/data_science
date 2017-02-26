

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
            valuesForTrial += np.random.uniform(low=-1, high=1, size=samples)
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


