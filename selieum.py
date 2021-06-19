from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os
from bs4 import BeautifulSoup
from PIL import Image
from requests.cookies import RequestsCookieJar
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def get_file(classid,cookie):
    url="https://course.ucas.ac.cn/access/content/group/"+str(classid)+r"/"
    #url="https://course.ucas.ac.cn/access/content/group/177648"
    html=requests.get(url,cookies=cookie).text
    soup=BeautifulSoup(html)
    pre_wb=soup.find_all(attrs={'class':'file'})
    pre_fd=soup.find_all(attrs={'class':'folder'})
    class_name=soup.find_all("h3")[0].string
    cmd="mkdir "+class_name
    os.system(cmd)
    for folder in pre_fd:
        cmdd=cmd+r"/"+str(folder.a['href'])
        os.system(cmdd)
        url_s=url+str(folder.a['href'])+r"/"
        htmls=requests.get(url_s,cookies=cookie).text
        soups=BeautifulSoup(htmls)
        pre_wbs=soups.find_all(attrs={'class':'file'})
        class_name_s=soups.find_all("h3")[0].string
        filelists=[]
        namelists=[]
        for i in pre_wb:
            # print(i.a.string)
            filelists.append(url_s+str(i.a['href']))
            namelists.append(i.a.string)
        for i in range(len(filelists)):
            filename=class_name+"\\"+class_s_name+"\\"+namelists[i]
            filename=filename.replace("-","_")
            if  os.path.isfile(filename):
                #print(filename+"课件已存在,进行跳过")
                pass
            else:
                req=requests.get(filelists[i],cookies=cookie).content
                print("完成下载课件"+filename)
                with open(filename,"wb")as f:
                    f.write(req)

    #find class_name
    filelists=[]
    namelists=[]
    for i in pre_wb:
        # print(i.a.string)
        filelists.append(url+str(i.a['href']))
        namelists.append(i.a.string)
    for i in range(len(filelists)):
        filename=class_name+"\\"+namelists[i]
        filename=filename.replace("-","_")
        if  os.path.isfile(filename):
            #print(filename+"课件已存在,进行跳过")
            pass
        else:
            req=requests.get(filelists[i],cookies=cookie).content
            print("完成下载课件"+filename)
            with open(filename,"wb")as f:
                f.write(req)
def get_folder(cmd):
    pass
def get_classid(url,cookie):
    html=requests.get(url,cookies=cookie).text
    soup=BeautifulSoup(html)
    pre_wb=soup.find_all(attrs={'target':'_top'})[1:]
    classids=[]
    for i in pre_wb:
        classids.append((i['href'].split("/")[-1]))
    return classids
# driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver=webdriver.Chrome()
driver.get("http://sep.ucas.ac.cn/")
#assert "Python" in driver.title
elem_name = driver.find_element_by_name("userName")
elem_name.send_keys("YOUR username")
elem_pwd= driver.find_element_by_name("pwd")
elem_pwd.send_keys("Your PASSWD")
# img_url= driver.find_element_by_id("code").get_attribute('src')
# img_content=requests.get(img_url).content
# with open("img.png","wb")as f:
#     f.write(img_content)
driver.save_screenshot("img.png")
img=Image.open("img.png")
img.show()
data=input("please input the code:")
try:
    elem_code=driver.find_element_by_name("certCode")
    elem_code.send_keys(str(data))
    elem_code.send_keys(Keys.RETURN)
except:
    elem_pwd.send_keys(Keys.RETURN)
finally:
    driver.get("http://sep.ucas.ac.cn/portal/site/16/801")
cookies_bw=driver.get_cookies()
cookies={}
for cookie in cookies_bw:
    cookies[cookie['name']]=cookie['value']
url="YOUR COURSE URL"
classids=get_classid(url,cookies)
# classids=get_classid(url,cookies)
for classid in classids:
    get_file(classid,cookies)

# print(elem_class)
# print (driver.page_source)5
