function scrollToBottom() {
    var chatbox = $("#chatbox");
    chatbox.scrollTop(chatbox[0].scrollHeight);
}

function addTextToChat(event){
    var user_input = "";
    const input_type = event.target.elements.input_type.value;
    if (input_type === "text") {
        user_input = event.target.elements.user_input.value
    }

    let textDecoder = new TextDecoder('utf-8')

    fetch('/add_to_chat', {
        method: 'POST',
        body: JSON.stringify({
            "input_type": input_type,
            "user_input": user_input
        })
    }).then(function(response) {
        // The response from the fetch API is a ReadableStream
        // We need to use the getReader and read the stream data
        return response.body.getReader().read()
    }).then(function(conversation_data) {
        let result = textDecoder.decode(conversation_data.value);
        refreshChatBox(JSON.parse(result));
        getChatGPTResponse();
    });

    return false;
}

function getChatGPTResponse() {
    let textDecoder = new TextDecoder('utf-8')
    fetch('/chat', {
        method: 'GET'
    }).then(function(response) {
        // The response from the fetch API is a ReadableStream
        // We need to use the getReader and read the stream data
        return response.body.getReader().read()
    }).then(function(conversation_data) {
        let result = textDecoder.decode(conversation_data.value);
        refreshChatBox(JSON.parse(result));
    })
}

function refreshChatBox(conversation){
    // Use Jquery to get chatbox and remove the existing content
    var chatbox = $("#chatbox");
    chatbox.empty();
    $("#user_input").val("");

    // for each message in the conversation
    for (i in conversation) {
        message = conversation[i]

        if (message.role == "user") {
            chatbox.append(`<p class="user-message">${message.content}</p>`)
        } else if (message.role == "assistant") {
            chatbox.append(`<p class="bot-message">${message.content}</p>`)
        }
    }
}

$(document).ready(function() {
    scrollToBottom();
});
