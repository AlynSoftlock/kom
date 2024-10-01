import openai

  
client = openai.OpenAI(api_key="sk-A2rMjkfd6SKSGdBO422883A3103d46A883F5395d39235405", base_url="https://api.keyai.shop/v1")

response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "hello who are you"
            }
        ]
    )
print(response)
