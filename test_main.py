from main import *
import pandas as pd

data = pd.read_excel("Project-Management-Sample-Data.xlsx")
x = data['Days Required']


def test_mean():
    assert round(get_mean(x), 5) == round(x.mean(), 5)

def test_median():
    assert round(get_median(x), 5) == round(x.median(), 5)

def test_std():
    assert round(get_std(x), 5) == round(x.std(), 5)

if __name__ == "__main__":
    test_mean()
    test_median()
    test_std()
    get_plot(x)
