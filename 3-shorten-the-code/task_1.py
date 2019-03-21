values = [None, 0, -1, 0, False, True, 5, 0, False, 255]

new_values = []
zero_values = []

for value in values:
    if not isinstance(value, bool) and value != 0:
        new_values.append(value)
    else:
        zero_values.append(value)

new_values.extend(zero_values)

print(new_values)
