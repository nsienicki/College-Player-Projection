import csv

years = [2025]
#years = list(range(2010, 2026))

headers = [
    "player_name", "team", "conf", "GP", "Min_per", "ORtg", "usg", "eFG", "TS_per", "ORB_per",
    "DRB_per", "AST_per", "TO_per", "FTM", "FTA", "FT_per", "twoPM", "twoPA", "twoP_per", "TPM",
    "TPA", "TP_per", "blk_per", "stl_per", "ftr", "yr", "ht", "num", "porpag", "adjoe", "pfr",
    "year", "pid", "type", "Rec Rank", " ast/tov", " rimmade", " rimmade+rimmiss", " midmade",
    " midmade+midmiss", " rimmade/(rimmade+rimmiss)", " midmade/(midmade+midmiss)", " dunksmade",
    " dunksmiss+dunksmade", " dunksmade/(dunksmade+dunksmiss)", " pick", " drtg", "adrtg",
    " dporpag", " stops", " bpm", " obpm", " dbpm", " gbpm", " mp", " ogbpm", " dgbpm", " oreb",
    "dreb", "treb", "ast", "stl", "blk", "pts", "pos_class"
]

headers = [header.strip() for header in headers]

for year in years:
    filename = f"trank_data_{year}.csv"
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as infile:
            reader = list(csv.reader(infile))

        cleaned_rows = [row[:-1] if len(row) > len(headers) else row for row in reader]

        with open(filename, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(headers)
            writer.writerows(cleaned_rows)
        print(f"Headers added successfully to {filename}")

    except FileNotFoundError:
        print(f"File {filename} not found. Skipping.")
