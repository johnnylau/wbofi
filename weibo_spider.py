#-*- coding: utf-8 -*-
import sys
import getopt
import getHeadIcon



#???????
def getFerList(userName, pageContent):
	pass



#帮助信息
def usage():
    print "wbofi usage:"
    print "-h --help: help message"
    print "-v --version: print version"
    print "-p --path: set output path"
    print "-u --user: set user id or name"
    print "--headicon: get user headIcon"

#版本信息  后面可以进行调整
def version():
    print "wbofi version 0.0.0.0"


def main(argv):
    path = ''
    user = ''
    try :
        opts, args = getopt.getopt(argv[1:], 'hvp:u:',['help', 'version', 'path=', 'user=', 'headicon'])
        '''getopt的三个参数：
        参数1： 待处理数组
        参数2： 短命令  短命令参数后面如果加上:则意味着后面要加参数 例如 p: 意味着输入 -p 后要加一个参数（路径） 
                h 则意味着输入 -h 不需要参数
        参数3： 长命令  长命令后面加 = 意味着后面要加参数  同上

        新增加命令的时候请务必修改此处
        '''
    except getopt.GetoptError, err:
        print str(err)
        usage()
        sys.exit(2)

#以下用于处理参数
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
            getHeadIcon.getHeadIcon(path, user)
            sys.exit(1)
        else:
            sys.exit(3)

if __name__ == "__main__":
	main(sys.argv)










