import click
import json
from pathlib import Path 
import os
import subprocess

template='/home/nm/Code/Sublime/template.cpp'
solpath='/home/nm/Code/Sublime/solution.cpp'
solDir='/home/nm/Code/Sublime/'

def changeDir():
    global solDir
    os.chdir('..')
    os.chdir(solDir)

def compile():
    compilecmd='g++ -std=c++17 -w -o solution -O2'
    listcompile=compilecmd.split(' ')
    listcompile.append('solution.cpp')
    x=subprocess.call(listcompile)
    return x
def run():
    subprocess.call('./solution')

def build():
    compilecmd='g++ -std=c++17 -Wshadow -Wall -o solution -g -fsanitize=address -fsanitize=undefined -D_GLIBCXX_DEBUG'
    listcompile=compilecmd.split(' ')
    listcompile.append('solution.cpp')
    x=subprocess.call(listcompile)
    return x

@click.command()
def cli():
    changeDir()
    global solDir,solpath  
    returnstatus=compile()
    if returnstatus != 0:
        click.secho('Compilation Error',fg='bright_red')
        return
    run()
    click.secho("......................\n")