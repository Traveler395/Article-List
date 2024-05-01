from flask import Flask, Response
from flask_cors import CORS
import json
import openai_wrapper
import os

app = Flask(__name__)
CORS(app)
ai = openai_wrapper.OpenAIWrapper()

sample_article = '''
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

sample_topic = 'current GDP readings'

#set current dir to this script's dir
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

#collect first four articles for "input" data
sample_rollup = []
with open('../Articles/Affluent Americals driving US Economy.txt', 'r', encoding='UTF-8') as f:
    content = f.read()
    sample_rollup.append(content)
with open('../Articles/GDP Growth Slowed to 1.6%.txt', 'r', encoding='UTF-8') as f:
    content = f.read()
    sample_rollup.append(content)
with open('../Articles/Global Debt hasn\'t been this bad since Napoleon.txt', 'r', encoding='UTF-8') as f:
    content = f.read()
    sample_rollup.append(content)
with open('../Articles/Key Fed Inflation Measure Rose.txt', 'r', encoding='UTF-8') as f:
    content = f.read()
    sample_rollup.append(content)

sample_rollup_titles = [
    'Affluent Americans are driving US economy and likely delaying need for Fed rate cuts',
    'GDP growth slowed to a 1.6% rate in the first quarter, well below expectations',
    'Global debt hasn’t been this bad since the Napoleonic Wars, says World Economic Forum president',
    'Key Fed inflation measure rose 2.8% in March from a year ago, more than expected'
]


@app.route('/hello', methods=['POST'])
def hello():
    data = {'message': 'hello wrold'}
    return Response(json.dumps(data), mimetype='application/json')

#advisor view

@app.route('/summary', methods=['POST'])
def summary():
    data = ai.summarize_article(sample_article)
    return Response(data, mimetype='application/json')

@app.route('/recommendations_article', methods=['POST'])
def recommendations_article():
    data = ai.recommendations_from_article(sample_article)
    return Response(data, mimetype='application/json')

@app.route('/recommendations_topic', methods=['POST'])
def recommendations_topic():
    data = ai.recommendations_from_topic(sample_topic)
    return Response(data, mimetype='application/json')

@app.route('/topics', methods=['POST'])
def topics():
    data = ai.topics_from_article(sample_article)
    return Response(data, mimetype='application/json')

#sales view

@app.route('/topics_rollup', methods=['POST'])
def topics_rollup():
    data = ai.topics_rollup(sample_rollup)
    return Response(data, mimetype='application/json')

@app.route('/summary_rollup', methods=['POST'])
def summary_rollup():
    data = ai.summary_rollup(sample_rollup)
    return Response(data, mimetype='application/json')

@app.route('/next_best_action', methods=['POST'])
def next_best_action():
    data = ai.recommendations_rollup(sample_rollup_titles)
    return Response(data, mimetype='application/json')

if __name__ == '__main__':
    app.run()
