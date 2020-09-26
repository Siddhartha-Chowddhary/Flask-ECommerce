from Imports import *
from App_Settings import *
from Routing import *
from Database import *


# usersflies = '/static'

class RegisterForms(FlaskForm):

  Name = StringField('Name', [DataRequired(), Length(min=1, max=50)])


  Email =  StringField('Email', [DataRequired(), Email(), Length(min=6, max=120)])

  Username = StringField('Username', [DataRequired(), Length(min=5, max=20)])
  Password = PasswordField('Password', [DataRequired(), Length(min=6, max=15)])

  Address = StringField('Address', [Length(min=2, max=120)])


  # Password =  PasswordField('Password', [
  #   DataRequired(), EqualTo('confirm', message='Password do not match')

  #   ])
  submit = SubmitField('Sign Up')

  def validate_Username(self, Username):
    user = User.query.filter_by(Username=Username.data).first()
    if user:
      raise ValidationError('That username is taken please choose a diffrent one')

  def validate_Email(self, Email):
      user = User.query.filter_by(Email=Email.data).first()
      if user:
        raise ValidationError('That Email is taken please choose a diffrent one')



  # def validate_Social_Media_Link(self, Social_Media_Link):
  #     user = User.query.filter_by(Social_Media_Link=Social_Media_Link.data).first()
  #     if user:
  #       raise ValidationError('That Social Media account is taken please choose a diffrent one')


class LoginForms(FlaskForm):


  Username = StringField('Username', [DataRequired(), Length(min=4, max=50)])
  Password = PasswordField('Password', [DataRequired(), Length(min=6, max=15)])

  submit = SubmitField('Login')



@app.route('/register', methods=['GET','POST'])
def register():

  if current_user.is_authenticated:
    return redirect(url_for('index2'))

  form = RegisterForms()
  if form.validate_on_submit():
    Hashed_Password =  bcrypt.generate_password_hash(form.Password.data).decode('utf-8')
    user = User(Full_Name = form.Name.data, Email=form.Email.data, Username=form.Username.data, 
                Password=Hashed_Password, Address=form.Address.data)
    db.session.add(user)
    db.session.commit()
    flash (f'Account Created for {form.Username.data}! You can now Signin', 'success')

    os.chdir(os.path.join('static', 'Users'))
    os.makedirs(f'{form.Username.data}')


    os.makedirs(f'{form.Username.data}/Shopping_Cart_Items/')
    
    print(form.Username.data)
    return redirect(url_for('LOGIN'))
  return  render_template('/Forms/Register.html', title='Register', form=form)


@app.route('/LOGIN', methods=['GET','POST'])
def LOGIN():

  if current_user.is_authenticated:
    return redirect(url_for('index2'))
  form2 = LoginForms()
  if form2.validate_on_submit():
    user = User.query.filter_by(Username=form2.Username.data).first()
    if user and bcrypt.check_password_hash(user.Password, form2.Password.data):
      login_user(user)
      print(current_user.Username)
      return redirect(url_for('index2'))
    else:
      flash('Login Unsuccessful')
  return  render_template('/Forms/LoginForms.html', title='LOGIN', form2=form2)

@app.route('/LOGOUT'  )
def LOGOUT():
  logout_user()
  return redirect(url_for('index2'))
