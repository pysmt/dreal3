import os, sys
import optparse

from setuptools import setup
from distutils.extension import Extension

p = optparse.OptionParser('%prog [options] [-- [setup_options]]')
p.add_option('--dreal-dir', help='directory of the dReal solver',
             default=None)

try:
    idx = sys.argv.index('--')
    optargs = sys.argv[1:idx]
    argv = sys.argv[idx+1:]
except ValueError:
    optargs, argv = sys.argv[1:], []

sys.argv = [sys.argv[0]] + argv

opts, args = p.parse_args(optargs)

if args:
    sys.argv = [sys.argv[0]] + args + sys.argv[1:]

DREAL_DIR = None
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if opts.dreal_dir is not None:
    DREAL_DIR = opts.dreal_dir
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DREAL_DIR = BASE_DIR

dreal_ext = Extension('_drealpy',
                        [os.path.join(BASE_DIR, 'dreal_python.i')],
                        swig_opts=['-I%s' % os.path.join(DREAL_DIR, "include/dreal")],
                        include_dirs=[os.path.join(DREAL_DIR, "include/dreal")],
                        library_dirs=[os.path.join(DREAL_DIR, "lib")],
                        runtime_library_dirs=[os.path.join(DREAL_DIR, "lib")],
                        libraries=['dreal', 'ibex', 'capd', 'nlopt', 'glpk'],
                        language='c',
                        )

short_description="dReal SMT-Solver Wrapper"
long_description=\
"""
========================
dReal SMT-Solver Wrapper
========================

Provides a basic wrapping around the dReal SMT Solver.

"""

setup(name='dreal',
      version="0.1",
      author='PySMT Team',
      author_email='info@pysmt.org',
      url='https://github.com/dreal/dreal3',
      license='BSD',
      description=short_description,
      long_description=long_description,
      ext_modules=[dreal_ext],
      py_modules=['drealpy'],
      classifiers = [
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
  )
