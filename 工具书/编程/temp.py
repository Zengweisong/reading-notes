# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# b = [a[x][:] for x in a]

D1 = {'a': 1, 'b': 3}
D2 = {'a': 1, 'b': 3}
print(sorted(D1.items()) < sorted(D2.items()))  # False
