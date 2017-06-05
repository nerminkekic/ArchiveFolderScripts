This is i a collection of Python scripts that i have writen for my production enviroment. 

1.  ArchiveFolderCleanUP.py script is used to remove old files from specific application folder.
    This script was writen so that it keeps the applicaiton directory clean. In my enviroment if these folders are left 
    to grow, eventually  they will crash production applicaiton. Therefore the need came to write this script. 
    It is writen to monitor for any new folders that start with "ASP". ASP folders are designated applicaiton folders that need 
    to be monitored and any files deleted after certain amount of time has passed. 

    ArchiveFolderCleanUP.py can easly be modified to fit in your enviroment. The parameters that i used is to delete any
    data that is older then three months. Constant "THREEMONTHSOLD" in the script is used for that parameter and 
    can be modified easly to reflect the time that is applicable for your enviroment. 

    WORKDIR list is used store all the directorys in the "D:\Archive" folder. You should change this to reflect the directory
    of your enviroment. 

2.  CountWorkFiles.py is script that will go into each Work direcotry and display total amount of files. This script i have used 
    to help with troubleshooting. Typcally Work directorys should have no more then 10-15 files while the application is working
    with them. If Work directorys starts building up large amount of files, that is a red flag that something might not be processing
    properlly with the applicaiton. 

3.  DisplayFiles.py displays the actaull file names, with last modified date in each Work sub directory that are three months
    and older. 

