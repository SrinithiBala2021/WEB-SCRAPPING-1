from bs4 import BeautifulSoup
import requests
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

request = requests.get(START_URL)

soup = BeautifulSoup(request.text, "html.parser")

headers = ["name","distance","mass","radius"]

stars_data = []

temp_list = []

for tr_tag in soup.find("table").find_all("tr"):

    td_tags = tr_tag.find_all("td")

    row = [i.text.strip() for i in td_tags]
    
    temp_list.append(row)


for i in range(1, len(temp_list)):

    data = [temp_list[i][1], temp_list[i][3], temp_list[i][5], temp_list[i][6]]

    stars_data.append(data)

with open("data.csv", "w") as f:
    
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)