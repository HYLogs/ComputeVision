import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

categories = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']


df = pd.DataFrame([[976, 0, 0, 0, 6, 18, 0],
                    [0, 997, 0, 0, 3, 0, 0],
                    [1, 0, 982, 0, 0, 6, 11],
                    [1, 2, 2, 995, 0, 0, 0],
                    [14, 0, 0, 0, 975, 11, 0],
                    [17, 0, 0, 0, 5, 978, 0],
                    [0, 0, 3, 0, 0, 0, 997]],
                    index=categories,
                    columns=categories)

print(df)

plt.pcolor(df)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.gca().invert_yaxis() #y축 반전

plt.title('Heatmap', fontsize=20)
plt.xlabel('Estimated Label')
plt.ylabel('True Label')
plt.colorbar()

plt.show()