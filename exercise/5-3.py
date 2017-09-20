import sys
argv=sys.argv
def grade(a):
    result=""
    if a>100 or a<0:
        result="you have give a wrong number"
    elif a>=90:
        result='A'
    elif a>=80:
        result='B'
    elif a>=70:
        result='C'
    elif a>=60:
        result='D'
    else:
        result='F'
    return result
print grade(int(argv[1]))
