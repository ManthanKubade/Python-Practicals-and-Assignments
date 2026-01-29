num = 1
for i in range(1, 5):
    for j in range(1, i + 1):
        print(f"{num:2}", end=" ")
        num += 1
    print()
