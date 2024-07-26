file_name="index.main.offor.js"
file_name2="h.jpg"

all_format={'txt','jpg','png'}

def cheak(filname):
    
    return '.' in filname and filname.rsplit(".",1)[1] in all_format



print(cheak("index"))