
const toggle = document.getElementById('togglepassword')
const password = document.getElementById('password')

toggle.onclick =()=>{
    if (password.type ==='password') {
        password.type ='text';
        toggle.innerHTML ='<i class="fa-regular fa-eye-slash"></i>'
    }
    else{
        password.type ='password';
        toggle.innerHTML ='<i class="fa-regular fa-eye"></i>'
    }
}