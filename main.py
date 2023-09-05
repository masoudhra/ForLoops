# shopping_list = ["milk", "bread", "flower"]
# for item in shopping_list:
#     print(item)


# text = "Hello how are you"
# count = 0
# for item in text:
#     if item == "a":
#         count += 1
#
# print(count)

# tabe range az 0 ta oon addad ro dar nazar migire
# ba 2 voroodi az hamoon adad ta yeki ghabl az adade dovom ro dar nazar migire
# for i in range(2, 6):
#     print(i)
#ba 3 voriddi voroodie aval ta voroodie dovom ba tedad ghadame voroodie 3
# for i in range(1, 10, 2):
#     print(i)

def compute_power(base, power):
    result = 1
    for i in range(power):
        result = result * base
    return result

base = int(input("Please inset the base: "))
power = int(input("Please inset the power: "))
print(compute_power(base, power))


