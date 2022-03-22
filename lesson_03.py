# # --- if - elif -else -----
# a = 40
# b = 10
# if a < b:
#     print("b ig greater than a")
# elif a == b:
#     print("a is equal b")
# else:
#     print("a is greater than b")

## ---- operators AND and OR -----
# a = 7
# b = 9
# c = 10
# if (a < b) and (b < c):
#     print("Both condidtions are True")
# print("-----")
# a = 10
# b = 9
# c = 0
# if (a < b) or (b < c):
#     print("At least one condidtion is True")

# # ----- query in query -----
# a = 7
# b = 11
# c = 10
# if a < b:
#     if b < c:
#         print("Both condidtions are True")
#     else:
#         print("At least one condidtion is True")

#3 ----- loop FOR ------
# for x in range(6):
#     print(x)
# print("-----")
# for x in range(6):
#     print(x + 3)
# print("-----")
# for x in range(6, 12):
#     print(x)
# print("-----")
# for x in range(6, 12, 3):
#     print(x)
# print("-----")
y = 100
for x in range(1, 5):
    y += 1
    print(x, y)
print("-----")
y = 100
for x in range(3):
    if x == 2:
        print(x, y)
    y += 1
