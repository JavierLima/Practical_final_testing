$('#buttonId').click(function() {    
    $.ajax({
        url: "/",
        method: 'GET', // or another (GET), whatever you need
        success: function (data) {        
            // success callback
            // you can process data returned by function from views.py
        }
    });
});