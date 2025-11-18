from enum import Enum

class QOLColumns(str, Enum):
    HC = "Health Care Index"
    TCT = "Traffic Commute Time Index"
    PPIR = "Property Price to Income Ratio"
    COL = "Cost of Living Index"
    PPI = "Purchasing Power Index"
    SI = "Safety Index"
    PI = "Pollution Index"
    CI = "Climate Index"
    QOL = "Quality of Life"
