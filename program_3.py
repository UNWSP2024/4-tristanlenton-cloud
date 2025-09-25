years = int(input("Enter the number of years: "))
rainfall = 0
for year in range(years):
    print("Year", year)
    for month in range(1, 13):
        print("Month", month)
        rainfall += float(input("Enter total rainfall in inches for this month: "))
months = years * 12
print("Total number of months is ", months)
print("Total rainfall is ", rainfall, "inches")
print("Average rainfall per month is", rainfall/months, "inches")