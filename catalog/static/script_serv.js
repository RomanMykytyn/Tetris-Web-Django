var signInForm = document.querySelector('.sign_in');
var signUpForm = document.querySelector('.sign_up');

$( "#closeButton" ).click(function() {
  signInForm.style.display = "none";
});

$( "#closeButton2" ).click(function() {
  signUpForm.style.display = "none";
});

$( "#sign_in" ).click(function() {
  signInForm.style.display = "block";
  signUpForm.style.display = "none";
});

$( "#sign_up" ).click(function() {
  signUpForm.style.display = "block";
  signInForm.style.display = "none";
});

$( "#exitAcc" ).click(function() {
  $.get("/exitAcc/", function(data) {location.reload()}
)});

$( "#sendComment" ).click(function() {
  var text = $('#textComment').val();
  if (text) {
    $.get("/ajaxView/", {text: text},  function() {updateComments();} );
    $('#textComment').val('');
  }});

function updateComments() {
  $.get("/ajaxView/", {update: "ok"},  function(data) {$(".viewComments").html(data);} )
}
