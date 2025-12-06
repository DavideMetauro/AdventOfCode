with open("input_day6.txt") as file:
    lines = file.readlines()

columns = []
for l in lines:
    numbers = [tok for tok in l.split() if tok.strip().isdigit()]
    for i, num in enumerate(numbers):
        if i >= len(columns):
            columns.append([])
        columns[i].append(int(num))

operands = []
for op in lines[-1].split():
    operands.append(op)

count=0
for col, op in zip(columns, operands):
    if op == '+':
        result = sum(col)
    elif op == '*':
        result = 1
        for n in col:
            result *= n
    count += result
print(count)