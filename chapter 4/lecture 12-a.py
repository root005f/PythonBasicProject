specs = {"DS&AI": 4, "CS": 2, "SE": 3, "IS": 2}

"""for k in specs.values(): # we use .value to select the values in the specs like DS&AI...
    print(k,specs[k])"""

"""for v in specs.values():
    print(v)

for k in specs.keys(): # we use .keys to select the keys in the specs like 4,2,3,...
    print(k)"""

for k, v in specs.items():  # we use .item to select the keys and values in the specs like DS&AI 4,...
    print(k, v)

dept_counts = list(specs.values())
print(dept_counts)

depts = list(specs.keys())
print(depts)
