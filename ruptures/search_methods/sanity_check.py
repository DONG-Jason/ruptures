from math import ceil
import numpy as np


def sanity_check(n_samples, n_regimes, jump, min_size):
    """
    Check if a partition if possible given the parameters.

    Args:
        n_samples (int): number of point in the signal
        n_regimes (int): number of segments
        jump (int): the start index of each regime can only be a multiple of
            "jump" (and the end index = -1 modulo "jump").
        min_size (int): the minimum size of a segment.

    Returns:
        bool: True if there exists a potential configuration of
            breakpoints for the given parameters. False if it does not.
    """
    assert isinstance(
        n_regimes, (int, np.integer)), "n_regimes: {} (type {})".format(
        n_regimes, type(n_regimes))
    assert isinstance(n_samples, int)
    assert isinstance(jump, int)
    assert isinstance(min_size, int)

    q = int(n_samples / jump)  # number of possible breakpoints

    # Are there enough points for the given number of regimes?
    if n_regimes > q + 1:
        return False
    if (n_regimes - 1) * ceil(min_size / jump) * jump + min_size > n_samples:
        return False
    return True
