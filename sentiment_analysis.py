import pandas as pd
from textblob import TextBlob
import os

# Check if the file exists
if not os.path.exists("reviews.csv"):
    print("❌ Error: `reviews.csv` not found! Run the scraper script first.")
    exit()

# Load the reviews
df = pd.read_csv("reviews.csv")

# Perform Sentiment Analysis
def analyze_sentiment(text):
    if pd.isna(text) or text.strip() == "":
        return "Neutral"  # If no review text, assume neutral
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Review"].apply(analyze_sentiment)

# Save results
df.to_csv("processed_reviews.csv", index=False, encoding="utf-8")
print("✅ Sentiment Analysis completed! Results saved to `processed_reviews.csv`.")
