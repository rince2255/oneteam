function validateForm() {
    let fname = document.forms["myForm"]["fname"].value;
    let age = document.forms["myForm"]["age"].value;
    if (fname == "") {
        alert("Name must be filled out");
        return false;
    }

    if (age == "") {
        alert("Age must be filled out");
        return false;
    }
}