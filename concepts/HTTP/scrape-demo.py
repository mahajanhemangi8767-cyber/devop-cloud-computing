# pipenv install beautifulsoup

from bs4 import BeautifulSoup

html="""

<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My first Heading.</h1>
<h1 class="info"> My Second Heading</h1>
<p> My first paragraph.</p>

</body>
</html>"""

# parse string in html

soup=BeautifulSoup(html,"html.parser")
print("Title:",soup.title.text)
print("Heading: ",soup.h1.text)
print("Heading:",soup.find("h1",class_="info").text)
print("paragraph:",soup.p.text)




# Execution of code:
# pipenv shell
# pyhton3 scrape-demo.py

