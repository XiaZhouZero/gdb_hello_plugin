# extend_gdb_with_python
Extend GDB with python-support

## Environment
- Ubuntu 18.04
- Python 3.6
- GDB 9.1

## Build
- Build gdb with python-support and target arm-none-eabi architecture
```bash
$ ./build.sh
```

## Usage
- Use hello.py in gdb
```
$ ./gdb
(gdb) source hello.py
(gdb) hello
Hello Debugger!
```