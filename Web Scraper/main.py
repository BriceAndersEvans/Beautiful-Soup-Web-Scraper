from bs4 import BeautifulSoup
import requests

print('Specufy skills you would like to filter out of job listings: ')
undeq_skill = input('>')
print(f'Filtering out: {undeq_skill}')

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
#print(html_text)
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
# print(job)
for job in jobs:
    posted_date = job.find('span', class_='sim-posted').span.text
    if 'few' in posted_date:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
        skills = job.find('span', class_='srp-skills').text.replace(' ','')
        posting_url = job.header.h2.a['href']
        # print(company_name)
        # print(skills)
        # print(posted_date)
        if undeq_skill not in skills:
            print(f'Company Name: {company_name.strip()}')
            print(f'Required Skills: {skills.strip()}')
            print(f'Job Posting Link: {posting_url}')

            print('')
