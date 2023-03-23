# Import required libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import yfinance as yf

# Set the stock symbol and data range
symbol = "AAPL"
start_date = "2015-01-01"
end_date = "2021-12-31"

# Get the stock data from Yahoo Finance
stock_data = yf.download(symbol, start_date, end_date)

# Create a new column with the stock's closing price shifted by 1 day
stock_data['Previous_Close'] = stock_data['Close'].shift(1)

# Remove any rows with missing data
stock_data.dropna(inplace=True)

# Define the input features and target variable
X = stock_data['Previous_Close'].values.reshape(-1, 1)
y = stock_data['Close'].values.reshape(-1, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Predict the stock prices for the testing data
y_pred = lr_model.predict(X_test)

# Print the model's accuracy
print("Model Accuracy: ", lr_model.score(X_test, y_test))

# Predict the stock price for tomorrow
prev_close = stock_data.iloc[-1]['Close']
next_close = lr_model.predict([[prev_close]])[0][0]
print(f"Tomorrow's predicted closing price for {symbol}: ${next_close:.2f}")
