# Receive an integer input
# Instantiate a variable "maximum_int" with a value of the input which will keep track of the greatest number
#
# While the input is greater or equal to 0
#
#   If the input is greater than maximum_int
#     Make the input the new maximum_int
#
# Print out the maximum_int variable


num_int = int(input("Input a number: "))    # Do not change this line
maximum_int = num_int

# Fill in the missing code

while num_int >= 0:
  if num_int > maximum_int:
    maximum_int = num_int
  
  num_int = int(input("Input a number: "))

print("The maximum is", maximum_int)    # Do not change this line
