#Number of dates between two given dates.
start_date = (2014, 7, 2)
end_date = (2014, 7, 11)
difference = end_date[-1] - start_date[-1]
print("The difference between the two given dates is: " + str(difference) + " Days")

#given solution
'''from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)'''