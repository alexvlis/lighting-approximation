import numpy as np
import matplotlib.pyplot as plt

N = 100
mu = [15, 5]
sigmas = [[[20, 0], [0, 10]], [[20, 14], [14, 10]], [[20, -14], [-14, 10]]]

for sigma in sigmas:
    samples = np.random.multivariate_normal(mu, sigma, size=N)

    mu_mle = 1/N * np.sum(samples, axis=(0))
    sigma_mle = 1/N * np.dot((samples - mu).T, (samples - mu))
    print("mu: ", mu_mle)
    print("sigma: ", sigma_mle)

    plt.scatter(samples[:, 0], samples[:, 1])
    plt.show()
