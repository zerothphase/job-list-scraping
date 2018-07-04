from bs4 import BeautifulSoup
import requests
import re
import time



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
    page = requests.get(searchUrl, timeout=7, headers=headers)
    page_soup = BeautifulSoup(page.text, "html.parser")
    #container = page_soup.find_all("div",{"class":"position-title header-text"})
    
    # Find all listings
    position_list = page_soup.find_all("a", {"id":re.compile("^position_title_\d{1,2}$")})
    #len(position_list)
    
    # Extract job links
    for item in position_list:
    #    print(item["href"])
        jobLink.append(item["href"])
    
    time.sleep(5)
    
#jobLink[0]
#len(jobLink)
#link = 'https://www.jobstreet.com.sg/en/job/vpavp-data-scientist-big-data-analytics-group-data-management-office-6595321?fr=21&src=16&srcr=16'
csv_headers = 'job_title; company; company_size; industry; required_experience; posting_date; closing_date; link; job_description\n'
try:
    with open("job.csv", "w", encoding='utf-8') as file:
        file.write(csv_headers)
except:
    print('error')
        
    

for item in jobLink[12:]:
    print('Grabbing: {}'.format(item))
    try:
        t0 = time.time()
        jobPage = requests.get(item, timeout=7, headers=headers)
        response_delay = time.time() - t0
        
    except:
        print('Error link: {}'.format(item))
        print('Sleeping for 60 s...')
        time.sleep(60)
        continue
    print('Parsing...')
    job_soup = BeautifulSoup(jobPage.text, "html.parser") #exclude_encodings=["ISO-8859-7"]
    
    position_title = job_soup.find("h1", {"id":"position_title"}).text.strip()
    company = job_soup.find("div", {"id":"company_name"}).text.replace('\n', '')
    company_size = job_soup.find("p", {"id":"company_size"}).text
    industry = job_soup.find("p", {"id":"company_industry"}).text
    experience = job_soup.find("span", {"id":"years_of_experience"}).text.replace('\n', '').replace('\t', '')
    posting_date = job_soup.find("p", {"id":"posting_date"}).text.replace('Advertised: ', '')
    closing_date = job_soup.find("p", {"id":"closing_date"}).text.strip().replace('Closing on ', '')
    job_des = job_soup.find("div", {"id":"job_description"}).get_text().replace('\n', '|').replace('\r', '|').replace(';', '|')
        
    
    with open("job.csv", "a", encoding='utf-8') as file:
        file.write(position_title +';' + company +';' + company_size +';' + industry +';' + experience +';' + posting_date +';' + closing_date +';' + item +';' + job_des + '\n')
    print('Current iteration success')
    time.sleep(50*response_delay)
    

print('Complete')

# with open("job.csv", "a", encoding='utf-8') as file:
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