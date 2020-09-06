# coding: utf-8


import os
import re
import sys



def inlet(file_re, file_src, file_output):
    fo = open(file_re, "r")
    co = open(file_src, "r")
    fout = open(file_output, "w")
    colines = fo.readlines()

    for line in co.readlines():
        has_it = False
        linesrc = line = line.strip()
        while line:
            if not '/' in str(line): break
            matchObj = re.search(line, "{}".format(colines), re.M | re.I)
            if matchObj:
                has_it = True
                break
            else:
                data = re.search("(.*)/", line, re.M | re.I)
                if not data is None:
                    line = data.group().strip('/')
                    if not '/' in str(line): break
            pass
        if not has_it:
            fout.write("{}\n".format(linesrc))
    pass

    fo.close()
    co.close()
    fout.close()



if __name__ == "__main__":
    inlet("dataa", "datab", "output")
    pass
