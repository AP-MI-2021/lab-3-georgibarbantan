import math

def citire_lista():
    """
    citeste lista ca string
    :return: lista ca int
    """
    result_list = []
    string_lista = input('Introduceti lista: ')
    string_elemente = string_lista.split(sep = " ")
    for string_element in string_elemente:
        element = int(string_element)
        result_list.append(element)

    return result_list

def is_prime(nr):
    """
    verifica daca nr este prim
    :param nr:
    :return:
    """
    if nr < 2:
        return False
    elif nr == 2 or nr == 3:
        return True
    elif nr % 2 == 0:
        return False
    else:
        for x in range(3, int(math.sqrt(nr)) + 1, 2):
            if nr % x == 0:
                return False
    return True

def all_not_prime(lista):
    """
    :param lista: verifica daca o subsecventa din lista are numai numere neprime
    :return:
    """
    for element in lista:
        if is_prime(element) == True:
            return False
    return True

def get_longest_all_not_prime(lista):
    """
    :param lista: determina cea mai lunga subsecventa cu proprietatea ceruta
    :return:
    """
    lista_secvente = []
    for start in range(0, len(lista)):
        for end in range(start + 1, len(lista)+1):
            if all_not_prime(lista[start:end]) == True:
                lista_secvente.append(lista[start:end])

    max_sec = []

    for secventa in lista_secvente:
        if len(secventa) > len(max_sec):
            max_sec = secventa

    return max_sec
def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([1, 2, 3, 5]) == [1]
    assert get_longest_all_not_prime([2, 3, 6, 10, 12]) == [6, 10, 12]

def average_below(lista, nr):
    """
    verifica daca media aritmetica a elementelor din lista e mai mica decat nr
    :param lista:
    :param nr:
    :return:
    """
    s = 0
    for element in lista:
        s += element
    n = len(lista)
    if s/n < nr:
        return True
    else:
        return False

def get_longest_average_below(lista, nr):
    """
    determina cea mai lunga subsecventa cu proprietatea ceruta
    :param lista:
    :param nr:
    :return:
    """
    lista_secvente2 = []
    for start in range(0, len(lista)):
        for end in range(start + 1, len(lista) + 1):
            if average_below(lista[start:end], nr) == True:
                lista_secvente2.append(lista[start:end])

    max_sec = []

    for secventa in lista_secvente2:
        if len(secventa) > len(max_sec):
            max_sec = secventa

    return max_sec

def test_get_longest_average_below():
    assert get_longest_average_below([10, 56, 23, 89, 12, 5], 20) == [12, 5]
    assert get_longest_average_below([123, 456, 23, 78, 16, 42, 3, 1, 5, 9, 42], 50) == [23, 78, 16, 42, 3, 1, 5, 9, 42]

def digit_count(nr):
    """
    functia calculeaza numarul de cifre al parametrului nr
    :param nr:
    :return: numarul de cifre
    """
    nrcif = 0
    while nr != 0:
        nr = nr//10
        nrcif += 1
    return nrcif

def digit_count_desc(lista):
    """
    verifica daca lista are numarul de cifre al elementelor in ordine descrescatoare
    :param lista:
    :return:
    """
    for i in range(len(lista)-1):
        if digit_count(lista[i]) < digit_count(lista[i+1]):
            return False
    return True

def get_longest_digit_count_desc(lista):
    """
    determina cea mai lunga subsecventa cu proprietatea ceruta
    :param lista:
    :return:
    """
    lista_secvente3 = []
    for start in range(0, len(lista)):
        for end in range(start + 1, len(lista) + 1):
            if digit_count_desc(lista[start:end]) == True:
                lista_secvente3.append(lista[start:end])

    max_sec = []

    for secventa in lista_secvente3:
        if len(secventa) > len(max_sec):
            max_sec = secventa

    return max_sec
def test_get_longest_digit_count_desc():
    assert get_longest_digit_count_desc([1, 2, 3, 56698, 45663, 4563, 4521, 459, 123, 75, 12, 5, 0]) == [56698, 45663, 4563, 4521, 459, 123, 75, 12, 5, 0]
    assert get_longest_digit_count_desc([456, 123, 11, 8, 741, 25, 6]) == [456, 123, 11, 8]

def main():
    while True:
        print("""
            1--> Citire lista
            2--> Determinare cea mai lungă subsecvență formata doar din numere neprime
            3--> Determinare cea mai lungă subsecvență unde media numerelor nu depășește o valoare citită
            4--> Determinare cea mai lunga subsecventa formata doar din numere unde numărul de cifre este în ordine descrescătoare
            5--> Iesire
            """
        )
        optiune = input('Alege comanda: ')
        if optiune == '1':
            lista = citire_lista()
            print(f'Lista:', lista)
        elif optiune == '2':
            print('Cea mai lunga subsecventa formata doar din numere neprime este: ')
            test_get_longest_all_not_prime()
            print(get_longest_all_not_prime(lista))
        elif optiune == '3':
            i = float(input('Dati numarul: '))
            print(f'Cea mai lunga subsecventa formata doar din numere unde media numerelor nu depășește valoarea citită {i} este: ')
            test_get_longest_average_below()
            print(get_longest_average_below(lista, i))
        elif optiune == '4':
            print('Cea mai lunga subsecventa formata doar din numere unde numărul de cifre este în ordine descrescătoare este: ')
            test_get_longest_digit_count_desc()
            print(get_longest_digit_count_desc(lista))
        elif optiune == '5':
            break
        else:
            print('Optiune invalida!')

main()