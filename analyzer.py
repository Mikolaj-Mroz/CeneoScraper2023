import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

print(*[filename.removesuffix(".json") for filename in os.listdir('./opinions')], sep="\n")

product_code = input("Podaj kod produtu: ")

opinions = pd.read_json(f'./opinions/{product_code}.json')

opinions.score = opinions.score.map(lambda x: x.split("/")[0].replace(",", ".")).astype(float)

opinions_count = opinions.shape[0]
average_score = opinions.score.mean()
pros_count = opinions.pros.astype(bool).sum()
cons_count = opinions.cons.astype(bool).sum()

print(f"""
         Dla produktu o identyfikatorze {product_code} pobranych zostało {opinions_count} opinii.
         Dla {pros_count} opinii autor podana została lista zalet, a dla {cons_count} lista wad.
         Średnia ocen produktu wynosi {average_score:.2f}""")


# create a bar chart with stars
stars = opinions.score.value_counts(dropna=True).reindex(list(np.arange(0, 5.5, 0.5)))


# create a pie chart with recommendations

recommendation = opinions.recommendation.value_counts(dropna = False)

figure, axis = plt.subplots(ncols=2)

figure.suptitle("Podsumowanie opinii")

axis[0].set_title("Oceny")
axis[0].bar(stars.index.astype(str), stars.values)

axis[1].set_title("Opinie")
axis[1].pie(recommendation.values, labels = recommendation.index, autopct = "%1.1f%%")


if not os.path.exists('./plots'):
    os.mkdir('./plots')

plt.savefig(f"./plots/{product_code}.png")

plt.show()


## TODO
# drugi wykres kołowy polecam / nie polecam
# zapis do pliku katalog plots