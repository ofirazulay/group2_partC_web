
  function myFunction() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
  }


  // Get the modal
var modalD = document.getElementById("myModalD");



  function CountCheked() {
    var Treatment = document.forms[0];
    var i;
    var CountRadio =0;
    for (i = 0; i < Treatment.length; i++) {
      if (Treatment[i].checked) {
        CountRadio=CountRadio+1;
      }
    }
  return CountRadio ; }



// Get the <span> element that closes the modal
var spanD = document.getElementsByClassName("closeD")[0];



function showModel(Treatment_type, treatmentsDetails ) {
  const currMain = document.querySelector("mainModel")
  const section = document.createElement('section')
    section.innerHTML = `
     <div id=" Shiatsu_div" >
            
          <!-- Shiatsu - single treatment -->
  
             <input type="radio" id="${Treatment_type}" name="Treatment" value="${Treatment_type}"  required onclick="checkPrice()" checked >
              <label for="${Treatment_type}"  class="inpTEXT">
             ${Treatment_type} - single treatment - 
             </label><br>
             <!-- Shiatsu - 10 treatments -->
             <input type="radio" id="${Treatment_type}" name="Treatment" value="${Treatment_type}" onclick="checkPrice()"  >
             <label for="${Treatment_type}" class="inpTEXT">
              ${Treatment_type} - 10 treatments
              </label><br>   
                </div>
        `
        currMain.appendChild(section)
        currMain.replaceChild(section, currMain.childNodes[0]);



modalD.style.display = "block";
}



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


