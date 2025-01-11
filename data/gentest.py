import numpy as np
import pandas as pd

t = np.linspace(0,5,20)
m = 2
b = 1
y = m*t + b + np.random.randn(len(t))*0.1
df = pd.DataFrame({'t':t,'y':y})
df.to_csv('data/test.csv',index=False)

