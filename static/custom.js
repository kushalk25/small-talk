function addTextToChat(event){
    var user_input = "";
    const input_type = event.target.elements.input_type.value;
    if (input_type === "text") {
        user_input = event.target.elements.user_input.value
    } else if (input_type == "speech") {
        updateStatus("Listening");
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
        updateStatus("Processing");
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
        updateStatus("Ready");
    })
}

$(document).ready(function() {
    scrollToBottom();
});
