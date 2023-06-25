#!/bin/python3

import shutil

## UNFINISHED

def replace_in_file(filepath: str, to_replace: str, replacement: str):
    with open(filepath, 'r') as file:
        filedata = file.read()

    filedata = filedata.replace(to_replace, replacement)
    
    with open(filepath, 'w') as file:
        file.write(filedata)

print("ForgeTemplate Setup")

MCMOD = "src/main/java/PKG1/PKG2/MODID/McMod.java"
MIXINLOADER = "src/main/java/PKG1/PKG2/MODID/mixins/MixinLoader.java"
MIXINJSON = "src/main/resources/mixins.MODID.json"

package = input("Enter your mod package (eg. me.nixuge): ")
pkg1, pkg2 = package.split('.')
id = input("Enter your mod ID (eg. nochunkunload):")
name = input("Enter your full mod name (eg. No Chunk Unload): ")
author = input("Enter the mod author: ")
# description = input("Enter your mod description: ")
link = input("Enter your mod link: ")
if not "https://" in link and not "http://" in link:
    link = f"https://github.com/{author}/{link}"
version = input("Enter your mod version (or leave blank for 1.0.0)")

# pkg
for file in ("gradle.properties", MCMOD, MIXINLOADER, MIXINJSON):
    replace_in_file(file, "<MODPACKAGE>", package)

# id
for file in ("gradle.properties", MCMOD, MIXINLOADER, MIXINJSON):
    replace_in_file(file, "<MODID>", id)

# name
for file in ("gradle.properties", MCMOD):
    replace_in_file(file, "<MODNAME>", name)

# version
for file in ("gradle.properties", MCMOD):
    replace_in_file(file, "<MODVERSION>", version)

# name



# shutil.move() 
#package


