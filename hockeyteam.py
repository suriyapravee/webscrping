from bs4 import BeautifulSoup
import requests
import pandas  as pd
link="https://www.scrapethissite.com/pages/forms/"
page=requests.get(link)
print(page.status_code)
s=BeautifulSoup(page.content,"html.parser")
table = s.find("table", class_="table")
table_head=table.find_all("th")
head_list = [h.text.strip() for h in table_head]
print(head_list)
df = pd.DataFrame(columns=head_list)
print(df)
table_row = table.find_all("tr")
for row in table_row[1:]:
    for data in row.find_all("td"):
            row_list = [data.text.strip() for data in row.find_all("td")]
            print(row_list)
            print(len(df))
            df.loc[len(df)] = row_list
print(df)
df.to_csv('./hockyteam.csv')



