$(document).ready(() => {

    $('#new-post').submit(e => {

        let title = $('#title').val();
        let description = $('#description').val();
        let body = $('#body').val();

        e.preventDefault();
        $.ajax({
            url: '/api/post/new',
            type: 'POST',
            data: {
                title: title,
                description: description,
                body: body
            },
            success: response => {
                document.location.href = '/';
            }
        });
    });

});