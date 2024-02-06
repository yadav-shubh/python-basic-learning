import openai

openai.api_key = "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"
response = openai.completions.create(
    model="davinci-002",
    prompt="What is the Java Langugage"
)

print(response)
print(response.choices[0].text)