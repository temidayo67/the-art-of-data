import pandas as pd
import numpy as np
desired_width=320

pd.set_option('display.width', desired_width)

np.set_printoptions(linewidth=desired_width)

pd.set_option('display.max_columns',10)
pepe = pd.read_csv("C:\\Users\\TOSHIBA\\Downloads\\export-token-0x6982508145454Ce325dDbE47a25d4ec3d2311933.csv")
print(pepe.head())
print(pepe.columns)
print(pepe[['Method']])
pepe_addresses = pepe[["Txhash","From", "To", "Method", "DateTime"]]
print(pepe_addresses.head(20))
print(pepe_addresses.shape)
transaction_type = pepe_addresses.groupby("Method")
print(transaction_type.size())
swap_trades = transaction_type.get_group("Swap")
print(swap_trades.head())
swap_trades.to_excel("Pepe Trades.xlsx")
