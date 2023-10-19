def Collatzify(num):
    if num % 2 == 0:
        return num/2
    else:
        return (3*num) + 1

best_num = 1
best_Collatz_chain = 1

for x in range(1, 1000000):
    result = x
    result_Collatz_chain = 1
    while result != 1:
        result = Collatzify(result)
        result_Collatz_chain += 1
    if result_Collatz_chain > best_Collatz_chain:
        best_num = x
        best_Collatz_chain = result_Collatz_chain
        print("Best known seed updated:", best_num)
        print("Chain Length:", best_Collatz_chain)
        print()

print("The best Collatz chain seed under 1M is", best_num)
print("with a chain length of", best_Collatz_chain)
