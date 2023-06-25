#!/bin/python3

import shutil

## UNFINISHED

def replace_in_file(file: str, to_replace: str, replacement: str):
    with open(file, 'r') as file:
        filedata = file.read()

    filedata = filedata.replace(to_replace, replacement)
    
    with open(file, 'w') as file:
        file.write(filedata)

print("ForgeTemplate Setup")

package = input("Enter your mod package (eg. me.nixuge): ")
pkg1, pkg2 = package.split('.')
id = input("Enter your mod ID (eg. nochunkunload):")
name = input("Enter your full mod name (eg. No Chunk Unload): ")
description = input("Enter your mod description: ")
link = input("Enter your mod link: ")
version = input("Enter your mod version (or leave blank for 1.0.0)")

#pkg
for file in ("gradle.properties", "java/PKG1/PKG2/MODID/McMod.java", "java/PKG1/PKG2/MODID/mixins/MixinLoader.java", "src/main/resources/mixins.MODID.json"):
    replace_in_file(file, "<MODPACKAGE>", "<MODID>")



shutil.move() 
#package


