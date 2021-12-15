
Author: Jimmy Easter
email: jeaster@my365.bellevue.edu

Hello - Please follow these steps to run the project

0. Download Week_9_Module_12.zip

    ZIP FILE CONTENTS
    -- Test Case Template (Jimmy_Test Case Template_12_14_21.docx)
    -- README.TXT
    -- whatabook.py
    -- whatabook_init.sql



1. Backup Your Database [OPTIONAL]
    
    TO BACKUP your DB: (now) 
        run this command from a folder in your command prompt
        example: 
        jimmyleast:~/csd/csd-310/module_12$ mysqldump -u root -p --databases whatabook >  whatabook_backup.sql
    
    TO RESTORE your DB: (later)
        run this command from a "mysql" command prompt
        example: 
        mysql> source /home/jimmyleast/csd/csd-310/module_12/whatabook_backup.sql

2. Run WhatABook Database Setup Script
    Run this command from a mysql command prompt
    example:
    mysql> C:\Users\User\Desktop\whatabook_init.sql
    * where path_to_file lines up with where the file is on your system

4. Launch the Python Program
    # use your favorite IDE. 
    whatabook.py