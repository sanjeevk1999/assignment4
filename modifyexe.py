# Author: Sanjeev Krishnan 
# Date: 2021/11/15
# Usage: modifyexe.py <password>
# Description: Modify the password of the exe file
#              The password is hashed using sha1
#              The password is stored at the offset # 0x1D3E4
#              The exe file is modified in place
# Note: It works depending on the offset of sha1 stored in exe.

import hashlib
import sys

def modify(file, password, offset):
    sha1 = hashlib.sha1(password.encode('utf-8')).digest()
    with open(file, 'r+b') as f:
        f.seek(offset)
        f.write(sha1)
        
if __name__ == '__main__':
    offset = 0x1D3E4
    file = "91616862.program2.exe"
    password = sys.argv[1].strip()
    modify(file, password, offset)
    print('Done')


