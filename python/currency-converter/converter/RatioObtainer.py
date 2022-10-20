import json, datetime, urllib.request


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # TODO
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise
        try:
            with open("ratios.json", "r") as f:
                data = json.load(f)
                for exchange in data:
                    if exchange['base_currency'] == self.base and exchange['target_currency'] == self.target and exchange['date_fetched'] == str(datetime.date.today()):
                        return True
                else:
                    return False
        except FileNotFoundError:
            return False

    def fetch_ratio(self):
        # TODO
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it
        url = f'https://api.exchangerate.host/convert?from={self.base}&to={self.target}'
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        self.save_ratio(data['result'])
        return data['result']

    def save_ratio(self, ratio):
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        try:
            with open("ratios.json", "r") as f:
                data = json.load(f)
                for exchange in data:
                    if exchange['base_currency'] == self.base and exchange['target_currency'] == self.target:
                        exchange['ratio'] = ratio
                        exchange['date_fetched'] = str(datetime.date.today())
        except FileNotFoundError:
            data = []
        record = {
            "base_currency": self.base, 
            "target_currency": self.target, 
            "date_fetched": str(datetime.date.today()),
            "ratio": ratio
        }
        data.append(record)
        with open("ratios.json", "w") as f:
            json.dump(data, f, indent=4)

    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        with open("ratios.json", "r") as f:
            data = json.load(f)
            for exchange in data:
                if exchange['base_currency'] == self.base and exchange['target_currency'] == self.target:
                    return exchange['ratio']