from .convert import qol_to_csv
from .clean import clean_apartment, clean_qol
from .plot import plot_all
from pathlib import Path

if __name__ == "__main__":
    qol_to_csv(Path("./rankings.jsp"), "data/qol.csv")
    clean_apartment()
    clean_qol()
    plot_all()
