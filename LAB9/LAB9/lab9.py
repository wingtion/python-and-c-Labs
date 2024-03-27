import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database connection parameters
db_params = {
    "host": "your_host",
    "user": "your_user",
    "password": "your_password",
    "database": "your_database"
}

# Function to add data to the database
def add_data():
    # Open a pop-up window
    popup_window = tk.Toplevel(root)

    # Function to handle the "OK" button click
    def ok_button_click():
        # Retrieve the text from the text box
        text = text_entry.get()

        # Insert the data into the database
        try:
            conn = mysql.connector.connect(**db_params)
            cursor = conn.cursor()
            query = "INSERT INTO movies (ID, MOVIE, DATE, MCU_PHASE) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (selected_id.get(), text, "", ""))
            conn.commit()
            messagebox.showinfo("Success", "Data added to the database.")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"Failed to add data: {error}")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

        # Close the pop-up window
        popup_window.destroy()

    # Function to handle the "Cancel" button click
    def cancel_button_click():
        # Close the pop-up window
        popup_window.destroy()

    # Set up the pop-up window
    popup_window.title("Add Data")
    popup_window.geometry("300x100")

    # Add a text entry widget to enter the data
    text_label = tk.Label(popup_window, text="Enter Movie:")
    text_label.pack()
    text_entry = tk.Entry(popup_window)
    text_entry.pack()

    # Add "OK" and "Cancel" buttons
    ok_button = tk.Button(popup_window, text="OK", command=ok_button_click)
    ok_button.pack(side=tk.LEFT, padx=10)
    cancel_button = tk.Button(popup_window, text="Cancel", command=cancel_button_click)
    cancel_button.pack(side=tk.RIGHT, padx=10)

# Function to list all data from the database
def list_all_data():
    try:
        conn = mysql.connector.connect(**db_params)
        cursor = conn.cursor()
        query = "SELECT * FROM movies"
        cursor.execute(query)
        result = cursor.fetchall()

        # Clear the text box
        text_box.delete("1.0", tk.END)

        # Print the data in the text box
        for row in result:
            text_box.insert(tk.END, f"ID: {row[0]}, MOVIE: {row[1]}, DATE: {row[2]}, MCU_PHASE: {row[3]}\n")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to retrieve data: {error}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Set up the main window
root = tk.Tk()
root.title("Marvel Database")
root.geometry("400x300")

# Connect to the database and create the table if it doesn't exist
try:
    conn = mysql.connector.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS movies (ID INT, MOVIE VARCHAR(255), DATE DATE, MCU_PHASE VARCHAR(50))")
except mysql.connector.Error as error:
    messagebox.showerror("Error", f"Failed to connect to the database: {error}")

# Dropdown list for IDs
selected_id = tk.StringVar()
id_dropdown = tk