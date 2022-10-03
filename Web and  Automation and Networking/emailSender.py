import requests
from bs4 import BeautifulSoup  # pip install bs4
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib 

def automateEmail(url):
    container = ''
    response = requests.get(url)
    contents = response.content
    # step 1 - scraping data
    # create soup
    soup = BeautifulSoup(contents, 'html.parser')
    # print(soup)
    source = soup.find_all('div', attrs={'class':'hm'})
    i = 1
    for item in source:
        if item.findChildren('h2'):
            anchor = item.find('a')
            text = item.text
            link = anchor.get('href')
            if 'https:' not in link:
                link = url+link
            # print(link)
            container += str(i) +':'+text + f"<a href={link}>click here</a><br>"
            i+=1
    return container

update = automateEmail('https://medium.com')
# print(update)

# server-
SERVER = 'smtp.gmail.com'
PORT = 587
FROM = 'your gmail id'
TO = 'gmail ids (whom to send)' # you can add multiple id using list[]
PASS = 'your password'

# messge
msg = MIMEMultipart()
msg['Subject'] = 'Trending Medium blogs - Automate'
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(update, 'html'))

# server start
server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

server.quit()