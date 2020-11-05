$(document).ready(() => {

    $(document).on('click', '#delete', e => {
        iRequest.deletePost(postId);
    });

    let iRequest = {
        drawPost: id => {
            $.ajax({
                url: '/api/post/' + id,
                type: 'GET',
                success: response => {
                    $('#title').append(response.title);
                    $('#title').append("\n" +
                        "                    <p id=\"delete\" class=\"float-right\">\n" +
                        "                        <svg width=\"1em\" height=\"1em\" viewBox=\"0 0 16 16\" class=\"bi bi-x-circle\" fill=\"currentColor\"\n" +
                        "                             xmlns=\"http://www.w3.org/2000/svg\">\n" +
                        "                            <path fill-rule=\"evenodd\"\n" +
                        "                                  d=\"M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z\"/>\n" +
                        "                            <path fill-rule=\"evenodd\"\n" +
                        "                                  d=\"M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z\"/>\n" +
                        "                        </svg>\n" +
                        "                    </p>");
                    $('#body').append(response.body);
                }
            });
        },
        deletePost: id => {
            $.ajax({
                url: '/api/post/' + id,
                type: 'DELETE',
                success: response => {
                    document.location.href = '/';
                }
            });
        }
    };

    let IInit = () => {
        iRequest.drawPost(postId);
    };

    IInit();

});