$(document).ready(function() {

    var processURL = '/process';

    $('#process').on('click', function () {
        var btn = $(this);
        $.ajax({
            type: "POST",
            url: processURL,
            dataType: "json",
            data: $(".formatter form").serialize(),
            error: function (request, status, error) {
                alert(request.responseText);
            },
            success: function success(data) {
                var editor = new JsonEditor('#json-display');
                editor.load(data);
            }
        });
    });

});
