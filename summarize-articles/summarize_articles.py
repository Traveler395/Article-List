#git bash: source /c/shared/venv312/Scripts/activate

import json
from openai import OpenAI
import requests
import os

# get api key from shared file for team_4
api_keys_file = r"C:\shared\content\config\api-keys\hackathon_openai_keys.json"
openai_key = json.load(open(api_keys_file))['team_4']
# print(openai_key)

# initialize openAI client
client = OpenAI(api_key=openai_key)

# read all articles from folder and add them to a list
article_texts = []
directory = '../Articles'
files = os.listdir(directory)
for file in files:
    with open(os.path.join(directory, file), 'r', encoding='UTF-8') as f:
        content = f.read()
        article_texts.append(content)

        
# print article contents (debugging)
# for index, text in enumerate(article_texts):
#     print('===================')
#     print(f'Article content #{index}:\n\n', text)
#     print('===================')
# print('Articles content list:\n\n', article_texts)

#This is the string to be used as input for OpenAI API call
# instruction can be user input from UI input box
# article_texts is the list of full texts of each article
instruction = 'Summarize the following articles in detail'
input_string = f'{instruction}: {article_texts}'

# perform the API call
chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": input_string
        }
    ]
)

# print out input and response
# returns chat_completion.choices[0].message.content, this is the response from OpenAI API call
print('*************************')
print('*************************')
print(f'Input: {input_string}')
print('*************************')
print(f'Response: {chat_completion.choices[0].message.content}')
print('*************************')
print('*************************')