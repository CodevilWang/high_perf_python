#/usr/bin/env python
import numpy as np
from multiprocessing import Pool
import time
def estimate_nbr_points_in_quarter_circle(nbr_samples):
    np.random.seed()
    xs = np.random.uniform(0, 1, nbr_samples)
    ys = np.random.uniform(0, 1, nbr_samples)
    estimate_inside_quarter_unit_circle = (xs * xs + ys * ys) <= 1
    nbr_trials_in_quarter_unit_circle = np.sum(estimate_inside_quarter_unit_circle)
    return nbr_trials_in_quarter_unit_circle

if __name__ == "__main__":
    nbr_samples_in_total = 1e8
    nbr_parallel_blocks = 4
    pool = Pool(processes = nbr_parallel_blocks)
    nbr_samples_per_worker = nbr_samples_in_total / nbr_parallel_blocks
    print "Making {} samples per worker".format(nbr_samples_per_worker)
    nbr_trials_per_prcess = [nbr_samples_per_worker] * nbr_parallel_blocks
    t1 = time.time()
    nbr_in_unit_circles = pool.map(estimate_nbr_points_in_quarter_circle, nbr_trials_per_prcess)
    pi_estimate = sum(nbr_in_unit_circles) * 4 / nbr_samples_in_total
    print "Estimated pi", pi_estimate
    print "Delta:", time.time() - t1
