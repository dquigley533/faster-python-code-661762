"""memory_profiler example"""

@profile
def sum_of_diffs(vals):
    """Compute sum of diffs"""

    total = 0

    for i in range(1,len(vals)):
        total += vals[i] - vals[i-1]

    return total


if __name__ == '__main__':
    vals = list(range(1, 1_000_000, 3))
    print(sum_of_diffs(vals))
