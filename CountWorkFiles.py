'''
This program will show total count of DCM files for each Work directory.
'''
import glob

#Create a list of Work directorys in Archive folder
WORKDIR = glob.glob("D:\\Archives\\ASP*\\Work*")

def count_workdir_files():
    '''
    This function will go through all Work subdirectories,
    and display total of DCM files for each Work subdirectory.
    '''
    for mydir in enumerate(WORKDIR):
        total_dcm_files = glob.glob(mydir[1] + "\\" + "*.dcm")
        print(mydir[1] + " has total of: " + str(len(total_dcm_files)) + ' files.')

#Run program
count_workdir_files()
