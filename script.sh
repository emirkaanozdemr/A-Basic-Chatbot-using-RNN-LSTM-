jq -s '[.[].intents] | add | {intents: .}' \
    /kaggle/input/books-dataset/intents.json \
    /kaggle/input/chatbot-dataset/intents.json \
    /kaggle/input/simple-chatbot-dataset/intents.json \
    /kaggle/input/d/mohammadnourullahi/chatbot-dataset/intents.json \
    /kaggle/input/computer-science-theory-qa-dataset/intents.json \
    /kaggle/input/it-helpdesk-chatbot-dataset/intents.json \
    /kaggle/input/star-wars-chat-bot/starwarsintents.json \
    > merged_intents.json
echo "Done"