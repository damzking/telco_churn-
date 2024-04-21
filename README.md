
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
  data:image/png;base64,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119/PY477rjo0KFD9OjRIyZOnBgff/xxnX1mzZoVBxxwQFRWVsauu+4a06ZNa+zplUxDzw3UcYNinEfUZw18/vnn4wtf+EK0a9cuqqur46qrrtou89seinXO0WzrmEpk+vTpqaKiIt10003phRdeSGeccUbq0qVLevvtt0s1pK2677770ne/+9105513pohId911V53tkydPTp07d0533313eu6559Lxxx+fBgwYkD788MPSDHgzRo4cmaZOnZrmzp2b5syZk4499tjUt2/ftGrVqsI+Z555Zqqurk6PPPJIevrpp9PnP//5dPDBB5dw1Ju655570r333ptefvnlNG/evPSd73wntW3bNs2dOzelVB5z+KSnnnoq9e/fP+2zzz7p7LPPLlxeDvO45JJL0l577ZWWLFlS+HnnnXcK28thDiml9P7776d+/fqlsWPHpieffDK9+uqr6YEHHkjz588v7NPUH+PLli2rcz889NBDKSLSzJkzU0rlc1+Uu+ayzja2cl73GktzWIcay5VXXpl22mmn9Pvf/z4tXLgw/eY3v0kdO3ZMV199dWGfllKbYpyPjho1Ku27777pz3/+c/rTn/6Udt1113TSSSdt55k0jqz6LF++PI0YMSL96le/Sn/729/SE088kQ466KA0ZMiQOtfRnOvTUOX43K2xFaPff/zxx2nvvfdOI0aMSM8++2y67777Urdu3dLFF19c2OfVV19NHTp0SOeee2568cUX009/+tPUunXrNGPGjO063+2hoecG6rhBsc4jtrYGrlixIvXs2TONHj06zZ07N91+++2pffv26frrr9+u820sxTrnaK51LFmIeNBBB6Vx48YVfl+/fn2qqqpKkyZNKtWQtsmnT0pqa2tTr1690g9/+MPCZcuXL0+VlZXp9ttvL8EI62fZsmUpItKjjz6aUtow5rZt26bf/OY3hX1eeumlFBHpiSeeKNUw66Vr167pxhtvLLs5rFy5Mu22227poYceSocffnihYZbLPC655JK07777bnZbucwhpZQuvPDCdOihh25xezk+xs8+++w0cODAVFtbW1b3RXPTnNbZYin3da+xNMd1qFiOO+64dOqpp9a57Ctf+UoaPXp0Sqnl1qYh56Mvvvhiiog0e/bswj73339/yuVy6a233tpuY98eNheyftpTTz2VIiK99tprKaWWVZ9tUe7P3baHhvT7++67L7Vq1SotXbq0sM+1116b8vl8WrNmTUoppQsuuCDttddedW7rxBNPTCNHjmzsKW1Xn+XcQB03KMZ5RH3WwJ/97Gepa9euhdpuvO3dd9+92FMqiWKcczTnOpbk48xr166NZ555JkaMGFG4rFWrVjFixIh44oknSjGkz2zhwoWxdOnSOnPq3LlzDBs2rEnPacWKFRERseOOO0ZExDPPPBPr1q2rM49BgwZF3759m+w81q9fH9OnT4+///3vMXz48LKbw7hx4+K4446rM96I8rovXnnllaiqqopddtklRo8eHa+//npElNcc7rnnnhg6dGj867/+a/To0SP233//uOGGGwrby+0xvnbt2rjlllvi1FNPjVwuV1b3RXPTHNbZYmsO615jaG7rUDEdfPDB8cgjj8TLL78cERHPPfdcPPbYY3HMMcdERMuuzSfVpw5PPPFEdOnSJYYOHVrYZ8SIEdGqVat48sknt/uYS23FihWRy+WiS5cuEaE+m9Mcn7s1hob0+yeeeCIGDx4cPXv2LOwzcuTIqKmpiRdeeKGwz6f75ciRI5td7T/LuYE6blCM84j6rIFPPPFEHHbYYVFRUVHYZ+TIkTFv3rz44IMPGnuaja4Y5xzNuY5tSnGj7777bqxfv77OgzwiomfPnvG3v/2tFEP6zJYuXRoRsdk5bdzW1NTW1saECRPikEMOib333jsiNsyjoqKicCK1UVOcx1//+tcYPnx4fPTRR9GxY8e46667Ys8994w5c+aUzRymT58ef/nLX2L27NmbbCuX+2LYsGExbdq02H333WPJkiVx2WWXxRe+8IWYO3du2cwhIuLVV1+Na6+9Ns4999z4zne+E7Nnz47x48dHRUVFjBkzpuwe43fffXcsX748xo4dGxHl8++puSn3dbYxNId1r7E0t3WomC666KKoqamJQYMGRevWrWP9+vVx5ZVXxujRoyOiPM/DGkN96rB06dLo0aNHne1t2rSJHXfcsUXVKmLD31m78MIL46STTop8Ph8R6rM5zfG5W7E1tN8vXbp0s3XduC1rn5qamvjwww+jffv2jTGl7eqznhuo4wbFOI+ozxq4dOnSGDBgwCbXsXFb165dG2V+20sxzjmacx1LEiLSNIwbNy7mzp0bjz32WKmH0iC77757zJkzJ1asWBG//e1vY8yYMfHoo4+Welj19sYbb8TZZ58dDz30ULRr167Uw2mwja/IRETss88+MWzYsOjXr1/8+te/LqtmXFtbG0OHDo3//M//jIiI/fffP+bOnRvXXXddjBkzpsSj23Y///nP45hjjomqqqpSD6VFK/d1ttiay7rXWJrbOlRMv/71r+PWW2+N2267Lfbaa6+YM2dOTJgwIaqqqlp8bWiYdevWxde+9rVIKcW1115b6uFQ5vT7hnNuUDzOI4rDOUe2knycuVu3btG6detNvlHp7bffjl69epViSJ/ZxnGXy5zOOuus+P3vfx8zZ86MPn36FC7v1atXrF27NpYvX15n/6Y4j4qKith1111jyJAhMWnSpNh3333j6quvLps5PPPMM7Fs2bI44IADok2bNtGmTZt49NFH4yc/+Um0adMmevbsWRbz+LQuXbrE5z73uZg/f37Z3BcREb17944999yzzmV77LFH4aPZ5fQYf+211+Lhhx+O008/vXBZOd0XzUVzWGeLrbmue8XSnNahYps4cWJcdNFF8W//9m8xePDgOPnkk+Occ86JSZMmRUTLrs0n1acOvXr1imXLltXZ/vHHH8f777/fYmq1MUB87bXX4qGHHiq8CzFCfTanOT53K6bP0u979eq12bpu3Ja1Tz6fL6sX7LekGOcG6rhBMc4j6rMG1qfe5awY5xzNuY4lCRErKipiyJAh8cgjjxQuq62tjUceeSSGDx9eiiF9ZgMGDIhevXrVmVNNTU08+eSTTWpOKaU466yz4q677oo//OEPm7x9dsiQIdG2bds685g3b168/vrrTWoem1NbWxtr1qwpmzkceeSR8de//jXmzJlT+Bk6dGiMHj268P/lMI9PW7VqVSxYsCB69+5dNvdFRMQhhxwS8+bNq3PZyy+/HP369YuI8nmMR0RMnTo1evToEccdd1zhsnK6L8pdc15nP6vmuu4VS3Nah4pt9erV0apV3dPW1q1bR21tbUS07Np8Un3qMHz48Fi+fHk888wzhX3+8Ic/RG1tbQwbNmy7j3l72xggvvLKK/Hwww/HTjvtVGd7S6/P5jTH527FUIx+P3z48PjrX/9aJ2zYGGxvDIOGDx9e5zo27tNcal+McwN13KAY5xH1WQOHDx8ef/zjH2PdunWFfR566KHYfffdm+xHcLdFMc45mnUdS/WNLtOnT0+VlZVp2rRp6cUXX0z/8R//kbp06VLnG5WampUrV6Znn302Pfvssyki0pQpU9Kzzz5b+Da3yZMnpy5duqT//d//Tc8//3w64YQTNvma71L75je/mTp37pxmzZqVlixZUvhZvXp1YZ8zzzwz9e3bN/3hD39ITz/9dBo+fHgaPnx4CUe9qYsuuig9+uijaeHChen5559PF110UcrlcunBBx9MKZXHHDbnk99EllJ5zOO8885Ls2bNSgsXLkyPP/54GjFiROrWrVtatmxZSqk85pDShm9nbNOmTbryyivTK6+8km699dbUoUOHdMsttxT2KYfH+Pr161Pfvn3ThRdeuMm2crkvyl1zWWe3l3Jc9xpLc1mHGsOYMWPSzjvvnH7/+9+nhQsXpjvvvDN169YtXXDBBYV9WkptinE+OmrUqLT//vunJ598Mj322GNpt912SyeddFKpplRUWfVZu3ZtOv7441OfPn3SnDlz6qzRn/x2zOZcn4Yqx+duja0Y/f7jjz9Oe++9dzr66KPTnDlz0owZM1L37t3TxRdfXNjn1VdfTR06dEgTJ05ML730UrrmmmtS69at04wZM7brfLenbT03UMcNinUesbU1cPny5alnz57p5JNPTnPnzk3Tp09PHTp0SNdff/12nW9jKdY5R3OtY8lCxJRS+ulPf5r69u2bKioq0kEHHZT+/Oc/l3I4WzVz5swUEZv8jBkzJqW04au+v//976eePXumysrKdOSRR6Z58+aVdtCfsrnxR0SaOnVqYZ8PP/wwfetb30pdu3ZNHTp0SF/+8pfTkiVLSjfozTj11FNTv379UkVFRerevXs68sgjCwFiSuUxh835dMMsh3mceOKJqXfv3qmioiLtvPPO6cQTT0zz588vbC+HOWz0u9/9Lu29996psrIyDRo0KP3P//xPne3l8Bh/4IEHUkRsdlzldF+Us+ayzm4v5bjuNabmsA41hpqamnT22Wenvn37pnbt2qVddtklffe7360T/LSU2hTjfPS9995LJ510UurYsWPK5/PpG9/4Rlq5cmUJZlN8WfVZuHDhFtfomTNnFq6jOdfnsyi3526NrVj9ftGiRemYY45J7du3T926dUvnnXdeWrduXZ19Zs6cmfbbb79UUVGRdtlllzq30Rw15NxAHTcoxnlEfdbA5557Lh166KGpsrIy7bzzzmny5MmNPrftpVjnHM21jrmUUmqkNzkCAAAAAM1ASf4mIgAAAABQPoSIAAAAAEAmISIAAAAAkEmICAAAAABkEiICAAAAAJmEiAAAAABAJiEiAAAAAJBJiAgAAAAAZBIiAgA0E7lcLu6+++4tbp81a1bkcrlYvnx5UW932rRp0aVLl6JeJwBszdb63uboWdBwQkRapCOOOCImTJhQ6mEA0EyMHTs2crlcnHnmmZtsGzduXORyuRg7dmzRbu/SSy+N/fbbr2jXtzUzZ86MY489Nnbaaafo0KFD7LnnnnHeeefFW2+9td3GAEDTlcvlMn8uvfTSLR67aNGiyOVyMWfOnKKMRc+CxiNEhBJKKcXHH39c6mEAUATV1dUxffr0+PDDDwuXffTRR3HbbbdF3759Sziyz+b666+PESNGRK9eveKOO+6IF198Ma677rpYsWJF/OhHP2rU2163bl2jXj8AxbFkyZLCz3//939HPp+vc9n555+/XcahZ0HjEiLS4owdOzYeffTRuPrqqwuvjC1atCjmzp0bxxxzTHTs2DF69uwZJ598crz77ruF44444ogYP358XHDBBbHjjjtGr1696ryitrlX0JYvXx65XC5mzZoVEf/4GNn9998fQ4YMicrKynjssceitrY2Jk2aFAMGDIj27dvHvvvuG7/97W+3U0UAKIYDDjggqqur48477yxcduedd0bfvn1j//33L1y2Zs2aGD9+fPTo0SPatWsXhx56aMyePbuwfWOveOSRR2Lo0KHRoUOHOPjgg2PevHkRseFjWJdddlk899xzhT42bdq0wvHvvvtufPnLX44OHTrEbrvtFvfcc89mx/v3v/898vn8Jv3m7rvvjh122CFWrlwZb775ZowfPz7Gjx8fN910UxxxxBHRv3//OOyww+LGG2+MH/zgB3WOfeCBB2KPPfaIjh07xqhRo2LJkiWFbbNnz46jjjoqunXrFp07d47DDz88/vKXv9Q5PpfLxbXXXhvHH3987LDDDnHllVdGRMQVV1wRPXr0iE6dOsXpp58eF1100SbvxLzxxhtjjz32iHbt2sWgQYPiZz/7WWHb2rVr46yzzorevXtHu3btol+/fjFp0qTN1gWAbderV6/CT+fOnSOXyxV+79GjR0yZMiX69OkTlZWVsd9++8WMGTMKxw4YMCAiIvbff//I5XJxxBFHRET9+sYn6VmwHSRoYZYvX56GDx+ezjjjjLRkyZK0ZMmS9O6776bu3buniy++OL300kvpL3/5SzrqqKPSF7/4xcJxhx9+eMrn8+nSSy9NL7/8cvrFL36RcrlcevDBB1NKKS1cuDBFRHr22WcLx3zwwQcpItLMmTNTSinNnDkzRUTaZ5990oMPPpjmz5+f3nvvvXTFFVekQYMGpRkzZqQFCxakqVOnpsrKyjRr1qztWRoAGmjMmDHphBNOSFOmTElHHnlk4fIjjzwy/fjHP04nnHBCGjNmTEoppfHjx6eqqqp03333pRdeeCGNGTMmde3aNb333nsppX/0imHDhqVZs2alF154IX3hC19IBx98cEoppdWrV6fzzjsv7bXXXoU+tnr16pRSShGR+vTpk2677bb0yiuvpPHjx6eOHTtuct0ffPBBSimlM844Ix177LF15nL88cenU045JaWU0pQpU1JEpMWLF2fOf+rUqalt27ZpxIgRafbs2emZZ55Je+yxR/r3f//3wj6PPPJIuvnmm9NLL72UXnzxxXTaaaelnj17ppqamsI+EZF69OiRbrrpprRgwYL02muvpVtuuSW1a9cu3XTTTWnevHnpsssuS/l8Pu27776F42655ZbUu3fvdMcdd6RXX3013XHHHWnHHXdM06ZNSyml9MMf/jBVV1enP/7xj2nRokXpT3/6U7rtttvqdd8CsG2mTp2aOnfuXPh9ypQpKZ/Pp9tvvz397W9/SxdccEFq27Ztevnll1NKKT311FMpItLDDz+clixZUuhZ9e0bd911V+F29CxoXEJEWqTDDz88nX322YXfL7/88nT00UfX2eeNN95IEZHmzZtXOObQQw+ts8+BBx6YLrzwwpTStoWId999d2Gfjz76KHXo0CH93//9X53rPu2009JJJ530WacKwHawMURctmxZqqysTIsWLUqLFi1K7dq1S++8804hRFy1alVq27ZtuvXWWwvHrl27NlVVVaWrrroqpfSPXvHwww8X9rn33ntTRKQPP/wwpZTSJZdcUucJyUYRkb73ve8Vfl+1alWKiHT//ffXue6NIeKTTz6ZWrduXXjC9fbbb6c2bdoUXsT65je/mfL5/FbnP3Xq1BQRaf78+YXLrrnmmtSzZ88tHrN+/frUqVOn9Lvf/a7O+CdMmFBnv2HDhqVx48bVueyQQw6pM/+BAwdu8gTr8ssvT8OHD08ppfTtb387/dM//VOqra3d6lwA+Gw+HSJWVVWlK6+8ss4+Bx54YPrWt76VUtr886jN2VLf2Bgi6lnQ+HycGSLiueeei5kzZ0bHjh0LP4MGDYqIiAULFhT222effeoc17t371i2bNk2397QoUML/z9//vxYvXp1HHXUUXVu/5e//GWd2wag6evevXscd9xxMW3atJg6dWocd9xx0a1bt8L2BQsWxLp16+KQQw4pXNa2bds46KCD4qWXXqpzXZ/sOb17946IqFfP+eRxO+ywQ+Tz+S0ed9BBB8Vee+0Vv/jFLyIi4pZbbol+/frFYYcdFhEb/nZvLpfb6m1GRHTo0CEGDhxYZ8yfvN233347zjjjjNhtt92ic+fOkc/nY9WqVfH666/XuZ5P9siIiHnz5sVBBx20ybg3+vvf/x4LFiyI0047rU4fveKKKwp9dOzYsTFnzpzYfffdY/z48fHggw/Wa04AfDY1NTWxePHiOn0vIuKQQw7ZpO99Wn37xkZ6FjS+NqUeADQFq1atii996UvxX//1X5ts2/jELWLDE71PyuVyUVtbGxERrVptyORTSoXtW/rjujvssEOd246IuPfee2PnnXeus19lZeW2TAOAJuDUU0+Ns846KyIirrnmmgZfzyd7zsYnRRt7Tn2P23hs1nGnn356XHPNNXHRRRfF1KlT4xvf+Ebh9j73uc/FihUrYsmSJXX6YX1v95M9ccyYMfHee+/F1VdfHf369YvKysoYPnx4rF27ts5xn+yR9bGxj95www0xbNiwOttat24dERv+XuXChQvj/vvvj4cffji+9rWvxYgRI/z9YYAmrL59YyM9CxqfdyLSIlVUVMT69esLvx9wwAHxwgsvRP/+/WPXXXet81PfxtC9e/eIiDp/kPeTX7KyJXvuuWdUVlbG66+/vsltV1dXb9vEACi5UaNGxdq1a2PdunUxcuTIOtsGDhwYFRUV8fjjjxcuW7duXcyePTv23HPPet/Gp/vYZ/H1r389XnvttfjJT34SL774YowZM6aw7V/+5V+ioqIirrrqqs0eu3z58nrfzuOPPx7jx4+PY489Nvbaa6+orKys8wVmW7L77rvX+eKZiKjze8+ePaOqqipeffXVTfroxj/WHxGRz+fjxBNPjBtuuCF+9atfxR133BHvv/9+vccPwLbL5/NRVVVVp+9FbOgJG/teRUVFRMQmfW1b+4aeBY3POxFpkfr37x9PPvlkLFq0KDp27Bjjxo2LG264IU466aTCty/Pnz8/pk+fHjfeeGPhVaEs7du3j89//vMxefLkGDBgQCxbtiy+973vbfW4Tp06xfnnnx/nnHNO1NbWxqGHHhorVqyIxx9/PPL5fJ0ncwA0fa1bty58ROvT/WOHHXaIb37zmzFx4sTYcccdo2/fvnHVVVfF6tWr47TTTqv3bfTv3z8WLlwYc+bMiT59+kSnTp0a/O71rl27xle+8pWYOHFiHH300dGnT5/Cturq6vjxj38cZ511VtTU1MQpp5wS/fv3jzfffDN++ctfRseOHeNHP/pRvW5nt912i5tvvjmGDh0aNTU1MXHixGjfvv1Wj/v2t78dZ5xxRgwdOjQOPvjg+NWvfhXPP/987LLLLoV9Lrvsshg/fnx07tw5Ro0aFWvWrImnn346Pvjggzj33HNjypQp0bt379h///2jVatW8Zvf/CZ69eoVXbp02eZ6AbBtJk6cGJdcckkMHDgw9ttvv5g6dWrMmTMnbr311oiI6NGjR7Rv3z5mzJgRffr0iXbt2kXnzp23uW/oWdD4vBORFun888+P1q1bx5577hndu3ePtWvXxuOPPx7r16+Po48+OgYPHhwTJkyILl26FD6mXB833XRTfPzxxzFkyJCYMGFCXHHFFfU67vLLL4/vf//7MWnSpNhjjz1i1KhRce+999Z5NQqA8pHP5yOfz2922+TJk+OrX/1qnHzyyXHAAQfE/Pnz44EHHoiuXbvW+/q/+tWvxqhRo+KLX/xidO/ePW6//fbPNN7TTjst1q5dG6eeeuom2771rW/Fgw8+GG+99VZ8+ctfjkGDBsXpp58e+Xw+zj///Hrfxs9//vP44IMP4oADDoiTTz45xo8fHz169NjqcaNHj46LL744zj///MJHvMaOHRvt2rUr7HP66afHjTfeGFOnTo3BgwfH4YcfHtOmTSv00U6dOsVVV10VQ4cOjQMPPDAWLVoU99133zb1eAAaZvz48XHuuefGeeedF4MHD44ZM2bEPffcE7vttltERLRp0yZ+8pOfxPXXXx9VVVVxwgknRETD+oaeBY0rlz75wX8AAFqcm2++Oc4555xYvHhx4WNlTdlRRx0VvXr1iptvvrnUQwGATHoWzYmPMwMAtFCrV6+OJUuWxOTJk+P//b//1yQDxNWrV8d1110XI0eOjNatW8ftt98eDz/8cDz00EOlHhoA1KFn0dx5PywAQAt11VVXxaBBg6JXr15x8cUXl3o4m5XL5eK+++6Lww47LIYMGRK/+93v4o477ogRI0aUemgAUIeeRXPn48wAAAAAQCbvRAQAAAAAMgkRAQAAAIBMQkQAAAAAIJMQEQAAAADIJEQEAAAAADIJEQEAAACATEJEAAAAACCTEBEAAAAAyPT/AfGk4QGt5wf3AAAAAElFTkSuQmCC
  

  
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

