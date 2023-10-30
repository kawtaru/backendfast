
import openai

openai.api_key = "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" # Add your OpenAI API key here

def check_text(input):
    messages = [
        {"role": "user",
         "content": ""},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply
