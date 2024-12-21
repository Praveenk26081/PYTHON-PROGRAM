list1 = list(map(int, input("Enter list1 elements separated by space: ").split()))
list2 = list(map(int, input("Enter list2 elements separated by space: ").split()))

merged_list = []
while list1 and list2:
    if list1[0] < list2[0]:
        merged_list.append(list1.pop(0))
    else:
        merged_list.append(list2.pop(0))

merged_list.extend(list1)
merged_list.extend(list2)

print("Merged List:", merged_list)
