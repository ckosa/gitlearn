import numpy as np
import pandas as pd

numrow = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(numrow)

numrow2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(numrow2)

keypad = pd.DataFrame(numrow2, columns=['a', 'b', 'c'])
print(keypad)
