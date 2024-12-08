import ollama

response = ollama.chat(
    model="llama3.1",
    messages = [

        {
            'role':'system',
            'content':'you are o1 an intelligent AI assistant focusing on clear resoning and step by step analysis you break down complex problem and explain your thought process'
            
        },
        {
            'role': 'user',
            'content' : 'solve difficult math problem'
        }
    ]
)

print(response['message']['content'])