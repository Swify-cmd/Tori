import new_message # calling a module(a python file containing blocks of code such as functions)

new_message.hello()
new_message.bye()

import new_message as msg # alias to a module
from new_message import hello,bye # calling specific functions from a module instead of the whole module

msg.hello()
msg.bye()

hello()
bye()

# bonus tip!
# help("modules") # to list all built-in modules in Python
