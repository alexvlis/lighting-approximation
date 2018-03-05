import numpy as np
import matplotlib.pyplot as plt

def posterior_likelihood_estimate(sigma, n, r, plot=False):
    z = np.random.normal(0, 1, size=(n))
    x = np.random.normal(0, 5, size=(2, n))

    densities = np.zeros((2*r,2*r))
    contour_levels = np.arange(100, 1000, 50)
    w = np.array([1, 1])
    y = np.dot(w.T, x) + z

    min_estimate = 10000000
    for w1 in np.arange(-r, r):
        for w2 in np.arange(-r, r):
            w = np.array([w1, w2])
            p = w.T - np.dot(np.dot(y, x.T), np.linalg.inv(np.dot(x, x.T) -
                                                        np.linalg.inv(sigma)))
            posterior = np.dot(p, p.T)

            if posterior < min_estimate:
                min_estimate = posterior
                mle = (w, min_estimate)

            densities[w1+r, w2+r] = posterior

    if plot:
        plt.contour(np.arange(-r, r), np.arange(-r, r), densities, contour_levels)
        plt.xlabel("w1")
        plt.ylabel("w2")
        plt.title("Posterior Likelihood Distribution")
        plt.show()

    return mle

if __name__ == "__main__":
    N = [5, 50, 500]
    sigmas = [[[1, 0], [0, 1]], [[1, 0.25], [0.25, 1]], [[1, 0.9], [0.9, 1]],
    [[1, -0.25], [-0.25, 1]], [[1, -0.9], [-0.9, 1]], [[0.1, 0], [0, 0.1]]]

    for n in N:
        for sigma in sigmas:
            mle = posterior_likelihood_estimate(sigma, n, 20, plot=True)
            print(mle)
