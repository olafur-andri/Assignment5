# Input an integer "n"
# Instantiate the integer "a1 = 1", "a2 = 2" and "a3 = 3" which will be tracking changes in the sequence
# Instantiate the integer "sum_int = 0" which will be the sum of a1, a2 and a3
#
# Print out a1
# Print out a2
# Print out a3
#
# for loop from 0 to (n - 4)
#   Make the sum_int equal to a1 + a2 + a3
#   Make a1 = a2
#   Make a2 = a3
#   Make a3 = sum_int
#   Print out sum_int

n = int(input("Enter the length of the sequence: ")) # Do not change this line
a1 = 1
a2 = 2
a3 = 3
sum_int = 0

print(a1)
print(a2)
print(a3)

for i in range(n - 3):
  sum_int = a1 + a2 + a3
  a1 = a2
  a2 = a3
  a3 = sum_int
  print(sum_int)