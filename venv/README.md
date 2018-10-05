# packed_project
This project focuses on Python folder structure, Documenation, Logging &amp; Unit testing (using pytest)

1. When we create virtual environment, folders like, bin, inclue, lib, lib64 are automatically created.</br >
   For demostration purpose, under venv folder, I created my source code folder by name **packed_project**
    
2. We need to  create setup file first. check the same for the sample content
    and we have to execute the same to get the relevant files created under **packed_project.egg-info**
    command to execute setup.py file (if you are developing a project from scratch), 
    
    `$ python setup.py develop`
    
    If you are setting up any existing project, then
    
    `$ python setup.py build`
    
    `$ python setup.py install`
    
3.  The above step generates **packed_project.egg-info** folder and files under it (or) it will install all the necessary dependencies given in setup.py

4.  Under our source folder, packed_project, we need to have `__init__.py` which will execute before every file executes. We need to include all the files in it so that it can bring out all the libraries under the folder

5.  
