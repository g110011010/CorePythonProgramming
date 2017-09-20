import sys
argv=sys.argv
def multiply(a,b):
    return a*b
print argv
print multiply(int(argv[1]),int(argv[2]))
print type(argv)
