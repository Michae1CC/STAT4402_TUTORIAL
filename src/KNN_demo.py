import time
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets


def train_KNN_classifier(n_jobs=1):

    med_data = datasets.load_breast_cancer()

    clf = KNeighborsClassifier(
        n_neighbors=10, weights='uniform', n_jobs=n_jobs)

    # Use 4/5 of the data to train and 1/5 to test
    train_index = int(len(med_data.data) * (4/5))

    x_train = med_data.data[:train_index]
    y_train = med_data.target[:train_index]

    clf.fit(x_train, y_train)

    predictions = clf.predict(med_data.data[train_index:])
    # Get the number of correct predictions
    num_correct = sum(predictions == med_data.target[train_index:])

    print("Test accuracy: ", num_correct / len(predictions))

    return


def time_KNN():

    THREADS_USED = 1

    t0 = time.time()
    train_KNN_classifier(n_jobs=THREADS_USED)
    elapsed = time.time() - t0

    print(f"Time using {THREADS_USED} thread: ", elapsed)


def main():
    time_KNN()


if __name__ == '__main__':
    main()
