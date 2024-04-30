import json
import os
from openai import OpenAI

class OpenAIWrapper:
    def __init__(self):
        self.should_log = True

        #set current dir to this script's dir
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)

        #get api key & init client
        api_keys_file = r"C:\shared\content\config\api-keys\hackathon_openai_keys.json"
        api_key = json.load(open(api_keys_file))['team_4']
        self.client = OpenAI(api_key=api_key)

        #load articles from library
        self.article_library = []
        directory = '../Articles'
        files = os.listdir(directory)
        for file in files:
            with open(os.path.join(directory, file), 'r', encoding='UTF-8') as f:
                content = f.read()
                self.article_library.append(content)

    def log(self, msg):
        if self.should_log:
            print(msg)

    def openai_call(self, input_string, model="gpt-3.5-turbo"):
        self.log('calling openai')
        chat_completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": input_string
                }
            ]
        )
        self.log(f'chat completion obj: {chat_completion}')
        return chat_completion.choices[0].message.content
    
    def summarize_article(self, article_text):
        instruction = f'I read this article, what are the main topics discussed in it? {article_text}'
        return self.openai_call(instruction)

    def recommendations_from_article(self, article_text, num_articles=3):
        instruction = f'Please list the top {num_articles} articles from the article library related to the following text: {article_text}. Article library: {self.article_library}'
        return self.openai_call(instruction)

    def recommendations_from_topic(self, topic):
        instruction = f'Which of the following articles from the article library should I read to understand more about {topic}? Article library: {self.article_library}'
        return self.openai_call(instruction)

    def topics_from_article(self, article_text):
        instruction = f'I read this article, how would you tag the main topics discussed in it? Provide a few tags. {article_text}'
        return self.openai_call(instruction)