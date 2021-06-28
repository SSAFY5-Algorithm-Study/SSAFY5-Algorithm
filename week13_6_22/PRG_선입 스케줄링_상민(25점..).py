def solution(n, cores):
    original_cores = cores.copy()
    cores_length = len(cores)
    last_core = 0
    if n > cores_length:
        n -= cores_length
    while n > 0:
        for core_idx in range(cores_length):
            cores[core_idx] -= 1
            if cores[core_idx] == 0:
                n -= 1
                last_core = core_idx
                cores[core_idx] = original_cores[core_idx]
    return last_core + 1