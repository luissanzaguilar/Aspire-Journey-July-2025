import pandas as pd
# from src.main import my_function  # Importa tu función

def test_dataframe_creation():
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    assert df.shape == (2, 2)
