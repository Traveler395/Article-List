# Article-List
Listing of articles for hackathon

# Instructions for running backend service
Using git bash:

Activate the built-in venv

    source /c/shared/venv312/Scripts/activate

Create personal venv

    python -m venv ~/Documents/hackathon-venv

Activate personal venv

    source ~/Documents/hackathon-venv/Scripts/activate

Install dependencies into personal venv

   pip install -r requirements.txt

Run the program

    python summarize-articles/app.py


Use cases for hackathon

1. Summarize a list of articles provided to Chat-GPT
2a. Ask for articles related to a topic from the list provided to Chat-GPT
    Sample input: What articles do you have that discuss inflation?
    Sample output: Key Fed Inflation measure rose...
    Sample Input: What's going on with unemployment right now?
    Sample output: Strange Jobless Claims
2b. Provide an article and ask for more based on similar topics
    Sample input: I just read this article, {The last batch of inflation news that Federal Reserve officials will see before their policy meeting next week is in, and none of it is very good.

In the aggregate, Commerce Department indexes that the Fed relies on for inflation signals showed prices continuing to climb at a rate still considerably higher than the central bank’s 2% annual goal, according to separate reports this week.}, what do you have that covers something similar?
    Sample output: Key Fed Inflation Measure
3a. Provide a list of topics discussed in a set of articles I say I read
    Sample Input: I read these articles {article list}, what are the main topics discussed in them?
    Sample output: Inflation, Unemployment, the US Economy, etc.
3b. Using the results of 3a, count up the number of times each topic has appeared in our list of articles