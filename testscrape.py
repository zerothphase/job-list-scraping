from bs4 import BeautifulSoup
import requests
import re




#url = ('https://www.jobstreet.com.sg/en/job-search/job-vacancy.php?ojs=10&key="data+scientist"')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}


urlHead = 'https://www.jobstreet.com.sg/en/job-search/job-vacancy.php?key=%22data+scientist%22&area=1&option=1&job-source=1%2C64&classified=1&job-posted=0&sort=2&order=0&pg='
urlTail = '&src=16&srcr=16&ojs=10'
urlPage = [1, 2, 3]

jobLink = []

for i in urlPage:
    searchUrl = urlHead + str(i) + urlTail
    print(searchUrl)
    


# Request and parse page
page = requests.get(searchUrl, timeout=5, headers=headers)
page_soup = BeautifulSoup(page.text, "html.parser")
#container = page_soup.find_all("div",{"class":"position-title header-text"})

# Find all listings
#position_list = page_soup.find_all(class_ = "position-title header-text")
position_list = page_soup.find_all("a", {"id":re.compile("^position_title_\d{1,2}$")})
len(position_list)
position_list.a
position_list[0].a

# Extract job links
for con in position_list:
    print(con["href"])
#    jobLink.append(con.a["href"])
    
jobLink



# =============================================================================
# with open('output1.html') as html_file:
# 	soup = BeautifulSoup(html_file, 'html.parser')
# 
# with open('linklist.txt') as txt_file:
# 	soup = txt_file.read()
# =============================================================================


#match = soup.find('div', {"class":"panel "})
#linkList = soup.split("\n")
#print(linkList)