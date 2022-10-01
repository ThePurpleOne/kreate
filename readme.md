# KREATE

## Install

### Depedencies
Pip packages:
```bash
pip install shutil
pip install datetime
pip install colorama
```

You'll also need `tree`:
```bash
pacman -S tree
apt-get install tree
yum install tree
```


### Make Kreate executable 
Clone the repo
```bash
git clone git@github.com:ThePurpleOne/kreate.git
```

Add the script to usr/bin and make it executable
```bash
cd kreate/
sudo cp kreate.py /usr/bin/kreate
sudo chmod ugo+x /usr/bin/kreate
```

Add the base files at `~/.kreate/`
```bash
cp -r .kreate/ ~/.
```

You're all set.

## Run
Run it
```bash
kreate 
```


You should have a menu popping
```
1 - Complete project                 
2 - Module (code + header)                    
3 - Code only                        
4 - Header only                      
5 - Metafiles (Makefile, readme, clang, gitignore)                    
6 - Makefile                    
7 - clang                    
8 - readme                    
9 - gitignore
```