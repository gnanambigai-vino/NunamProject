import mysql.connector
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
import pandas as pd
import plotly.express as px

st.title("Nunam Internship Assignment")

st.header("State Of Health")
sidebar_name = st.sidebar.selectbox("Select an Option", ["Dashboard", "Cell Id:5329","Cell Id:5308"])

if sidebar_name == "Dashboard":

    # Connect to MySQL
    mydb = mysql.connector.connect(host="localhost",
                user="jai",
                password="jai123",
                database= "nunam",
                auth_plugin='mysql_native_password',
                charset='utf8mb4'
                )

    # Create a cursor object
    cursor = mydb.cursor()

    # Define your query for the first pie chart
    query = "SELECT Total_Cycle, Capacity_of_discharge FROM soh"

    # Execute the query
    cursor.execute(query)

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Get column names
    columns = [desc[0] for desc in cursor.description]

    # Create DataFrame
    df1 = pd.DataFrame(rows, columns=columns)

    # Close cursor and connection
    cursor.close()
    mydb.close()

    # Perform the necessary calculations
    df1['Capacity_of_discharge'] = (df1['Capacity_of_discharge'] / 3000) * 100

    # Create a pie chart for the first dataset
    fig1, ax1 = plt.subplots()
    labels1 = df1['Total_Cycle']
    sizes1 = df1['Capacity_of_discharge']
    explode1 = (0.1, 0, 0)  # explode the 1st slice (if needed)

    ax1.pie(sizes1, explode=explode1, labels=labels1, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.set_title("Capacity of Discharge per Total Cycle (soh)")

    # Convert the first plot to a PNG image and display it in Streamlit
    buf1 = io.BytesIO()
    plt.savefig(buf1, format="png")
    buf1.seek(0)

    # Connect to MySQL for the second dataset
    mydb = mysql.connector.connect(host="localhost",
                user="jai",
                password="jai123",
                database= "nunam",
                auth_plugin='mysql_native_password',
                charset='utf8mb4'
                )

    # Create a cursor object
    cursor = mydb.cursor()

    # Define your query for the second pie chart
    query = "SELECT Total_Cycle, Capacity_of_discharge FROM soh1"

    # Execute the query
    cursor.execute(query)

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Get column names
    columns = [desc[0] for desc in cursor.description]

    # Create DataFrame
    df2 = pd.DataFrame(rows, columns=columns)

    # Close cursor and connection
    cursor.close()
    mydb.close()

    # Perform the necessary calculations
    df2['Capacity_of_discharge'] = (df2['Capacity_of_discharge'] / 3000) * 100

    # Create a pie chart for the second dataset
    fig2, ax2 = plt.subplots()
    labels2 = df2['Total_Cycle']
    sizes2 = df2['Capacity_of_discharge']
    explode2 = (0.1, 0, 0)  # explode the 1st slice (if needed)

    ax2.pie(sizes2, explode=explode2, labels=labels2, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.set_title("Capacity of Discharge per Total Cycle (soh1)")

    # Convert the second plot to a PNG image and display it in Streamlit
    buf2 = io.BytesIO()
    plt.savefig(buf2, format="png")
    buf2.seek(0)

    # Display the plots side by side
    col1, col2 = st.columns(2)

    with col1:
        st.header("Cell ID:5329")
        st.image(buf1, caption="Capacity of Discharge per Total Cycle (soh)", use_column_width=True)

    with col2:
        st.header("Cell ID:5308")
        st.image(buf2, caption="Capacity of Discharge per Total Cycle (soh1)", use_column_width=True)



if sidebar_name == "Cell Id:5329":

    # Create two columns for side-by-side plots
    col1, col2 = st.columns(2)

    # Voltage vs Time
    with col1:
        st.subheader("Voltage vs Time")

        # Connect to MySQL
        mydb = mysql.connector.connect(host="localhost",
                user="jai",
                password="jai123",
                database= "nunam",
                auth_plugin='mysql_native_password',
                charset='utf8mb4'
                )

        # Create a cursor object
        cursor = mydb.cursor()

        # Define your query
        query = "SELECT Absolute_Time, Voltage FROM data1_detail LIMIT 20"

        # Execute the query
        cursor.execute(query)

        # Fetch all rows from the executed query
        rows = cursor.fetchall()

        # Get column names
        columns = [desc[0] for desc in cursor.description]

        # Create DataFrame
        df = pd.DataFrame(rows, columns=columns)

        # Close cursor and connection
        cursor.close()
        mydb.close()

        # Convert 'Absolute_Time' to datetime format
        df['Absolute_Time'] = pd.to_datetime(df['Absolute_Time'], format='%Y-%m-%d %H:%M:%S')

        # Sort the DataFrame by 'Absolute_Time'
        df = df.sort_values('Absolute_Time')

        # Plotting
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df['Absolute_Time'], df['Voltage'], marker='o', linestyle='-')
        ax.set_title("Voltage vs Time")
        ax.set_xlabel("Time")
        ax.set_ylabel("Voltage")
        ax.grid(True)
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

        # Display the plot in Streamlit
        st.pyplot(fig)

    # Current vs Time
    with col2:
        st.subheader("Current vs Time")

        # Connect to MySQL
        mydb = mysql.connector.connect(host="localhost",
                user="jai",
                password="jai123",
                database= "nunam",
                auth_plugin='mysql_native_password',
                charset='utf8mb4'
                )

        # Create a cursor object
        cursor = mydb.cursor()

        # Define your query
        query = "SELECT Cur, Absolute_Time FROM data1_detail LIMIT 20"

        # Execute the query
        cursor.execute(query)

        # Fetch all rows from the executed query
        rows = cursor.fetchall()

        # Get column names
        columns = [desc[0] for desc in cursor.description]

        # Create DataFrame
        df = pd.DataFrame(rows, columns=columns)

        # Close cursor and connection
        cursor.close()
        mydb.close()

        # Convert 'Absolute_Time' to datetime format
        df['Absolute_Time'] = pd.to_datetime(df['Absolute_Time'], format='%Y-%m-%d %H:%M:%S')

        # Sort the DataFrame by 'Absolute_Time'
        df = df.sort_values('Absolute_Time')

        # Plotting
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df['Absolute_Time'], df['Cur'], marker='o', linestyle='-')
        ax.set_title("Current vs Time")
        ax.set_xlabel("Time")
        ax.set_ylabel("Current (Cur)")
        ax.grid(True)
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

        # Display the plot in Streamlit
        st.pyplot(fig)

    mydb = mysql.connector.connect(host="localhost",
                user="jai",
                password="jai123",
                database= "nunam",
                auth_plugin='mysql_native_password',
                charset='utf8mb4'
                )
    cursor = mydb.cursor()

    # Query for Auxiliary Channel
    query_aux = """SELECT Absolute_Time, Auxiliary_channel 
                FROM data1_detail 
                JOIN data1_temp ON data1_detail.Record_Index = data1_temp.Record_Index 
                LIMIT 20"""
    cursor.execute(query_aux)
    rows_aux = cursor.fetchall()
    columns_aux = [desc[0] for desc in cursor.description]
    df_aux = pd.DataFrame(rows_aux, columns=columns_aux)

    # Close cursor and connection
    cursor.close()
    mydb.close()

    # Convert 'Absolute_Time' to datetime format and sort
    df_aux['Absolute_Time'] = pd.to_datetime(df_aux['Absolute_Time'], format='%Y-%m-%d %H:%M:%S')
    df_aux = df_aux.sort_values('Absolute_Time')

    # Connect to MySQL and fetch data for Capacity
    mydb = mysql.connector.connect(host="localhost",
                user="jai",
                password="jai123",
                database= "nunam",
                auth_plugin='mysql_native_password',
                charset='utf8mb4'
                )
    cursor = mydb.cursor()

    # Query for Capacity
    query_cap = "SELECT Absolute_Time, Capacity FROM data1_detail LIMIT 20"
    cursor.execute(query_cap)
    rows_cap = cursor.fetchall()
    columns_cap = [desc[0] for desc in cursor.description]
    df_cap = pd.DataFrame(rows_cap, columns=columns_cap)

    # Close cursor and connection
    cursor.close()
    mydb.close()

    # Convert 'Absolute_Time' to datetime format and sort
    df_cap['Absolute_Time'] = pd.to_datetime(df_cap['Absolute_Time'], format='%Y-%m-%d %H:%M:%S')
    df_cap = df_cap.sort_values('Absolute_Time')

    # Plotting both graphs side by side
    col1, col2 = st.columns(2)

    # Plot for Auxiliary Channel
    with col1:
        st.subheader("Auxiliary Channel vs Time")
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        ax1.plot(df_aux['Absolute_Time'], df_aux['Auxiliary_channel'], marker='o')
        ax1.set_title("Auxiliary Channel vs Time")
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Auxiliary Channel")
        ax1.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig1)

    # Plot for Capacity
    with col2:
        st.subheader("Capacity vs Time")
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        ax2.plot(df_cap['Absolute_Time'], df_cap['Capacity'], marker='o')
        ax2.set_title("Capacity vs Time")
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Capacity")
        ax2.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig2)


