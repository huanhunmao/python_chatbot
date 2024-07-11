import openai

class Chatbot:
    def __init__(self):
        openai.api_key = 'sk-proj-xxx'

    def get_response(self, user_input):
        response = openai.Completion.create(
            model='gpt-3.5-turbo',
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        )
        res = response.choices[0].text.strip()
        return res


if __name__ == '__main__':
    chatbot = Chatbot()
    res = chatbot.get_response('tell me a joke')
    print(res)
