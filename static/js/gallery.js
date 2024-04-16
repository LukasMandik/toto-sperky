$(document).ready(function () {
    $('.like-button').on('click', function (e) {
        e.preventDefault();
        var photoId = $(this).data('photo-id');
        var likeCount = $(this).find('.like-count');
        $.ajax({
            url: '/like-photo/',
            data: {
                'photo_id': photoId,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            method: 'POST',
            dataType: 'json',
            success: function (data) {
                if (data.success) {
                    likeCount.text(data.likes);
                }
            },
            error: function () {
                alert('Error occurred while processing your request.');
            }
        });
    });
});
