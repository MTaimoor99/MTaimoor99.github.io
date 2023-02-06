

function addToCartClick(){
  var product=document.getElementsByClassName('cart')
  var shopItem=document.getElementsByClassName('product')
  for (var i=0;i<product.length;i++)
  {
    var addToCartButton=product[i]
    addToCartButton.addEventListener('click',getItemName)
  }
}

function getItemName(event){
  var button=event.target
  var productTitle=(button.parentElement.parentElement.parentElement.getElementsByClassName('product')[0].innerText)
  var productPricePKR=(button.parentElement.parentElement.parentElement.getElementsByClassName('card-price')[0].innerText)
  //console.log(productTitle)
  //console.log(productPricePKR)
  addItemToCart(productTitle,productPricePKR)
  cartTotal()
  
}

function addItemToCart(productTitle,productPricePKR)
{
  var itemListing=document.getElementsByClassName('form-group-item') //Uploads name of the bought product to our form textbox
  var itemPrice=document.getElementsByClassName('form-group-price') //Uploads the price of the products to a textbox field
  console.log(itemListing)
  for (var i=0;i<itemListing.length;i++)
  {
   
      itemListing[i].value=productTitle
      console.log(itemListing[i].value)
  }
  for (var i=0;i<itemPrice.length;i++)
  {
   
      itemPrice[i].value=productPricePKR
      console.log(itemListing[i].value)
  }
}

function cartTotal()
{
var listItems=document.getElementsByClassName('form-group-price')
var total=0
for (var i=0;i<listItems.length;i++)
{
  if (listItems[i].value.trim().length==0)
  {
    break;
  }

  else
  {
    var cartItemDesc=listItems[i]
    cartItemDesc=listItems[i].value
    var cartItemPrice = cartItemDesc.substring(cartItemDesc.indexOf('-') + 1);
    console.log(cartItemPrice)
    var price=parseFloat(cartItemPrice)
    total=total+price
  }
  console.log(total)
  document.getElementById('Total').value="PKR-" + total
}
}

