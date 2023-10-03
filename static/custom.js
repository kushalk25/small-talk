function scrollToBottom() {
    var chatbox = $("#chatbox");
    chatbox.scrollTop(chatbox[0].scrollHeight);
}

$(document).ready(function() {
    scrollToBottom();
});
