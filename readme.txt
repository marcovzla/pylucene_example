instructions to install pylucene on linux:

conda create -n pylucene python=3
source activate pylucene
conda install gxx_linux-64

curl -O http://apache.cs.utah.edu/lucene/pylucene/pylucene-7.5.0-src.tar.gz
tar xzvf pylucene-7.5.0-src.tar.gz
cd pylucene-7.5.0/jcc/
JCC_ARGSEP=" " JCC_CFLAGS="-fpermissive -D__STDC_FORMAT_MACROS" JCC_JDK=/usr/lib/jvm/java-1.8.0 LD_LIBRARY_PATH=$CONDA_PREFIX/lib python setup.py build
JCC_JDK=/usr/lib/jvm/java-1.8.0 python setup.py install
cd ..

vim Makefile
# set these variables:
#   PREFIX_PYTHON=$(CONDA_PREFIX)
#   ANT=JAVA_HOME=/usr/lib/jvm/java-1.8.0 /usr/bin/ant
#   PYTHON=$(PREFIX_PYTHON)/bin/python3
#   JCC=$(PYTHON) -m jcc --shared
#   NUM_FILES=8
make
make test
make install






for mac:

install clangxx_osx-64 instead of gxx_linux-64

use $(/usr/libexec/java_home)

https://github.com/Homebrew/legacy-homebrew/issues/39492#issuecomment-104934179
