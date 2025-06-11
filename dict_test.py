import uuid

generate_uid = uuid.uuid4()
test_dict = {}

action1 = input("Please give one action")
test_dict[str(uuid.uuid4())] = action1

action2 = input("Please give one action")
test_dict[str(uuid.uuid4())] = action2

action3 = input("Please give one action")
test_dict[str(uuid.uuid4())] = action3

action4 = input("Please give one action")
test_dict[str(uuid.uuid4())] = action4

dictm = []

for x in len(test_dict.items()):
    dictm.append(list(test_dict.items()[x][1]))
    
print(dictm)
print(test_dict)
