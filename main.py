import urllib2
import os.path
import url
def getUserName():
    print "usrname:"
    user = raw_input()
    print "password"
    password = raw_input()
    return user,password
def getFileInput(filename) :
	with open(filename) as f:
		import json
		ret = json.loads(f.read())
	return ret["username"] , ret["password"]
if __name__ == "__main__":
    userfile = os.path.expanduser("~/.atcoder")
    user = ""
    password = ""
    if not os.path.exists(userfile):
    	user,password = getUserName()
    else :
    	try :
	    	user,password  = getFileInput(userfile)
	    	print user,password
	    except :
	    	print "Invalid format for %s " %userfile
	    	getUserName()