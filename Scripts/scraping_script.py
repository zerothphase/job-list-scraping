from bs4 import BeautifulSoup
import requests
import re
import time



# Header for the request.get() to trick the website that I am accessing the website through a browser
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}


# This URL searches for the exact keyword "data scientist". Manual search on the website gives
# 3 pages of results.
urlHead = 'https://www.jobstreet.com.sg/en/job-search/job-vacancy.php?key=%22data+scientist%22&area=1&option=1&job-source=1%2C64&classified=1&job-posted=0&sort=2&order=0&pg='
urlTail = '&src=16&srcr=16&ojs=10'
urlPage = [1, 2, 3, 4]


# Grabbing all the links of job listing found by the search.
jobLink = []

for i in urlPage:
    searchUrl = urlHead + str(i) + urlTail
    print(searchUrl)

    # Request and parse page
    page = requests.get(searchUrl, timeout=7, headers=headers)
    page_soup = BeautifulSoup(page.text, "html.parser")

    # Find all listings
    position_list = page_soup.find_all("a", {"id":re.compile("^position_title_\d{1,2}$")})
 
    # Extract job links
    for item in position_list:
    #    print(item["href"])
        jobLink.append(item["href"])
    
    time.sleep(20)
    

# For testing using a valid link
# jobLink = ["https://www.jobstreet.com.sg/en/job/data-scientist-5-days-semiconductor-mfg-sso-430629-6584336?fr=21&src=16"]

# Create a new .csv file to store the data.
csv_headers = 'job_title; company; company_size; industry; required_experience; posting_date; closing_date; link; job_description\n'
try:
    with open("job.csv", "w", encoding='utf-8') as file:
        file.write(csv_headers)
except:
    print('error')
        
    
# Scrape each of the job links
for item in jobLink:
    print('Grabbing: {}'.format(item))
    # Scrape and parse html
    try:
        t0 = time.time()
        jobPage = requests.get(item, timeout=10, headers=headers)
        
    except:
        print('Error link: {}'.format(item))
        print('Sleeping for 60 s...')
        time.sleep(60)
        continue
    print('Parsing...')
    job_soup = BeautifulSoup(jobPage.text, "html.parser")
    
    # Grab interesting informations
    try:
        position_title = job_soup.find("h1", {"id":"position_title"}).text.strip().replace(';', '|')
        company = job_soup.find("div", {"id":"company_name"}).text.replace('\n', '').replace(';', '|')
        company_size = job_soup.find("p", {"id":"company_size"}).text.replace(';', '|')
        industry = job_soup.find("p", {"id":"company_industry"}).text.replace(';', '|')
        experience = job_soup.find("span", {"id":"years_of_experience"}).text.replace('\n', '').replace('\t', '').replace(';', '|')
        posting_date = job_soup.find("p", {"id":"posting_date"}).text.replace('Advertised: ', '')
        
        # The closing_date has special case which requires extra cleaning. This special case occurs
        # at the expiring listings.
        closing_date = job_soup.find("p", {"id":"closing_date"}).text.strip().replace('Closing on ', '')
        temp = re.search("Closing\D*\d{1}\D*(\d{2})",closing_date)
        if temp:
            closing_date = closing_date.replace(temp[0],temp[1])
        
        job_des = job_soup.find("div", {"id":"job_description"}).get_text().replace('\n', '|').replace('\r', '|').replace(';', '|')
        
    except:
        time.sleep(20)
        continue
        
    # Append to the .csv file
    with open("job.csv", "a", encoding='utf-8') as file:
        file.write(position_title +';' + company +';' + company_size +';' + industry +';' + experience +';' + posting_date +';' + closing_date +';' + item +';' + job_des + '\n')
    print('Current iteration success')
    time.sleep(20)
    

print('Complete')

