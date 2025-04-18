# Instruction to run:
1) Clone the repo
2) Go and create a copy of data folder outside the repo folder. For example if path of repo is home/user/GPTJ, create the copy of data folder outside the repo for example home/user/data
3) Download docker
4) Go to cmd and insert the following commands:

     a) set cmd's path to GPTJ folder. Can be done cd [path where you have downloaded the rep]/GPTJ.
   
     b) docker build -t my_app . (Full stop is part of the command)
   
     c) docker run -v [path of copied data folder]:/app/data -p 8501:8501 my_app
     
    
