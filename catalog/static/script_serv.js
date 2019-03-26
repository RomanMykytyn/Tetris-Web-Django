var signInForm = document.querySelector('.sign_in');
var signUpForm = document.querySelector('.sign_up');

updateComments();
updatePlayers();
updateYourGames();

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
  $.get("/ajaxView/", {updateComments: "ok"},  function(data) {$(".viewComments").html(data);} )
}

function updatePlayers() {
  $.get("/ajaxView/", {updatePlayers: "ok"},  function(data) {$("#scoreList").remove();
  $(".bestScore").append(data);} )
}

function updateYourGames() {
  $.get("/ajaxView/", {updateYourGames: "ok"},  function(data) {$("#yourGameList").remove();
  $(".youScore").append(data);} )
}
