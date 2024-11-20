# Task 1: Adding Basic Analystic to Track User Interactions

## Final Report


### 1. Introduction 
This task aimed to devalop a dashboard for analyzing chatbot interactions. By tracking key metrics scuh as the number of queries, most common topics , and user satisfaction ratings, the dashboard provides actionable insights into chatbot usage and performance. This tool is designed to aid in evaluating user behavior and enhancing the chatbot's effectiveness.

### 2. Background
In today's digital landscape, chatbot play an essential role in authomating customer interactions across industies. To ensure their effectiveness, organization rely on analytics to evaluate user engagement  and satisfaction. This task utilized data from the "NLP Chatbot" dataset on Kaggle to extrect meaning ful patterns and create an interactive dashboard.

Dataset :
Raw dataset link : 
[URL](https://github.com/VigneshvickyData/Intern_project-1_Analytics_Chatbot/raw/refs/heads/main/notebook/data/chatbot_dataset.csv)

Processed dataset link:
[URL](https://github.com/VigneshvickyData/Intern_project-1_Analytics_Chatbot/raw/refs/heads/main/notebook/Processed_dataset.csv)

### 3. Learning Objectives
1. Apply data analysis and visualization techniques to derive insights.
2. Learn to create interactive dashboards using Streamlit.
3. Summarize large datasets into clear and concise metrics.

### 4. Activities and Tasks
Dataset Preparation:
* Loaded the "NLP Chatbot"  dataset from Kaggle. 
* Cleaned and processed data to calculate key matrics.
Metrics Development:
* Calculated total queries and the average user satisfaction score.
* Identified the most common topics based on user queries.

Visualization:

Designed visuals, including:
* Query trends over time.
* Satisfaction rating distribution.
* Most common topics.
Dashboard Creation:
* Built an interactive dashboard using Streamlit, enabling user to explore chatbot metrics.

### 5. Skills and Competencies
Technical Skills:
* Python: Used Libraries such as Pandas ,Matplotlib, Seaborn, and Streamlit.
* Data preprocessing and cleaning.
* Data visualization techniques.
       
Core Competencies:
* Analytical thinking for interpreting data insights.
* Attention to detail to ensure data and visualizations are accurate.
* Presentation of technical insights in an intuitive dashboard.

### 6. Feedback and Evidence
Feedback:
* Positive remark from the mentor on the dashboard's clarity and user-friendliness.
* Received suggestion for adding interactive filters, which can be explored in future tasks.
Evidence:
### Screenshots of the final dashboard :

![App Screenshot](https://github.com/VigneshvickyData/Data_Branching/blob/main/1.png?raw=true)

![App Screenshot](https://github.com/VigneshvickyData/Data_Branching/blob/main/2.png?raw=true)

![App Screenshot](https://github.com/VigneshvickyData/Data_Branching/blob/main/3.png?raw=true)

![App Screenshot](https://github.com/VigneshvickyData/Data_Branching/blob/main/4.png?raw=true)

### Running Source Code: (GITHUB repository link)
[URL](https://github.com/VigneshvickyData/Intern_project-1_Analytics_Chatbot)  

### 7. Challenge and Solutions 
Challenge 1. Cleaning raw data to accurately identify common topics.

* Solution: Create a PReprocessing pipeline to filter noise and applied basic NLP techniques to extract query topics.

Challenge 2. Improving Streamlit performance with large datasets.

* Solution: Implemented caching mechanism to optimize data loading and improve responsiveness.

### 8. Outcomes and impact 
Outcomes:

Developed a functional dashboard displaying:
* Total queries, query trends, and most common topics.
* Satisfaction rating distribution.
* Delivered insights for optimizing chatbot responses and enchancing user satisfaction.
      
Impact:
* The dashboard provides a foundation for future enhancements, such as integrating real-time data or interactive filters.

* Improved my technical knowledge and project management skills for real-world  data analysis projects.          

### 9. Conclusion
Task 1 Successfully demonstrated how analyttics can transform raw chatbot data into meaningful insights. By developing an interactive dashboard, I gained valuable experience in data processing, visulation, and software development. These skils will contribute significant to future tasks in this internship.

### 10. Development Process (Dily Report Summary)
Day 1 
- Experimental work: explored the dataset and outlined a rough project structure.

Day 2 
- Create the Project structure.
- Performed exploratory data analysis (EDA ) and davelopment the code for metrics and dashboard visualization.

Day 3 
- Conducted final validation and testing of the chatbot analytics dashboard.
- Verified metric calculations and chart rendering.
- Uploaded the source code to github.
- Prepared and reviewed the final report for submission.

Day 4  
- submit the final report with source code of the task 1 in github        

### To run the Environment:
- Environment -> conda create -n intern_task1 python=3.9 -y
### Activitie the Environment :
-  conda activate intern_task1