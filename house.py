import pandas as pd
import numpy as np
import math
from sklearn import linear_model
import tkinter as tk
from tkinter import messagebox

# Load and prepare the data
df = pd.read_excel("C:/Users/yassi/Videos/Book 1.xlsx")

# Handle missing values
median = math.floor(df.bedrooms.median())
df.bedrooms = df.bedrooms.fillna(median)

# Train the model
reg = linear_model.LinearRegression()
reg.fit(df[['area', 'bedrooms', 'age']], df.price)

# GUI
def predict_price():
    try:
        area = float(entry_area.get())
        bedrooms = float(entry_bedrooms.get())
        age = float(entry_age.get())
        
        prediction = reg.predict([[area, bedrooms, age]])
        messagebox.showinfo("Predicted Price", f"Estimated Price: ${int(prediction[0]):,}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input!\n{str(e)}")

# Create the window
root = tk.Tk()
root.title("House Price Predictor")
root.geometry("300x250")
root.resizable(False, False)

# Labels and Entries
tk.Label(root, text="Area (sqft):").pack(pady=5)
entry_area = tk.Entry(root)
entry_area.pack()

tk.Label(root, text="Bedrooms:").pack(pady=5)
entry_bedrooms = tk.Entry(root)
entry_bedrooms.pack()

tk.Label(root, text="Age of House:").pack(pady=5)
entry_age = tk.Entry(root)
entry_age.pack()

# Predict Button
tk.Button(root, text="Predict Price", command=predict_price).pack(pady=20)

# Start the GUI
root.mainloop()
