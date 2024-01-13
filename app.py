from flask import Flask, render_template, send_file
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd

app = Flask(__name__)

# Function to read data from a CSV file
def read_csv():
    # Replace 'your_data.csv' with the actual name of your CSV file
    df = pd.read_csv('data.csv')
    return df

# Function to generate a plot from CSV data
def generate_plot():
    # Read data from CSV
    df = read_csv()

    # Assuming the CSV file has columns 'x' and 'y'
    x = df['x']
    y = df['y']

    # Create a plot
    plt.plot(x, y)
    plt.title('Data from CSV')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Save the plot to a BytesIO object
    img_stream = BytesIO()
    plt.savefig(img_stream, format='png')
    img_stream.seek(0)

    # Clear the plot to avoid memory leaks
    plt.clf()

    return img_stream

# Route to serve the plot
@app.route('/api/plot')
def serve_plot():
    plot = generate_plot()
    return send_file(plot, mimetype='image/png')

# Route to display an HTML page with the plot
@app.route('/')
def index():
    return render_template('index.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
