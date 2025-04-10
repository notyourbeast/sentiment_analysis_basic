import openai
import pandas as pd
import os

# Load Data
df = pd.read_csv("processed_reviews.csv")
st.dataframe(df)
# OpenAI API Key
openai.api_key = "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"

# Generate Summary
def generate_insights(text):
    prompt = f"Summarize and provide insights for these reviews:\n{text}"
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Get AI-generated insights
#df["AI Insights"] = generate_insights(" ".join(df["Review"][:10]))

# Save to CSV
#df.to_csv("final_reviews.csv", index=False)
#print("AI Insights added!")
