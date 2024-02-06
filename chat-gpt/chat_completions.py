import openai

openai.api_key = "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"

user_input = input("Enter your message: ")

response = openai.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": user_input,
        },
    ],
    model="gpt-3.5-turbo",
)

response_msg = response.choices[0].message.content
print(f"Response from the Chat-GPT: {response_msg}")
