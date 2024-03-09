
from flask import Flask,request,render_template,session
app = Flask(__name__)
app.template_folder='templates/'
app.config['SECRET_KEY']="987458744kjhkjcbvcbv#$%lpoplxjciuoy"

@app.route('/index')
def welcome_page():
    return render_template('login.html')

@app.route('/login',methods = ['POST'])
def authenticate():
    error = ''
    if request.method == 'POST':
        formdata = request.form
        if formdata and formdata.get('username') and formdata.get('password'):
            if formdata.get('username') == 'Admin' and formdata.get('password') == 'Admin123':
                session['userinfo']= formdata.get('username')
                return render_template('home.html')
            else:
                error = 'invalid crediantials'
        else:
            error = 'Username And Password can not be empty'
    return render_template('login.html',error = error)

@app.route('/show', )
def show_list():
    if session.get('userinfo'):
        return render_template('list.html', values = ['A','B','C'])
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    if session.get('userinfo'):
        session.pop('userinfo')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)