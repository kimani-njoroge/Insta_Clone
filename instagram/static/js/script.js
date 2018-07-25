/**
 * Created by sam on 25/07/18.
 */
// comments part

function enterPressed(e) {
  if (e.key === "Enter") { return true; }
  return false;
}


function validComment(text) {
  if (text == '') return false;
  return true;
}


function create_comment(success_cb, error_cb) {
  var comment_text = $(this).val();
  var post_pk = $(this).parent().siblings('.hidden-data').find('.post-pk').text();

  console.log(comment_text, post_pk);

  $.ajax({
    type: "POST",
    url: '/comment/',
    data: {
      comment_text: comment_text,
      image_pk: image_pk
    },
    success: function(data) { success_cb(data); },
    error: function(error) { error_cb(error); }
  });
}


function comment_update_view(data) {
  console.log(data);
  var $post = $('.hidden-data.' + data.post_pk);
  var commentHTML = '<li class="comment-list__comment"><a class="user" href="' + data.commenter_info.profile_url
                  + '">' + data.commenter_info.username + '</a> <span class="comment">'
                  + data.commenter_info.comment_text +'</span></li>'

  $post.closest('.view-update').find('.comment-list').append(commentHTML);
}


$('.add-comment').on('keyup', function(e) {
  if (enterPressed(e)) {
    if (validComment($(this).val())) {
      create_comment.call(this, comment_update_view, error_cb);
      $(this).val('');
    }
  }
});