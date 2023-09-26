# Video Encoding Execution Prediction Model

## Overview

Welcome to the Video Encoding Execution Prediction Model project! This repository contains code and resources for building a prediction model that estimates video encoding execution times. The model is a crucial component for effective resource allocation in video coding applications.

## Data Source

We utilize the video complexity dataset from [ITEC at AAU](https://ftp.itec.aau.at/datasets/video-complexity/) as the primary data source. This dataset comprises various video characteristics, encoding parameters, and corresponding execution times, making it a valuable resource for our research.

## Machine Learning Algorithms

To develop an accurate prediction model, we employ a range of machine learning algorithms, including:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regression
- Random Forest Regression
- Gradient Boosting Regression
- Support Vector Regression

These algorithms collectively enable us to capture complex relationships between video properties, encoding settings, and execution times.

## Evaluation Metrics

The performance of our prediction model is assessed using several evaluation metrics, including:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Percentage Error

These metrics help us gauge the model's accuracy and reliability in estimating execution times for video encoding tasks.

## Application

Our prediction model plays a pivotal role in effective resource allocation within video coding applications. By accurately estimating encoding execution times, we empower developers and system administrators to optimize resource allocation, leading to enhanced real-time performance, reduced latency, and improved overall user experience.

## How to Use

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/sr-mtg/vvc_prediction
   cd vvc_prediction
