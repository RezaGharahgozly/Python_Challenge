import os
import csv
csvpath = os.path.join('budget_data.csv')
type(csvpath)
ProfitLosses = []
Date=[]
diff=[]
count = 0
Sum = 0
Sum_dif=0
Max = 0
Min = 0
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        ProfitLosses.append(int(row[1]))
        Date.append(row[0])
for row in ProfitLosses:
    count += 1
    Sum += int(row)

diff = [j-i for i, j in zip(ProfitLosses[:-1], ProfitLosses[1:])]
diff.insert(0, ProfitLosses[0])
for row in diff:
    Sum_dif += int(row)
    if int(row) > Max:
        Max = int(row)
    elif int(row) < Min:
        Min = int(row)
        
#print(count)
#print(Sum)
#print((Sum_dif-diff[0])/(count-1))
#print(Max)
#print(Min)
#print(Date[diff.index(Max)])
#print(Date[diff.index(Min)])
print("""Financial Analysis
---------------------------------------
Total Months: {}
Total: ${}
Average  Change: ${}
Greatest Increase in Profits: {} (${})
Greatest Decrease in Profits: {} (${})
""".format(count, Sum,(Sum_dif-diff[0])/(count-1),Date[diff.index(Max)], Max, Date[diff.index(Min)], Min ))