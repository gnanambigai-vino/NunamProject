Assignment
Nunam Technologies India Pvt Ltd

Overview:
This project involves creating data visualizations and analytics dashboards using data from a MySQL database. 
The project includes generating pie charts and line graphs to visualize various metrics such as Capacity of Discharge, Voltage, Current, and Auxiliary Channel over time. 
The data is fetched from a MySQL database and displayed using Streamlit for interactive web applications.

In addition, I have created a video to showcase the working of the website.

Features:
Dashboard Visualization: Displays interactive charts for various metrics.
Data Fetching: Connects to a MySQL database to retrieve data.
Visualizations: Includes pie charts and line graphs for data analysis.
Streamlit Integration: Provides an interactive web interface for visualizing data.

Project Structure:
Nunam project/nunam.py: Main Streamlit application file.
streamlit run nunam.py --server.port 8080 
README.md: Project documentation.

Queries and Data:
SELECT Total_Cycle, Capacity_of_discharge FROM soh: Query used to fetch data for the Capacity of Discharge pie chart.
SELECT Absolute_Time, Voltage FROM data1_detail: Query used to fetch data for Voltage vs Time line graph.
SELECT Absolute_Time, Cur FROM data1_detail: Query used to fetch data for Current vs Time line graph.
SELECT Absolute_Time, Auxiliary_channel FROM data1_detail JOIN data1_temp ON data1_detail.Record_Index=data1_temp.Record_Index: Query used to fetch data for Auxiliary Channel vs Time line graph.
Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements.

Function: Codebase was done on Jupyter notebook, and streamlit was run on VS Code.
