
    var rIndex,
    table = document.getElementById("table1");

    function selectedRowToInput()
{

    for(var i = 1; i < table.rows.length; i++)
    {
        table.rows[i].onclick = function()
        {
          // get the seected row index
          rIndex = this.rowIndex;
        };
    }
}
selectedRowToInput();

function removeSelectedRow()
{
    table.deleteRow(rIndex);
    // clear input text
}


function chooseKindShow(){

    document.getElementById("chooseKind").style.display = "table";
    document.getElementById("cancleOrder").style.display = "table";
    document.getElementById("addTreat").style.display = "none";
    document.getElementById("Search").style.display = "table";
  }

  function chooseKindHide(){
    document.getElementById("chooseKind").style.display = "none";
    document.getElementById("cancleOrder").style.display = "none";
    document.getElementById("addTreat").style.display = "table";
    document.getElementById("Search").style.display = "none";
  }


    // Get the modal



// Get the <span> element that closes the modal
var modalB = document.getElementById("myModalB"); ;

var span = document.getElementsByClassName("close")[0];
var span2 = document.getElementsByClassName("close2")[0];

// When the user clicks 1 of the 3  buttons, open the modal
Search.onclick = function() {

  /*/ if (TypeSelectes =="") {
    modalB = document.getElementById("myModalC");
    ShowModal (modal);

  }
  else { /*/

    modalB = document.getElementById("myModalB");
    changeType();
    ShowModal (modalB);
}


function ShowModal( modalB) {
modalB.style.display = "block";
}

span2.onclick = function() {
  modalB.style.display= "none";
}


// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modalB.style.display= "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modalB) {
    modalB.style.display = "none";
  }
}


var b1 = document.getElementById("ShowAllBtn");
var b2 = document.getElementById("ShowClosestDateBtn");
var b3 = document.getElementById("ShowNearestBranchBtn");


b1.onclick = function() {
     b1.style.background = "grey";
     b1.style.color = "White";
     b2.style.background = "";
     b2.style.color = "";
     b3.style.background = "";
     b3.style.color = "";
}

b2.onclick = function() {
     b1.style.background = "";
     b1.style.color = "";
     b2.style.background = "grey";
     b2.style.color = "White";
     b3.style.background = "";
     b3.style.color = "";
}

b3.onclick = function() {
     b1.style.background = "";
     b1.style.color = "";
     b2.style.background = "";
     b2.style.color = "";
     b3.style.background = "grey";
     b3.style.color = "White";
}


var  TypeSelectes="Reflexology";

function GetSelect(){
  TypeSelectes = document.getElementById("kindsList").value;
  changeType();
}


function  changeType(){
  document.getElementById("TypeOf").innerText =" Available "+ TypeSelectes + " Treatments This Week :" ;
}



let tid = "#table2";

let headers = document.querySelectorAll(tid + " th");

// Sort the table element when clicking on the table headers
headers.forEach(function(element, i) {
  element.addEventListener("click", function() {
    w3.sortHTML(tid, ".item", "td:nth-child(" + (i + 1) + ")");
  });
});





function GetLocation() {
  if (navigator.geolocation) {
  console.log("in get location");
  navigator.geolocation.getCurrentPosition(showPosition);
  } else {
  document.getElementById("p").innerHTML="Geolocation is not supported by this browser.";
  }}


  function showPosition(position) {
      var z1= document.getElementById("p1");


      console.log(position);

      z3= calcCrow(position.coords.latitude, position.coords.longitude, 31.23926535269584,34.7909099763604 ); //distance to beersheba
      z4= calcCrow(position.coords.latitude, position.coords.longitude,32.09956781703534,34.774063172134504 ); //distance to tlv
      z5= calcCrow(position.coords.latitude, position.coords.longitude,32.7965,35.015 ); //distamce to Haifa
      z6= calcCrow(position.coords.latitude, position.coords.longitude,29.56,34.95 );//distamce to Eilat
      // x.innerHTML=("distance to Beersheba  " + z3 + "       Distance to tlv" +z4)
      if (z3<z4 && z3<z5 && z3<z6 ) {
       z1.innerHTML= "The nearest branch is: BeerSheba only " + z3.toFixed(3) + " Km away!"
        } if(z4<z3 & z4<z5 & z4<z6) {
          z1.innerHTML= "The nearest branch is: Tel Aviv only " + z4.toFixed(3) + " Km away!"
        }
      if(z5<z3 & z5<z4 & z4<z6) {
          z1.innerHTML= "The nearest branch is: Haifa only " + z5.toFixed(3) + " Km away!"
        }if(z6<z3 & z6<z5 & z6<z4) {
          z1.innerHTML= "The nearest branch is: Eilat only " + z6.toFixed(3) + " Km away!"
        }

  }

function convertDate(d) {
  var p = d.split("/");
  return +(p[2]+p[1]+p[0]);
}

function sortByDate() {
  var tbody = document.querySelector("#results tbody");
  // get trs as array for ease of use
  var rows = [].slice.call(tbody.querySelectorAll("tr"));

  rows.sort(function(a,b) {
    return convertDate(a.cells[0].innerHTML) - convertDate(b.cells[0].innerHTML);
  });

  rows.forEach(function(v) {
    tbody.appendChild(v); // note that .appendChild() *moves* elements
  });
}

document.getElementById("b").addEventListener("click", sortByDate);









  //This function takes in latitude and longitude of two location and returns the distance between them as the crow flies (in km)
    function calcCrow(lat1, lon1, lat2, lon2)
    {
      var R = 6371; // km
      var dLat = toRad(lat2-lat1);
      var dLon = toRad(lon2-lon1);
      var lat1 = toRad(lat1);
      var lat2 = toRad(lat2);

      var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
        Math.sin(dLon/2) * Math.sin(dLon/2) * Math.cos(lat1) * Math.cos(lat2);
      var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
      var d = R * c;
      return d;
    }

    // Converts numeric degrees to radians
    function toRad(Value)
    {
        return Value * Math.PI / 180;
    }


    function deleteRow(r) {
      var i = r.parentNode.parentNode.rowIndex;
      document.getElementById("table1").deleteRow(i);
    }






 function show() {
                var rowId =
                    event.target.parentNode.parentNode.id;
              //this gives id of tr whose button was clicked
                var data =
              document.getElementById(rowId).querySelectorAll(".row-data");
              /*returns array of all elements with
              "row-data" class within the row with given id*/
                var OrderdDate = data[0].innerHTML;
                var Orderdday = data[2].innerHTML;
                var Orderdhour = data[3].innerHTML;
                var Orderdbranch = data[4].innerHTML;
                var OrderdTetapist = data[5].innerHTML;
                document.getElementById('id02').style.display='block'
                document.getElementById('replace-me').innerText = '\nTreatment Date:  ' +OrderdDate + '\nTreatment Day:  ' + Orderdday + '\nTreatment hour:  ' + Orderdhour+ '\nBranch:  ' + Orderdbranch+ '\nTetapist: ' + OrderdTetapist
                document.getElementById('dateToOrder').value = OrderdDate.replaceAll(" ", "");
                document.getElementById('dayToOrder').value = Orderdday;
                document.getElementById('hourToOrder').value = Orderdhour;
                document.getElementById('branchToOrder').value = Orderdbranch;
                document.getElementById('TetapistToOrder').value = OrderdTetapist;
            }

// success alert close window function
function closeFunction(){
    alertDiv= document.getElementById('alertDiv')
    alertDiv.style.display = "none";
}
