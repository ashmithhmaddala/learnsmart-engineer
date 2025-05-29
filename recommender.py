import pandas as pd

def generate_recommendations(df: pd.DataFrame, score_cols: list[str] | None = None) -> list[str]:
    if score_cols is None:
        score_cols = df.select_dtypes(include="number").columns.tolist()
    if not score_cols:
        raise ValueError("No numeric columns found.")
    df["__weakest__"] = df[score_cols].idxmin(axis=1)
    counts = df["__weakest__"].value_counts().to_dict()
    df.drop(columns="__weakest__", inplace=True)
    return [
        f"Focus on improving **{col}** — weakest in {cnt} records"
        for col, cnt in counts.items()
    ]