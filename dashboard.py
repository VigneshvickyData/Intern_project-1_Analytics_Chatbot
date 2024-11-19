import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("notebook\Processed_dataset.csv")  #notebook\Processed_dataset.csv

df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Day'] = df['Timestamp'].dt.day
df['Hour'] = df['Timestamp'].dt.hour

# Metrics
total_queries = df.shape[0]
avg_satisfaction = df['User_Rating'].mean()
queries_per_day =df.groupby('Day').size()
queries_per_hour =df.groupby('Hour').size()
top_topics = df['Entities'].value_counts().head(10)

# Dashboard
st.title("Chatbot Analystics Dashboard")


st.subheader("Key Statistics")
st.metric("Total Queries", total_queries)
st.metric("Average User Satisfaction", round(avg_satisfaction, 2))

st.subheader("Total Queries Over Time")
st.line_chart(queries_per_day)

# satisfaction ratings

st.subheader("Satisfaction Rating Distribution")
fig, ax = plt.subplots()
sns.histplot(df['User_Rating'], kde=True, bins=5, ax=ax)
ax.set_title("User Satisfaction Ratings")
st.pyplot(fig)

#most common topics
st.subheader("Most Common Topics")
st.bar_chart(top_topics)


# queries by hour
st.subheader("Queries by hour")
st.bar_chart(queries_per_hour)


st.text("Dashboard built with Streamlit")