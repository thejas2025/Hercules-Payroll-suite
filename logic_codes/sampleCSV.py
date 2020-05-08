import csv

pay_dict = {}

with open('March_2020.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    linecount = 0
    a=0
    for row in csv_reader:
        if linecount == 0: 
            a=1
            linecount = 1
        else:
            
            if(row[0] not in pay_dict):
                
                # print(string)
                pay_dict[row[0]] = {'empid':row[0],'present':0,'absent':0}
                if row[2] == 'P':
                    pay_dict[row[0]]['present'] +=1
                elif row[2] == 'A':
                    pay_dict[row[0]]['absent'] +=1

            else:
                if row[2] == 'P':
                    pay_dict[row[0]]['present'] += 1    
                elif row[2] == 'A':
                    pay_dict[row[0]]['absent'] += 1


                    
    print(pay_dict)
            
        




