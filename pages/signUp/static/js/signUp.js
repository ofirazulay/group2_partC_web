// -----------------------------------signUp Function----------------------



var check1 = function(){
  if (document.getElementById('psw').value ==
  document.getElementById('confirm_password').value) {
  document.querySelector('#submitContact').disabled = false;
  document.getElementById('matched').textContent= 'Match';


} else {
   document.querySelector('#submitContact').disabled = true;
   document.getElementById('matched').textContent= 'Not Match';



}
}
var myInput = document.getElementById("psw");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");



// When the user clicks on the password field, show the message box
myInput.onfocus = function() {
document.getElementById("message").style.display = "block";
}

// When the user clicks outside of the password field, hide the message box
myInput.onblur = function() {
document.getElementById("message").style.display = "none";
}

// When the user starts to type something inside the password field
myInput.onkeyup = function() {
// Validate lowercase letters
var lowerCaseLetters = /[a-z]/g;
if(myInput.value.match(lowerCaseLetters)) {
  letter.classList.remove("invalid");
  letter.classList.add("valid");
} else {
  letter.classList.remove("valid");
  letter.classList.add("invalid");
}

// Validate capital letters
var upperCaseLetters = /[A-Z]/g;
if(myInput.value.match(upperCaseLetters)) {
  capital.classList.remove("invalid");
  capital.classList.add("valid");
} else {
  capital.classList.remove("valid");
  capital.classList.add("invalid");
}

// Validate numbers
var numbers = /[0-9]/g;
if(myInput.value.match(numbers)) {
  number.classList.remove("invalid");
  number.classList.add("valid");
} else {
  number.classList.remove("valid");
  number.classList.add("invalid");
}

// Validate length
if(myInput.value.length >= 8) {
  length.classList.remove("invalid");
  length.classList.add("valid");
} else {
  length.classList.remove("valid");
  length.classList.add("invalid");
}

}

var dtToday = new Date();
      var month = dtToday.getMonth() + 1;
      var day = dtToday.getDate();
      var year = dtToday.getFullYear();
      var maxYear = year - 18;
      if(month < 10)
          month = '0' + month.toString();
      if(day < 10)
          day = '0' + day.toString();

      var maxDate = maxYear + '-' + month + '-' + day;
      var minYear = year - 80;
      var minDate = minYear + '-' + month + '-' + day;
      document.querySelectorAll("#txtDate")[0].setAttribute("max",maxDate);

      document.querySelectorAll("#txtDate")[0].setAttribute("min",minDate);

      function SignUpEnd(){
        var getDetailsSignUp = document.getElementById('getDetails');
        var signInConfirmBut = document.getElementById('signInConfirm');

        getDetailsSignUp.style.display = "none";
        signInConfirmBut.style.display = "block";
      }

// -----------------------------------end signUp Function----------------------