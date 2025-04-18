# Instruction to run:
1) Clone the repo
2) Go and create a copy of data folder outside the repo folder. For example if path of repo is home/user/GPTJ, create the copy of data folder outside the repo for example home/user/data
3) Download docker
4) Go to cmd and insert the following commands:
     a) docker build -t my_app .
   
     b) docker run -v <path of copied data folder>:/app/data -p 8501:8501 my_app
     
    
