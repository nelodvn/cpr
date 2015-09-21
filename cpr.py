import clipboard
import sys

def usage():
    print """[*] cpr.py

Usages:
    ./ctc /path/to/file
                    Copy the content of a file to the clipboard.
                    Now just ctrl+v wherever you want.
    
    ./ctc -c /path/to/file 
                    Copy the clipboard content to the specified file.
                    
"""

def copy(dest):
    try:
        f = open(sys.argv[1], "r")
        payload = f.read()
        clipboard.copy(payload)
        f.close()
        sys.exit()
    except Exception as e:
        print "[*] Impossible to open file %s." %sys.argv[1]
        print e

def paste(dest):
    try:
        f = open(dest, "w")
        payload = clipboard.paste()
        f.write(payload)
        f.flush()
        f.close()
        sys.exit()
    except Exception as e:
        print "[!] Impossible to write to file: %s." % dest
        print e

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if "-h" in sys.argv:
            usage()
            sys.exit()
        if "-c" in sys.argv:
            paste(sys.argv[2])
        else:
            copy(sys.argv[1])
            
    else:
        print "No input. See -h for help."