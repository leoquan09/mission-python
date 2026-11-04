def larger_than_n(l, n):
    larger = []
    for i in l:
        if i > n:
            larger.append(str(i))
    return ", ".join(larger)

print(larger_than_n([1,23,4,5,6], 5))
