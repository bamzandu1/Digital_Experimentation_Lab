import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello() -> str:
    df = pd.read_csv(
    "../input/datasets/book_sales.csv",
    index_col='Date',
    parse_dates=['Date'],
)

    df['Time'] = np.arange(len(df.index))   

    plt.style.use("seaborn-whitegrid")
    plt.rc(
        "figure",
        autolayout=True,
        figsize=(11, 4),
        titlesize=18,
        titleweight='bold',
    )
    plt.rc(
        "axes",
        labelweight="bold",
        labelsize="large",
        titleweight="bold",
        titlesize=16,
        titlepad=10,
    )
    
    fig, ax = plt.subplots()
    ax.plot('Time', 'Hardcover', data=df, color='0.75')
    ax = sns.regplot(x='Time', y='Hardcover', data=df, ci=None, scatter_kws=dict(color='0.25'))
    ax.set_title('Time Plot of Hardcover Sales');
  
    return fig


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=False)


