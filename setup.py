#!/bin/python3

import os
import shutil

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

if not os.path.isfile("dev"):
    if os.path.isdir(".git"):
        shutil.rmtree(".git")
        print("Git folder removed")
    else:
        print("Git folder already removed")

package = input("Enter your mod package (eg. me.nixuge): ")
pkg1, pkg2 = package.split('.')
id = input("Enter your mod ID (eg. nochunkunload): ").lower()
name = input("Enter your full mod name (eg. No Chunk Unload): ")
author = input("Enter the mod author: ")
dev_username = input("Enter your dev username: ")
description = input("Enter your mod description: ")
link = input("Enter your mod link (will be replaced by github.com/author/... if no full url set): ")
if not "https://" in link and not "http://" in link:
    link = f"https://github.com/{author}/{link}"
version = input("Enter your mod version (or leave blank for 1.0.0): ")
if not version or version.strip() == "":
    version = "1.0.0"

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

gradleproperties_only = {
    "<MODAUTHOR>": author,
    "<MODDESCRIPTION>": description,
    "<MODLINK>": link,
    "<DEVUSERNAME>": dev_username
}
for to_replace, replacement in gradleproperties_only.items():
    replace_in_file("gradle.properties", to_replace, replacement)



# rename 1 by 1 to not have to delete folders after lol
shutil.move("src/main/java/PKG1/PKG2/MODID", f"src/main/java/PKG1/PKG2/{id}") 
shutil.move("src/main/java/PKG1/PKG2", f"src/main/java/PKG1/{pkg2}") 
shutil.move("src/main/java/PKG1", f"src/main/java/{pkg1}") 

shutil.move("src/main/resources/mixins.MODID.json", f"src/main/resources/mixins.{id}.json")

# readme
with open("README.md", "w") as file:
    file.write("# " + name + "\n")
    file.write(description)

if input("Run git init? (y/n): ").lower() in ['y', "yes"]:
    os.system("git init")

# not sure if this works on windows
if input("Try to delete this script? (y/n): ").lower() in ['y', "yes"]:
    os.remove("setup.py")
