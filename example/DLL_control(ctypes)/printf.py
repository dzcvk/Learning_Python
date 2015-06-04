import ctypes
from ctypes import *
#help(ctypes)

# libc=cdll.LoadLibrary('msvcrt.dll')
# libc.printf('t')
# word=c_int(0)
# libc.scanf("%d",word)
# print(libc.time(None))
# print(word)
# libc.scanf("%d",word)


# print(windll.kernel32)
messagebox=windll.user32.MessageBoxW
messagebox(0,'Great','hello',0)