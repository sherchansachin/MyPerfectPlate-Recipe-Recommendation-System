// transparent navbar turns white when scrolling down and returns transparent when is at the top of the screen

const nav = document.querySelector('.navbar');
window.addEventListener('scroll', function(){
    if(window.pageYOffset > 70){
        nav.classList.add('active');
    }else{
        nav.classList.remove('active');
    }
})


const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#password');

if(togglePassword){
  togglePassword.addEventListener('click', function (e) {
    // toggle the type attribute
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);
  });
}


// character remaining counter
$(document).ready(function(){
  var start = 0;
  var limit = 400;

  $("#message").keyup(function(){
    start = this.value.length
    if (start > limit) {
      return false;
    }
    else if(start == 400){
      $("#remaining").html("Remaining letters: " + (limit - start)).css('color', '#dc3545');
      swal("oops! ", "Character limit exceeded!", "info");
    }
    else if(start > 384 ){
      $("#remaining").html("Remaining letters: " + (limit - start)).css('color', '#dc3545');
    }
    else if(start < 400 ){
      $("#remaining").html("Remaining letters: " + (limit - start)).css('color', '#198754');
    }
    else{
      $("#remaining").html("Remaining letters: " + (limit)).css('color', '#198574');
    }
  })

});