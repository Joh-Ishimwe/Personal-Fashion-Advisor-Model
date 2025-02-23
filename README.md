# Personal Fashion Advisor

## Overview
This project aims to create a machine learning-based recommendation system that delivers personalized outfit and accessory suggestions by integrating user inputs such as body type, event type, and preferred colours.

## Dataset
The dataset used in this project was synthetically generated to include features like body type, event type, preferred colours, and style category. The dataset contains 10,000 samples.

## Models Implemented
1. **Classical ML Algorithms**: Logistic Regression, SVM, XGBoost
2. **Neural Network**: Simple model without optimization and a model with optimization techniques.

## Results
| Training Instance | Optimizer Used | Regularizer Used | Epochs | Early Stopping | Number of Layers | Learning Rate | Accuracy | F1 Score | Recall | Precision |
|-------------------|----------------|------------------|--------|----------------|------------------|---------------|----------|----------|--------|-----------|
| Instance 1        | -              | -                | 50     | No             | 2                | 0.001         | 0.85     | 0.84     | 0.83   | 0.85      |
| Instance 2        | Adam           | L2               | 100    | Yes            | 3                | 0.0001        | 0.88     | 0.87     | 0.86   | 0.88      |
| Instance 3        | RMSprop        | L1               | 75     | No             | 4                | 0.0005        | 0.87     | 0.86     | 0.85   | 0.87      |
| Instance 4        | Adam           | L2               | 50     | Yes            | 3                | 0.0001        | 0.89     | 0.88     | 0.87   | 0.89      |

## Summary
The best-performing model was Instance 4, which used the Adam optimizer, L2 regularization, 50 epochs, early stopping, 3 layers, and a learning rate of 0.0001. The neural network outperformed the classical ML algorithms in terms of accuracy and F1 score.

## Instructions
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the notebook `notebook.ipynb` to train the models and evaluate their performance.
4. Load the best saved model from the `saved_models` directory using the provided instructions in the notebook.