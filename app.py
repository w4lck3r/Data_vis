import threading
import multiprocessing
from flask import Flask, render_template, request, redirect, url_for, send_file
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import os

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

    # Create a background process to create the figures
    p = multiprocessing.Process(target=create_figures, args=(df,))
    p.start()
    p.join()  # Wait for the process to complete

    # Return the result template
    return render_template('result.html')



# Function to create Matplotlib figures for the uploaded data
def create_figures(df):
    # Get the absolute path to the static folder
    static_folder = os.path.join(os.getcwd(), 'static')

    # Create line chart
    plt.figure(figsize=(10, 6))
    for column in df.columns:
        plt.plot(df[column], label=column)
    plt.title('Line Chart')
    plt.legend()

    # Save the line chart as a PNG image in the static folder
    line_chart_path = 'line_chart.png'
    plt.savefig(os.path.join(static_folder, line_chart_path))
    plt.close()

    # Create histogram
    plt.figure(figsize=(10, 6))
    for column in df.columns:
        plt.hist(df[column], bins=20, alpha=0.5, label=column)
    plt.title('Histogram')
    plt.legend()

    # Save the histogram as a PNG image in the static folder
    histogram_path = 'histogram.png'
    plt.savefig(os.path.join(static_folder, histogram_path))
    plt.close()

    # Create heat map
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Heat Map')

    # Save the heat map as a PNG image in the static folder
    heat_map_path = 'heat_map.png'
    plt.savefig(os.path.join(static_folder, heat_map_path))
    plt.close()

    # Return the relative paths to the generated image files
    return line_chart_path, histogram_path, heat_map_path


if __name__ == '__main__':
    app.run(debug=True)