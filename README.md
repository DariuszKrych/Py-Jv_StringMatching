# Project Introduction

A group project created by Dariusz Krych (DK) & Nathan Micallef (NM) for the CIS1221 module in UM with the title of the submitted work being "A3-Stringmatching Project".    
This project was meant as a way of practicing coding while simultaneously creating something interesting.  
The project at it's core pertains to string matching algorithms.
The code in Python and Java have the same string matching algorithms implemented.  
This is meant to simply showcase the performance difference between Python and Java. 
The Python and Java code was written and maintained by DK & NM respectively throughout late 2024.  


# Evaluation Guidelines

#### Aquisition of data for string matching algorithms.
- Is the data appropriate for comapring various string matching algorithms?
- Is the data processed and formatted to a size where running algorithms through it takes a reasonable, measurable amount of time for comparisons sake between alogrithms (no more than a few seconds per algorithm to run)?
- Is the method of processing the data acceptable and how easy/difficult is selecting given processed data (.csv with all reviews for x game in 2017 on steam) for the algorithms to run through?

#### Accuracy of algorithm implementation.
- Are the algorithms written properly in accordance to their theoretical description?

#### General code quality.
- Are there bugs, if so how serious are they? 
- Is the code easily editable for example how easy/hard is it to add another algorithm? 
- Are there any pieces of code which are repeated?


# Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and/or testing purposes.  
With the first three steps being mandatory and the final step being optional if the user wishes to unlock extra functionality.

### Step 1: Download the repository

Go to the repository on the github website, click on the green code button and click on 'Download ZIP'
or copy the web URL seen in the same menu and in CMD type WGET (insert copied URL).

### Step 2: Setup the environments for running the project

1. Python environment setup: Conda env or a venv
In the 'Python' folder you will find a 'environment.yml' and a 'requirements.txt' file for creating an environment with the required libraries in a Conda env or a venv respectively as personally preffered.

    #### Conda Env   (option 1)
    - open the 'Anaconda Prompt'
    - type: cd path/to/project/folder/Python/env_setup_files
    - type: conda env create -f environment.yml -n String_Matching_Py_Env
    - type: conda activate String_Matching_Py_Env
    #### Venv        (option 2)
    - open CMD
    - type: cd path/to/project/folder/Python/env_setup_files
    - type: python -m venv String_Matching_Py_Venv
    - Windows type: String_Matching_Py_Venv\Scripts\activate
    - Linux/MacOS type: source String_Matching_Py_Venv/bin/activate
    - type: pip install -r requirements.txt  

2. Java setup:

    ####
    - Install intellij using this [link](https://www.jetbrains.com/idea/download/?source=google&medium=cpc&campaign=EMEA_en_WEST_IDEA_Branded&term=intellij&content=693349187751&gad_source=1&gclid=Cj0KCQiA4L67BhDUARIsADWrl7FPqNNOjc-STfK8U8uynHYUVBqTb__dXFDBgTAo9_MAU6hknkd48gQaAgMGEALw_wcB&section=windows)
    - Open intellij, click Open 
    - Select the Java file
    - click the arrow next to String Matching.1
    - click the arrow next to the blue src folder
    - click on main class
    - click 'setup JDK' on top right corner
    - click downlaod JDk
    - then click download

### Step 3: Running the project code
*
    - Open up path/to/project/folder/Python in your preferred IDLE/IDE and set the created Python env to run the Python code in main.py.  
    In an IDE such as pycharm for example, press on your current env in the bottom right, press add new interpreter, press add local interpreter.  
    (option 1) For a conda env select the Conda Environment option, select the env created earlier press ok.  
    (option 2) For a Venv select the Virtualenv Environment option, select the existing option and go to path/to/project/folder/Python/env_setup_files/your_created_venv_name/Scripts/python.exe , then press ok.  
    Run main.py.  

    - Open up path/to/project/folder/Java in your preferred IDLE/IDE to run the Java code.

### Step 4: (EXTRA - for additional functionality)

Following this step will unlock the functionality of splitting the steam 2017 game review csv database into separate csv game review files.
The project comes pre-packaged with a few csv game review files. The csv game review files are used as real world data for use with the string matching algorythms.

*
    - Downloading :  
 The database can be downloaded from [here](https://www.kaggle.com/datasets/andrewmvd/steam-reviews?resource=download)  
Download -> Download Dataset As Zip (719mb)

    - Extracting :  
 Extract the achive.zip. This will create a achive folder with a 2.0GB dataset.csv file inside it.

    - Moving :  
 Move the dataset.csv from the archive folder to the Put_Dataser_Here folder found in the root of this project.