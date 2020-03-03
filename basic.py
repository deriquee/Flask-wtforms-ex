from flask import Flask,render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,DateTimeField,RadioField,SelectField,TextField,TextAreaField
from wtforms.validators import DataRequired

app=Flask(__name__)

app.config['SECRET_KEY']='myseckey'

class InfoForm(FlaskForm):

    name = StringField("Name:",validators=[DataRequired()])
    wellness=BooleanField("Are you vaccinated?")
    gender=RadioField("Gender:",choices=[('gen_1','Male'),('gen_2','Female')])
    food_choice=SelectField('Pick your fav food',choices=[('chi','chicken'),('bf','beef')])
    bio=TextAreaField()
    submit=SubmitField("Submit")

@app.route('/',methods=['GET','POST'])
def index():
    form=InfoForm()
    if form.validate_on_submit():
        session['name']=form.name.data
        session['wellness']=form.wellness.data
        session['gender']=form.gender.data
        session['food_choice']=form.food_choice.data
        session['bio']=form.bio.data

        return redirect(url_for("thankyou"))

    return render_template('index.html',form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if  __name__=='__main__':
    app.run(debug=True)
