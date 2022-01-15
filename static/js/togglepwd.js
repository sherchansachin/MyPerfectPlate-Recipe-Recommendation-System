// login

const getpass = document.querySelector('#togglePassword');
const password3 = document.querySelector('#password3');

if(getpass){
  getpass.addEventListener('click', function(e){
    const type3 = password3.getAttribute('type') === 'password' ? 'text' : 'password';
    password3.setAttribute('type', type3);
    
  });
}
