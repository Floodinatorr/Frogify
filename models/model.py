from ollama import Ollama

model = Ollama(model="llama3-8b-8192",key="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")
print(model.ask("Hi, how are you doing today?"))