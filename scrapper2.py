from bs4 import BeautifulSoup 
import requests
import pandas as pd


START_URL = (
'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
)
page= requests.get(START_URL)
soup = BeautifulSoup(page.text, "html.parser")
table = soup.find_all('table')
print(len(table))


temp_list= []
table_rows = table[4].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
print(temp_list)



mass = []
name = []
distance = []
radius = []


for i in range(1,len(temp_list)):
    
    mass.append(temp_list[i][7])
    name.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    radius.append(temp_list[i][8])

df = pd.DataFrame(list(zip(mass,name,distance,radius,)),
columns=['Mass','Star_name','Distance','Radius'])
print(df)

df.to_csv('128.csv')
