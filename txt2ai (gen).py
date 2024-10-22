from speech2txt import *
from groq import Groq

client = Groq(
    api_key="",
)
def aiCall(prompt,aiSpec):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": aiSpec,
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-70b-8192",
    )
    print(chat_completion.choices[0].message.content)

content = "You are a helpful..."


aiCall(txt(),content)
