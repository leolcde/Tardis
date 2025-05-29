# Tardis

**Diana, Mathilde, Léo**

**Tardis** is a prediction app created to display train delays and help passengers anticipate them earlier. The project uses a machine learning model trained to estimate probability of delays based on all data related to past delays recorded, their causes, the number of occurences, and more.
Long story short, Tardis is made to help you travel without the stress of being uninformed :)

## 🔧 Installation

How to clone the repository :

```
git clone https://github.com/EpitechPGEPromo2029G-AIA-210-STG-2-1-tardis-leo.lacordaire.git tardis
cd tardis
```

### 🔍 Run a virtual environnement to use Tardis

In order to execute the dataset cleaning and the prediction model, you need to create a virtual environnement.
In your terminal :

```
python -m venv [name_of_your_env]
```

Then, to activate your virtual env :

```
source [name_of_your_env]/bin/activate
```

### Run *tardis_eda.ipynb* to clean the dataset

You will find `'.ipynb'` files, including one named `'tardis_eda.ipynb'`.
These are Jupyter Notebook files that you can execute without the terminal, by simply clicking the **Run All** button in the notebook.
This will create a new file named `'cleaned_dataset.csv'`, which contains the entire dataset after bein cleaned. This helps prevent bad values from affecting the prediction model's accuracy.

### Run the prediction model with your chosen data

For this step, a JSON file is mandatory to indicate the datas of the train you want to predict the delays for.
Execute it with the `'.json'` furnished in the repository : 
```
python predict_model input.json
```
Once executed, the model will provide the following information :
- `The departure and arrival stations`
- `The probability of delay of the train`
- `The level of risk of getting a delay`

Later on, all these predictions will help developping a dashboard to visualize these delays on our app.

## NOW PREDICT THE UNPREDICTABLE 
