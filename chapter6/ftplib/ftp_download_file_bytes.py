#!/usr/bin/env python3

import os, sys
from ftplib import FTP

f = FTP('ftp.free.fr')
f.login()

f.cwd('/mirrors/ftp.kernel.org/linux/kernel/Historic/')
f.voidcmd("TYPE I")

datasock, size = f.ntransfercmd("RETR linux-0.01.tar.gz")
bytes_so_far = 0
fd = open('linux-0.01.tar.gz', 'wb')

while 1:
    buf = datasock.recv(2048)
    if not buf:
        break
    fd.write(buf)
    bytes_so_far += len(buf)
    print("\rReceived", bytes_so_far, end=' ')
    if size:
        print("of %d total bytes (%.1f%%)" % (
            size, 100 * bytes_so_far / float(size)), end=' ')
    else:
        print("bytes", end=' ')
    sys.stdout.flush()

print()
fd.close()
datasock.close()
f.voidresp()
f.quit()
