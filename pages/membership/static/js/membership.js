
  // Get the modal
  var modalD = document.getElementById("myModalD");


  purchaseMore.onclick = function() {
  modalD.style.display = "block";
}

// Get the <span> element that closes the modal
var spanD = document.getElementsByClassName("closeD")[0];

// When the user clicks on <span> (x), close the modal
spanD.onclick = function() {
  modalD.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modalD) {
    modalD.style.display = "none";
  }
}


function checkPrice() {
    var price = 0;
    if (document.getElementById("Shiatsu1").checked==true ) {
        price = 160;
    }
    if ( document.getElementById("Reflexology1").checked==true) {
      price = 120;
  }
  if ( document.getElementById("Chinese1").checked==true) {
    price = 140;
}
    if (document.getElementById("Shiatsu10").checked==true) {
      price = 1300;
  }
  if ( document.getElementById("Reflexology10").checked==true) {
    price = 900;
}
  if ( document.getElementById("Chinese10").checked==true) {
    price = 1100;
}



    document.getElementById("price").innerText = "Price: " + price + "   ILS";
}