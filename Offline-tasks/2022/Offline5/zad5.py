# Płowiec Jakub
# Do kolejki priorytetowej wrzucam wszystkie wartosci zamienione na ujemne (abym mogl potem latwo wyciagnac max) razem z indeksem pola
# Zawsze dodaje je w petli ktora bada mozliwe pola na podstawie paliwa przez co nigdy nie dodaje/ sprawdzam 2 razy tego samego pola
# Co kazda iteracje petli wrzucam maksymalna wartosc jezeli nie moge skoczyc do mety i powtarzam az do skutku.
# W zwiazku z tym ze czesto samochod bedzie sie "wracal", na koniec sortuje tablice wynikowa
from zad5testy import runtests
from queue import PriorityQueue


def plan(T):
    que = PriorityQueue()
    answer = [0]
    power = T[0]
    position = 0
    finish = 0 # zmienna pozwalajaca zapamietac ktory ostatni element w petli sprawdzalem aby nastepnie od niego zaczynac szukac
    while True:
        if power + position >= len(T) - 1:
            break
        for i in range(finish + 1, position + power + 1):
            que.put((-T[i], i))
        finish = position + power
        a = que.get()
        answer.append(a[1])
        if a[1] > position:
            power = power - (a[1] - position) + T[a[1]]
            position = a[1]
        else:
            power = power + T[a[1]]
    answer.sort()
    return answer


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )