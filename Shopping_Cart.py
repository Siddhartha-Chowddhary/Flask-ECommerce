from Imports import *
from App_Settings import *
from Routing import *
from Database import *
from Auth import *
#https://stackoverflow.com/questions/45949631/passing-json-data-to-the-flask-server-using-ajax

@app.route('/Temp_Shopping_Cart', methods=['POST', 'GET'])
def Temp_Shopping_Cart():

    basewidth = 300 

    form = RegisterForms()
    if current_user.is_authenticated:
        

            Cart_Data = request.get_json(force = True)
            # print(Cart_Data)    
            Product_name = Cart_Data['PRODUCT_NAME']
            Product_description = Cart_Data['PRODUCT_DESCRIPTION']
            Product_price = Cart_Data['PRODUCT_PRICE']
            Product_count = Cart_Data['PRODUCT_COUNT']
            Product_image_path = Cart_Data['PRODUCT_IMAGE_NAME']
            Product_image_name = os.path.split(Product_image_path)
            
            print(Product_count, Product_price)    
            Product_SubTotal= int(Product_count) * int(Product_price)
            print(Product_SubTotal)

            path  =  f"./static/img/shop-details/{Product_image_name[1]}"
            print(path)
            img = Image.open(path)         
            wpercent = (basewidth/float(img.size[0]))          
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), Image.ANTIALIAS)
            img.save(f'./static/Users/{current_user.Username}/{Product_image_name[1]}') 
            


            Cart = Temporary_Shopping_Cart(User= current_user.Username, Product_Name = Product_name, 
                                           Product_Description=Product_description, Product_Count=Product_count, 
                                           Product_Image_name=Product_image_name[1], User_Address=current_user.Address, Product_Price=Product_price, Product_Price_SubTotal=Product_SubTotal)
            db.session.add(Cart)
            db.session.commit()
            return ('', 204)

    else: 
        return redirect(url_for('LOGIN'))  


@app.route('/Dispaly_Temp_Shopping_Cart', methods=['POST', 'GET'])
def Dispaly_Temp_Shopping_Cart():
    
    user = current_user.Username
    Price_List= []
    Final_Price = 0
    Shopping_Cart = Temporary_Shopping_Cart.query.filter_by(User=user).all()
    for Shopping_Cart_Subtotal in Shopping_Cart:
        Total = Shopping_Cart_Subtotal.Product_Price_SubTotal
        Price_List.append(Total)
        Final_Price = sum(Price_List)
        
    return render_template('CART.html', CART=Shopping_Cart, USER=user, Subtotal=Final_Price)


@app.route('/DeleteItems/<int:id>', methods=['POST', 'GET'])
def DeleteItems(id):
    item = Temporary_Shopping_Cart.query.get(id)
    print(item)
    try:
        db.session.delete(item)
        db.session.commit()
        return redirect('/Dispaly_Temp_Shopping_Cart')     
    except:
        return flash("There was a problem while deleting the item from the cart.",'error')   

@app.route('/UpdateItems/<int:id>', methods=['POST', 'GET'])
def UpdateItems(id):
    item = Temporary_Shopping_Cart.query.get(id)
    print(item)
    if request.method == "POST":
        item.Product_Count = request.form['Item_Count']
        item.Product_Price_SubTotal = int(item.Product_Price) * int(item.Product_Count)        
        print(item.Product_Price_SubTotal)
    try:

        db.session.commit()
        return redirect('/Dispaly_Temp_Shopping_Cart')     
    except:
        return flash("There was a problem in updating the item count in the cart.",'error') 



@app.route('/Final_Shopping_cart_Checkout',  methods=['POST', 'GET']) 
def Final_Shopping_cart_Checkout():

    Price_Data = request.get_json(force = True)
    print(Price_Data)
    user = current_user.Username
    Total = Price_Data['PRODUCT_SUBTOTAL']
    print(Total)

    Product_Number = uuid.uuid1().hex
    print(Product_Number)
    Shopping_Cart = Temporary_Shopping_Cart.query.filter_by(User=user).all()
    for Shopping_Cart_items in Shopping_Cart:
        
        Product_name = Shopping_Cart_items.Product_Name
        
        Product_description = Shopping_Cart_items.Product_Description
        Product_count = Shopping_Cart_items.Product_Count
        
        Product_image_name = Shopping_Cart_items.Product_Image_name
        Product_price = Shopping_Cart_items.Product_Price
        Product_Subtotal_price = Shopping_Cart_items.Product_Price_SubTotal

        Final_Cart = Final_Shopping_Cart(User= current_user.Username, Product_Name = Product_name, 
                                        Product_Description=Product_description, Product_Count=Product_count, 
                                        Product_Image_name=Product_image_name, User_Address=current_user.Address, 
                                        Product_Price=Product_price, Total_Product_Price = Product_Subtotal_price, 
                                        Grand_Total_Price=Total, Product_Number=str(Product_Number) )
        db.session.add(Final_Cart)
        db.session.commit() 
    return ('Thank for shopping with us') 



