all_data = []


def getConversationMessages(conversation):
    messages = []
    currentNode = conversation["current_node"]
    while currentNode != None:
        node = conversation["mapping"][currentNode]
        if (
            node["message"]
            and node["message"]["content"]
            and node["message"]["content"]["content_type"] == "text"
            and len(node["message"]["content"]["parts"]) > 0
            and len(node["message"]["content"]["parts"][0]) > 0
            and (
                node["message"]["author"]["role"] != "system"
                or node["message"]["metadata"]["is_user_system_message"]
            )
        ):
            author = node["message"]["author"]["role"]
            if author == "assistant":
                author = "ChatGPT"
            elif (
                author == "system"
                and node["message"]["metadata"]["is_user_system_message"]
            ):
                author = "Custom user info"
            messages.append(
                {"author": author, "text": node["message"]["content"]["parts"][0]}
            )

        currentNode = node["parent"]
    return messages[::-1]


def onload(jsonData, _range=range(10, 15)):
    for conversation in jsonData[_range.start : _range.stop]:
        global all_data
        # print(f"## {conversation['title']}")
        all_data.append(f"## {conversation['title']}")
        messages = getConversationMessages(conversation)
        for message in messages:
            # print(f"### {message['author']}: {message['text']}")
            all_data.append(f"### {message['author']}: {message['text']}")


"""
<script>
    function getConversationMessages(conversation) {
        var messages = [];
        var currentNode = conversation.current_node;
        while (currentNode != null) {
            var node = conversation.mapping[currentNode];
            if (
                node.message &&
                node.message.content &&
                node.message.content.content_type == "text"
                && node.message.content.parts.length > 0 &&
                node.message.content.parts[0].length > 0 &&
                (node.message.author.role !== "system"  || node.message.metadata.is_user_system_message)
            ) {
                author = node.message.author.role;
                if (author === "assistant") {
                    author = "ChatGPT";
                } else if (author === "system" && node.message.metadata.is_user_system_message) {
                    author = "Custom user info"
                }
                messages.push({ author, text: node.message.content.parts[0] });
            }
            currentNode = node.parent;
        }
        return messages.reverse();
    }

    // on load, add messages to the root div
    window.onload = function() {
        var root = document.getElementById("root");
        for (var i = 0; i < jsonData.length; i++) {
            var conversation = jsonData[i];
            var messages = getConversationMessages(conversation);
            var div = document.createElement("div");
            div.className = "conversation";
            div.innerHTML = "<h4>" + conversation.title + "</h4>";
            for (var j = 0; j < messages.length; j++) {
                var message = document.createElement("pre");
                message.className = "message";
                message.innerHTML = `<div class="author">${messages[j].author}</div><div>${messages[j].text}</div>`;
                div.appendChild(message);
            }
            root.appendChild(div);
        }
    }
</script>
"""
