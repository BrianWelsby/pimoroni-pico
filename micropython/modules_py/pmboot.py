import cppmem
# Switch C++ memory allocations to use MicroPython's heap test
cppmem.set_mode(cppmem.MICROPYTHON)
