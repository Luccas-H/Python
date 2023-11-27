number_den = 1 
number = 4
signal_change = -1
number_den += 2 
operation = number + signal_change*4/number_den

while abs(operation-number) > 0.000005:
    number = operation
    number_den += 2 
    signal_change = signal_change*(-1)
    operation = number + signal_change*4/number_den
print(f"Pi value is {operation}")