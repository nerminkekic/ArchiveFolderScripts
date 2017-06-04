import glob

WORKDIR = glob.glob("D:\\Archives\\ASP*\\Work*")

for item in enumerate(WORKDIR):
    print(item[1])
    