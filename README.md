# Personal Fashion Advisor

## Overview
This a classification machine learning recommendation system that aims to delivers personalized outfit and accessory suggestions by integrating user inputs. The primary focus of the project is classifying fashion items based on attributes such as material, color, price, season, and comfort to improve existing systems lacking personalized outfit recommendations.

## Dataset
The dataset is syntethic genereted data using pandas, due to unavailablity of existing non-generic dataset that algin the puporse of my model. It contains 10,000 samples with features like material type, color brightness, price, season, and comfort level, correlated with five fashion categories (Casual, Formal, Sportswear, Partywear, Traditional)

## Models Implemented
1. **Classical ML Algorithms**: 
    - Logistic Regression with hyperparameter tuning using GridSearchCV.
    - XGBoost with hyperparameter tuning using GridSearchCV.
2. **Neural Network**: 
    - A simple model without any optimization techniques.
    - Models with various optimization techniques including:
        - Adam and SGD optimizers.
        - Varying learning rates.
        - Varying number of hidden layers.
        
## Results
| Training Instance | Optimizer Used | Regularizer Used | Epochs | Early Stopping | Number of Layers | Learning Rate | Accuracy | F1 Score | Recall | Precision |
|-------------------|----------------|------------------|--------|----------------|------------------|---------------|----------|----------|--------|-----------|
| Instance 1 (Basic NN) | -              | -                | 10     | No             | 2                | Default       | 0.79     | 0.79     | 0.79   | 0.79      |
| Instance 2 (Optimized NN) | Adam           | -               | 100    | No            | 50               | 0.0001        | 0.81     | 0.81     | 0.81   | 0.81      |
| Instance 3 (Optimized NN)| SGD            | -               | 100    | No             | 50               | 0.0005        | 0.82     | 0.82     | 0.82   | 0.82      |
| Instance 4 (Logistic Regression) | liblinear/lbfgs | - | - | - | - | - | 0.83 | 0.83 | 0.83 | 0.83 |
| Instance 5 (XGBoost) | - | - | - | - | - | - | **0.85** | **0.85** | **0.85** | **0.85** |



## Summary
The best-performing model was **Instance 5, XGBoost with Hyperparameter Tuning**, achieving an accuracy and F1 score of 0.85. XGBoost outperformed both the classical ML algorithm (Logistic Regression) and the Neural Network models in terms of accuracy, F1 score, recall, and precision. Although the neural networks showed potential, further experimentation and hyperparameter optimization might be required for them to surpass XGBoost's performance on this particular dataset.

## Link to video 
https://vimeo.com/1059531045/bf40bdeade?share=copy

## Instructions
1. Clone the repository.
2. Install Dependencies
Ensure you have all necessary libraries installed by running:
 `pip install -r requirements.txt`
3. Run the notebook `Summative_Intro_to_ml_[Josiane_Ishimwe_number]_assignment.ipynb` to train the models and evaluate their performance.
4. Load the best saved model from the `saved_models`.