if sidebar_name == "Cell Id:5308":

    # Create two columns for side-by-side plots
    col1, col2 = st.columns(2)

    # Voltage vs Time
    with col1:
        st.subheader("Voltage vs Time")

        # Connect to MySQL
        mydb = mysql.connector.connect(host="localhost",
                user="jai",
                password="jai123",
                database= "nunam",
                auth_plugin='mysql_native_password',
                charset='utf8mb4'
                )

        # Create a cursor object
        cursor = mydb.cursor()

        # Define your query
        query = "SELECT Absolute_Time, Voltage FROM data2_detail LIMIT 20"

        # Execute the query
        cursor.execute(query)

        # Fetch all rows from the executed query
        rows = cursor.fetchall()

        # Get column names
        columns = [desc[0] for desc in cursor.description]

        # Create DataFrame
        df = pd.DataFrame(rows, columns=columns)

        # Close cursor and connection
        cursor.close()
        mydb.close()

        # Convert 'Absolute_Time' to datetime format
        df['Absolute_Time'] = pd.to_datetime(df['Absolute_Time'], format='%Y-%m-%d %H:%M:%S')

        # Sort the DataFrame by 'Absolute_Time'
        df = df.sort_values('Absolute_Time')

        # Plotting
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df['Absolute_Time'], df['Voltage'], marker='o', linestyle='-')
        ax.set_title("Voltage vs Time")
        ax.set_xlabel("Time")
        ax.set_ylabel("Voltage")
        ax.grid(True)
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

        # Display the plot in Streamlit
        st.pyplot(fig)

    # Current vs Time
    with col2:
        st.subheader("Current vs Time")

        # Connect to MySQL
        mydb = mysql.connector.connect(host="localhost",
                user="jai",
                password="jai123",
                database= "nunam",
                auth_plugin='mysql_native_password',
                charset='utf8mb4'
                )

        # Create a cursor object
        cursor = mydb.cursor()

        # Define your query
        query = "SELECT Cur, Absolute_Time FROM data2_detail LIMIT 20"

        # Execute the query
        cursor.execute(query)

        # Fetch all rows from the executed query
        rows = cursor.fetchall()

        # Get column names
        columns = [desc[0] for desc in cursor.description]

        # Create DataFrame
        df = pd.DataFrame(rows, columns=columns)

        # Close cursor and connection
        cursor.close()
        mydb.close()

        # Convert 'Absolute_Time' to datetime format
        df['Absolute_Time'] = pd.to_datetime(df['Absolute_Time'], format='%Y-%m-%d %H:%M:%S')

        # Sort the DataFrame by 'Absolute_Time'
        df = df.sort_values('Absolute_Time')

        # Plotting
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(df['Absolute_Time'], df['Cur'], marker='o', linestyle='-')
        ax.set_title("Current vs Time")
        ax.set_xlabel("Time")
        ax.set_ylabel("Current (Cur)")
        ax.grid(True)
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

        # Display the plot in Streamlit
        st.pyplot(fig)

    mydb = mysql.connector.connect(host="localhost",
                user="jai",
                password="jai123",
                database= "nunam",
                auth_plugin='mysql_native_password',
                charset='utf8mb4'
                )
    cursor = mydb.cursor()

    # Query for Auxiliary Channel
    query_aux = """SELECT Absolute_Time, Auxiliary_channel 
                FROM data2_detail 
                JOIN data2_temp ON data2_detail.Record_Index = data2_temp.Record_Index 
                LIMIT 20"""
    cursor.execute(query_aux)
    rows_aux = cursor.fetchall()
    columns_aux = [desc[0] for desc in cursor.description]
    df_aux = pd.DataFrame(rows_aux, columns=columns_aux)

    # Close cursor and connection
    cursor.close()
    mydb.close()

    # Convert 'Absolute_Time' to datetime format and sort
    df_aux['Absolute_Time'] = pd.to_datetime(df_aux['Absolute_Time'], format='%Y-%m-%d %H:%M:%S')
    df_aux = df_aux.sort_values('Absolute_Time')

    # Connect to MySQL and fetch data for Capacity
    mydb = mysql.connector.connect(host="localhost",
                user="jai",
                password="jai123",
                database= "nunam",
                auth_plugin='mysql_native_password',
                charset='utf8mb4'
                )
    cursor = mydb.cursor()

    # Query for Capacity
    query_cap = "SELECT Absolute_Time, Capacity FROM data2_detail LIMIT 20"
    cursor.execute(query_cap)
    rows_cap = cursor.fetchall()
    columns_cap = [desc[0] for desc in cursor.description]
    df_cap = pd.DataFrame(rows_cap, columns=columns_cap)

    # Close cursor and connection
    cursor.close()
    mydb.close()

    # Convert 'Absolute_Time' to datetime format and sort
    df_cap['Absolute_Time'] = pd.to_datetime(df_cap['Absolute_Time'], format='%Y-%m-%d %H:%M:%S')
    df_cap = df_cap.sort_values('Absolute_Time')

    # Plotting both graphs side by side
    col1, col2 = st.columns(2)

    # Plot for Auxiliary Channel
    with col1:
        st.subheader("Auxiliary Channel vs Time")
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        ax1.plot(df_aux['Absolute_Time'], df_aux['Auxiliary_channel'], marker='o')
        ax1.set_title("Auxiliary Channel vs Time")
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Auxiliary Channel")
        ax1.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig1)

    # Plot for Capacity
    with col2:
        st.subheader("Capacity vs Time")
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        ax2.plot(df_cap['Absolute_Time'], df_cap['Capacity'], marker='o')
        ax2.set_title("Capacity vs Time")
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Capacity")
        ax2.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig2)
