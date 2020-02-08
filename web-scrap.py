import requests as req
import bs4 as bs
import webbrowser as wb
import wget
import pandas as pd
from datetime import datetime as dt
df = pd.read_excel("login-data.xlsx")
dob = []
for i in list(df['dob']):
    dob.append(i.strftime("%m/%d/%Y"))
rn = list(df['rn'])
login_data = []
for i in range(len(rn)):
    login_data.append({'Srollno' : rn[i],'Password' : dob[i]})

    


for i in login_data:
    with req.Session() as s:
        url = "http://results.skcet.ac.in:613/index.php/Welcome/Login"
        dash = s.post(url,data=i)
        dash_content = bs.BeautifulSoup(dash.content,'html5lib')
        image_url = dash_content.find('img')
        image_url = image_url['src']
        #a = wget.download(image_url)
        roll_no = dash_content.find(class_='hidden-xs')
        roll_no = roll_no.text
        name = dash_content.find('a',class_='pull-right')
        name = name.text        
        profile = '<img src="'+roll_no+'.jpg"'  "height=""100 " "width=""100"" ><h3>"+name+"</h3><h3>"+roll_no+"</h3>"
        file = open("result.html","w")
        file.write(profile)
        file.close()
        result = s.get("http://results.skcet.ac.in:613/index.php/Result")
        result_content = bs.BeautifulSoup(result.content,'html5lib')
        table = result_content.find(class_='box-body')
        file = open("result.html","a")
        file.write(str(table))
        s.close()
        file.close()
        wb.open("result.html")
    
