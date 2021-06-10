from flask import Flask, render_template, url_for, flash, redirect
from forms import RegForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'egwfla78420fsjlbr892n'

dest = [
{
    'location': 'Maldives',
    'price':'40k'
},
{
    'location': 'Berlin',
    'price':'6k'
}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/destination")
def destination():
    return render_template('destination.html', destinations = dest)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('reg.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data  == 'hej@mail.com' and form.password.data == 'password':
            flash('You are logged in!', 'success')
            return redirect(url_for('home'))
        else: 
            flash('Login Unsuccessful', 'danger')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)