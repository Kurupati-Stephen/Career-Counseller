from ollama import chat

response = chat(model='llama3', messages=[{"role": "user", "content": "Hello, how are you?"}])
print(response["message"]["content"])
