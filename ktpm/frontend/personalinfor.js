$(document).ready(function() {
    var username = localStorage.getItem('username');
    var name = localStorage.getItem('name'); 

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
    });
    $('#personalinfor-button').click(function() {
        window.location.href = 'personalinfor.html';
    

    const storedUsername = localStorage.getItem('username');
    if (storedUsername) {
        console.log('Sending request to /userinfo with username:', storedUsername);
        fetch(`/userinfo?username=${storedUsername}`)
            .then(response => response.json())
            .then(data => {
                console.log('Received response from /userinfo:', data); 
                if (data.error) {
                    alert(data.error);
                } else {
                    $('#username').text(data.username);
                    $('#name').text(data.name);
                    $('#gender').text(data.gender);
                    $('#role').text(data.role);
                    $('#area').text(data.area);
                    $('#phone').text(data.phone);
                    $('#academic').text(data.academic);
                }
            })
            .catch(error => console.error('Error:', error));
    }
});
});
