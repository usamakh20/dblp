import matplotlib.pyplot as plt
import pandas as pd

df_FoR = pd.read_csv("ML_data/publications_in_FoR_by_year.csv")
df_journal = pd.read_csv("ML_data/publications_in_journal_by_year.csv")
df_conference = pd.read_csv("ML_data/publications_in_conference_by_year.csv")

df_FoR['label'] = [int(count / 100) if int(count / 100) < 100 else 100 for count in df_FoR['count']]
df_journal['count'] = [int(count / 10) if int(count / 10) < 10 else 10 for count in df_journal['count']]
df_conference['label'] = [int(count / 100) if int(count / 100) < 10 else 10 for count in df_conference['count']]

df_FoR.to_csv("FoR_bin_100.csv")
df_journal.to_csv("Journal_bin_10.csv")
df_conference.to_csv("Conference_bin_100.csv")

# plt.scatter(df['year'],df['count'])
# plt.show()
