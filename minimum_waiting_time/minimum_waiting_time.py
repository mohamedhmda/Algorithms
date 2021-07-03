def minimum_waiting_time(queries):
    queries.sort()
    MinimumWaitingTtime = 0

    for n in range(len(queries)):
        MinimumWaitingTtime += queries[n] * (len(queries)- n - 1)

    return MinimumWaitingTtime

