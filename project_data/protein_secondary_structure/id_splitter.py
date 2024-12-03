'''
reads "entry_ids.txt" and inserts the first 15,000 ids into "0_5000_entry_ids.txt",
"5000_10000_entry_ids.txt", and "10000_15000_entry_ids.txt" respectively.
'''
with open("entry_ids.txt") as file :
    for line in file :
        line = line.replace('[', '').replace(']', '').replace('"', '')
        line = line.split(',')
        
        with open("0_5000_entry_ids.txt", 'w') as file1 :
            print(', '.join(line[:5000]), file=file1)
            
        with open("5000_10000_entry_ids.txt", 'w') as file2 :
            print(', '.join(line[5000:10000]), file=file2)
        
        with open("10000_15000_entry_ids.txt", 'w') as file3 :
            print(', '.join(line[10000:15000]), file=file3)
            

