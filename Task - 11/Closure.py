def lead_counter():
    count = 0
    def add():
        nonlocal count
        count += 1
        return count
    return add


counter = lead_counter()

print(counter())
print(counter())
print(counter())