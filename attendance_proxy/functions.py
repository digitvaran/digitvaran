from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup
keys=webdriver.common.keys.Keys


def scroll_element_into_view(driver, element):
    """Scroll element into view"""
    y = element.location['y']
    driver.execute_script('window.scrollTo(0, {0})'.format(y))

def get_attendance(program,semester,month):
    #display for pythonanywhere.com
    display = Display(visible=0, size=(800, 600))
    display.start()
    # we can now start Firefox and it will run inside the virtual display
    browser = webdriver.Firefox()
    browser.get('http://sscattendance.formistry.com/report/')
    prog=browser.find_element_by_id('program')
    sem=browser.find_element_by_id('semester')
    mth=browser.find_element_by_id('month')
    #select appropriate options
    for i in range(program):
        prog.send_keys(keys.DOWN)
    prog.send_keys(keys.ENTER)
    for i in range(semester):
        sem.send_keys(keys.DOWN)
    sem.send_keys(keys.ENTER)
    for i in range(month):
        mth.send_keys(keys.DOWN)
    mth.send_keys(keys.ENTER)
    #------scroll to end and extract records
    pagesize=browser.find_element_by_id('pagesize')
    scroll_element_into_view(browser,pagesize)
    pagesize.send_keys('100\n')
    report=browser.find_element_by_id('report_block')
    text=report.get_attribute('innerHTML')
    #close the browser and the display.
    browser.quit()
    display.stop() # ignore any output from this.
    #create a soup
    soup=BeautifulSoup(text)
    #get the headers fo rthe subjects
    header=soup.find("table", { "id" : "table-header" }).contents[0]
    heads=[i.text for i in header.findAll('th') if ('tbl_heading' in i.get('class',''))]
    header=heads[2:]
    #first one is the student name second is blank and for asthetics
    #-----get the data
    tbody=soup.find('table',{'id':'tableid'}).contents[1]
    #parse data
    students=[]
    for number in tbody.findAll('tr'):#for every student
        columns=[i for i in number.findAll('td')]
        student_name=columns[0].text
        columns=columns[2:]#only attendance data
        data=[student_name]
        #for every subject
        for i in range(len(header)):
            la,ld=columns[i].text ,columns[i+1].text
            ta,td=columns[i+2].text ,columns[i+3].text
            pa,pd=columns[i+4].text ,columns[i+5].text
            data.append(str(la)+'/'+str(ld))
            data.append(str(ta)+'/'+str(td))
            data.append(str(pa)+'/'+str(pd))
        students.append(data)
    return students,headers

if __name__=='__main__':
    data=get_attendance(33,1,1)
    for key in data.keys():
        print(key)
        print(data[key])
        print('-'*100)
