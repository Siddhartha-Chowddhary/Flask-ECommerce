from Imports import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '657413574sfdsdf6b34c4d85856sd455afs6487f015be5d62694e08d198a1a4d215af19a1555'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Soncur_Users.db'
# app.config['SQLALCHEMY_BINDS'] = {'POSTS': 'sqlite:///Mr_Valitines_Users_Posts.db'}


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
Login_Manager = LoginManager(app)

# socketio = SocketIO(app)
#
# ROOMS = ["Games", "Programming", "Sports"]
