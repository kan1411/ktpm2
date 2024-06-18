$(document).ready(function() {
    var name = localStorage.getItem('name');
    var username = localStorage.getItem('username');

    if (name && username) {
        $('#username-display').text(name);
        $('#userDropdown').show();
        $('#loginSignup').hide();
    } else {
        $('#userDropdown').hide();
        $('#loginSignup').show();
    }

    $('#logout-button').click(function() {
        localStorage.removeItem('username');
        localStorage.removeItem('name');
        window.location.href = 'login.html'; 
    });
    $('#service-button').click(function() {
        window.location.href = 'service.html';
    })
    $('#personalinfor-button').click(function() {
        window.location.href = 'personalinfor.html';
    })
});