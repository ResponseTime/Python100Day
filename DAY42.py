arr = [12, 32, 43, 54, 65, 776]

for i, k in enumerate(arr, start=1):
    if i % 2 == 0:
        print(f"arr[{i}] = {k} even")
        continue
    print(f"arr[{i}] = {k}")
