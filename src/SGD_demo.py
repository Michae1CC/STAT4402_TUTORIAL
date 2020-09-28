#!/usr/bin/env python3

__author__ = 'Michael Ciccotosto-Camp'
__version__ = ''

import argparse
import time

import numpy as np
from sklearn import datasets
from sklearn.linear_model import SGDClassifier


def train_SGD_classifier(n_jobs=1):

    digits = datasets.load_digits()

    clf = SGDClassifier(loss="hinge", penalty="l2",
                        max_iter=100, n_jobs=n_jobs)

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


def time_SGD(num_threads):

    t0 = time.time()
    train_SGD_classifier(n_jobs=1)
    elapsed = time.time() - t0

    print("Time using 1 thread: ", elapsed)


def main():
    parser = argparse.ArgumentParser(
        description="Trains a SGD classifier a subset of the MNIST digits data.")

    parser.add_argument('-t', '--num_threads', type=int, default=1,
                        help='The number of threads to be used in the training process.')
    args = parser.parse_args()

    time_SGD(args.num_threads)


if __name__ == '__main__':
    main()
