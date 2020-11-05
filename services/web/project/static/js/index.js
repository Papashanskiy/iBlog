$(document).ready(() => {

    $(document).on('click', '#new_post', e => {
        document.location.href = '/post/new';
    });

    let iRequests = {
        drawPosts: (count = -1) => {
            $.ajax({
                url: '/api/posts/' + count,
                type: 'GET',
                success: response => {
                    for (let i = 0; i < response.posts.length; i++) {
                        let post = response.posts[i];
                        $('#posts').append("<a href='" + '/post/' + post.id + "' id='" + post.id + "' class=\"post col-sm-6\">\n" +
                            "            <h3>" + post.title + "</h3>\n" +
                            "            <p class=\"description\">" + post.description + "</p>\n" +
                            "        </a>");
                    }
                },
            });
        }
    };

    let IInit = () => {
        iRequests.drawPosts(10);
    };

    IInit();

});