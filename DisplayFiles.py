'''
This program will go through all Work subdirectorys in "D:\\Archvies" folder
and display all files that are three months or older.
'''
import os.path
import glob
import time

#Create a list of Work directorys in Archive folder
WORKDIR = glob.glob("D:\\Archives\\ASP*\\Work*")
#Variable holds three months of time in seconds
THREEMONTHSOLD = (time.time()) - (90 * 86400)

def display_files_to_delete():
    '''
    This program will go through all Work subdirectorys in "D:\\Archvies" folder
    and display all files that are three months or older.
    '''
    #Variable to keep counter of deleted files
    files_left = 0
    #Loop through each Work subdirectory and delete all .DCM files older then 3 months
    for mydir in enumerate(WORKDIR):
        #Store all directory files in a list
        dcmfiles = glob.glob(mydir[1] + "\\" + "*.dcm")
        #Compare Modified Date of each DCM file and delete if older then 3 Months
        for file in enumerate(dcmfiles):
            if os.path.getmtime(file[1]) < THREEMONTHSOLD:
                print(file[1] + " " + time.ctime(os.path.getmtime(file[1])))
                files_left += 1
    print("Total Files  that will be Deleted :" + str(files_left))

#Run program
display_files_to_delete()
