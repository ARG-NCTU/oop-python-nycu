
# go to https://platform.openai.com/
# 'Personal' -> 'View API keys' -> 'Create New secret key'

import openai

openai.api_key = "your api key"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": "Can you generate a pytest for checking numpy package existing?"},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)