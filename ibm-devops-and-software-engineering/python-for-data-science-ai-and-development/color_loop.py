color = ["orange", "orange", "purple", "orange", "skyblue"]
orange_list = []

print(f'Length: {len(color)}')

# for color in color:
#     if color == "orange":
#         orange_list.append(color)
#     else:
#         continue
#
# print(orange_list)

# while True:
#     for color in color:
#         if color == 'orange':
#             orange_list.append(color)
#         else:
#             continue
#     break
#
# print(orange_list)

i = 0
while i < len(color) and color[i] == "orange":
    orange_list.append(color[i])
    i += 1

print(orange_list)
