def euclidean_algo(a,b):
  while b!=0:
    remainder = a % b
    print(f"{a} = {a//b}*{b} + {remainder})
    a = b
    b = remainder
  return a

a = 120
b = 25
print("The Euclidean algorithm using division:\n")
print(f"The GCD of {a} and {b} is: {euclidean_algorithm(a, b)}")

# output : 
# 120=4*25 + 20
# 25=1*20 + 5
# 20=4*5 + 0
# The GCD of 120 and 25 is: 5
