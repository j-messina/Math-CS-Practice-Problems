import sys
sys.path.append('/Users/johnmessina/Documents/GitHub/Math-CS-Practice-Problems/Math-CS-Practice-Problems/')
from Algorithms.RemovePrintPath import *
RemovePrintPath()

from Algorithms.isPrime import *

# Starting Step: Set default value for coefficients A and B

# Middle Step: Given A and B, run through quadratic expression
#              and count consecutive primes
#   - stop on non-prime found
#   - store best performing A and B, update on better found
#       - store A, B, and consec prime count

# End step: Output product of coefficients A and B
 
def QuadraticFormula(n, a, b):
    return (n**2) + (a * n) + b

def Run_Ns(a, b):
    consecutive_primes_count = 0
    n = 0
    while isPrime(QuadraticFormula(n, a, b)):
        consecutive_primes_count+=1
        n+=1
    return consecutive_primes_count
    
best_a = 0
best_b = 0
best_primes_count = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        # print("Trying", a, "and", b)
        candidate_primes_count = Run_Ns(a,b)
        if candidate_primes_count > best_primes_count:
            best_primes_count = candidate_primes_count
            best_a = a
            best_b = b
            print("New best a,b:", best_a,best_b, "with", best_primes_count, "primes!")

print("Best coefficients products", best_a, "*", best_b, "=", best_a*best_b)