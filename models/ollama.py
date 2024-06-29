
from crewai import Agent, Task, Crew, Process
import os

class Ollama:
    def __init__(self, key, model):
        os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
        os.environ["OPENAI_MODEL_NAME"] = model
        os.environ["OPENAI_API_KEY"] = key

        self.sentiment_classifier = Agent(
            role="sentence emotions classifier",
            goal="accurately classify sentences based on their emotions. give every sentence one of these emotions: 'joy','surprise','fear','anger','saddnes','information' ",
            backstory="You are an AI assistant whose only job is to classify sentences accurately and honestly. Do not be afraid to give emails bad emotions if they're. Your job is to help the user understand the emotions of the sentence.",
            verbose = True,
            allow_delegation = False
        )

        self.prompt_responder = Agent(
            role="prompt responder",
            goal="Based on the message of prompt, give short answers like a human would. You can swear, you can ask questions. You are free about this. Instead of giving your answers in substance, give them as if a person would speak normally. chat with person",
            backstory="You are an AI assistant whose only job is to write short responses to prompt. You can ask questions, you can swear, you can be sarcastic. You are free to do whatever you want. Your job is to keep the conversation flowing.",
            verbose = True,
            allow_delegation = False
        )

    def ask(self, prompt):
        response_prompt = Task(
            description=f"Response the following prompt: {prompt}",
            agent=self.prompt_responder,
            expected_output="A response to the prompt based on the message of the prompt. Short and concise, like a human would speak.",
        )
    
        crew = Crew(
            agents = [self.prompt_responder],
            tasks=[response_prompt],
            verbose=2,
            process= Process.sequential
        )

        return crew.kickoff()

    def sentiment(self, sentence):
        classify_sentence = Task(
            description=f"Classify the following sentence: {sentence}",
            agent=self.sentiment_classifier,
            expected_output="One of these six options: 'joy','surprise','fear','anger','saddnes','information'",
        )
    
        crew = Crew(
            agents = [self.sentiment_classifier],
            tasks=[classify_sentence],
            verbose=2,
            process= Process.sequential
        )

        return crew.kickoff()


