import pyperclip
import time
import os
from itranslate import itranslate as itrans
if __name__=='__main__':
    print('we are now in clip del mode')
    pyperclip.copy('start')
    del_space_flag=0
    to_keep_s=''
    while 1:
        time.sleep(0.5)
        oldString=pyperclip.paste()
        if oldString=='start' or oldString==to_keep_s:
            continue
        if '\n' in oldString:
            if del_space_flag:
                newString=oldString.replace('\r','').replace("-\n",'').replace("\n",' ')
                print(newString)
                print("---------------------------")
                pyperclip.copy(newString)
                try:
                    print(itrans(newString))
                except:
                    pass
                to_keep_s=newString
            else:
                newString=oldString.replace('\r','').replace("-\n",'').replace("\n",'')
                print(newString)
                print("---------------------------")
                pyperclip.copy(newString)
                try:
                    print(itrans(newString))
                except:
                    pass
                to_keep_s=newString
        else:
            newString=oldString                
            print(newString)
            print("---------------------------")
            pyperclip.copy(newString)
            try:
                print(itrans(newString))
            except:
                pass
            to_keep_s=newString

        if 'END'==oldString:
            os.system('notify-send delN Stop')
            break
        if 'del_space'==oldString:
            del_space_flag=1-del_space_flag
            os.system("notify-send \"taggle del_space_flag {}\"".format(str(del_space_flag)))
            pyperclip.copy(str(del_space_flag))

