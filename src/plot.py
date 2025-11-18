import pandas as pd
import matplotlib.pyplot as plt

def plot_all():
    # Load cleaned data
    qol = pd.read_csv("data/qol_cleaned.csv")
    apmt_data = pd.read_csv("data/apmt_cleaned.csv")

    # Filter QOL columns to plot
    qol_columns = {
        "Health Care Index",
        "Cost of Living Index",
        "Property Price to Income Ratio"
    }

    # Filter apartment data to only "overall" bed size
    apmt_overall = apmt_data[apmt_data["bed_size"] == "overall"]

    # Calculate total number of plots needed
    total_plots = len(qol_columns) + 1  # QOL metrics + 1 apartment plot

    # Calculate grid dimensions
    n_cols = 2
    n_rows = (total_plots + n_cols - 1) // n_cols

    # Create a single figure with subplots for ALL plots
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(9, 6 * n_rows))
    axes = axes.flatten()

    # Plot QOL metrics
    for i, column in enumerate(qol_columns):
        ax = axes[i]
        
        # Create vertical box plot
        ax.boxplot([qol[column]], positions=[0], vert=True)

        # Mark Cleveland on box plot
        cleveland_value = qol[qol["City"] == "Cleveland"][column]
        if not cleveland_value.empty:
            ax.scatter(
                [0],
                cleveland_value.values,
                color="red",
                s=100,
                zorder=5,
                label="Cleveland",
            )
            ax.legend()

        ax.set_title(f"{column}", fontsize=20)
        ax.set_xticks([])
        ax.grid(True, alpha=0.3)

    # Plot apartment rent prices for "overall" bed size
    apmt_idx = len(qol_columns)
    ax = axes[apmt_idx]

    # Create vertical box plot for overall rent prices
    ax.boxplot(
        [apmt_overall["rent_price"]],
        labels=["Overall"],
        vert=True,
    )

    # Add Cleveland data point if available
    cleveland_data = apmt_overall[
        apmt_overall["location_name"].str.contains("Cleveland", case=False, na=False)
    ]
    if not cleveland_data.empty:
        cleveland_rent = cleveland_data["rent_price"].iloc[0]
        ax.scatter(
            [1],
            [cleveland_rent],
            color="red",
            s=100,
            zorder=5,
            label="Cleveland",
        )
        ax.legend()

    ax.set_title("Rent Prices (Overall)", fontsize=20)
    ax.grid(True, alpha=0.3)
    ax.set_xticks([])

    # Hide unused subplots
    for i in range(total_plots, len(axes)):
        axes[i].axis('off')

    plt.tight_layout()
    plt.savefig("./plots/all_plots.png", dpi=150, bbox_inches='tight')
    print(f"Saved plot with {total_plots} subplots to ./plots/all_plots.png")

if __name__ == "__main__":
    plot_all()