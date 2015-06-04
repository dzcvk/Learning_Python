import re
filename=str(raw_input("Please type in the filename to filter the blank lines:\n"))
fr=open(filename,'rb')
fw=open(filename+'_deblanked.txt','wb')
pattern=re.compile("^\r$")
lines=fr.readlines()
index=len(lines)
print 'Total Lines:%d'%(index)
raw_input("Click Enter to Continue")
blanklines=0
for i in range(index):
    line=pattern.match(lines[i])
    if line is None:
        fw.writelines(lines[i])
    else:
        blanklines=blanklines+1
print "Total blankines:%d"%(blanklines)
fr.close()
fw.close()
raw_input("Click Enter to Close")
