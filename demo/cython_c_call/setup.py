from distutils.core import setup, Extension
from Cython.Distutils import build_ext

setup(
        cmdclass={'build_ext': build_ext},
        ext_modules=[Extension("fibonacci_with_cython", sources=["Fibonacci.pyx", "fib.c"])]
)
