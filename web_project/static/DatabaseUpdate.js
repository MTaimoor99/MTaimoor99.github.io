

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
  console.log(productTitle)
  console.log(productPricePKR)
  addItemToCart(productTitle,productPricePKR)
  cartTotal()
  
}

function addItemToCart(productTitle,productPricePKR)
{
  var itemListing=document.getElementsByClassName('list-group-item')
  //console.log(itemListing)
  for (var i=0;i<itemListing.length;i++)
  {
   
      itemListing[i].innerHTML=productTitle + " " + productPricePKR
      //console.log(itemListing[i].innerHTML)
      
    
  
  }
}

function cartTotal()
{
var listItems=document.getElementsByClassName('list-group-item')
var total=0
for (var i=0;i<listItems.length-1;i++)
{
  if (listItems[i].innerHTML.trim().length==0)
  {
    break;
  }

  else
  {
    var cartItemDesc=listItems[i]
    cartItemDesc=listItems[i].innerHTML
    var cartItemPrice = cartItemDesc.substring(cartItemDesc.indexOf('-') + 1);
    //console.log(cartItemPrice)
    var price=parseFloat(cartItemPrice)
    total=total+price
  }
  
  document.getElementById('cart-total-price').innerHTML="Total: PKR-" + total
}
}

