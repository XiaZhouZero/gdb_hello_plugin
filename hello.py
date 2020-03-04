# -*- coding: utf-8 -*-
#!/usr/bin/python3

import gdb

class Hello(gdb.Command):
    """A hello command"""
    def __init__(self):
        super(self.__class__, self).__init__('hello', gdb.COMMAND_USER)

    def invoke(self, para_str, from_tty):
        print("Hello Debugger!")

# Register this command
Hello()