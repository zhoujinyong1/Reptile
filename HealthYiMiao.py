import requests,time
from pynput import mouse
from pynput.mouse import Button, Controller
import time
import ctypes
from urllib.parse import parse_qs, urlencode, urlparse

#获取健康深圳页面(具体根据抓包信息自行更换，有些信息涉及本人就用信息代替)
reservation_headers = {
    "Accept-Encoding" :"gzip, deflate, br",
    "User-Agent" :"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "Cookie" :"信息",
    "Content-Length" :"247",
    "content-type" :"application/x-www-form-urlencoded;charset=UTF-8",
    "Referer" :"https://servicewechat.com/wx430d371fb280bcd5/114/page-frame.html",
    "Connection" :"keep-alive",
    "Host" :"www.newhealth.com.cn"
}
reservation_data = {
  "platOrgId" :"信息",
  "platDeptId" :"信息",
  "schDate" :"",
  "channelId" :"信息",
  "rn" :"8056871556673852",
  "rtime" :"20210603111735",
  "sko" :"d67373293b966a60a362f5cb01b7610b",
  "_wx_url" :"信息",
  "_wx_mini_requestId" :"信息"
}
reservation_url = 'https://www.newhealth.com.cn/hos/portal/appt/getDoctorSchInfo'
fast_access_url_is = requests.post(reservation_url,data=reservation_data,headers=reservation_headers).json()['body']['dataList']
print(time.strftime("%Y-%m-%d %X"),"--",fast_access_url_is[0]['platOrgName'],"--",fast_access_url_is[0]['platDeptName'],":",fast_access_url_is[0]['numTypeName'])
'''用模拟鼠标来预约疫苗
if fast_access_url_is[0]['numTypeName']=="约满" and fast_access_url_is[0]['platDeptName']=="新冠疫苗接种（北京科兴）":
    print("1")
else:  #有号
    print("2")
    PROCESS_PER_MONITOR_DPI_AWARE = 2
    ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)
    mouse_er = Controller()
    mouse_er.position = (1856, 462)
    mouse_er.press(Button.left)
    mouse_er.release(Button.left)

    time.sleep(3)
    mouse_er.position = (1454, 163)
    mouse_er.press(Button.left)
    mouse_er.release(Button.left)
    time.sleep(1)
    mouse_er.position = (1422, 901)
    mouse_er.press(Button.left)
    mouse_er.release(Button.left)
    time.sleep(1)
    mouse_er.position = (1680, 876)
    mouse_er.press(Button.left)
    mouse_er.release(Button.left)
    print("预约成功")
'''

