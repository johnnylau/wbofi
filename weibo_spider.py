#-*- coding: utf-8 -*-
import re, requests, signal, sys, shutil
import sys
import getopt


from lxml import etree
from os.path import expanduser

def handleTimeOut(signum, frame):
	print "超时 请检查防火墙设置或更改超时时间"
	sys.exit(1)

def cheTimeOut(handler, sec):
	signal.signal(signal.SIGALRM, handleTimeOut)
	signal.setitimer(signal.ITIMER_REAL, sec)

def getContent(userId):
	try:
		userId = "http://weibo.com/"+str(userId)
		userAgent = {'User-agent': 'Googlebot'}
		return requests.get(userId, headers=userAgent)
	except requests.exceptions.ConnectionError:
		print "请检查您的网络连接"
		sys.exit(1)

def getName(pageContent):
	try:
		return re.findall(r"CONFIG\['onick'\]='(.*?)'", pageContent.text)[0].encode('utf-8')
	except IndexError:
		print "没有找到这个用户"
		sys.exit(1)

def getOid(pageContent):
	try:
		return re.findall(r"CONFIG\['oid'\]='(.*?)'", pageContent.text)[0].encode('utf-8')
	except IndexError:
		print "没有找到这个用户"
		sys.exit(1)

def getHeadPic(userName, pageContent, path):
	if path=='':
		path = expanduser("~")+'/'+userName+'.jpg'
	else:
		path = path+'/'+userName+'.jpg'
	xhtml = etree.HTML(pageContent.text)
	imgLis = xhtml.xpath('//div[@class="pf_head_pic"]/img/@src')
	loadedImg = requests.get(imgLis[0], stream=True)
	if loadedImg.status_code == 200:
		with open(path, 'wb') as f:
			loadedImg.raw.decode_content = True
			shutil.copyfileobj(loadedImg.raw, f)   
			print "头像已下载到: "+path

def getFerList(userName, pageContent):
	pass


def getHeadIcon(path, userId):
	cheTimeOut(handleTimeOut, 8)
	content = getContent(userId)
	userName = getName(content)
	userOid = getOid(content)
	getHeadPic(userName, content, path)
	print "用户名: "+userName

def usage():
    print "wbofi usage:"
    print "-h --help: help message"
    print "-v --version: print version"
    print "-p --path: set output path"
    print "-u --user: set user id or name"
    print "--headicon: get user headIcon"

def version():
    print "wbofi version 0.0.0.0"


def main(argv):
    path = ''
    user = ''
    try :
        opts, args = getopt.getopt(argv[1:], 'hvp:u:',['help', 'version', 'path=', 'user=', 'headicon'])
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

    for o, a in opts:
        if o in('-h', '--help'):
            usage()
            sys.exit(1)
        elif o in ('-v', '--version'):
            version()
            sys.exit(1)
        elif o in ('-p', '--path'):
            path = a
        elif o in ('-u', '--user'):
            user = a
        elif o in ('--headicon'):
            getHeadIcon(path, user)
            sys.exit(1)
        else:
            sys.exit(3)

if __name__ == "__main__":
	main(sys.argv)










