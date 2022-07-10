from pathlib import Path
import os
parition = 'dev'
speaker_dirs = str(os.getcwd()).glob("*")             #(* i.e., All) directories and files in the folder
print(speaker_dirs)
for s in speaker_dirs:
    print()