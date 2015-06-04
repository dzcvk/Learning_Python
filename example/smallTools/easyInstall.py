import os
package=input("please tpye in package name:\n>>")
os.system('easy_install -i http://c.pypi.python.org/simple -U %s'%package)
input("enter to exit")