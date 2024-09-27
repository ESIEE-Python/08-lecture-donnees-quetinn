""" fonction qui lit et analyse le contenu d'un fichier csv
    """
#### Imports et définition des variables globales
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        l = file.readlines()
        return [[int(num) for num in line.strip().split(';')] for line in l]

def get_list_k(data, k):
    """retourne la valeur correspondant au k-ieme  element de la liste

    Args:
        data, k: liste et numéro de l'élément de la liste que l'on veut

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    if k < len(data):
        return data[k]
    return None

def get_first(l):
    """ une autre fonction secondaire ...
    """
    return l[0]

def get_last(l):
    """ une autre fonction secondaire ...
    """
    i = len(l) -1
    return l[i]

def get_max(l):
    """ une autre fonction secondaire ...
    """
    return max(l)

def get_min(l):
    """ une autre fonction secondaire ...
    """
    return min(l)

def get_sum(l):
    """ une autre fonction secondaire ...
    """
    return sum(l)


#### Fonction principale


def main():
    """ appel des fonctions
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))

if __name__ == "__main__":
    main()
