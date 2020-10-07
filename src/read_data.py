import pandas as pd

data = pd.read_excel("spider_twosides_table.xlsx").set_index(["mol_id", "alldrugs_TWOSIDES"])