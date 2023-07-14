const form = document.querySelector('#create-account');
const usernameInput = document.querySelector('#username');
const emailInput = document.querySelector('#email');
const passwordInput = document.querySelector('#password');
const cpasswordInput = document.querySelector('#cpassword');

form.addEventListener('submit', (event) => {

    event.preventDefault();
    validateForm();
});

function validateForm() {

    if (usernameInput.value.trim() == '') {
        setError(usernameInput, 'Name can not be empty');
    }


}


function setError(element, errorMessage) {

    const parent = element.parentElement;
    parent.classList.add('error')

}