list1 = [
    {"positions": [0, 5], "values": ["a"]},
    {"positions": [4, 9], "values": ["b"]}
]

list2 = [
    {"positions": [1, 3], "values": ["x"]},
    {"positions": [6, 10], "values": ["y"]}
]

all_items = list1 + list2

def get_left_position(item):
    return item["positions"][0]

all_items.sort(key=get_left_position)

combined = {}

for i in range(len(all_items)):
    left = all_items[i]["positions"][0]
    values = all_items[i]["values"]

    if left in combined:
        combined[left] += values
    else:
        combined[left] = values

print(combined)
