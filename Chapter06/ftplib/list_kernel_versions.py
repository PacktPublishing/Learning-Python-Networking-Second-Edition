#!/usr/bin/env python3

from ftplib import FTP

entries = []
f = FTP('ftp.free.fr')
f.login()
f.cwd('/mirrors/ftp.kernel.org/linux/kernel/')
f.dir(entries.append)
print("%d entries:" % len(entries))
for entry in entries:
    print(entry)
f.quit()
