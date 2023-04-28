import requests

# Telegram Bot API endpoint
API_ENDPOINT = "https://api.telegram.org/bot6090033764:AAG4IQB589lEcqmV7Z7t7okTfwj4qLlfvOw"

def delete_all_chats():
    # Get a list of all chats
    response = requests.get(f"{API_ENDPOINT}/getUpdates")
    if response.status_code != 200:
        print("Error retrieving chat list")
        return
    
    chat_data = response.json()
    if not chat_data["ok"]:
        print("Error retrieving chat list")
        return
    
    chat_ids = []
    for update in chat_data["result"]:
        chat_id = update["message"]["chat"]["id"]
        chat_ids.append(chat_id)
    
    # Delete each chat
    for chat_id in chat_ids:
        response = requests.get(f"{API_ENDPOINT}/leaveChat?chat_id={chat_id}")
        if response.status_code != 200:
            print(f"Error leaving chat {chat_id}")
            continue
        
        leave_data = response.json()
        if not leave_data["ok"]:
            print(f"Error leaving chat {chat_id}")
    
    print("All chats have been left.")

# Run the script
delete_all_chats()
