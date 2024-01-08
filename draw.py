import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('speeds.csv')

plt.scatter(df.index, df['31摄氏度'], color='red', label='31°C')
plt.scatter(df.index, df['21摄氏度'], color='green', label='21°C')
plt.scatter(df.index, df['1摄氏度'], color='blue', label='1°C')


mean_31 = df['31摄氏度'].mean()
mean_21 = df['21摄氏度'].mean()
mean_1 = df['1摄氏度'].mean()


plt.axhline(mean_31, color='red', linestyle='--', label=f'31°C: {mean_31:.2f} m/s')
plt.axhline(mean_21, color='green', linestyle='--', label=f'21°C: {mean_21:.2f} m/s')
plt.axhline(mean_1, color='blue', linestyle='--', label=f'1°C: {mean_1:.2f} m/s')



plt.legend()
plt.xlabel('Index')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity at different temperature')

plt.show()
