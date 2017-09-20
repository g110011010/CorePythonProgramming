#encoding=utf-8
'本程序接受用户输入一个年份,然后调用函数判断是否为闰年,并输出结果给用户'
import sys
argv=sys.argv
def runnian(year):
    '接受一个参数年份,判断是否为闰年,返回判断结果'
    if (year%4==0 and year%100!=0) or (year%4==0 and year%100==0):
        return '%d是闰年' % year
    else:
        return "%d不是闰年" % year
print runnian(int(argv[1]))
