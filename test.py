l = []

for i in range(5):
    if i == 4:
        l.append(False)
    else:
        l.append(True)
    
print(l)
print(all(l))