import csv

khan_vote=[]
correy_vote=[]
li_vote=[]
tool_vote=[]
list_again=[]

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

    vote_k=("{0:.3f}%".format(vote1))
    vote_c=("{0:.3f}%".format(vote2))
    vote_l=("{0:.3f}%".format(vote3))
    vote_t=("{0:.3f}%".format(vote4))

    vote_list=[len(khan_vote),len(correy_vote),len(li_vote),len(tool_vote)]
    #print(vote_list)
       
    print("Election Results")
    print("----------------------")
    print(f"Total Votes:{lines-1}")
    print(f"Complete list of candidates:{candidates}")
    print("----------------------")
    print(f"Percentage of Votes-Khan: {vote_k} ({len(khan_vote)})")
    print(f"Percentage of Votes-Correy: {vote_c} ({len(correy_vote)})")
    print(f"Percentage of Votes-Li: {vote_l} ({len(li_vote)})")
    print(f"Percentage of Votes-O'Tooley: {vote_t} ({len(tool_vote)})")
    print("-----------------------")

    def merge(list1, list2): 
        merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
        return merged_list 
      
    another_list=merge(vote_list, candidates)
    answer=max(another_list)

    print(f"Winner: {answer[1]}")
    print(f"----------------------")
    
with open("output.txt", 'w') as outfile:
    outfile.write("Election Results\n")
    outfile.write("----------------------\n")
    outfile.write(f"Total Votes:{lines-1}\n")
    outfile.write(f"Complete list of candidates:{candidates}\n")
    outfile.write("----------------------\n")
    outfile.write(f"Percentage of Votes-Khan: {vote_k} ({len(khan_vote)})\n")
    outfile.write(f"Percentage of Votes-Correy: {vote_c} ({len(correy_vote)})\n")
    outfile.write(f"Percentage of Votes-Li: {vote_l} ({len(li_vote)})\n")
    outfile.write(f"Percentage of Votes-O'Tooley: {vote_t} ({len(tool_vote)})\n")
    outfile.write("-----------------------")
