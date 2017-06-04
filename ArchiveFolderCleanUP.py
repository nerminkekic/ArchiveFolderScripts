'''
This program will go through all Work subdirectorys in "D:\\Archvies" folder
and delete all DCM files older then three months.
'''
import os.path
import glob
import time

#Create a list of Work directorys in Archive folder
WORKDIR = glob.glob("D:\\Archives\\ASP*\\Work*")
#Variable holds three months of time in seconds
THREEMONTHSOLD = (time.time()) - (90 * 86400)

def deletdcmfiles():
    '''
    This function will go through all Work subdirectorys in "D:\\Archvies" folder
    and delete all DCM files older then three months.
    '''
    #Variable to keep counter of deleted files
    deleted_files = 0
    #Loop through each Work subdirectory and delete all .DCM files older then 3 months
    for mydir in enumerate(WORKDIR):
        #Store all directory files in a list
        dcmfiles = glob.glob(mydir[1] + "\\" + "*.dcm")
        #Compare Modified Date of each DCM file and delete if older then 3 Months
        for file in enumerate(dcmfiles):
            try:
                if os.path.getmtime(file[1]) < THREEMONTHSOLD:
                    print("Deleted " + file[1] + " " + time.ctime(os.path.getmtime(file[1])))
                    os.remove(file[1])
                    deleted_files += 1
            except FileNotFoundError:
                print("File does not exist.")

    print("Total Files Deleted :" + str(deleted_files))

#Run program
deletdcmfiles()
