// models are build with bootstrap

document.getElementById("sign-btn").addEventListener('click', function() {
    document.getElementById('second').style.display = 'block';
    document.getElementById('first').style.display = 'none';
    document.getElementById("log-btn").innerText = "Login Here";
    document.getElementById("sign-btn").innerText = "SignUp";
    document.getElementById("sign-btn").style.display = 'none';
    document.getElementById("log-btn").style.display = 'inline-block';
    // document.getElementById("Procced").addEventListener('click', function() {
    //     window.location.href = "/login"
    // })
})

document.getElementById("log-btn").addEventListener('click', function() {
    document.getElementById('first').style.display = 'block';
    document.getElementById('second').style.display = 'none';
    document.getElementById("log-btn").innerText = "Login";
    document.getElementById("sign-btn").innerText = "SignUp Here";
    document.getElementById("log-btn").style.display = 'none';
    document.getElementById("sign-btn").style.display = 'inline-block';
    // document.getElementById("Procced").addEventListener('click', function() {
    //     window.location.href = "/signup"
    // })
})

document.getElementById("log-btn").style.display = "none";

// document.getElementById('Procced').addEventListener('click', function() {
//     alert('hello');
// })