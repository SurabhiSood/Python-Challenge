import os
import csv

lines=0
Total=0

#reading the csv in the same folder
with open('budget_data.csv','r') as csvfile:
    
    bank_reader=csv.reader(csvfile)
    next(bank_reader)

#counting the columns
#creating new lists to calculate the average change    
    Val=[]  
    Val_month=[]   
    for row in bank_reader:
        lines=bank_reader.line_num
        Total=Total+int(row[1])
        Val.append(int(row[1]))
        Val_month.append(row[0])
    
    List2=[]
    myList=[]
    myList=Val.copy()
    myList.remove(867884)
    List2=myList.copy()
    
    Val_month.remove("Jan-2010")
    
    difference=[]
    zip_object = zip(Val, List2)
    for Val_i, List2_i in zip_object:
        difference.append(Val_i-List2_i)
    
    difference_sum=0
    for num in difference:
        difference_sum=difference_sum+num
    AverageChange=(difference_sum/85)
    
    #Zipping to lists
    #obtain greates increase in profits and 
    # decrease in loss
    
    def merge(list1, list2): 
        merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
        return merged_list 
      
    another_list=merge(difference, Val_month)
    answer=max(another_list)
    answer1=min(another_list)  


    #Financial Analysis Output
    print("-------------------\nFinancial Analysis\n-------------------")
    print(f"Total number of Months :{lines-1}")
    print(f"Total Amount of 'Profit/Losses': ${Total}")
    print(f"Average Change:${AverageChange}")
    print(f"Greatest Increase in Profits:{answer}")
    print(f"Greatest Decrease in Profits:{answer1}")

f=open('output.txt', 'w')
pass