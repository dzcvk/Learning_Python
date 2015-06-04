import re
print "Please type in the filename to convert:"
filename=str(raw_input(':>'))
fr=open(filename,'rb')
fw=open(filename+'_Exbreaked.txt','wb')
pattern=re.compile("([^\r]+)(\r)$")
lines=fr.readlines()
index=len(lines)
print 'Total Lines:%d'%(index)
raw_input("Click Enter to Continue")
for i in range(index-1):
    match=pattern.match(lines[i])
    processedline=pattern.sub(r'\1%q%\2',match.group())
#    print processedline
    fw.writelines(processedline+'\n')
fr.close()
fw.close()
raw_input("Click Enter to Close")
