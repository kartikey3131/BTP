
import json_lines
import json

def load_jsonl_data(file: str) -> list:
    """
    Reads the data as saved in a .jsonl file
    
    Args:
    ----
    file: String corresponding to the path to a .jsonl file which contains the 
          tweets as received from the TwitterAPI.

    Returns:
    -------
    tweets: A list of all the data saved in the .jsonl file.
    """
    
    tweets = []
    with open(file, 'rb') as f:
        for tweet in json_lines.reader(f, broken=True):
            try:
                tweets.append(tweet)
            except json_lines.UnicodeDecodeError or json.JSONDecodeError:
                pass

        return tweets


tweets =[]
tweets = load_jsonl_data(r"C:\Users\Kartikeya gupta\OneDrive\Desktop\BTP\Twitter_Sentiment_Analysis-master\output_files\raw_data\twitter_30day_results_2020-01-171000_2020-01-171200.jsonl")

print(tweets)