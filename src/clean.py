import pandas as pd

def clean_apartment():
    """
    Clean our apartment input CSV
    """
    apmt_data = pd.read_csv("data/apmt.csv")

    date_columns = [col for col in apmt_data.columns if col.startswith("20")]

    melted_data = pd.melt(
        apmt_data,
        id_vars=["location_name", "location_type", "bed_size"],
        value_vars=date_columns,
        var_name="date",
        value_name="rent_price",
    )

    melted_data = melted_data.dropna(subset=["rent_price"])

    city_data = melted_data[melted_data["location_type"] == "City"].copy()

    location_summary = (
        city_data.groupby(["location_name", "bed_size"])["rent_price"]
        .median()
        .reset_index()
    )

    location_summary.to_csv("data/apmt_cleaned.csv", index=False)

def clean_qol():
    """
    Clean our scraped QOL CSV
    """
    qol = pd.read_csv("data/qol.csv")
    qol = qol[qol["City"].str.endswith(", United States")]
    qol[["City", "State", "Country"]] = qol["City"].str.extract(r"^(.*), ([A-Z]{2}), (.*)$")

    qol.to_csv("data/qol_cleaned.csv", index=False)

if __name__ == "__main__":
    clean_apartment()
    clean_qol()
