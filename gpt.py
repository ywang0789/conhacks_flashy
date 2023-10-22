import openai 
import api_keys as keys

MODEL = "gpt-3.5-turbo"

class gpt:
    def __init__(self, key):
        self.key = key
        openai.api_key = self.key
        self.history = []
        self.history.append(
            {
                "role": "system",
                "content": "you are a help assistant.",
            }
        )

    def chat(self, user_input):
        self.history.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(model=MODEL, messages=self.history, max_tokens=50)

        response = response["choices"][0]["message"]["content"]

        self.history.append({"role": "system", "content": response})
        return response


# if __name__ == "__main__":
#     b = bot(keys.gpt_api_key)

#     print(b.chat("255 255 255"))
#     print(b.chat("0 0 0"))
#     print(b.chat("255 0 0"))