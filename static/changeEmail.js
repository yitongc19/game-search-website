var confirmChange = function () {
    confirm("Your email has been successfully updated!" +
        "\nClick 'OK' and you will be taken back to your account page!");
    var new_email = document.getElementById("new_email").value;
    var account_url = account_with_new_email.replace('NOTANAME', new_email);
    window.location = account_url;
}