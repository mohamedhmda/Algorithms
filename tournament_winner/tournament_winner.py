def most_frequent(array):
    return max(set(array), key = array.count)

def tournament_winner(competitions, results):
    table = []
    for n in range(len(competitions)):
        if results[n] == 1:
            table.append(competitions[n][0])
        elif results[n] == 0:
            table.append(competitions[n][1])

    return most_frequent(table)

