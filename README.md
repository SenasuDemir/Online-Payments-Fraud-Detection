# 💳 Online Payment Fraud Detection - Machine Learning Model

## 📊 Introduction
With the increasing digitalization of financial transactions, online payment fraud has become a significant concern for financial institutions, businesses, and consumers. Fraudulent transactions can lead to substantial financial losses and erode trust in online payment systems. This project aims to develop a machine learning model to detect fraudulent transactions in online payments, helping to prevent fraud and enhance transaction security.

## 🎯 Aim
The objective of this project is to analyze online transaction data and build a predictive model to identify fraudulent activities. By leveraging various machine learning techniques, we aim to detect patterns that distinguish fraudulent transactions from legitimate ones, ultimately improving fraud detection systems.

## 🗃️ Dataset Description
The dataset consists of multiple transaction records, each containing information about the transaction type, amount, source, destination, and fraud labels. Below is a brief description of the dataset columns:

- **step**: Represents the unit of time (typically an hour) when the transaction was made.
- **type**: The type of transaction (e.g., PAYMENT, TRANSFER, CASH_OUT).
- **amount**: The amount of money involved in the transaction.
- **nameOrig**: The identifier of the sender of the transaction.
- **oldbalanceOrg**: The sender's balance before the transaction.
- **newbalanceOrig**: The sender's balance after the transaction.
- **nameDest**: The identifier of the receiver of the transaction.
- **oldbalanceDest**: The receiver's balance before the transaction.
- **newbalanceDest**: The receiver's balance after the transaction.
- **isFraud**: A binary indicator (1 for fraudulent transactions, 0 for legitimate ones).
- **isFlaggedFraud**: A binary indicator showing if the transaction was flagged as fraudulent by the system.

You can download the dataset from [Kaggle: Online Payments Fraud Detection Dataset](https://www.kaggle.com/datasets/rupakroy/online-payments-fraud-detection-dataset).

## 📈 Evaluation and Results

### 🔍 Model Performance:
The machine learning models evaluated for detecting fraudulent transactions include Random Forest, Decision Tree, K-Nearest Neighbors, and Gradient Boosting. The following summarizes the results:

- **Random Forest Classifier** achieved the highest accuracy of **99.97%**, outperforming other models in terms of both accuracy and computational efficiency.
- **Deep Learning models** showed competitive performance with an accuracy of **99.87%**, but the Random Forest model was slightly better with lower computational cost.
- The **confusion matrix** for the Random Forest model highlights its effectiveness in detecting both fraudulent and non-fraudulent transactions with minimal false positives and false negatives.

### 📌 Key Insights:
- **Random Forest** is the top-performing model in terms of accuracy, with excellent results in detecting fraudulent and legitimate transactions.
- **Deep Learning** models also performed well but required more computational resources.
- Future improvements could include further **feature engineering**, handling **class imbalance**, and experimenting with **ensemble learning** techniques.

## 🌐 [Hugging Face Space](https://huggingface.co/spaces/Senasu/Online_Payment_Fraud_Detection)
Check out the live fraud detection tool for this project on [Hugging Face Space](https://huggingface.co/spaces/Senasu/Online_Payment_Fraud_Detection)! 🎉

## 🖥️ Original Code
You can find the original code for this project on my [Kaggle Notebook](https://www.kaggle.com/code/senasudemir/online-payments-fraud-detection/notebook).
