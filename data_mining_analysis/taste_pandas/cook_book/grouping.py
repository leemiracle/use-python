import pandas as pd
import numpy as np

df = pd.DataFrame({'animal': 'cat dog cat fish dog cat cat'.split(), 'size': list('SSMMMLL'), 'weight': [8, 10, 11, 1, 20, 12, 12],'adult' : [False] * 5 + [True] * 2})

# List the size of the animals with the highest weight.
df.groupby('animal').apply(lambda subf: subf['size'][subf['weight'].idxmax()])

# Using get_group
gb = df.groupby(['animal'])
gb.get_group('cat')
