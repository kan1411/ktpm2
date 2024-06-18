$(document).ready(function() {
    $('#loginForm').submit(function(event) {
        event.preventDefault();
  
        var username = $('#username').val();
        var password = $('#password').val();
  
        $.ajax({
            url: 'http://localhost:5000/login',
            method: 'POST',
            data: JSON.stringify({
                username: username,
                password: password
            }),
            contentType: 'application/json',
            dataType: 'json',
            success: function(response) {
                Swal.fire({
                    title: 'Thành công!',
                    text: response.message,
                    icon: 'success',
                    timer: 2000,
                    showConfirmButton: false
                }).then(() => {
                    localStorage.setItem('username', response.name);
                    localStorage.setItem('name', response.name);
                    window.location.href = 'mainpage.html'; 
                });
            },
            error: function(error) {
                console.log(error);
                Swal.fire({
                    title: 'Lỗi!',
                    text: 'Tài khoản hoặc mật khẩu lỗi',
                    icon: 'error'
                });
            }
        });
    });
  
    var username = localStorage.getItem('username');
    if (username) {
        $('#userDropdown').text(username);
    }
  });