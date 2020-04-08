import re
from collections import Counter, defaultdict


class FlowerBoutique:
    """ Bouquets generation Class"""

    regex = re.compile('[0-9]+[a-z]')

    def __init__(self, flowers, *args, **kwargs):
        self.flowers = Counter(flowers)

    def _check_flowers_count(self, bouquet):
        success = True
        for k, v in bouquet.items():
            if self.flowers[k] < v:
                success = False
        return success

    @staticmethod
    def _translate_bouquet(bqt):
        flowers = FlowerBoutique.regex.findall(bqt)
        bouquet_dct = {s[-1] + bqt[1]: int(s[:-1]) for s in flowers}
        return bouquet_dct

    def _take_flowers(self, bqt):
        for k, v in bqt.items():
            self.flowers[k] -= v
        return bqt

    def _create_bouquet(self, bqt):
        if self._check_flowers_count(bqt):
            return self._take_flowers(bqt)
        else:
            return {}

    def take_order(self, bouquet_name):
        bouquet = self._translate_bouquet(bouquet_name)
        created_bouquet = self._create_bouquet(bouquet)
        return bouquet_name

    def find_max(self, bouquets):
        available_bouquets = Counter(defaultdict(int))

        # Until least 1 of each specie is available
        while not any(v == 0 for k, v in self.flowers.items()):
            bqts = list(map(self.take_order, bouquets))
            for item in bqts:
                available_bouquets[item] += 1
        return available_bouquets


if __name__ == '__main__':
    file = "app/src/sample.txt"

    try:
        with open(file) as f:
            data_str = [str.replace('\n', '') for str in f.readlines()]
            index = data_str.index('')
            bouquets, flowers = data_str[:index], data_str[index + 1:]
            boutique = FlowerBoutique(flowers)

            print(f"You can create: {boutique.find_max(bouquets)}!")

    except IOError:
        print("Input file was not found!")
