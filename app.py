from flask import Flask,render_template,request
from reviewer import analyze_code

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    feedback=""
    code=""
    if request.method=='POST':
        code=request.form['code']
        feedback=analyze_code(code)
    return render_template('index.html',feedback=feedback,code=code)
if __name__=='__main__':
    app.run(debug=True)