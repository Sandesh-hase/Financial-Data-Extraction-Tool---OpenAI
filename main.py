import openai
from secret_key import open_ai_key
openai.api_key = open_ai_key


def poem_on_samosa():
    prompt = "write a poem on samosa"


    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": "write a poem on samosa"}
        ]
    )
    print(response['choices'][0]['message'])

if __name__ == '__main__':
    poem_on_samosa()