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
    stream=True,
    model="gpt-3.5-turbo",
)

for stream in response:
    response_msg = stream.choices[0].delta.content
    print(response_msg or "", end="")
