#!/usr/bin/env python3

from ftplib import FTP

f = FTP('ftp.free.fr')
f.login()
f.cwd('/mirrors/ftp.kernel.org/linux/kernel/')
entries = f.nlst()
entries.sort()
print(len(entries), "entries:")
for entry in entries:
    print(entry)
f.quit()
