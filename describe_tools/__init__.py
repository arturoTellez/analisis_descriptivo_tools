import pandas as pd
import matplotlib.pyplot as plt
def graficar_variables(df):
  for col_name, col_values in df.iteritems():
    print(col_values.dtype)
    plt.title(col_name)
    if str(col_values.dtype) == "object":
      temp = col_values.value_counts(normalize = True)
      temp = temp[temp >= 0.05]
      temp.plot.bar()
    else:
      col_values.hist()
    plt.show()


