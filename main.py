#coding=utf-8
import requests
def tuisong(title,text):
    print("get "+title+"text:\n"+text)

def weather():
    import requests
    r = requests.get('http://www.weather.com.cn/data/sk/101010100.html')
    r.encoding = 'utf-8'
    #print(r.json()["weatherinfo"])
    return "温度："+r.json()['weatherinfo']['temp']+"\n风："+r.json()['weatherinfo']['WSE']+"级"+r.json()['weatherinfo']['WD']+"\n是否有雨："+r.json()['weatherinfo']['rain'].replace("0","无").replace("1","有")

def service(url):
    if url.find("http://")==-1:
        url="http://"+url.replace(" ","")
    import requests
    req = requests.get(url)
    try:
        content=req.text  # 获取返回的内容，为字符串类型
        if content.find("LANMP一键安装包,集lamp,lnmp,lnamp,wdcp,wdos,wddns,wdcdn,云主机linux服务器管理系统面板软件")==-1:
            return "Tip:"+url+"  工作正常"
        else:return "Warning:" + url + "服务器出现问题"

    except:
        return "Warning:"+url+"服务器出现问题"

#print(service("me.muxxs.com"))


def news():
    url="http://news.baidu.com/ns?word=新闻关键字&tn=newsfcu&from=news&cl=2&rn=2&ct=0"
    china=url.replace("新闻关键字","中国")
    america=url.replace("新闻关键字","美国")
    china_req = requests.get(china)
    china_content=china_req.text
    x=1
    all_news=""
    for i in china_content.split("<a href="):
        if x==4 or x==5:
            href=i.split('"')[1].replace(" ","")
            content='<a href="'+href+'">'+i.split(">")[1].split("</a")[0]+"</a>"
            all_news = all_news + "<tr><td> " + content + "<td><tr> "
        x=x+1

    am_req = requests.get(america)
    am_content = am_req.text
    x=1
    for i in am_content.split("<a href="):
        if x==4 or x==5:
            href=i.split('"')[1].replace(" ","")
            content='<a href="'+href+'">'+i.split(">")[1].split("</a")[0]+"</a>"
            all_news=all_news+"<tr><td> "+content+"<td><tr> "
        x=x+1


    return all_news
#print(news())
def what():
    import datetime
    ti = datetime.datetime.now()
    wea=weather()
    ser1=service("me.muxxs.com")
    ser2=service("www.muxxs.com")
    new=news()
    html='''

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
　<head>
　　<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
　　<title>[todaytime]  报告</title>
　　<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
　</head>
    <body style="margin: 0; padding: 0;">
　<table border="1" cellpadding="0" cellspacing="0" width="100%">[todaytime]  报告
　　<tr>
　　　
        <table align="center" border="1" cellpadding="0" cellspacing="0" width="600" style="border-collapse: collapse;">
　           <tr>
　　      <td> [weather]</td>
　           </tr>
　           <tr>
　　      <td> [service1]\n [service2] </td>
　           </tr>
　           <tr>
　　      <td> [news] </td>
　           </tr>
</table>



　　</tr>
　</table>
</body>


</html>


    '''
    html=html.replace("[todaytime]",str(ti)).replace("[weather]",wea).replace("[service1]",ser1).replace("[service2]",ser2).replace("[news]",new)

    print(html)
    email("每日报告",html)

def email(title,content):
    #content="你好"
    print (title,content)
    import smtplib
    import smtplib
    import email.mime.multipart
    import email.mime.text
    from email.mime.text import MIMEText
    from email.header import Header
    sender = '747306970@qq.com'
    receiver = "747306970@qq.com"
    subject = str(title)
    smtpserver = 'smtp.qq.com'
    username = '747306970@qq.com'
    password = 'lqflqwijoscmbcag'
    msg = MIMEText(content, 'html', 'utf-8')  # 中文需参数‘utf-8'，单字节字符不需要
    msg['From'] = sender
    msg['To'] = receiver
    print ("get users")
    msg['Subject'] = Header(subject, 'utf-8')
    smtp = smtplib.SMTP_SSL('smtp.qq.com',465)
    print ("connected")
    smtp.login(username,password)
    print ("login finished")
    smtp.sendmail(sender, receiver, msg.as_string())
    print ("send finished")
    smtp.quit()


def iftime(time_target):
    import datetime
    ti = datetime.datetime.now()
    hours=str(ti.hour)
    min=str(ti.minute)
    seco=str(ti.second)
    all=hours+","+min+","+seco
    all=all.replace(" ","")
    if all == time_target:
        return True
def doit():
    import datetime
    ti = datetime.datetime.now()
    try:
        return what()
    except:
        tuisong("失败",str(ti)+"\n执行程序失败")
import datetime,time
print("working...")
while True:
    if iftime("5,59,58"):
        time.sleep(2)
        what()
    if iftime("11,59,58"):
        time.sleep(2)
        what()
