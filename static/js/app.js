"use strict";
$(function () {
    $('#form-contact').click(controler_data);
})

function showNav() {
    let x = document.getElementById("personal-navbar-responsive");
    if(x.className === "personal-navbar-container") {
        x.className += " responsive";
    } else {
        x.className = "personal-navbar-container";
    }
}
function form_contact() {
    let prenom = document.getElementById('prenom');
    let nom = document.getElementById('nom');
    let email = document.getElementById('email');
    let message = document.getElementById('message');
    $.ajax({
        url: "src/form_contact.php",
        type: "post",
        data: {
            prenom: prenom.value,
            nom: nom.value,
            email: email.value,
            message: message.value
        },
        dataType: "json",
        error: function(request) {
            alert(request.responseText);
        },
        success: function(data) {
            if(data == 1) {
                prenom.value = '';
                nom.value = '';
                email.value = '';
                message.value = '';
                $('#alert-success').modal('show');
            }
        }
    })
}

function controler(input, message) {
    input.value = input.value.trim();
    let valeur = input.value;
    if(valeur.length === 0) {
        message.innerText = "Merci de remplir le champ suivant";
        return false;
    }
    message.innerText = '';
    return true;
}


function controler_data() {
    let prenomOk = controler(prenom, messagePrenom);
    let nomOk = controler(nom, messageNom);
    let emailOk = controler(email, messageEmail);
    let messageOk = controler(message, messageMessage);
    if(prenomOk && nomOk && emailOk && messageOk) {
        form_contact();
    }
}