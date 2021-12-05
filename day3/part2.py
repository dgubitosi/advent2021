
measurements = list()
with open('input.txt') as f:
    for line in f:
        measurements.append(line.strip())

# find o2 rating using most common value or 1
pos = 0
values = measurements.copy()
while len(values) > 1:
    # separate list based off value of current position
    group = [ list(), list() ]
    for v in values:
        group[int(v[pos])].append(v)
    pos += 1
    print(pos, len(values), len(group[0]), len(group[1]))
    values.clear()
    if len(group[1]) >= len(group[0]):
        values = group[1].copy()
    else:
        values = group[0].copy()

print(values)
o2 = int(values[0], 2)

# find co2 rating using least common value or 0
pos = 0
values = measurements.copy()
while len(values) > 1:
    # separate list based off value of current position
    group = [ list(), list() ]
    for v in values:
        group[int(v[pos])].append(v)
    pos += 1
    print(pos, len(values), len(group[0]), len(group[1]))
    values.clear()
    if len(group[0]) <= len(group[1]):
        values = group[0].copy()
    else:
        values = group[1].copy()

print(values)
co2 = int(values[0], 2)

print(f"O2 generator rating = {o2}")
print(f"CO2 scrubber rating = {co2}")
print(f"Life support rating = {o2 * co2}")
