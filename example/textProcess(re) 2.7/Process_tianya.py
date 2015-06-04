import re
filename=str(raw_input("Please type in the filename to convert:\n"))
fr=open(filename,'rb')
fw=open(filename+'_processed.txt','wb')
pattern=re.compile("^[^\t\n@]{1,50}@[^\t\n\.@]{1,50}\.[^\t\n@]{1,50}\t[^\t\n]{0,50}$")
lines=fr.readlines()
index=len(lines)
print 'Total Lines:%d'%(index)
raw_input("Click Enter to Continue")
errorlines=0
for i in range(index):
    match=pattern.match(lines[i])
    if match is None:
        errorlines=errorlines+1
    else:
        print match.group()
        fw.writelines(match.group()+'\n')
print errorlines
fr.close()
fw.close()
