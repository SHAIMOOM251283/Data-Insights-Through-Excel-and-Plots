# Data Insights Through Excel and Plots

## Overview
This project automates the extraction of product data from an e-commerce test site and saves the data in Excel files for structured analysis. Additionally, it visualizes this data using interactive plots to uncover insights. The primary goal is to enable efficient data extraction and leverage Excel's versatility for further data manipulation and reporting.

### Key Tools and Libraries
- **Selenium:** Automates browser actions for web scraping.
- **Pandas:** Handles and structures scraped data for efficient storage and analysis.
- **OpenPyXL:** Facilitates saving data into Excel files.
- **Plotly:** Creates interactive and visually appealing scatter plots for insights.

## Project Structure
```
Data_Insights_Through_Excel_and_Plots/
│
├── EcomData/                     # Folder to store scraped data in Excel files
│   ├── laptops_data.xlsx         # Data for laptops
│   ├── phones_data.xlsx         # Data for tablets
│   └── tablets_data.xlsx          # Data for phones
│
├── ecommerce_data_scraper.py     # Script for scraping data
└── data_visualization.py         # Script for visualizing data
```
## Features
- **Excel File Integration:** Scraped data is organized and stored in Excel files, offering a practical format for further analysis or reporting.
- **Web Scraping with Selenium:** Automates navigation and data extraction from dynamically loaded e-commerce pages.
- **Data Handling with Pandas:** Processes the extracted data into structured formats suitable for Excel storage and visualization.
- **Interactive Visualizations with Plotly:** Generates scatter plots for an intuitive exploration of product data, such as price distribution and ratings.

## Installation

### Step 1: Clone the Repository

You have multiple options to clone the repository based on your preference:

#### Option 1: Using the Terminal
1. Open a terminal window.
2. Run the following commands:

   ```bash
   git clone https://github.com/SHAIMOOM251283/Data-Insights-Through-Excel-and-Plots.git
   cd Data_Insights_Through_Excel_and_Plots
   ```
#### Option 2: Using VS Code's Git Integration
1. Open **Visual Studio Code**.
2. Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS) to open the Command Palette.
3. Type **Git: Clone** and select it.
4. Enter the repository URL:

   ```
   https://github.com/SHAIMOOM251283/Data-Insights-Through-Excel-and-Plots.git
   ```

5. Choose a local folder to clone the repository into, then select **Open** to load the repository in VS Code.

#### Option 3: Using VS Code's Integrated Terminal
1. Open **VS Code**.
2. Open the integrated terminal by pressing `Ctrl + ` (backtick) or by navigating to **Terminal > New Terminal**.
3. Run the following commands in the integrated terminal:

   ```bash
   git clone https://github.com/SHAIMOOM251283/Data-Insights-Through-Excel-and-Plots.git
   cd Data_Insights_Through_Excel_and_Plots
   ```

### Step 2: Set Up the Python Environment and Install Dependencies

Ensure you have Python installed (preferably version 3.8 or later).

1. **Create a Virtual Environment** (recommended for isolated dependencies):
   
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:
   - **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```

3. **Install Required Packages**:

   Run the following command to install all necessary packages:

   ```bash
   pip install -r requirements.txt
   ```
   
   The project explicitly depends on the following libraries:
   - `selenium`
   - `plotly`
   - `pandas`
   - `openpyxl`

### Step 3: Verify Installation in VS Code

1. **Open the Project Folder**:
   - In VS Code, go to `File > Open Folder`, and select the `sky-scope` directory.

2. **Select Python Interpreter**:
   - Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS) to open the Command Palette.
   - Type **Python: Select Interpreter** and select the interpreter from the `.venv` directory created in Step 2.

### Step 4: Set up WebDriver:
   - Ensure you have [geckodriver](https://github.com/mozilla/geckodriver/releases) installed and added to your system’s PATH for Firefox. 

## Usage
1. **Run the data scraper:**
   ```bash
   python ecommerce_data_scraper.py
   ```
   This script:
   - Navigates the e-commerce site.
   - Extracts product data (laptops, tablets, and phones).
   - Saves the data in Excel files under the `EcomData` directory for easy access.

2. **Run the data visualization script:**
   ```bash
   python data_visualization.py
   ```
   This script:
   - Reads the Excel files.
   - Generates interactive scatter plots to analyze product prices and attributes.

## Visualizations
The project includes the following types of visualizations:
- **laptops_scatter_plot**: Scatter plot displaying product prices and attributes of laptops.
![Scatter Plot](https://github.com/SHAIMOOM251283/Data-Insights-Through-Excel-and-Plots/blob/main/laptops_scatter_plot.png)
- **tablets_scatter_plot**: Scatter plot displaying product prices and attributes of tablets.
![Scatter Plot](https://github.com/SHAIMOOM251283/Data-Insights-Through-Excel-and-Plots/blob/main/tablets_scatter_plot.png)
- **phones_scatter_plot**: Scatter plot displaying product prices and attributes of phones. 
![Scatter Plot](https://github.com/SHAIMOOM251283/Data-Insights-Through-Excel-and-Plots/blob/main/phones_scatter_plot.png)

## Functionality Demonstration
Watch the video below to see the interactive scatter plots:
[![Watch the Dashboard Functionality Screencast](https://img.shields.io/badge/Watch%20Video-Click%20Here-blue)](https://github.com/SHAIMOOM251283/Data-Insights-Through-Excel-and-Plots/blob/main/ScatterPlotsScreencast.mp4)

## Project Highlights
- **Seamless Data Storage:** Excel files serve as the backbone of this project, offering a universally accepted format for data storage and usage. This makes the data readily usable for business analysis, reporting, or further processing.
- **Module Utilization:**
  - **Selenium:** Efficiently scrapes data from dynamic web pages with support for "load more" buttons.
  - **Pandas:** Structures and cleans data for accurate storage and visualization.
  - **OpenPyXL:** Writes data into Excel files, enabling reuse and easy sharing of insights.
  - **Plotly:** Converts raw data into interactive visualizations, enhancing the ability to derive actionable insights.
- **User-Friendly Approach:** Each product category (laptops, tablets, and phones) is handled separately for clear organization and analysis.

## License
This project is licensed under the [MIT License](LICENSE).

