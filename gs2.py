from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd

def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    
   
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    # options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)
    
    url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword="+keyword+"&sc.keyword="+keyword+"&locT=&locId=&jobType="
    #url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    driver.get(url)
    print('ok')
    jobs = []

    # while len(jobs) < num_jobs:
    for j in range(1):
        i=0
        for i in range(31):
            print('whlie...')
            time.sleep(slp_time)
            if i!=0:
                s=str(i)
                time.sleep(6)
                st="//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/article[1]/div[1]/ul[1]/li["+s+"]"
                print(st)
                try:
                    driver.find_element_by_xpath(st).click()
                    # time.sleep(3)
                    print('done')
                    try:
                        driver.find_element_by_css_selector('[alt="Close"]').click() #clicking to the X.
                        # time.sleep(5)
                        print(' x out worked')
                    except NoSuchElementException:
                        print(' x out failed')
                        pass
                    
                    
                    try:
                        # cs="//body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/article[1]/div[1]/ul[1]/li[2]/div[2]/div[1]/a[1]/span[1]"
                        company_name = driver.find_element_by_xpath('//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]').text.split()
                        # company_name = driver.find_element_by_xpath('//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]').text.split()
                        cn=""
                        rating = company_name[-1]
                        for n in range(len(company_name)-1):
                            cn+=company_name[n]
                        time.sleep(2)    
                        job=driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]").text
                        # time.sleep(1)
                        location=driver.find_element_by_xpath('//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[3]').text
                        # time.sleep(1)
                        try:
                            salary=driver.find_element_by_xpath('//body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[4]').text
                        # salary=driver.find_element_by_xpath('//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[4]/span[1]/span[1]').text
                        except:
                            salary='not found-------------------'
                        try:
                            jobtype=driver.find_element_by_xpath('//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]').text    
                        except:
                            jobtype='not found'  
                        try:
                            time.sleep(5)
                            size=driver.find_element_by_xpath('//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]').text.split()
                            time.sleep(2)
                            ctype=driver.find_element_by_xpath('//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]').text.split()
                            sector=driver.find_element_by_xpath('//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[5]').text.split()
                            time.sleep(2)
                            founded=driver.find_element_by_xpath('//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]').text.split()
                            # time.sleep(1)
                            industry=driver.find_element_by_xpath('//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]').text.split()
                            # time.sleep(1)
                            revenue=driver.find_element_by_xpath('//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/article[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[6]').text.split()
                        except:
                            # time.sleep(3)
                            size=['not found','--']
                            ctype=['not found','--']
                            sector=['not found','--']
                            founded=['not found','--']
                            industry=['not found','--']
                            revenue=['not found','--']      
                    except:
                        print('opps')        
                    time.sleep(3)

                    print(j,'.',i,'  ',cn,' Rating: ',rating,' ',job,' ',location,' ',salary,' ',jobtype[10:],'\n')  
                    # time.sleep(3)
                    isize=(size[1:])
                    itype=(ctype[1:])
                    # time.sleep(3)
                    isector=(sector[1:])
                    ifounded=(founded[1:])
                    # time.sleep(3)
                    iindustry=(industry[1:])
                    # time.sleep(3)
                    irevenue=(revenue[1:])
                    # time.sleep(3)
                    fsize=' '.join([str(e) for e in isize])
                    # time.sleep(3)
                    ftype=' '.join([str(e) for e in itype])
                    fsector=' '.join([str(e) for e in isector])
                    ffounded=' '.join([str(e) for e in ifounded])
                    # time.sleep(3)
                    findustry=' '.join([str(e) for e in iindustry])
                    frevenue=' '.join([str(e) for e in irevenue])
                    
                    print('size:',fsize)
                    print('type:',ftype)
                    print('sector:',fsector)
                    print('founded:',ffounded)
                    print('industry:',findustry)
                    print('revenue:',frevenue)
                    # time.sleep(4)
                    jobs.append({"Company Name" : cn,
                    "Job Title" : job,
                    "Rating" : rating,
                    "Salary Estimate" : salary,
                    "Location" : location,
                    "Job Type" : jobtype[10:],
                    "Size" : fsize,
                    "Founded" : ffounded,
                    "Type of ownership" : ftype,
                    "Industry" : findustry,
                    "Revenue" : frevenue})
                    del cn
                    del job
                    del rating
                    del salary
                    del location
                    del jobtype
                    del fsize
                    del ffounded
                    del ftype
                    del findustry
                    del frevenue
                except ElementClickInterceptedException:
                    print('noooo')
                    pass
            else:
                print('it was 0.')
            if i==30:
                    try:
                        time.sleep(3)
                        driver.find_element_by_xpath('//body/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/article[1]/div[2]/div[2]/div[1]/div[1]/ul[1]/li[7]/a[1]/span[1]').click()
                    except:
                        print('fail to load new page')
            time.sleep(2)
        time.sleep(1)
    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.