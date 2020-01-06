# from datetime import date
#
# def main():
#
#     born_before = date(2000,7,20)
#     _date = promptandextractdate()
#     while _date is not None:
#         if _date <= born_before:
#             print("is at least 21 years of age.")
#         _date = promptandextractdate()
#
#
# def promptandextractdate():
#     month = int(input("month(0 to quit): "))
#     if month == 0:
#         return None
#     else:
#         day = int(input("day: "))
#         year = int(input("year: "))
#         return date(year,month,day)
#
# print(main())
# print(promptandextractdate())
