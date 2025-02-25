# Personal Fashion Advisor

## Overview
The **Personal Fashion Advisor** is a machine learning-based recommendation system designed to provide personalized outfit and accessory suggestions. By integrating user inputs and analyzing key attributes such as material, color, price, season, and comfort, the system aims to improve upon existing solutions that lack personalized recommendations. The project focuses on classifying fashion items into categories (e.g., casual, formal) to deliver tailored suggestions.

---

## Dataset
The dataset used in this project is **synthetically generated** using Python's `pandas` library. This approach was taken due to the unavailability of existing non-generic datasets that align with the project's goals. The dataset contains **10,000 samples** with the following features:

- **`material_type`**: Type of material (e.g., cotton, wool, polyester).
- **`color_brightness`**: Brightness of the color (normalized between 0 and 1).
- **`price`**: Price of the item (in a specified range).
- **`season`**: Seasonality of the item (e.g., summer, winter, all-season).
- **`comfort`**: Comfort rating of the item (on a scale of 1 to 5).
- **`category`**: Target variable representing the category of the item (e.g., casual, formal, sportswear, partywear, traditional).

---

## Models Implemented

### 1. **Classical Machine Learning Algorithms**
- **Logistic Regression**:
  - Tuned hyperparameters using `GridSearchCV`
  - Evaluated using accuracy, precision, recall, and F1 score.

- **SVM (Support Vector Machine)**:
  - Tuned hyperparameters using `GridSearchCV`
  - Evaluated using accuracy, precision, recall, and F1 score.

- **XGBoost**:
  - Tuned hyperparameters using `GridSearchCV`
  - Evaluated using accuracy, precision, recall, and F1 score.

---

### 2. **Neural Networks**
- **Basic Neural Network**:
  - Simple feedforward architecture:
    - Input layer: 32 neurons (ReLU activation).
    - Hidden layer: 128 neurons (ReLU activation).
    - Output layer: 5 neurons (softmax activation).
  - Trained for 10 epochs with default settings.

- **Optimized Neural Networks**:
  - Techniques used:
    - **Optimizers**: Adam and SGD.
    - **Regularization**: L1 and L2 .
    - **Learning Rates**: Varied ( 0.0001, 0.0005).
    - **Early Stopping**: There was no to overfitting, i didn't use early stopping.
    - **Hidden Layers**: Varied ( 50 layers).
  - Evaluated using accuracy, precision, recall, and F1 score.

## Results Table

## Results

| Training Instance         | Optimizer Used | Regularizer Used | Epochs | Early Stopping | Number of Layers | Learning Rate | Accuracy | F1 Score | Recall | Precision |
|---------------------------|----------------|------------------|--------|----------------|------------------|---------------|----------|----------|--------|-----------|
| **Instance 1 (Basic NN)** | -              | -                | 10     | No             | 2                | Default       | 0.785    | 0.756    | 0.760  | 0.781     |
| **Instance 2 (Optimized NN)** | Adam         | L1               | 50     | Yes            | 50               | 0.0001        | 0.810    | 0.800    | 0.804  | 0.800     |
| **Instance 3 (Optimized NN)** | SGD          | L2               | 100    | Yes            | 50               | 0.0005        | 0.772    | 0.757    | 0.758  | 0.772     |
| **Instance 4 (Logistic Regression)** | liblinear/lbfgs | - | - | - | - | - | 0.748 | 0.747 | 0.748 | 0.749 |
| **Instance 5 (SVM)** | - | - | - | - | - | - | 0.8055 | 0.81 | 0.8055 | 0.81 |
| **Instance 6 (XGBoost)** | - | - | - | - | - | - | **0.838** | **0.839** | **0.838** | **0.842** |

---

### **Summary**
- **Best Model**: XGBoost (Instance 6) achieves the highest accuracy (0.838), F1 score (0.839), recall (0.838), and precision (0.842).
- **Second Best Model**: SVM (Instance 5) performs well with an accuracy of 0.8055.
- **Worst Model**: Logistic Regression (Instance 4) has the lowest performance metrics.
- **Neural Networks**: The optimized neural networks (Instances 2 and 3) perform better than the basic neural network (Instance 1), but XGBoost outperforms all of them.

## Video 
link:  (https://vimeo.com/1059531045/bf40bdeade?share=copy)

---

## Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Run the Notebook**:
   ```bash
   jupyter notebook Summative_Intro_to_ml_[Josiane_lshimwe_number]_assignment.ipynb

4. **Load Saved Models**
The trained models are saved in the saved_models folder.

5. **Explore the Dataset** saved fashion_df.csv

7. Save and Load Models

8. **Run Predictions**
After loading a model, you can use it to make predictions on new data
   ```bash
   predictions = model.predict(X_test)