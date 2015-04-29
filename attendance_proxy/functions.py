from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup
keys=webdriver.common.keys.Keys


def scroll_element_into_view(driver, element):
    """Scroll element into view"""
    y = element.location['y']
    driver.execute_script('window.scrollTo(0, {0})'.format(y))

def get_attendance(program,semester,month):
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
    #everybody is on the page
    report=browser.find_element_by_id('report_block')
    text=report.get_attribute('innerHTML')
    #tidy-up
    browser.quit()
    display.stop() # ignore any output from this.
    #create a soup
    soup=BeautifulSoup(text)
    resultant_data={}
    #get the headers
    header=soup.find("table", { "id" : "table-header" }).contents[0]
    heads=[]
    for i in header.findAll('th'):
        if ('tbl_heading' in i.get('class','')):heads.append(i.text)
    header=heads[2:]
    #-----get the data
    tbody=soup.find('table',{'id':'tableid'}).contents[1]
    #parse data
    for number in tbody.findAll('tr'):#for every student
        columns=[i for i in number.findAll('td')]
        student_name=columns[0].text
        student_data={}
        for i in header:
            student_data[i]={}
        columns=columns[2:]
        for i in range(int(len(columns)/len(header))):
            ld=columns[i].text
            la=columns[i+1].text
            td=columns[i+2].text
            ta=columns[i+3].text
            pd=columns[i+4].text
            pa=columns[i+5].text
            lecture=str(la)+'/'+str(ld)
            theory=str(ta)+'/'+str(td)
            practical=str(pa)+'/'+str(pd)
            student_data[header[i]]['lecture']=lecture
            student_data[header[i]]['theory']=theory
            student_data[header[i]]['practical']=practical
        resultant_data[student_name]=student_data
    return resultant_data

if __name__=='__main__':
    data=get_attendance(33,1,1)
    for key in data.keys():
        print(key)
        print(data[key])
        print('-'*100)
