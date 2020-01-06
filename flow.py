# def cuboid_difference():
#     a = []
#     b = []
#     try:
#         print("Enter the dimensions of the first cuboid:")
#         for i in range(3):
#             num = int(input())
#             a.append(num)
#         print("Enter the dimension for the second cuboid")
#         for j in range(3):
#             new = int(input(""))
#             b.append(new)
#     except ValueError as e:
#         print("Dimension cannot be less than or equal to zero",e)
#     else:
#         vol1 = 1
#         vol2 = 1
#         for i in range(len(a)):
#             vol1 *= a[i]
#             vol2 *= a[i]
#         difference = vol1 - vol2
#         print("The difference of the cuboids is ",difference)
#
# print(cuboid_difference())

def create_list(filename):
    file = open(filename,"r")
    result = []
    for lines in file.read():
        result.append(lines)
    word = "".join(result)
    new = word.split(" ")
    my_list = []
    for i in new:
        if i.isdecimal():
            my_list.append(int(i))
    return my_list



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j > 0  and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key

def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
        if i % 50 == 0:
            print()

algo1 = create_list("random21.txt")
algo2 = create_list("random22.txt")
algo3 = create_list("random23.txt")
algo4 = create_list("random24.txt")

def counting_sort(arr,place):
    size = len(arr)
    count = [0] * 10
    output = [0] * size

    for i in range(size):
        index = arr[i] // place
        count[index%10] += 1

    for i in range(1,10):
        count[i] += count[i-1]

    i = size - 1
    while i > 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index%10] -= 1
        i -= 1

    for i in range(size):
        arr[i] = output[i]


def radix_sort(arr):
    max_element = max(arr)
    place = 1
    while max_element // place > 0:
        counting_sort(arr,place)
        place *= 10

radix_sort(algo4)
print(algo4)