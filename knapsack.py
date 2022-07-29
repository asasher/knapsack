from functools import cache
from random import randint
import csv
import sys

def knapsack(items, weights, capacity, limit):
    @cache
    def _knapsack(i, capacity, limit):
        if i < 0 or limit <= 0:
            return 0, []
        
        item, weight = items[i], weights[i]

        if weight > capacity:
            return _knapsack(i - 1, capacity, limit)

        return max(
            _knapsack(i - 1, capacity, limit),
            tuple([a + b for a, b in zip(_knapsack(i - 1, capacity - weight, limit - 1), (weight, [item]))])
        )
    return _knapsack(len(items) - 1, capacity, limit)

def read_citi_transactions(filename):
    '''
    Read a csv file with transactions and return as a list of lists.
    '''

    transactions = []
    points = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            transactions.append(row[0].strip())
            points.append(int(row[1].strip()))
    
    return transactions, points

if __name__ == '__main__':
    capacity = int(sys.argv[1])
    transactions, points = read_citi_transactions('./transactions.csv')
    weight, items = knapsack(transactions, points, capacity, 4)
    print(weight, capacity, capacity - weight)
    for item in items:
        print(item)