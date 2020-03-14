n = int(input())
min_value = int(input())
diff = (-1) * min_value

for i in range(n - 1):
    rt = int(input())
    diff = max(diff, rt - min_value)
    min_value = min(rt, min_value)

print(diff)