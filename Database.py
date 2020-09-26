from Imports import *
from App_Settings import *
from Routing import *

@Login_Manager.user_loader
def Load_User(user_id):
  return User.query.get(int(user_id))

class User(db.Model, UserMixin):
  
  id = db.Column(db.Integer, primary_key=True)
  
  Full_Name = db.Column(db.String(50), unique=False, nullable=False)

  Email = db.Column(db.String(120), unique=True, nullable=False)
  Address = db.Column(db.String(120), unique=False)
  
  Username = db.Column(db.String(20), unique=True, nullable=False)
  Password = db.Column(db.String(60), unique=False, nullable=False)

  # Image_name = db.Column(db.String(120))

  Temporary_ShoppingCart = db.relationship('Temporary_Shopping_Cart', backref='Temporary_Shopping_Cart_Author', lazy=True)
  Final_ShoppingCart = db.relationship('Final_Shopping_Cart', backref='Final_Shopping_Cart_Author', lazy=True)

  # bio = db.relationship('BIO', backref='BIO_Author', lazy=True)

  def __repr__(self):
    return f"User('{self.Full_Name}','{self.Username}','{self.Email}', ,'{self.Address}')"

class Temporary_Shopping_Cart(db.Model):
  # __bind_key__ = 'POSTS'
  
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)

  # User_Id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
  User = db.Column(db.String(20), db.ForeignKey('user.Username'), nullable = False)

  Product_Name = db.Column(db.String(120))
  Product_Description = db.Column(db.String(1000))
  
  Product_Count = db.Column(db.Integer())
  Product_Image_name = db.Column(db.String(120))
  
  User_Address =  db.Column(db.String(1000))
  Product_Price = db.Column(db.Float())
  Product_Price_SubTotal = db.Column(db.Float())
  # Image = db.Column(db.LargeBinary)

  Date = db.Column(db.DateTime, unique=True, nullable=False, default = datetime.utcnow)


  def __repr__(self):
    return f"Temporary_Shopping_Cart('{self.Product_Name}', '{self.Product_Description}', '{self.Product_Count}', '{self.Product_Image_name}', '{self.User_Address}',  '{self.Product_Price}')"

class Final_Shopping_Cart(db.Model):
  # __bind_key__ = 'POSTS'
  
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)

  # User_Id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
  User = db.Column(db.String(20), db.ForeignKey('user.Username'), nullable = False)

  Product_Name = db.Column(db.String(120))
  Product_Description = db.Column(db.String(1000))
  
  Product_Count = db.Column(db.Integer())
  Product_Image_name = db.Column(db.String(120))
  
  User_Address =  db.Column(db.String(1000))
  Product_Price = db.Column(db.Float())
  
  Total_Product_Price = db.Column(db.Float())
  Grand_Total_Price = db.Column(db.Float())
  Product_Number = db.Column(db.String(1000), nullable=False)

  # Image = db.Column(db.LargeBinary)

  Date = db.Column(db.DateTime, unique=True, nullable=False, default = datetime.utcnow)


  def __repr__(self):
    return f"Final_Shopping_Cart('{self.Product_Name}', '{self.Product_Description}', '{self.Product_Count}', '{self.Product_Image_name}', '{self.User_Address}', '{self.Product_Price}', '{self.Total_Product_Price}, '{self.Grand_Total_Price}, '{self.Product_Number}')"
