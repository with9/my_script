import time
import pickle
import os
import sys
import random
import argparse
import requests
import shutil
import threading
from bs4 import BeautifulSoup


class Wallpaper:
    def __init__(self):
        self.locktime = time.time()
        self.file = os.path.expanduser('~/Image/wallpaper_class')
        self.folder = os.path.expanduser("~/Image/Wallpapers")
        self.onehaven_folder = os.path.expanduser("~/Image/one_wallhaven")
        self.homewallpaper = os.path.expanduser("~/.wallpaper")
        self.picture_name = ''  # 当前壁纸
        self.locked = False
        self.wallpaper_list = []
        self.temp_wallpaper_list = []
        self.onehaven_img = []
        self.count = 0  # 统计get值用于判断是否需要生成新的onehavenlist
        self.index = -1  # 目前在列表中的索引位置
        self.waring = 0  # 数量过多警告

    def mkfolders(self):
        # 初始化创建文件夹
        for i in [self.folder, self.onehaven_folder, os.path.join(self.folder, 'star')]:
            if not os.path.exists(i):
                os.mkdir(i)
                print(f'mkdir {i}')

    def file_name(self, file_dir):
        # 获取路径下文件
        for root, dirs, files in os.walk(file_dir):
            return [root, dirs, files]

    def set_wallpaper(self):
        self.back_to_normal_index()
        if self.wallpaper_list:
            self.picture_name = self.wallpaper_list[self.index]
            os.system(f"feh --bg-fill \"{self.picture_name}\"")
        else:
            print('no image in list')

    def isLock(self):
        # 简单的判断是否有另一个get方法再跑
        nowtime = time.time()
        if self.locked == False:
            return False
        else:
            if nowtime-self.locktime >= 600:
                self.locked = False
                return False
            else:
                return True

    def tolock(self):
        self.locked = True
        self.locktime = False

    def save(self):
        # 将实例化的对象保存在本地
        f = open(self.file, 'wb')
        pickle.dump(self, f)
        f.close()

    def randomall(self, submode='all'):
        # 从wallpapers文件夹随机一张图片作为壁纸
        if self.isLock():
            os.system('notify-send lockde')
            sys.exit()
        file_dir = self.folder
        if submode == 'star':
            file_dir = os.path.join(self.folder, 'star')
        list_picture = self.file_name(file_dir)[2]
        while list_picture:
            choosen = random.choice(list_picture)
            picture_name = os.path.join(file_dir, choosen)
            pic = picture_name
            if os.path.islink(picture_name):
                picture_name = os.readlink(picture_name)
                if '.' == picture_name[0]:
                    picture_name = os.path.abspath(
                        os.path.join(file_dir, picture_name))
            if 'image' in os.popen("file -i {}".format(picture_name)).read().split(':')[-1]:
                break
            else:
                list_picture.remove(choosen)
                continue
        if not list_picture:
            print('no Image find')
            sys.exit()
        self.wallpaper_list.insert(self.index+1, pic)
        self.index = self.index+1
        self.set_wallpaper()

    def back(self):
        # 列表上一张作为图片
        self.index = self.index-1
        if self.index <= -1:
            self.index = (len(self.wallpaper_list)-1)
        self.set_wallpaper()

    def next(self):
        # 列表下一张作为图片
        self.index = self.index+1
        if self.index >= len(self.wallpaper_list):
            self.index = 0
        self.set_wallpaper()

    def get_wallhaven_list(self, submode='110'):
        # 获取wallhaven.cc的图片列表
        if self.isLock():
            os.system('notify-send lockde')
            sys.exit()
        url_old = f"https://wallhaven.cc/search?categories={submode}&purity=100&topRange=1M&sorting=toplist&order=desc&page="
        try:
            requests.get("https://www.bing.com")
        except:
            sys.exit()
        if self.count == 0:
            for i in range(1, 10):
                url = url_old+str(i)
                req = requests.get(url)
                soup = BeautifulSoup(req.text, 'lxml')
                li_list = soup.find_all("li")
                li_list = list(filter(None, li_list))
                for i in li_list:
                    if i.a:
                        if 'class' in i.a.attrs:
                            if i.a['class'] == ["preview"]:
                                self.onehaven_img.append(i.a['href'])
            print(f"oneheaven list:{len(self.onehaven_img)}")
        self.count = 1
        self.save()

    def get_one(self):
        # 获取一张haven图片作为壁纸
        self.get_wallhaven_list()
        if self.locked:
            pass
        else:
            self.locktime = time.time()
            self.locked = True
            self.save()
        self.picture_name = self.download_one(random.choice(self.onehaven_img))
        self.wallpaper_list.insert(self.index+1, self.picture_name)
        self.index = self.index+1
        self.set_wallpaper()
        self.locked = False

    def keep_pic(self):
        # 将当前的onehaven图片丢入壁纸文件夹
        if self.picture_name:
            to_keep_pic = os.path.join(
                self.folder, self.picture_name.split('/')[-1])
            try:
                shutil.copyfile(self.picture_name, to_keep_pic)
            except:
                print('Already in')
            for i in range(len(self.wallpaper_list)):
                if self.wallpaper_list[i] == self.picture_name:
                    self.wallpaper_list[i] = to_keep_pic
            self.picture_name = to_keep_pic

    def star(self):
        # 将当前的壁纸图片丢入收藏夹
        if '/Image/Wallpapers' in self.picture_name:
            to_keep_pic = os.path.join(
                os.path.join(self.folder, 'star'), self.picture_name.split('/')[-1])
            try:
                os.symlink(self.picture_name, to_keep_pic)
            except:
                print("Already in")
            for i in range(len(self.wallpaper_list)):
                if self.wallpaper_list[i] == self.picture_name:
                    self.wallpaper_list[i] = to_keep_pic
            self.picture_name = to_keep_pic

    def trim(self):
        # 列表超过500的时候压缩到300
        if len(self.wallpaper_list) >= 500:
            if self.index < 150:
                self.wallpaper_list = self.wallpaper_list[:310]
            elif (len(self.wallpaper_list)-self.index) < 150:
                old_len = len(self.wallpaper_list)
                self.wallpaper_list = self.wallpaper_list[-300:]
                self.index = self.index-(old_len-300)
            else:
                self.wallpaper_list = self.wallpaper_list[self.index -
                                                          150:self.index+151]
                self.index = 150

    def to_home(self):
        # 复制图片到$HOME/.wallpaper,并设定权限
        if self.picture_name and self.wallpaper_list:
            if os.path.exists(self.homewallpaper):
                os.remove(self.homewallpaper)
            shutil.copy(self.picture_name, self.homewallpaper)
            os.system('chmod 666 {}'.format(self.homewallpaper))

    def clear(self):
        self.wallpaper_list = []
        self.index = -1

    def remove_img(self, submode='soft'):
        # 从列表删除该图片
        if not self.wallpaper_list:
            sys.exit()
        del self.wallpaper_list[self.index]
        if submode == 'hard':
            os.remove(self.picture_name)  # 同时删除文件
            def fc(n): return n != self.picture_name
            self.wallpaper_list = list(
                filter(fc, self.wallpaper_list))  # 从列表里面全部删除
        if self.wallpaper_list:
            self.set_wallpaper()
        else:
            self.clear()

    def add_one(self, file=None):
        file = file.replace('\n', '')
        if not file:
            print('You should select one picture')
        elif 'image' not in os.popen("file -i \"{}\"".format(file)).read().split(':')[-1]:
            print('The file looks like not image file')
        else:
            self.wallpaper_list.insert(self.index+1, file)
            self.index = self.index+1
            self.set_wallpaper()

    def download_one(self, url):
        # 从haven下载一张图片
        i = 0
        while 1:
            try:
                i = i+1
                req = requests.get(url)
                soup = BeautifulSoup(req.text, 'lxml')
                img_tag = soup.find(id='wallpaper')
                img_url = img_tag['src']
                filename = img_url.split('/')[-1]
                filename = os.path.join(self.onehaven_folder, filename)
                if os.path.exists(filename):
                    print('exist')
                    return filename
                os.system(f"wget {img_url} -O {filename}")
                self.temp_wallpaper_list.append(filename)
                return filename
                break
            except:
                #             print('{}not ok'.format(url))
                continue
                if i >= 10:
                    break

    def init_folder(self):
        # 初始化,获取havenimg列表,下载30张图片,把这些图片都加入壁纸列表
        self.get_wallhaven_list()
        print(f'init downloading some picture')
        ts = []
        lock = threading.Lock()
        self.temp_wallpaper_list = []
        for i in random.sample(self.onehaven_img, 30):
            lock.acquire()
            try:
                t = threading.Thread(target=self.download_one, args=(i,))
                t.start()
                ts.append(t)
            finally:
                lock.release()
        for t in ts:
            t.join()
        self.count = self.count+1
        self.wallpaper_list = self.wallpaper_list+self.temp_wallpaper_list
        self.next()

    def remove_duplicate(self):
        # 去重
        if self.wallpaper_list:
            self.wallpaper_list = list(set(self.wallpaper_list))
            self.index = self.wallpaper_list.index(self.picture_name)
            print(f'len:{len(self.wallpaper_list)}')

    def print(self):
        # 显示一些基本内容
        for i in range(len(self.wallpaper_list)):
            print("{:<10d}{}".format(i, self.wallpaper_list[i]))
        print("now       {}\nindex:{}\ncount:{}".format(
            self.picture_name, self.index, self.count))

    def back_to_normal_index(self):
        if self.index >= len(self.wallpaper_list):
            self.index = len(self.wallpaper_list)-1
        if self.index < 0:
            self.index = 0


