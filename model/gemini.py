import google.generativeai as genai

class ChatModel:
    def __init__(self, api_key, language):
        self.api_key = api_key
        self.language = language
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro', safety_settings={'HARASSMENT':'block_none'})
        self.chat = self.model.start_chat(history=[])

    def ask(self, question):
        response = self.chat.send_message(question, stream=True)
        print("Model: ",end="")
        """for chunk in response:
            print(chunk.text, end="")
        print("")"""
        return response
    
    def history(self):
        return self.chat.history
