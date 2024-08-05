# PRODIGY_ML_01

# House Prices Prediction Using Linear Regression

This project demonstrates the use of linear regression to predict house prices based on various features.

## Table of Contents
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Model Evaluation](#model-evaluation)
- [Visualization](#visualization)
- [Acknowledgements](#acknowledgements)

## Dataset
The dataset used in this project contains information about house prices and various features related to the houses. The dataset is loaded from a CSV file named `train.csv`.

## Requirements
- Python 3.6+
- pandas
- scikit-learn
- matplotlib

## Installation
Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
```

Install the required packages:

```bash
pip install pandas scikit-learn matplotlib
```

## Usage

### Loading the Dataset
The dataset is loaded using pandas.

### Feature Selection
The features used for prediction are:
- GrLivArea (Above grade (ground) living area square feet)
- BedroomAbvGr (Number of bedrooms above basement level)
- FullBath (Number of full bathrooms)

### Splitting the Data
The dataset is split into training and testing sets using an 80-20 split.

### Model Training
A linear regression model is trained using the training data.

### Model Prediction
The model predicts house prices on the test data.

### Running the Code
Execute the code to train the model and make predictions:

```python
python train.py
```

## Model Evaluation
The model is evaluated using the following metrics:
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)

Sample evaluation results:

```
Mean Squared Error: 2806426667.25
Root Mean Squared Error: 52975.72
R-squared: 0.63
```

## Visualization
A scatter plot is created to visualize the actual house prices vs. predicted house prices.

## Acknowledgements
- The dataset source for house prices prediction.
- The scikit-learn and pandas teams for their amazing libraries.

