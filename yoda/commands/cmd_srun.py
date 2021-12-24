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
    f2 = open(solDir+"tests", "r")  
    lines=f2.readlines()[0]
    f2.close()
    cases=json.loads(lines)
    correct=0
    testCase=0
    returnstatus=build()
    if returnstatus != 0:
        click.secho('Compilation Error',fg='bright_red')
        return
    for case in cases:
        testCase+=1
        ans=case['correct_answers']
        input=case['test']
        if isinstance(ans, list):
            ans=ans[0].strip()
        else:
            ans=ans.strip()
        if isinstance(input, list):
            input=input[0].strip()
        else:
            input=input.strip()
        myfile = Path(solDir+'input.txt')
        myfile.touch(exist_ok=True)
        f = open(myfile,'w')    
        f.writelines(input)
        f.close()
        
        run()
        
        with open(solDir+'/'+"output.txt", 'r') as file:
            myanswers = file.read().strip()
        click.secho(f'Test Case {testCase} :\n',fg='magenta')
        click.echo('Your Answer: \n')
        click.echo(myanswers)
        click.echo('........................\n')
        click.echo('Expected Answer: \n')
        click.echo(ans+'\n')

        if (myanswers==ans):
            correct+=1
            click.secho(f'Test Case {testCase} Passed ✅\n',fg='green')
        else:
            click.secho(f'Test Case {testCase} Failed ❌\n',fg='red')
        
            
    click.secho(f'{correct}/{testCase} Cases Passed\n',fg='yellow') 

    if testCase==correct:
        click.secho('✅ Correct Answer ✅\n',fg='bright_green')
    else:
        click.secho('❌ Wrong Answer ❌\n',fg='bright_red')
