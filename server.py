from flask import Flask, render_template,request,redirect,session
app=Flask(__name__)
app.secret_key='meow'

@app.route('/')
def count():
    num=0
    session['num']+=1
    return render_template('index.html')

@app.route('/plus2')
def double():
    num=0
    session['num']+=2
    return redirect('/')

@app.route('/reset')
def reset():
    session['num']=0
    return redirect('/')


app.run(debug=True)
    

