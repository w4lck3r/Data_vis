from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

app = Flask(__name__)

# Function to render the home page
@app.route('/')
def home():
    return render_template('index.html')

# Function to handle file upload and visualization
@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file is included in the request
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    # Check if the file has a valid extension (CSV)
    if file.filename == '' or not file.filename.endswith('.csv'):
        return redirect(request.url)

    # Read the CSV file
    df = pd.read_csv(file)

    # Visualize the data with Line charts
    plt.figure(figsize=(10, 6))
    for column in df.columns:
        plt.plot(df[column], label=column)
    plt.title('Line Chart')
    plt.legend()
    plt.savefig('static/line_chart.png')
    plt.close()  # Close the figure

    # Visualize the data with Histogram
    plt.figure(figsize=(10, 6))
    for column in df.columns:
        plt.hist(df[column], bins=20, alpha=0.5, label=column)
    plt.title('Histogram')
    plt.legend()
    plt.savefig('static/histogram.png')
    plt.close()  # Close the figure

    # Visualize the data with Heat map
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Heat Map')
    plt.savefig('static/heat_map.png')
    plt.close()  # Close the figure

    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
