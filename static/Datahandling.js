function Product_Data_Post() {
    
        var ProductName = document.getElementById("ProductName").innerHTML;
        var ProductDescription = document.getElementById("ProductDescription").innerHTML;
        var ProductPrice = document.getElementById("ProductPrice").innerHTML;
        
        var ProductCount = document.getElementById("ProductCount").value;
        var ProductImageName =  document.getElementById("ProductImageName").src;
        
        console.log(ProductImageName);
        
        var Post_Product_Data = {
        PRODUCT_NAME: ProductName,
        PRODUCT_DESCRIPTION: ProductDescription,
        PRODUCT_PRICE: ProductPrice,
        PRODUCT_COUNT: ProductCount,
        PRODUCT_IMAGE_NAME: ProductImageName

        }

        $.ajax({
            url: "/Temp_Shopping_Cart",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(Post_Product_Data),
            success: function(data)
            {
                console.log(data); 
            }
        });

}




function Product_SubTotal() {
    

    var SubtotalPrice = document.getElementById("Subtotal").innerHTML;
    

    
    console.log(SubtotalPrice);
    
    var Price_Total_Data = {

        PRODUCT_SUBTOTAL: SubtotalPrice

    }

    $.ajax({
        url: "/Final_Shopping_cart_Checkout",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(Price_Total_Data),
        success: function(data)
        {
            console.log(data); 
        }
    });

}



