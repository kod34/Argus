<h1><center>Argus</center></h1>

<p align="center"> A script that checks the validity of emails through brute force, a dictionnary or simply inputing the full email.  

</p>

## 📝 Table of Contents

- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)


## 🏁 Getting Started <a name = "getting_started"></a>


### Prerequisites

```
Python
```

### Installing


```
pip3 install -r requirements.txt  
```

## 🎈 Usage <a name="usage"></a>

```
argus.py [-b] [-c charset] [-i filein] [-o fileout] [-t xx]
    
    -e <email>          Single validation check
    -i <file in>        Dictionary
    -b                  Brute-force 
    -c [characters]     Characters set to bruteforce - Default is [a-z0-9.]
    -t [interval]       Set time between two verifications - Default is 0.3s - range is [0-600]
    -o [file out]       Ouput results to file
    -h                  Help
    
    Examples:
    Single Email verification
        argus.py -e example@example.com [-t 0.1]
    Dictionary verification
        argus.py -i dictionary.txt [-o results.txt] [-t 0.1]
    Brute-force verification
        argus.py -b examp**3*5@example.com [-c 1g7.] [-o results.txt] [-t 0.1]
```

## ⛏️ Built Using <a name = "built_using"></a>

- Python

## ✍️ Authors <a name = "authors"></a>

- [@kod34](https://github.com/kod34)