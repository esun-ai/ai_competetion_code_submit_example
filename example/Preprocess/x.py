"""
處理input成為因子
"""
import pandas as pd

def load_data(path=""):
    """
    this is an example function.
    input: path of origin files
    output: no output, but a csv file is saved.
    """
    df = pd.read_csv(path)
    df.to_csv('./features.csv)

class Example():
    """
    this is an example class
    attributes:
    - base: start number
    """
    def __init__(self):
        self.base = 1

    def add(number):
        """
        add number to base
        input: number to add
        output: no output but self.base is updated
        """
        self.base += number
