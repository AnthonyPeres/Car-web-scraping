import re

def clear_string(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    first_traitement = emoji_pattern.sub(r'', string)
    second_traitement = first_traitement.replace('\n', ' '.strip())
    third_traitement = " ".join(second_traitement.split())
    fourth_traitement = third_traitement.upper()
    return fourth_traitement


def clear_price(price):
    liste_int = [str(s) for s in price.split() if s.isnumeric()]
    new_price = ''.join(str(x) for x in liste_int)
    return int(new_price)


def clear_lieu(lieu):
    clear_string(lieu)
    ville = [str(s) for s in lieu.split() if not s.isdigit()]
    ville = ' '.join(ville)
    departement = [int(i) for i in lieu.split() if i.isdigit()][0]
    return ville, departement
