from bs4 import BeautifulSoup
import requests
import time, io
import _datetime as datetime

extn = str(datetime.datetime.now().strftime("%d-%m-%Y-%H%M%S"))
filename = "indeed-bpo-" + extn + ".txt"
filehandle = io.open(filename,"w", encoding="utf-8")

#pages = [10, 20, 30, 40, 50]
for page in range(6):
    if page == 0:
        source = requests.get('https://www.indeed.co.in/jobs?q=bpo&sort=date').text
    else:
        source = requests.get('https://www.indeed.co.in/jobs?q=bpo&sort=date&start={}'.format(page*10)).text

    soup = BeautifulSoup(source, 'html.parser')

    for jobs in soup.find_all(class_='result'):

        try:
            job_title = jobs.h2.text.strip()
        except Exception as e:
            job_title = None
        job_title = job_title + "\n"
        filehandle.write(job_title)


        try:
            company = jobs.span.text.strip()
        except Exception as e:
            company = None
        company = company + "\n"
        filehandle.write(company)

        try:
            salary = jobs.find('span',class_='no wrap').text.strip()
        except Exception as e:
            salary = None
        salary = str(salary) + "\n"
        filehandle.write(salary)

        try:
            location = jobs.find(class_='location').text.strip()
        except Exception as e:
            location = None
        location = location + "\n"
        filehandle.write(location)

        s = ""
        try:
            summary = jobs.find(class_='summary').text.strip()
        except Exception as e:
            summary = None
        filehandle.write(summary)

        try:
            date_posted = jobs.find('span', class_='date').text.strip()
        except Exception as e:
            date_posted = None
        date_posted = "\n" + date_posted + "\n"
        filehandle.write(date_posted)

        try:
            link = str(jobs.find(class_='jobtitle').get('href'))
        except Exception as e:
            link = None
        if link[0:8] == '/pagead/' or link[0:8] == '/company' or link[0:4] == '/rc/':
            link = "https://indeed.co.in" + link
        else:
            pass
        filehandle.write(link)

        filehandle.write("\n\n************** Next Job *************\n")

        time.sleep(2)
    print("New Page has been Scraped")

filehandle.close()



