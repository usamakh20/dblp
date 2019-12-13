import matplotlib.pyplot as plt
import pandas as pd
from itertools import repeat


def value_to_label(val, bin_width, max):
    if val * bin_width == max:
        return 'greater than ' + str(max)
    else:
        return '[' + str(val * bin_width) + '-' + str(val * bin_width + bin_width) + ')'


df_FoR = pd.read_csv("ML_data/publications_in_FoR_by_year.csv")
df_journal = pd.read_csv("ML_data/publications_in_journal_by_year.csv")
df_conference = pd.read_csv("ML_data/publications_in_conference_by_year.csv")
df_publication = pd.read_csv("ML_data/publications_by_year.csv")

df_FoR['label'] = list(map(value_to_label, [int(count / 50) if int(count / 50) < 5 else 5 for count in df_FoR['count']],
                      repeat(50), repeat(50 * 5)))

df_journal['label'] = list(map(value_to_label,
                          [int(count / 50) if int(count / 50) < 2 else 2 for count in df_journal['count']], repeat(50),
                          repeat(50 * 2)))

df_conference['label'] = list(map(value_to_label,
                             [int(count / 30) if int(count / 30) < 1 else 1 for count in df_conference['count']],
                             repeat(30), repeat(30 * 1)))

df_publication['label'] = list(map(value_to_label,
                             [int(count / 1000) if int(count / 1000) < 3 else 3 for count in df_publication['count']],
                             repeat(1000), repeat(1000 * 3)))


df_FoR[['id', 'year','label']].to_csv("ML_data/FoR.csv", index=False)
df_journal[['id', 'year', 'label']].to_csv("ML_data/Journal.csv", index=False)
df_conference[['id', 'year','label']].to_csv("ML_data/Conference.csv", index=False)
df_publication[['year','label']].to_csv("ML_data/Publication.csv", index=False)
