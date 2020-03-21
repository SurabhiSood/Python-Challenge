import csv
TotalKhan=0
TotalCorrey=0
TotalLi=0
TotalO=0

with open('election_data.csv','r') as csvfile:
    elec_reader=csv.reader(csvfile)
    elec_header=next(elec_reader)
    print(elec_header)
    
    for row in elec_reader:
        lines=elec_reader.line_num
            

    print("Election Results")
    print("----------------------")
    print(f"Total Votes:{lines-1}")
    print("----------------------")