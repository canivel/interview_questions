import os
c = "\n File Content test \n"
f_name = "file.tst"
with open(f_name, "a+") as f:
    f.write(c)


if os.path.exists(f_name):
    f = file(f_name, "r+")
    for line in f:
        print line


f.close()