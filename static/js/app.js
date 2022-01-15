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

