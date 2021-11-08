A script that checks the validity of emails through brute force, a dictionnary or simply inputing the full email.  
  
## Installation  
  
pip3 install -r requirements.txt  
  
## Usage  
  
emailreconer.py [-b] [-c charset] [-i filein] [-o fileout] [-t xx]
    
    -e <email>          Single validation check
    -i <file in>        Dictionary
    -b                  Brute-force 
    -c [characters]     Characters set to bruteforce - Default is [a-z0-9.]
    -t [interval]       Set time between two verifications - Default is 0.3s - range is [0-600]
    -o [file out]       Ouput results to file
    -h                  Help
    
    Examples:
    Single Email verification
        emailreconer.py -e example@example.com [-t 0.1]
    Dictionary verification
        emailreconer.py -i dictionary.txt [-o results.txt] [-t 0.1]
    Brute-force verification
        emailreconer.py -b examp**3*5@example.com [-c 1g7.] [-o results.txt] [-t 0.1]
  
## Disclaimer  
The sole purpose of writing this program was research, its misuse is the responsibility of the user only.