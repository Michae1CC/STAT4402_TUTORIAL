#!/usr/bin/env python3

__author__ = 'Michael Ciccotosto-Camp'

import threading
import queue
import numpy as np


def slave_sum(array, global_queue):
    """
    Computes the sum of a given array.

    Parameters:
        array:
            A numpy array to sum over.

        global_queue:
            A queue to push the result of our slave process.

    Returns:
        The local sum of the input array.
    """

    # Compute the local sum for this thread
    local_sum = np.sum(array)

    # Push our local sum onto the global queue to be retrieve by the
    # master process
    global_queue.put(local_sum)

    return


def parallel_array_sum(array, threads):
    """
    Computes the sum of a given array in parallel.

    Parameters:
        Parameters:
            array:
                A numpy array to sum over.

            threads:
                The number of thread to use.

    Returns:
        The sum of the array elements.
    """

    # Split the array into t equal partitions, where t is the number of threads
    partitions = np.array_split(array, threads)

    # Keep a reference to the threads we've spawned
    thread_refs = []

    # The results for each thread need to be put on a global queue since we
    # can't retrieve from join with using higher level threading API
    global_queue = queue.Queue()

    # Create a global sum to store
    global_sum = 0

    for partition in partitions:

        new_thread = threading.Thread(
            target=slave_sum, args=(partition, global_queue))
        thread_refs.append(new_thread)

        # Get that new thread to work!
        new_thread.start()

    for thread_ref in thread_refs:

        # Wait to each thread to finish and collect their result using join
        thread_ref.join()
        local_thread_sum = global_queue.get()

        # Add the local thread sum to our global sum
        global_sum += local_thread_sum

    return global_sum


def main():

    # Create a randomly generated vector of length 10000
    array_to_sum = np.random.rand(10000)

    array_sum = parallel_array_sum(array_to_sum, 4)

    print("Array sum is: ", array_sum)


if __name__ == '__main__':
    main()
