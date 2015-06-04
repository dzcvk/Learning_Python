import re
print "Please type in the filename to convert:"
filename=str(raw_input(':>'))
fr=open(filename,'rb')
fw=open(filename+'_processed.txt','wb')
fd=open(filename+'_droped.txt','wb')
pattern=re.compile(r'^([^\r]{0,100}\w)([\s,\t])([^\r]{0,100})\r$')
lines=fr.readlines()
index=len(lines)
print 'Total Lines:%d'%(index)
raw_input("Click Enter to Continue")
errorlines=0
for i in range(index):
    match=pattern.match(lines[i])
    if match is None:
        errorlines=errorlines+1
        fd.writelines(lines[i])
    else:
        processedline=pattern.sub(r'\1!q!\3',match.group())
        print processedline
        fw.writelines(processedline+'\n')
print 'Dropedlines:%d'%(errorlines)
fr.close()
fw.close()
fd.close()
raw_input("Click Enter to Close")
