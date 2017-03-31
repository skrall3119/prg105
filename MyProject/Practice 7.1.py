def average(lst):  # find average of list and return it
    ave = 0  # variable to store average
    for count in range(len(lst)):
        ave += lst[count]
    ave /= len(lst)
    return ave


def total_rainfall(lst):  # find total rain fall of list and return it trf=total rain fall
    trf = 0  # variable to store total
    for count in range(len(lst)):
        trf += lst[count]
    return trf


def highest(list):  # hihgest number of rain fall of list and return it
    high=0  # variable to store highest
    for i in range(len(list)):
        if list[i]>high:
            high=list[i]
    return highest


def lowest(list):  # lowest number of rain fall of list and return it
    low=list[1]  # variable to store lowest
    for i in range(len(list)):
        if list[i]<low:
            low = list [i]
    return lowest

rainfall = []  # stores each months rainfall amount

for i in range(12):
     rainfall.append(int(input("How much rainfall for month %d?"%(i+1))))

print("the total rain fall is", total_rainfall(rainfall))
print("the average rain fall is", average(rainfall))
print("the highest number of  rain fall is", highest(rainfall))
print("the lowest number of rain fall is", lowest(rainfall))
