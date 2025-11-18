from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

def qol_to_csv(html: Path, output_csv: str):
    """
    Convert the website scrape into an interpretable CSV
    """
    # Send HTTP request
    text = html.read_text()

    # Parse HTML
    soup = BeautifulSoup(text, "html.parser")

    # Find Table
    table = soup.find("table", id="t2")

    # Extract header
    headers = []
    for th in table.find("thead").find_all("th"):
        headers.append(th.get_text(strip=True))

    # Extract rows
    rows = []
    for tr in table.find("tbody").find_all("tr"):
        cells = tr.find_all(["td", "th"])
        row = [cell.get_text(strip=True) for cell in cells]
        rows.append(row)

    # Build DataFrame
    df = pd.DataFrame(rows, columns=headers)

    # Save to CSV
    df.to_csv(output_csv, index=False)
    print(f"Saved {len(df)} rows to {output_csv}")

if __name__ == "__main__":
    qol_to_csv(Path("./rankings.jsp"), "data/qol.csv")
