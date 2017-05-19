from store_data import store_data
from validate import validate
import numpy as np
import pandas as pd
import os
from write_errors import write_errors

def makeconnection(path,port):
    port_no = str(port)
    os.chdir(path)          #('Text_Corrector/LanguageTool-3.7/')
    os.system('java -cp languagetool-server.jar org.languagetool.server.HTTPServer --port '+port_no)


string = 'ahaProducts.csv'
pid,data = store_data(string)
path = 'LanguageTool-3.7/'
port = 8081
newpid = os.fork()

if newpid != 0:
	makeconnection(path,port)
	
else:
	data = data[range(10)]
	err = data.apply(lambda x: validate(x,port))
	write_errors(pid,data,err)
	os._exit(0)