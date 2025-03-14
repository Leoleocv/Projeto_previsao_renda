# CRISP-DM Process Documentation for Income Prediction

This document outlines the steps taken to analyze the income dataset and build a decision tree model for income prediction, following the CRISP-DM methodology.

## 1. Business Understanding

The goal of this project is to create a model that predicts a client's income based on their characteristics. This model can be used to offer financial products, adjust credit limits, and reduce the risk of default.

## 2. Data Understanding

The dataset contains information about clients, including their demographics, financial history, and income. The target variable is "renda" (income).

The following libraries were used for data understanding:

-   pandas: for data manipulation and analysis
-   seaborn: for data visualization
-   matplotlib: for data visualization
-   numpy: for numerical computations
-   ydata_profiling: for generating a comprehensive data profile report

## 3. Data Preparation

This stage involves preparing the data for modeling. The following steps were performed:

### Data Cleaning

Data cleaning involves handling missing values, outliers, and inconsistencies.

#### Handling Missing Values

Missing values were identified and handled using imputation or removal techniques. The specific approach depends on the nature and extent of missing data for each variable.

#### Addressing Outliers

Outliers were identified and addressed to prevent them from negatively impacting the model's performance. Techniques such as trimming, capping, or transformation were used.

#### Checking for Data Inconsistencies

Data inconsistencies were identified and corrected to ensure data quality and reliability.

### Feature Engineering

Feature engineering involves creating new features from existing ones to improve the model's performance.

#### Converting Categorical Variables

Categorical variables were converted into numerical format using one-hot encoding or label encoding. One-hot encoding creates a new binary variable for each category, while label encoding assigns a unique integer to each category.

### Data Splitting

The data was split into training and testing sets. The training set is used to train the model, while the testing set is used to evaluate its performance. A validation set was not used, as per the user's instructions.

## 4. Modeling

This stage involves building the decision tree model. The following steps were performed:

### Model Selection

Scikit-learn's `DecisionTreeClassifier` was used to build the decision tree model.

### Hyperparameter Tuning

The hyperparameters of the decision tree were tuned using techniques like cross-validation and grid search. This involves searching for the best combination of hyperparameters that maximizes the model's performance.

### Post-Pruning

Post-pruning techniques, such as Cost Complexity Pruning, were implemented to prevent overfitting. This involves simplifying the decision tree by removing branches that do not significantly improve its performance.

### Model Training

The decision tree model was trained on the training data.

## 5. Evaluation

This stage involves evaluating the model's performance on the testing data. The following metrics were used:

-   Accuracy: the proportion of correctly classified instances
-   Precision: the proportion of true positives among the instances predicted as positive
-   Recall: the proportion of true positives among the actual positive instances
-   F1-score: the harmonic mean of precision and recall
-   ROC AUC: the area under the receiver operating characteristic curve

A confusion matrix was generated to visualize the model's performance.

## 6. Deployment

This stage involves putting the model into production. The model will be integrated into the Streamlit app.