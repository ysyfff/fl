
def readFile(fn, buf_size=1024):
    f = open(fn, 'rb')
    while True:
        c = f.read(buf_size)
        if c:
            yield c
        else:
            break
    f.close()

f = readFile('explore_stp.py')
print f.next()
print '1-'*40
print f.next()
print '2-'*40
print f.next()