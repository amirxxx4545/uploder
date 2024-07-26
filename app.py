import os  
from flask import Flask, render_template, request  
from werkzeug.utils import secure_filename  

path = os.path.join("uploads")  
os.makedirs(path, exist_ok=True)  

app = Flask(__name__)  



all_format={'txt','jpg','png'}

def cheak(filname):
    
    return '.' in filname and filname.rsplit(".",1)[1] in all_format


@app.route("/")  
def index():  
    return render_template('form.html')  

@app.route("/submit", methods=["POST"])  
def showResult():  
    email = request.form["email"]  
    password = request.form["password"]  
    return render_template("result.html", email=email, password=password)  

@app.route("/upload")  
def upload():  
    return render_template("upload.html")  

@app.route("/uploaded", methods=['POST'])  
def savefile():  
    if "file" not in request.files:  
        return "No file part"  
    
    theFile = request.files["file"]  
    
    if theFile.filename == '':  
        return "No selected file"  

    
    if cheak(theFile.filename):
        
        
    
        try:  
            filename = secure_filename(theFile.filename)  
            goal_path = os.path.join(path, filename)  
            theFile.save(goal_path)  
            return "File uploaded successfully!"  
        except Exception as e:  
            return f"There is an error saving your file: {e}"  
    else:
        return "you file format is not allwed"
if __name__ == "__main__":  
    app.run(debug=True)