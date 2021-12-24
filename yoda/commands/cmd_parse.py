import click
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import threading
import shutil
from pathlib import Path 
import os
import subprocess

template='/home/nm/Code/Sublime/template.cpp'
solpath='/home/nm/Code/Sublime/solution.cpp'
solDir='/home/nm/Code/Sublime/'
url=''
timelimit=''
memorylimit=''
problemName=''
def MakeHandlerClassFromFilename(filename):
    class HandleRequests(BaseHTTPRequestHandler):
        def do_POST(self):
            global url,timelimit,memorylimit,problemName,solDir
            try:
                content_length = int(self.headers['Content-Length'])
                body = self.rfile.read(content_length)
                tests = json.loads(body.decode('utf8'))
                problemName=tests['name']
                url=tests['url']
                memorylimit=str(tests['memoryLimit'])
                timelimit=str(tests['timeLimit'])
                tests = tests["tests"]
                ntests = []
                for test in tests:
                    ntest = {
                        "test": test["input"],
                        "correct_answers": [test["output"].strip()]
                    }
                    ntests.append(ntest)
                nfilename = solDir+ filename
                with open(nfilename, "w") as f:
                    f.write(json.dumps(ntests))
            except Exception as e:
                print("Error handling POST - " + str(e))
            threading.Thread(target=self.server.shutdown, daemon=True).start()
    return HandleRequests


class CompetitiveCompanionServer:
    def startServer(filename):
        host = 'localhost'
        # port = 12345
        port = 1327
        HandlerClass = MakeHandlerClassFromFilename(filename)
        httpd = HTTPServer((host, port), HandlerClass)
        httpd.serve_forever()
        print("Server has been shutdown")

def prepend_line(file_name, line):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.cpp'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)


@click.command()
def cli():
    click.secho("Listening to Competitive Companion 🚀",fg='green') 
    CompetitiveCompanionServer.startServer('tests')

    myfile = Path(solpath)
    myfile.touch(exist_ok=True)
    f = open(myfile,'w')    
    shutil.copyfile(template,myfile)
    f.close()
    prepend_line(solpath,"// Url: "+url+"\n"+"// Time Limit: "+timelimit+'\n'+"// Memory Limit: " +memorylimit)
    os.system("subl "+solpath)    
    click.secho("🎊 Test Cases Parsed 🎊",fg='bright_green')
    
