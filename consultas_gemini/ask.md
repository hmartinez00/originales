```python
import pandas as pd

json_dict = {"Usuario1": "Texto1", "Usuario2": "Texto2", ...}

df = pd.DataFrame.from_dict(json_dict, orient="index")
df.columns = ["Texto"]
df.reset_index(inplace=True)
df.rename(columns={"index": "Usuario"}, inplace=True)
```