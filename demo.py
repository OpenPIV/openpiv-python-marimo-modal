# file: demo.py
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "anthropic==0.49.0",
#     "pandas==2.2.3",
# ]
# ///

import marimo

__generated_with = "0.12.2"
app = marimo.App(width="medium", layout_file="layouts/demo.grid.json")


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    data = {
        'Name': ['John', 'Emma', 'Michael', 'Sarah', 'David'],
        'Age': [25, 30, 35, 28, 32],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin'],
        'Salary': [50000, 60000, 75000, 55000, 65000]
    }

    df = pd.DataFrame(data)
    df
    return data, df


if __name__ == "__main__":
    app.run()
