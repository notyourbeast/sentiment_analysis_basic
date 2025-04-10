
 📊 Google Reviews Sentiment Analysis Dashboard

An interactive web application that scrapes, analyzes, and visualizes Google Reviews using sentiment analysis and rich data visualizations. Built with Python, Selenium, TextBlob, and Streamlit.


 🚀 Features

- 🔍 Scrape Google Maps reviews with a single URL input
- 🧠 Perform sentiment analysis using `TextBlob` (Positive, Negative, Neutral)
- 📈 Visualize trends over time:
  - Average Rating
  - Review Volume
  - Review Length
  - Reviewer Engagement
- 📊 Sentiment breakdown (Pie chart & Histogram)
- ☁️ Word cloud of review keywords
- 🧾 Full review data table
- 💡 (Optional) AI-generated review insights using OpenAI GPT-3.5


🗂️ Project Structure


├── app.py                   # Streamlit dashboard

├── scraper.py              # Google Maps review scraper using Selenium

├── sentiment_analysis.py   # Sentiment classification using TextBlob

├── insights.py             # (Optional) GPT-3.5 summarization script

├── reviews.csv             # Raw scraped reviews

├── processed_reviews.csv   # Processed reviews with sentiment labels


 🛠️ Tech Stack

- Python
- Selenium - Review scraping
- TextBlob - Sentiment Analysis
- Streamlit - Web dashboard
- Pandas, Seaborn, Matplotlib, WordCloud - Data processing and visualization
- OpenAI API (GPT-3.5) - (optional) Review summarization



⚙️ How to Run the Project

1. Clone the repository
bash
git clone https://github.com/your-username/google-reviews-sentiment-dashboard.git
cd google-reviews-sentiment-dashboard


 2. Install dependencies
bash
pip install -r requirements.txt


> Required Libraries: streamlit, selenium, pandas, textblob, matplotlib, seaborn, wordcloud, openai

 3. Run the scraper
bash
python scraper.py

> Enter the Google Maps business URL when prompted.

 4. Perform sentiment analysis
    bash
    python sentiment_analysis.py


5. Launch the Streamlit app
   bash
   streamlit run app.py



## 💡 Optional: GPT-3.5 Powered AI Insights

To enable AI-generated insights (via insights.py):

1. Create an OpenAI account and obtain your API key.
2. Replace the placeholder key in "insights.py":
   python
   openai.api_key = "your-openai-key"
 
3. Run the script (optional):
  bash
  python insights.py
 





## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io)
- [TextBlob](https://textblob.readthedocs.io/)
- [OpenAI](https://openai.com)
- [Selenium](https://www.selenium.dev/)



## 📬 Contact

For questions or collaborations: **saiprasadshiragave10@gmail.com**
