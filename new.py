# def draw_line(tick_length,tick_label=""):
#     line = "-" * tick_length
#     if tick_label:
#         line += " " + tick_label
#     print(line)
#
# def draw_interval(center_length):
#     if center_length > 0:
#         draw_interval(center_length -1)
#         draw_line(center_length)
#         draw_interval(center_length -1)
#
# def draw_ruler(num_inches,major_length):
#     draw_line(major_length, "0")
#     for j in range(1,1 + num_inches):
#         draw_interval(major_length - 1)
#         draw_line(major_length,str(j))
#
# draw_line(5)
# draw_interval(4)
# draw_ruler(4,5)

def binary_search(data,target,low,high):
    if low > high:
        return False
    else:
        sorted(data)
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data,target,low,mid-1)
        elif target > data[mid]:
            return binary_search(data,target,mid+1,high)
        else:
            return False

print(binary_search([2,3,4,5,6,7,8,9],4,2,9))