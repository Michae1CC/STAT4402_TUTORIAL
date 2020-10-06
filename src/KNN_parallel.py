import queue
import threading

import numpy as np
from sklearn import datasets
from random import shuffle


def slave_KNN(dataset_partition, k, x_unknown, global_queue):
    """
    Finds the kth closest examples from the given partition for the unknown 
    example.

    Parameters:
        dataset_partition:
            A partition of the data set to search for the closest examples.

        k:
            The number of closest examples to return.

        x_unknown:
            The feature vector we would like the find the closest 
            examples to.

        global_queue:
            A queue to push the result of our slave process.
    """

    def sample_dist(samp): return np.linalg.norm(samp[0] - x_unknown[0])

    sorted_partition = sorted(dataset_partition, key=sample_dist)

    # Get the kth closest feature vectors from the partition sorted by distance
    # from x_unknown
    k_closest = sorted_partition[:k]

    # Push our local closest classes onto the global queue to be retrieve by the
    # master process
    global_queue.put([int(element[1]) for element in k_closest])

    return


def parallel_KNN(data, x_unknown, threads, k=5):
    """
    Computes the sum of a given array in parallel.

    Parameters:
        array:
            Data (with classes) to train on.

        x_unknown:
            The feature vector we would like the find the closest 
            examples to.

        threads:
            The number of thread to use.

        k:
            The number of closest neighbors to make classifications.

    Returns:
        A prediction label for x_unknown.
    """

    # Split the array into t equal partitions, where t is the number of threads
    partitions = np.array_split(data, threads)

    # Keep a reference to the threads we've spawned
    thread_refs = []

    # The results for each thread need to be put on a global queue since we
    # can't retrieve from join with using higher level threading API
    global_queue = queue.Queue()

    # Keep a list of all the samples that closest globally
    global_closest = []

    for partition in partitions:

        new_thread = threading.Thread(
            target=slave_KNN, args=(partition, k, x_unknown, global_queue))
        thread_refs.append(new_thread)

        # Get that new thread to work!
        new_thread.start()

    for thread_ref in thread_refs:

        # Wait for each thread to finish
        thread_ref.join()
        local_thread_closest = global_queue.get()

        # Add the local thread sum to our global sum
        global_closest += list(local_thread_closest)

    # Get the most often occuring class from global_closest
    prediction = max(set(global_closest), key=global_closest.count)

    return prediction


def main():
    med_data = datasets.load_iris()

    # Zip feature vectors and classes together
    zipped_med = list(zip(med_data.data, med_data.target))
    shuffle(zipped_med)

    train = zipped_med[:-10]

    # Leave the last 10 values for training
    test = zipped_med[-10:]

    for x, y in test:
        prediction = parallel_KNN(train, x, 4)
        print("predicted ", prediction, " actual ", y)


if __name__ == '__main__':
    main()
