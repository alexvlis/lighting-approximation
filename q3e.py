from q3d import posterior_likelihood_estimate
import numpy as np

def tikhonov():
    pass

if __name__ == "__main__":
    for N in np.arange(5, 200, 5):
        z = np.random.normal(0, 1, size=(N))
        X = np.random.normal(0, 5, size=(2, N))

        w_star = np.array([1, 1])

        y_star = np.dot(w_star.T, X)
        y = np.dot(w_star.T, X) + z

        w0, mle = posterior_likelihood_estimate(np.cov(X), N, 20)

        alpha = 0.1
        gamma = alpha * np.identity(2)
        Q = np.dot(gamma.T, gamma)
        P = np.cov(y)
        w = np.dot(np.linalg.inv(np.dot(X.T, np.dot(P, X.T).T) + Q),
                    np.dot(X.T, np.dot(P, y)) + np.dot(Q, w0))
