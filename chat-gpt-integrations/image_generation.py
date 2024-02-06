from openai import OpenAI
import os

client = OpenAI(api_key="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")

image_path = "/Users/shubhamyadav/Documents/Personal/GitHub/python-basic-learning/chat-gpt/home_image.PNG"

if os.path.exists(image_path):
    response = client.images.create_variation(
        image=open(image_path, "rb"), n=2, size="1024x1024"
    )
    image_url = response.data[0].url
else:
    print(f"File not found: {image_path}")
