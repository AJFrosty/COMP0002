InputList = [("2023-02-19", 500.0), ("2023-02-28", 700.0), ("2022-09-16", 33.40),
("2023-07-20", 3000.0), ("2023-02-01", 1300.0), ("2023-07-15", 1700.0),
("2022-07-05",189.70)]

def calculateMonthlyTotal(info: list, dates:list, index):
    cost = 0
    for j in range(len(info)):
        if dates[index] == info[j][0][:7]:
            cost += info[j][1]
    return cost

def monthleyRevenue(info: tuple):
    Dates = [x for x in range(len(info))]
    uniqueDates = []
    output = []
    for i in range(len(info)):
        string = info[i][0][:7]
        Dates[i] = string
    for item in Dates:
        if item not in uniqueDates:
            uniqueDates.append(item)
    for i in range(len(uniqueDates)):
        output.append((uniqueDates[i], calculateMonthlyTotal(info, uniqueDates, i)))
    return output

print(monthleyRevenue(InputList))