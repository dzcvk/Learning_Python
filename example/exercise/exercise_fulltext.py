from whoosh.index import create_in
from whoosh.fields import *

schema=Schema(title=TEXT(stored=True),path=ID(stored=True),content=TEXT(stored=True))  
ix=create_in("indexdir",schema)
writer = ix.writer()
writer.add_document(title=u"First document",path=u"/a",content=u"this is the the first haha document we’ve added!")
writer.add_document(title=u"Second document", path=u"/a",content=u" the second one this haha is even more interesting!")
writer.commit()
searcher = ix.searcher()
results = searcher.find("content", u"the first haha document")
print(results)
#results = searcher.find("content", u"the")
#print(results[0])
#results = searcher.find("content", u"second")
#print(results[0])
