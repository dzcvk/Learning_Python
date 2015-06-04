from whoosh.index import create_in
from whoosh.fields import *

schema=Schema(title=TEXT(stored=True),path=ID(stored=True),content=TEXT(stored=True))  
ix=create_in("indexdir",schema)
writer = ix.writer()
writer.add_document(title=u"first",path=u"/files")
writer.add_document(title=u"Second document", path=u"/a",content=u" the second one second this haha is even more interesting!  \n second")
writer.commit()
searcher = ix.searcher()
results = searcher.find("content",u"second")
print(results)
#results = searcher.find("content", u"the")
#print(results[0])
#results = searcher.find("content", u"second")
#print(results[0])
