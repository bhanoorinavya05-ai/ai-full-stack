from ollama import chat

response = chat(
    model="llama3.2",
    messages=[
        {
            "role" : "user",
            "content": "what is SQL? Explain briefly."
        }
    ]
)

print(response.message.content)