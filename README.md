# DATA VISUALIZATION

DATA VIS ....

## Prerequisites

Make sure you have the following installed on your machine:

- [Python](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads/)

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:w4lck3r/Data_vis.git
    ```

2. Change into the project directory:

    ```bash
    cd Data_vis
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\Activate
        ```
        - IF it doesn't work try :
        ```bash
        cd DATA_VIS
        cd venv
        cd Scripts
        ./activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to [http://localhost:5000/](http://localhost:5000/).

## Additional Notes

- Customize the data source:

    Replace the sample data in the `data.csv` file with your own data.

- Customize the visualization:

    Modify the code in `app.py` to suit your specific data visualization needs.

