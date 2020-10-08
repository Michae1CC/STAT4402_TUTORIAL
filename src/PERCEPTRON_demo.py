import time
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn import datasets


def train_perceptron_classifier(n_jobs=1):

    digits = datasets.load_digits()

    clf = Perceptron(tol=1e-3, random_state=0, n_jobs=n_jobs)

    # Use 4/5 of the data to train and 1/5 to test
    train_index = int(len(digits.data) * (4/5))

    x_train = digits.data[:train_index]
    y_train = digits.target[:train_index]

    clf.fit(x_train, y_train)

    predictions = clf.predict(digits.data[train_index:])
    # Get the number of correct predictions
    num_correct = sum(predictions == digits.target[train_index:])

    print("Test accuracy: ", num_correct / len(predictions))

    return


def time_perceptron():

    THREADS_USED = 1

    t0 = time.time()
    train_perceptron_classifier(n_jobs=THREADS_USED)
    elapsed = time.time() - t0

    print(f"Time using {THREADS_USED} thread: ", elapsed)


def main():
    time_perceptron()


if __name__ == '__main__':
    main()
