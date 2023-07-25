change_list = []
import csv
csvfile= "Resources/budget_data.csv"
with open(csvfile) as data:
    reader = csv.reader(data)
    header = next(reader)
    counter=1
    change = 0
    first_row=next(reader)
    total = int(first_row[1])
    average_change = 0
    prev_net=int(first_row[1])
    greatest_increase=["",0]
    greatest_decrease=["",0]
    for row in reader:
        counter=counter +1
        total = total + int(row[1])
        change = int(row[1])-prev_net
        prev_net=int(row[1])
        change_list.append(change)
        if change>greatest_increase[1]:
            greatest_increase[1]=change
            greatest_increase[0]=row[0]
        if change<greatest_decrease[1]:
           greatest_decrease[1]=change
           greatest_decrease[0]=row[0]
    average_change=sum(change_list)/len(change_list)
print(counter)
print(total)
print(change_list)
print(average_change)
print(greatest_increase)
print(greatest_decrease)