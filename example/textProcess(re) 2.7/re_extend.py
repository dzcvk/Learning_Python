import re
#

filename=input("Please type in the filename to filter the blank lines:\n")
fr=open(filename,'rb')
fw=open(filename+'_prc.csv','w')
lines=fr.readlines()
index=len(lines)
print('Total Lines:%d'%(index))
input("Click Enter to Continue")

start='(^)'
end='($)'
blank='(\s)'
eMail='(\w+@\w+.\w+)'
password='(\w+)'
#book=['a_bc@aa.comdsf adsf','adsfafd adsf ','google@qq.comdsf	adsf']
index=len(book)
pattern=re.compile(start+eMail+blank+password+end)
#
unmatchlines=0
for i in range(index):
	match=pattern.match(lines[i].decode('gbk','ignore'))
	if match is None:
		unmatchlines=unmatchlines+1
	else:
		processedline=pattern.sub(r'\1\2,\4\5',match.group())
		fw.writelines(processedline)
		# print(processedline)
		# print(match.group())
print(unmatchlines)
