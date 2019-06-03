import pandas as pd
import re
from pandas import ExcelWriter

csv = pd.read_csv('1-100.csv')

for index, row in csv.iterrows():
    description = row['Descriptions']
    description = description.replace("CuisineCH", row['Main Cuisine'])
    try:
        description = description.replace("CityCH", row['City'])
    except:
        description = description.replace("MainCH", "Switzerland")
    description = description.replace("NameCH", row["Restaurant Name"])
    try:
        description = description.replace("MainCH", row["Main Product Sold"])
    except:
        description = description.replace("MainCH", "Food")
    try:
        description = description.replace("SecondCH", row["Secondary Sold"])
    except:
        description = description.replace("SecondCH", "Food")
    try:
        payment = row["Payment Method"].lower()
        description = description.replace("PayCH", payment)
    except:
        description = description.replace("PayCH", "any payment method")
    try:
        description = description.replace("PlatformCH", row["Web / Apps"])
    except:
        description = description.replace("PlatformCH", "our online platforms")
    description = re.sub(' +', ' ', description)
    csv.replace()
    row['Descriptions'] = description
    print(row['Descriptions'])
    csv.loc[index] = row

writer = ExcelWriter('new100.xlsx')
csv.to_excel(writer, 'Sheet1')
writer.save()
