#git bash: source /c/shared/venv312/Scripts/activate

import json
from openai import OpenAI
import requests
import os

#change dir to this script's dir
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

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

user_article_text = '''
For the past few years, the US economy has been growing at a pace that seemed too good to be true.

So, at first glance, Thursday’s gross domestic product report showing the US economy grew at an annualized rate of 1.6% in the first quarter of this year versus the 3.4% rate in the fourth quarter of last year seems to be just the medicine the Federal Reserve doctors ordered. But there’s just one problem: inflation.

The latest Consumer Price Index data shows inflation is rising, moving further away from the Fed’s 2% target. And economists are forecasting new inflation data due Friday will paint a similar picture. The GDP report gave another preview of what could come.


Included in the report was an update on inflation from the prior quarter, as measured by the Fed’s preferred gauge, the Personal Consumption Expenditures price index. The latest data showed prices ticked up to a 3.4% annualized rate in the first quarter compared to 1.8% in the last quarter of 2023.

Slowing economic growth combined with rising inflation is known as stagflation. It’s among the ugliest terms to central bankers.

To be fair, one GDP report isn’t necessarily indicative of a trend. And on top of that, Thursday’s data is subject to two subsequent revisions, which could end up showing the economy isn’t slowing as much or at all. But even if the data doesn’t change, the US is by far better positioned than the UK and Germany, where high inflation is coupled with nearly nonexistent GDP growth.

Still, the latest US GDP report isn’t a pleasant sign for the Fed — or investors, as evidenced by Thursday’s US stock market selloff.

Danger ahead?
Low rates of unemployment tend to compensate for some of the pain that high levels of inflation bring. That’s because businesses generally can only raise prices when people are earning enough to afford it. In contrast, when unemployment is high and people are cutting corners, businesses will have a tough time passing on higher prices to their customers, which keeps inflation low.

One of the worst bouts of stagflation happened in the 1970s after a spike in oil prices from the Arab oil embargo on the US and other countries that supported Israel in the 1973 Yom Kippur War raised the cost of living dramatically. But when the Fed tried to ease inflation by raising interest rates, the economy fell into a recession.

JPMorgan Chase CEO Jamie Dimon has concerns that history could repeat itself.

The latest GDP report showed that US economic growth slowed to 1.6% in the first quarter of the year, a much weaker pace than expected.

The US economy “looks more like the 1970s than we’ve seen before,” he said earlier this week at a discussion hosted by the Economic Club of New York. He repeated that message in a Wall Street Journal interview published Thursday before the GDP report was released. “Things looked pretty rosy in 1972 — they were not rosy in 1973,” Dimon said.

There are certainly eerie parallels to the 1970s, with heightened geopolitical tensions in the Middle East and rising oil prices, but many economists feel the US is nowhere near the situation it faced then. Even at its recent peak, inflation was well below the high of that decade of nearly 12%. At the current pace, prices are rising even more slowly when compared to the 1970s.

But the growing consensus among economists and investment strategists is that the days of the Goldilocks economy, where inflation was coming down without slowing GDP, are numbered.

“While the Goldilocks narrative has prevailed so far this year, in more ways than one it’s as if she tripped over today’s GDP report and scraped her knee,” wrote Mike Reynolds, vice president of investment strategy at Glenmede, in a note Thursday.'''


instruction_1 = f'I read these articles, what are the main topics discussed in them?'
instruction_2a = 'Which of the following articles should I read to understand more about current GDP readings'
instruction_2b = f'Please list the top 3 articles related to the following text {user_article_text}'
instruction_3 = f'I read these articles, how would you tag the main topics discussed in each of them? Provide a few tags for each article.'
# 4 - how many articles do we have that relate to xxx topic - squash #3 response down into a table -i.e. Economy:6, US: 4, etc....

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
# print(f'Input: {input_string}')
# print('*************************')
print(f'Response: {chat_completion.choices[0].message.content}')
print('*************************')
print('*************************')