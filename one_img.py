import requests
from bs4 import BeautifulSoup
import os
import random
import pickle
import sys
import shutil
import time


def get_img(url):#获取图片地址并进行下载
    req=requests.get(url)
    soup=BeautifulSoup(req.text,"lxml")
    for i in soup.find_all('img'):
        if 'id'in (i.attrs):
            img_pos=i['src']
            img_name=img_pos.split('/')[-1]
    img_name=os.path.expanduser('~')+r"/Image/one_wallhaven"+'/'+img_name
    print(img_name)
    if not os.path.exists(img_name):#防止重复下载
        cmd="wget "+'"'+img_pos+'"'+" -O "+img_name
        os.system(cmd)
        with open(img_name,"rb")as f:
            img=f.read()
            f.close()
        with open(img_name,"wb")as f:
            f.write(img)
            f.close()
    return img_name
url_old="https://wallhaven.cc/search?categories=110&purity=100&topRange=1M&sorting=toplist&order=desc&page="
try:
    requests.get("https://www.baidu.com")
except:
    sys.exit()
countf=os.path.expanduser('~')+"/my_shell/countimg"
now_pic=os.path.expanduser('~')+"/my_shell/.now_pic"
with open(countf,"r")as f:
    count=int(f.readlines()[-1])
tp_pickle=os.path.expanduser('~')+'/my_shell/img_list'#将图片链接存为一个二进制文件，防止重复运行浪费时间
if count ==0:
    img_list=[]
    for i in range(1,10):
        url=url_old+str(i)
        req=requests.get(url)
        soup=BeautifulSoup(req.text)
        li_list=soup.find_all("li")
        li_list=list(filter(None,li_list))
        for i in li_list:
            if i.a:
                if 'class' in i.a.attrs:
                    if i.a['class']==["preview"]:
                        img_list.append(i.a['href'])
    pickle_file=open(tp_pickle,"wb")
    pickle.dump(img_list,pickle_file)
    pickle_file.close()
else:
    pickle_file=open(tp_pickle,"rb")
    img_list=pickle.load(pickle_file)
    pickle_file.close()

LOCKF=os.path.expanduser('~')+"/my_shell/.imglock"
if os.path.exists(LOCKF) and (time.time()-os.path.getctime(LOCKF)>600):
    #lock文件创建时间超过10min后删除文件。
    os.remove(LOCKF)
if os.path.exists(LOCKF):
    print("locked ")
else:
    with open(LOCKF,"w")as f:
        f.write(str(time.time()))
        f.close()
    img_url=random.choice(img_list)
    picture_name=get_img(img_url)
    the_command="DISPLAY=:0 feh --bg-fill"+' "'
    the_command=the_command+picture_name+'"'
    os.system(the_command)
    home_pict= os.path.expanduser('~')+"/.wallpaper"
    home_pictb= os.path.expanduser('~')+"/.wallpaperB"
    if os.path.exists(home_pict):
        if os.path.exists(home_pictb):
            os.remove(home_pictb)
        shutil.copyfile(home_pict,home_pictb)
        os.remove(home_pict)
    copy_command="cp "+picture_name+" "+home_pict
    os.system(copy_command)
    count += 1
    print(count)
    if count>200:
        count=0
    else:
        pass
    with open(countf,'w')as f:
        f.write(str(count))
    with open(now_pic,"w")as f:
        f.write(str(picture_name))
    os.remove(LOCKF)