if __name__ == '__main__':
    if not os.path.exists(os.path.expanduser('~/Image')):
        os.mkdir(os.path.expanduser("~/Image"))
    wallpaper_file = os.path.expanduser('~/Image/wallpaper_class')
    if os.path.exists(wallpaper_file):
        f = open(wallpaper_file, 'rb')
        wallpaper = pickle.load(f)
        f.close()
    else:
        wallpaper = Wallpaper()
        wallpaper.mkfolders()
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", default='print')
    parser.add_argument("-s", "--submode", default='110')
    args = parser.parse_args()
    if args.mode == 'randomall':
        wallpaper.randomall()
    elif args.mode == 'back':
        wallpaper.back()
    elif args.mode == 'next':
        wallpaper.next()
    elif args.mode == 'get':
        wallpaper.get_one()
        wallpaper.count = wallpaper.count+1
        if wallpaper.count >= 500:
            wallpaper.count = 0
    elif args.mode == 'randomstar':
        wallpaper.randomall('star')
    elif args.mode == 'keep':
        wallpaper.keep_pic()
    elif args.mode == 'star':
        wallpaper.star()
    elif args.mode == 'add':
        wallpaper.add_one(os.popen(f"realpath \"{args.submode}\"").read())
    elif args.mode == 'rebuild':
        wallpaper.count = 0
        wallpaper.get_wallhaven_list(args.submode)
    elif args.mode == 'print':
        wallpaper.print()
        sys.exit()
    elif args.mode == 'remove':
        wallpaper.remove_img()
    elif args.mode == 'delete':
        wallpaper.remove_img('hard')
    elif args.mode == 'init':
        wallpaper.init_folder()
    elif args.mode == 'rd':
        wallpaper.remove_duplicate()
    elif args.mode == 'clear':
        wallpaper.clear()
    elif args.mode == 'trim':
        wallpaper.trim()
    elif args.mode == 'jump':
        try:
            wallpaper.index = int(args.submode)
            wallpaper.picture_name = wallpaper.wallpaper_list[wallpaper.index]
            os.system(f"feh --bg-fill \"{wallpaper.picture_name}\"")
        except:
            print("please input correct index")
            sys.exit()
    else:
        msg = '''
        randomall     :random one file
        back|next     :back &&next
        keep|star     :collect |star
        add           :add one file to list
        remove|delete :remove from list|delete file
        init          :download 30 file and add to the list
        rd            :remove duplicate
        print         :print basic message
        rebuild xxx   :rebuild the haven list xxx can  110(default) 1:genery 2:anime 3:people    
        clear         :clear img_list
        trim          :trim to 300

        '''
        print(msg)
    print("{:<10d}{}".format(wallpaper.index, wallpaper.picture_name))
    wallpaper.to_home()
    wallpaper.locked = False
    if len(wallpaper.wallpaper_list) >= 1000:
        wallpaper.waring = wallpaper.waring+1
        if wallpaper.waring >= 50:
            os.system('notify-send \'need to trim or rd\'')
            wallpaper.waring = 0
    wallpaper.save()
