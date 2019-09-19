import os
import csv
count = 0
max = 0
sum=0
can = []
count_l=[]
percent=[]
csvpath = os.path.join('election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        can.append(row[2])
del can[0]
for row in can:
    count += 1
#print(count)
uniq_l = list(dict.fromkeys(can)) 
for candid in uniq_l:
    count_l.append(can.count(candid))
#list comprehension
percent=[(100/count)*x for x in count_l]
#print(percent)
#print(count_l)            
#print(uniq_l)
for i in count_l:
    sum += i
    if i > max:
        max = i
#print(winner)
#print(uniq_l[count_l.index(max)])

#print(sum)
print("""Election Results
-------------------------
Total Votes: {}
-------------------------
{}: {}% ({})
{}: {}% ({})
{}: {}% ({})
{}: {}% ({})
-------------------------
Winner: {}
-------------------------
""".format((sum), uniq_l[0], round(percent[0], 4), count_l[0],
           uniq_l[1], round(percent[1], 4), count_l[1],
           uniq_l[2], round(percent[2], 4), count_l[2],
           uniq_l[3], round(percent[3], 4), count_l[3],
           uniq_l[count_l.index(max)]))