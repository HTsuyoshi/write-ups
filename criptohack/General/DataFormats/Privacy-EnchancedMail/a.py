from os import popen        
from ast import literal_eval
import Crypto.Util.number   
import argparse             

def str_proc(astr):
    anum = literal_eval('0x'+\
                        astr.replace("privateExponent:","").\
                        replace("\n","").replace(":","").replace(" ",""))
    return anum


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--filename',help="Specify the PEM Private Key file.")
    arg = parser.parse_args()
    pem_filename = arg.filename

    system_obj = popen("cat " + pem_filename +\
                       " | openssl rsa -text -noout | awk '/privateExponent/'"+\
                       " RS='prime1' | awk '/privateExponent/' RS=')' ")
    astr = system_obj.read()
    print(str_proc(astr))

if __name__=="__main__":
    main()
