data = [1,2,3,4]
other_data = [1,2]

intersection = []

for element in data:
    if element in other_data:
        intersection.append(element)


print(intersection)

data = {1,2,3,4}
other_data = {1,2}

print(data.intersection(other_data))