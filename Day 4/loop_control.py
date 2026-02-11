#break → Loop immediately stops
for i in range(1, 6):
    if i == 3:
        break
    print(i)

#continue → Skip current iteration
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#pass → Placeholder (do nothing)
for i in range(1, 6):
    if i == 3:
        pass
    print(i)
