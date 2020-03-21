import csv
khan_vote=[]
correy_vote=[]
li_vote=[]
tool_vote=[]
vote1=0.000

with open('election_data.csv','r') as csvfile:
    elec_reader=csv.reader(csvfile)
    elec_header=next(elec_reader)
    #print(elec_header)
    
    candidates=[]
    for row in elec_reader:
        lines=elec_reader.line_num
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2]=='Khan':
            khan_vote.append(row[0])
        elif row[2]=='Correy':
            correy_vote.append(row[0])
        elif row[2]=='Li':
            li_vote.append(row[0])
        else:
            tool_vote.append(row[0])

    vote1=(len(khan_vote)/(lines-1))*100
    vote2=(len(correy_vote)/(lines-1))*100
    vote3=(len(li_vote)/(lines-1))*100.00
    vote4=(len(tool_vote)/(lines-1))*100.00
       
    print("Election Results")
    print("----------------------")
    print(f"Total Votes:{lines-1}")
    print(f"Complete list of candidates:{candidates}")
    print("----------------------")
    print(f"Percentage of Votes-Khan: {vote1}%")
    print(f"Percentage of Votes-Correy: {vote2}%")
    print(f"Percentage of Votes-Li: {vote3}%")
    print(f"Percentage of Votes-O'Tooley: {vote4}%")
    print("-----------------------")

    if (vote1>vote2) and (vote1>vote3) and (vote1>vote4):
        print("Winner: Khan")
    elif (vote2>vote1) and (vote2>vote3) and (vote2>vote3):
        print("Winner: Correy")
    elif (vote3>vote1) and (vote2<vote3) and (vote4<vote3):
        print("Winner: Li")
    else:
        print("Winner: O'Tooley")
    print("-----------------------")