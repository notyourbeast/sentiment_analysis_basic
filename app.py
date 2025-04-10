import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load Data
df = pd.read_csv("processed_reviews.csv")

# Convert "Review Date" to datetime for trend analysis
if "Review Date" in df.columns:
    df["Review Date"] = pd.to_datetime(df["Review Date"], errors='coerce')
    df["Date"] = df["Review Date"].dt.date  # Extract date only

# Sidebar for user selection
st.sidebar.title("Google Reviews Analysis")
selected_sentiment = st.sidebar.selectbox("Filter by Sentiment", ["All", "Positive", "Negative", "Neutral"])

if selected_sentiment != "All":
    df = df[df["Sentiment"] == selected_sentiment]

# Main Dashboard
st.title("📊 Google Reviews Analysis")

# KPIs
total_reviews = df.shape[0]
positive_reviews = df[df["Sentiment"] == "Positive"].shape[0]
negative_reviews = df[df["Sentiment"] == "Negative"].shape[0]
neutral_reviews = df[df["Sentiment"] == "Neutral"].shape[0]

st.metric("Total Reviews", total_reviews)
st.metric("Positive Reviews", positive_reviews)
st.metric("Negative Reviews", negative_reviews)
st.metric("Neutral Reviews", neutral_reviews)

# 📌 Sentiment Distribution - Enhanced Pie Chart
st.subheader("📊 Sentiment Distribution - Pie Chart")
fig, ax = plt.subplots(figsize=(6, 6))
colors = sns.color_palette("pastel")  # Attractive pastel color scheme
ax.pie(
    [positive_reviews, negative_reviews, neutral_reviews],
    labels=["Positive", "Negative", "Neutral"],
    autopct="%1.1f%%",
    colors=colors,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1, 'antialiased': True},
    startangle=140,
)
ax.set_title("Sentiment Breakdown", fontsize=14, fontweight='bold')
st.pyplot(fig)

# 📈 Select Trend for Line Graph
st.sidebar.subheader("📈 Select Trend for Line Graph")
trend_option = st.sidebar.selectbox("Choose a trend:", ["Average Rating Over Time", "Number of Reviews Over Time", "Average Review Length Over Time", "Reviewer Engagement Over Time"])

# 📈 Line Graph - Average Rating Over Time (Default)
if trend_option == "Average Rating Over Time" and "Date" in df.columns:
    st.subheader("📈 Average Rating Over Time")
    df["Rating"] = pd.to_numeric(df["Rating"], errors='coerce')  # Convert to numeric
    rating_trend = df.groupby("Date")["Rating"].mean().reset_index()

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(x="Date", y="Rating", data=rating_trend, marker="o", ax=ax, color="orange")
    ax.set_xlabel("Date")
    ax.set_ylabel("Average Rating")
    ax.set_title("Average Rating Over Time", fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# 📈 Line Graph - Number of Reviews Over Time
elif trend_option == "Number of Reviews Over Time" and "Date" in df.columns:
    st.subheader("📈 Number of Reviews Over Time")
    review_trend = df.groupby("Date").size().reset_index(name="Review Count")

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(x="Date", y="Review Count", data=review_trend, marker="o", ax=ax, color="blue")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Reviews")
    ax.set_title("Review Trends Over Time", fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# 📈 Line Graph - Average Review Length Over Time
elif trend_option == "Average Review Length Over Time" and "Date" in df.columns:
    df["Review Length"] = df["Review"].apply(lambda x: len(str(x).split()))
    st.subheader("📈 Average Review Length Over Time")
    length_trend = df.groupby("Date")["Review Length"].mean().reset_index()

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(x="Date", y="Review Length", data=length_trend, marker="o", ax=ax, color="green")
    ax.set_xlabel("Date")
    ax.set_ylabel("Average Review Length (Words)")
    ax.set_title("Review Length Over Time", fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# 📈 Line Graph - Reviewer Engagement Over Time (How many unique reviewers per day)
elif trend_option == "Reviewer Engagement Over Time" and "Date" in df.columns:
    st.subheader("📈 Reviewer Engagement Over Time")
    engagement_trend = df.groupby("Date")["Reviewer Name"].nunique().reset_index()

    fig, ax = plt.subplots(figsize=(8, 4))
    sns.lineplot(x="Date", y="Reviewer Name", data=engagement_trend, marker="o", ax=ax, color="purple")
    ax.set_xlabel("Date")
    ax.set_ylabel("Unique Reviewers")
    ax.set_title("Reviewer Engagement Over Time", fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    st.pyplot(fig)

else:
    st.warning("No timestamp data available for trend analysis.")

# 📊 Histogram of Ratings
st.subheader("⭐ Rating Distribution - Histogram")
df["Rating"] = pd.to_numeric(df["Rating"], errors='coerce')  # Convert to numeric
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(df["Rating"].dropna(), bins=5, kde=True, color="purple")  # KDE for smoothness
ax.set_xlabel("Rating")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Ratings", fontsize=14, fontweight='bold')
st.pyplot(fig)

# 📝 Word Cloud
st.subheader("📝 Word Cloud")
if df["Review"].notna().sum() > 0:
    text = " ".join(str(review) for review in df["Review"].dropna())
    wordcloud = WordCloud(background_color="white", width=800, height=400).generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.warning("No reviews available for generating a word cloud.")

# 📋 Show Data Table
st.subheader("📋 Review Data")
st.dataframe(df[["Reviewer Name", "Rating", "Review", "Review Date", "Sentiment"]])
