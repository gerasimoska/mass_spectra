function upload(event) {
    event.preventDefault();
    var data = new FormData($('form').get(0));

    $.ajax({
        url: $(this).attr('action'),
        type: $(this).attr('method'),
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        success: function(data) {
            alert('success');
        }
    });
    return false;
}

$(function() {
    $('form').submit(upload);
});