import re
import string
print "Please type in the filename to Delete long lines:"
filename=str(raw_input(':>'))
fr=open(filename,'rb')
fw=open(filename+'_delonglined.txt','wb')
fd=open(filename+'_droped.txt','wb')
lines=fr.readlines()
index=len(lines)
print 'Total Lines:%d'%(index)
Maxlength=eval(raw_input("Delete lines longer than:"))
raw_input("Click Enter to Continue")
longlines=0
for i in range(index):
    length=len(lines[i])
    if (length>Maxlength):
        longlines=longlines+1
        fd.writelines('line %d  :'%(i)+lines[i])
        print '%d  :'%(longlines)+lines[i],
    else:
        fw.writelines(lines[i])
print '\nDropedlines:%d'%(longlines)
fr.close()
fw.close()
fd.close()
raw_input("Click Enter to Close")
