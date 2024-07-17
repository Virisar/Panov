numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
result = []

i = 0
while i < len(numbers) and numbers[i] >= 0:
    if numbers[i] != 0:
        result.append(numbers[i])
    else:
        i += 1
        continue
    i += 1

print(result)

