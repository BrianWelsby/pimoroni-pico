import cppmem
# Switch C++ memory allocations to use MicroPython's heap testing
cppmem.set_mode(cppmem.MICROPYTHON)
