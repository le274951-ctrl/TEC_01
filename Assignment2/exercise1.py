length = float(input("Enter length of a zander in centimeters:"))
def check_zander(length):
    if length < 42:
        different = 42 - length
        print("Release the fish back into the lake")
        print(f"The zander was {different} below the size limit.")
    else:
        print("You can keep the fish.")
check_zander(length)


# def check_zander():
#     length = float(input("Enter the length of the zander in centimeters: "))

#     if length < 42:
#         difference = 42 - length
#         print("Release the fish back into the lake.")
#         print(f"The fish was {difference:.1f} cm below the size limit.")
#     else:
#         print("The zander meets the size limit. You can keep the fish.")


# check_zander()