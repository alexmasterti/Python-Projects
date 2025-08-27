d1 = {'name':'sarah', 'class':'night', 'age':3}
thekeys = list(d1.keys())
print(thekeys)
thekeys.sort()
for key in thekeys:
    print(key, d1[key])
