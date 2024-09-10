from main import *
import pandas as pd

def test_df_exists(df):
    assert df is not None, "DataFrame was not loaded, check if it exists."
    
def test_mean(x):
    assert round(get_mean(x), 5) == round(x.mean(), 5)

def test_median(x):
    assert round(get_median(x), 5) == round(x.median(), 5)

def test_std(x):
    assert round(get_std(x), 5) == round(x.std(), 5)

if __name__ == "__main__":
    data = None
    try:
        data = pd.read_excel("Project-Management-Sample-Data.xlsx")
    except FileNotFoundError:
        pass
    days = data['Days Required']
    print(days.describe())
    
    test_df_exists(data)
    test_mean(days)
    test_median(days)
    test_std(days)
    get_plot(days)