// -----------------------------------logInFunction----------------------

var modal = document.getElementById('id01');

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function loadingUser() {
  var load = document.getElementById('loader');
  var Mycontain1 = document.getElementById('containerlogInID');
  var Mycontain2 = document.getElementById('containerSign');
  var Mycontain3 = document.getElementById('containerCan');

      load.style.display = "block";
      Mycontain1.style.display = "none";
      Mycontain2.style.display = "none";
      Mycontain3.style.display = "none";
      setTimeout(() => { location.replace('/userHomePage'); }, 3000);
    }


const activePage = window.location.pathname;

const navLinks = document.querySelectorAll('nav a').forEach(link => {
  console.log(activePage);
    if(link.href.includes(`${activePage}`)){
      link.classList.add('active');
    }
  });


// -----------------------------------end logInFunction----------------------
