
<a name="readme-top"></a>

<div align="center">
  <h1><b>Telco Churn </b></h1>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📗 Table of Contents](#-table-of-contents)
- Overview
- [🛠 Built With ](#-built-with-)
- [Tech Stack ](#tech-stack-)
- Packages and Libraries
- Cleaning The Data
- Exploratory Data Analysis
- Visualizations
- Analysis
- Findings
- [Key Insights ](#key-insights-)
- [💻 Getting Started ](#-getting-started-)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Install](#install)
- [Usage](#usage)
- [👥 Authors ](#-authors-)
- [🔭 Future Features ](#-future-features-)
- [🤝 Contributing ](#-contributing-)
- [⭐️ Show your support ](#️-show-your-support-)
- [🙏 Acknowledgments ](#-acknowledgments-)
- [📝 License ](#-license-)

<!-- PROJECT DESCRIPTION -->

#  Analyzing Customer Behavior and Predicting Churn in the Telecommunication Firm <a name="about-project"></a>

## Overview 

Machine learning is a vital tool for telecom companies to predict and mitigate customer churn. By analyzing data patterns, ML algorithms can anticipate customer behavior, identify dissatisfaction factors such as long wait times or rude service, and enhance self-service options. This proactive approach helps retain customers and maintain loyalty in an increasingly competitive and price-sensitive market.

## Data Sources 📊
- The dataset was provided in GitHub and SQL and was transformed to CSV format for transparency and reproductibility.
- Statistics on Telco Churn Rate.

## Topical Questions and Hypotheses
#### Questions 🤔:

ANALYTICAL QUESTIONS
The following analytical questions will help us gain insight and as well as confirm our hypothesis

1. How long Female and Male spent with Telco before Churning

2. What is the trend between Contract and churn

3. How long does it take each contract type before Churning

4. Which method of payment was prefered among the Senior Citizens and how much in total did both senior and non Senior citizens paid before churning

5. What is the churn trend for gender and dependents as well as their tenure

6. what is the trend between payment methods and gender and how it affect churning

7. What is the trend between tenure and paperlessBilling in relation to churn

8. What is the trend between tenure, Internet Service and senior citizen in relation to churn

9. What is the trend between StreamingMovies and senior citizen in relation to churn

10. How does internetService and OnlineSecurity affect churn

11. What is the trend between Contract and Payment Method in relation to churn

### Hypotheses 🔬:
#### A significance level (α) of 5% will used to perform all the hypothesis testing

The following hypothesis will be tested

1. The average number of churn for Female customers is greater than or equal to that of Male customers.

2. The average amount of TotalCharges for customers that churn is greater than or equal to those that did not churn.

3. The average number of tenure for customers that churn is less than or equal to those that did not churn

4. The average number of churn for customers that have Month_to_month contract is greater than or equal to those with 'One year' contract.

5. The average number of churn for customers that have Yes value for streamingTV is less than or equal to those with No values.

6. The average number of customers with dependents that will churn is greater than or equal to that of customers with no dependents.

7. The average number of churn for customers that have Yes values for seniorCitizen is greater than or equal to those with No values.

8. The PAYMENT METHOD does not influence customer churn

9. The average amount of TotalCharges for customers that churn is greater than or equal to those that did not churn
10. The average number of tenure for customers that churn is less than or equal to those that did not churn

11. The average number of churn for customers that have Month_to_Month contract is greater than or equal to those with 'One year' contract
12.
Gender does not influence customer churn
13.
The Internet service does not influence customer churn


###Data Dictionary
customerID - Uniquely identify each customer
gender - whether a customer is a Male or Female
SeniorCitizen - whether customer is >60 years or not (Yes or No)
Partner - Whether customer have a partner or not (Yes or No)
Dependents - Whether customer have a dependents or not (Yes or No)
tenure - How many months customer has been on the network
PhoneService - Whether the customer is satisfied with the phone services
MultipleLines - Whether the customer is satisfied with the multiple lines service
InternetService - Whether the customer is satisfied with the internet service
OnlineSecurity - whether the customer is satisfied with the online security service
OnlineBackup - Whether the customer is satisfied with the onlince backup service
DeviceProtection - Whether the customer is satisfied with the device protection service
TechSupport - Whether the customer is satisfied with the tech support service
StreamingTV - Whether the customer is satisfied with the streaming TV service
StreamingMovies - Whether the customer is satisfied with the streaming Movies service
Contract - Whether the customer opted for month-to-month, one-year and two-years contract with the Telco
PaperlessBilling - Whether the customer is satisfied with the Paperless Billing service
PaymentMethod - Whether the customer opted for electronic, mailed check, bank transfer and credit card payment methods
MonthlyCharges - Monthly customer charges
TotalCharges - Yearly customer charges
Churn - Whether a customer will stop using the Telco's network or not (Yes and No)




## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>





<details>
<summary>Language</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
  </ul>
</details>


<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.microsoft.com/en-us/sql-server">SQL</a></li>
  </ul>
</details>




## Packages and Libraries 📚
#### Collection of significant Python Libraries:
- Pandas
- Numpy
- Seaborn
- Scipy
- Matplotlib
- Pyodbc
- Dotenv
- Sklearn
- Scikit
- Imblearn
- Custom Imputer
- XG Boost
- Pipeline

## Cleaning the Data 🧹
#### We begin by thoroughly cleaning our data.
- Changing data types 
- Dealing with Nan values
- Replacing Values in categorical columns to be more consistent

## Exploratory Data Analysis 🕵



- Univariate Analysis
  
  ![image](https://github.com/Koanim/Team-Lawrencium-Indian--startup-funding-Analysis-from-2018-to-2021/assets/87522676/a70a3b7f-5ce0-4f52-8386-0bfdda76779c)

  
- Bivariate Analysis





## Visualizations 👀

- Line Chart 📈
- Bar chart 📊
- Swarm Plot ◼▪◾

## Analysis 🔍
- Utilizing Python and data analysis libraries such as Pandas, Matplotlib, and Seaborn, we performed exploratory data analysis (EDA) to uncover trends and insights.
- We analyzed funding trends by year, sector-wise funding distribution, top investors, geographical distribution, and funding rounds.

## Machine Learning Models and Hyperparameter Tuning
-   Gradient_Boosting
-	Random_Forest	
-	XGBoost	
-   Naive_Bayes	
-   Logistic_Regression	
-   Support_Vector_Machine	
-   Decision_Tree	
-   K-Nearest_Neighbors	





## Findings 📈
- Total Charges and Tenure are highly positively correlated
- Customers that did not churn are more than those that churned.
- There are approximately 4000 non senior citizens among the telcos' customers compared to around 500 seniors

## Key Files 📂
- `LP2_telco_churn.ipynb`: Jupyter Notebook containing the code for data cleaning, EDA, and visualization.
- Raw data used for analysis.
>Telco_churn_git.csv
>Telco_churn_sql.csv
-`README.md`: This file providing an overview of the project.



<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- Features -->

## Key Insights <a name="key-features"></a>

- **A dataset which analyzed the Indian startup ecosystem from 2018-2021**
- **Insights on the funding trends**
- **Insights on Amount in circulation from 2018-2021**
- **Sampling Techniques, Inferences, and Hypothesis tests on location and year for differences**


<p align="right">(<a href="#readme-top">back to top</a>)</p>



![image](https://raw.githubusercontent.com/Koanim/Team-Lawrencium-Indian--startup-funding-Analysis-from-2018-to-2021/27fa53558e249dc650bb404ee9c6ba3610a18d23/exploratoty%20data.JPG
![Exploratory Data Visualization](https://raw.githubusercontent.com/koanim/Team-Lawrencium-Indian--startup-funding-Analysis-from-2018-to-2021/branch/exploratory_data_viz.png)






<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python


### Setup

Clone this repository to your desired folder:


```sh
  cd my-folder
  git clone hhttps://github.com/Koanim/Team-Lawrencium-Indian--startup-funding-Analysis-from-2018-to-2021
```

Change into the cloned repository

```sh
  cd Team-Lawrencium-Indian--startup-funding-Analysis-from-2018-to-2021
  
```

Create a virtual environment

```sh

python -m venv env

```

Activate the virtual environment

```sh
    env/Scripts/activate
```


### Install

Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```



<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

🕵🏽‍♀️ **Victor Anim**                                   
🕵🏽‍♀️ **Aluko Oluwadamilola**                        [GitHub Profile](https://github.com/damzking?tab=repositories)
🕵🏽‍♀️ **Aminu Oluwarotimi Desmond**                  [GitHub Profile](https://github.com/bamzyyyy?tab=repositories)
🕵🏽‍♀️ **Nana Kwame Frimpong Baah**
🕵🏽‍♀️ **Leticia Blay**
🕵🏽‍♀️ **Richmond Tetteh**




<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

We acknowledge the following persons for their coaching and support

Violette Naa Adoley Allotey
Racheal Appiah-Kubi
Israel Anaba Ayamga

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

