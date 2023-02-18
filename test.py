from pandas import pandas as pd


data=pd.read_csv('test.csv')
print(len(data))
single_record={}
all_record=[]
for i in range(len(data)):
    main_row=data.iloc[i][4]
    if '/' in main_row:
        telepphone=main_row.split('/')
        for m in range(len(telepphone)):
                single_record['company_name']=data.iloc[i][0]
                single_record['address']=data.iloc[i][1]
                single_record['category']=data.iloc[i][2]
                single_record['category']=data.iloc[i][3]
                single_record['telephon']=str(telepphone[m])
                all_record.append(single_record)
                single_record={}
    else:
        single_record['company_name']=data.iloc[i][0]
        single_record['address']=data.iloc[i][1]
        single_record['category']=data.iloc[i][2]
        single_record['category']=data.iloc[i][3]
        single_record['telephon']=str(data.iloc[i][4])
        all_record.append(single_record)
        single_record={}
df=pd.DataFrame(all_record)
df.to_csv("list_of_dict_to_csv.csv")





