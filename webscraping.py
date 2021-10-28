import requests
from bs4 import BeautifulSoup
news = []
shotnews = []
image = []
link = []
for i in range(0, 15):
    URL = "https://www.indiatoday.in/india/?page=" + str(i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="content")
    elements = results.find_all("div", class_="catagory-listing")
    for job_element in elements:
        title_element = job_element.find("h2")
        news.append(title_element.text.strip())
        image1 = job_element.find("img")
        image.append(image1['src'])
        location_element = ""
        if job_element.find("a", href=True):
            location_element = job_element.find("a", href=True)
            if location_element == "":
                link.append("none")
            else:
                link1 = 'https://www.indiatoday.in' + location_element['href']
                link.append(link1)
        if job_element.find("p"):
            location_element = job_element.find("p")
            l1 = location_element.text.strip()
            location_element = l1
            shotnews.append(location_element)
x = [{'news': a, 'image': s, 'link': t, 'shortnews': l}
     for a, s, t, l in zip(news, image, link, shotnews)]

print(x)
