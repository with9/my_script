from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os
from bs4 import BeautifulSoup
from PIL import Image
from requests.cookies import RequestsCookieJar
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def evalue_one(driver,class_url):
    juery='''
    $("input.required[value$=5]").click()
    $("input.required.radio[id$=322]").click()
    $("input.required.checkbox").click()
    $("#item_316").val("这门课中我最喜欢的是老师有趣的讲解和讨论")
    $("#item_317").val("我认为本课程应从哪些方面需要进一步改进和提高的是跨学科的联系")
    $("#item_318").val("我平均每周在这门课程上花费大概2个小时")
    $("#item_319").val("在参与这门课之前，我对这个学科领域兴趣比较高")
    $("#item_320").val("我对该课程的课堂参参与度很高，按时完成作业，认真听讲")
    $("#item_364").val("这位老师的教学，我最喜欢什么他有趣的讲解和讨论")
    $("#item_365").val("对于这位老师我没有什么意见和建议，做的很好了")
    document.documentElement.scrollTop=10000
    '''
    driver.get(class_url)
    driver.execute_script(juery)
    driver.save_screenshot("img.png")
    img=Image.open("img.png")
    img.show()
    data=input("please input the code:")
    os.system('pkill display')
    try:
        elem_code=driver.find_element_by_name("adminValidateCode")
        elem_code.send_keys(str(data))
        elem_code.send_keys(Keys.RETURN)
    except:
        pass
    finally:
        driver.find_element_by_id("sb1").click()
        driver.find_element_by_class_name('jbox-button').click()




chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://sep.ucas.ac.cn/")
elem_name = driver.find_element_by_name("userName")
username=input('please input usename:')

elem_name.send_keys(str(username))
elem_pwd= driver.find_element_by_name("pwd")
pwd=input('please input pwd:')

elem_pwd.send_keys(str(pwd))


driver.save_screenshot("img.png")
img=Image.open("img.png")
img.show()
data=input("please input the code:")
os.system("pkill display")
try:
    elem_code=driver.find_element_by_name("certCode")
    elem_code.send_keys(str(data))
    elem_code.send_keys(Keys.RETURN)
except:
    elem_pwd.send_keys(Keys.RETURN)
finally:
    driver.get("http://sep.ucas.ac.cn/portal/site/226/821")
try:
    driver.switch_to.alert.accept()
except:
    pass
jwxk_web=driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[4]/ul/li/a').get_attribute('href')
while True:
    driver.get(jwxk_web)

    com_classes=driver.find_elements_by_class_name('btn.btn-primary')#获取课程评价链接
    class_urls=[]
    for com_class in com_classes:
        if com_class.get_attribute('text')=='修改评估':
            pass#排出已经评价的课程
        else:
            class_urls.append(com_class.get_attribute('href'))
    driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/ul/li[2]/a').click()#切换到教师评价页面

    com_classes=driver.find_elements_by_class_name('btn.btn-primary')#获取评价的链接
    for com_class in com_classes:
        if com_class.get_attribute('text')=='修改评估':
            pass#排出已经评价的课程
        else:
            class_urls.append(com_class.get_attribute('href'))
    if len(class_urls)==0:
        print("全都评价完啦")
        break
    for url in class_urls:
        evalue_one(driver,url)
