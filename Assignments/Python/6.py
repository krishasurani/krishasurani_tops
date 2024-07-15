#  Write python program that swap two number with temp variable and without temp variable. 

# # With a temporary variable:
# swap_with_temp(a, b):
#     temp = a
#     a = b
#     b = temp
#     return a, b

# # Without a temporary variable:
# swap_without_temp(a, b):
#     a, b = b, a
#     return a, b



# Swapping with temp 
x = 5
y = 10

Create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping:', x)
print('The value of y after swapping:', y)

# swapping without temp

x = 5
y = 10

print('x =', x)
print('y =', y)
