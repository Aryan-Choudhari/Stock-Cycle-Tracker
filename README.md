# Project Overview

This project is a web application that fetches and analyzes stock data from Yahoo Finance using the yfinance library. It calculates the maximum continuous gain and loss days, as well as the gain and loss percentages for a list of stocks. The results are displayed on a simple web interface.
This is a data minimg based trading strategy and which when combined with volume analysis can be helpful in identifying stocks which might experience a slight pull back or a minor bounce back from current levels based on historical trends analysed.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Function Descriptions](#function-descriptions)
  - [Backend (app.py)](#backend-apppy)
  - [Frontend (index.html, styles.css, script.js)](#frontend-indexhtml-stylescss-scriptjs)
- [How to Run the Code](#how-to-run-the-code)
- [Contribution](#contribution)
- [Contributing](#contributing)
- [License](#license)
- [Project Demo](#project-demo)

## Technologies Used

- Python
- Flask
- yfinance
- HTML
- CSS
- JavaScript
- Fetch API

## Function Descriptions

### Backend (app.py)

The backend of the project is built with Flask. Below are the main functions used:

- **max_continuous_gain_and_loss(symbol, period)**: Fetches stock data and calculates the maximum continuous gain and loss days.
- **max_current_gain(symbol, period_gain)**: Fetches stock data and calculates the current continuous gain days.
- **max_current_loss(symbol, period_loss)**: Fetches stock data and calculates the current continuous loss days.
- **max_pct_gain_and_loss(symbol, period)**: Fetches stock data and calculates the gain and loss percentages.
- **max_pct_gain(symbol, period)**: Fetches stock data and calculates the gain percentage.
- **max_pct_loss(symbol, period)**: Fetches stock data and calculates the loss percentage.

### Frontend (index.html, styles.css, script.js)

The frontend is built using HTML, CSS, and JavaScript.

- **index.html**: The main HTML file that sets up the structure of the web page, including buttons and sections to display results.
- **styles.css**: Contains styles to make the web page visually appealing, including layout, colors, and fonts.
- **script.js**: Handles the interaction with the backend using the Fetch API. It sends a request to the Flask server and displays the results on the web page.

## How to Run the Code

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/stock-analyzer.git
    ```
2. Navigate to the project directory:
    ```bash
    cd stock-analyzer
    ```
3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask server:
    ```bash
    python app.py
    ```
5. Open `index.html` in a web browser to interact with the web application.

## Contribution
The frontend to the project has been contributed to by Ayush Aswal(https://github.com/Ayush583-Aswal).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

## License

This project is licensed under the MIT License.

## Project Demo

You can add a GIF of the working project here.

![Project Demo](CycleTracking.gif)
