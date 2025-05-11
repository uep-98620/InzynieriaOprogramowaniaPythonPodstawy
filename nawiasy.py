"""
Zadanie 2 - Nawiasy

Opis zadania:
- Zweryfikuj, czy podany ciąg znaków zawiera poprawne nawiasy.
- Każdemu otwartemu nawiasowi '(' powinien odpowiadać nawias zamykający ')'.
- Jeśli nawiasy się zgadzają, funkcja ma zwrócić True, w przeciwnym wypadku False.
- Rozpatrujemy wyłącznie nawiasy okrągłe.

Przykładowe wejścia (True):
    "( if ( zero ? x ) max (/ 1 x ))"
    "I told ( that its not ( yet ) done ). (42)"
Przykładowe wejścia (False):
    ":-)"
    "Czesc (o kurcze, chyba niechcacy zamkne ten nawias dwa razy))"
    "())(("

Wymagania:
- Implementacja funkcji `check_parentheses(s: str) -> bool`.
- Użycie stosu do weryfikacji poprawności nawiasów.
"""

def check_parentheses(s: str) -> bool:
    """
    Sprawdza, czy w ciągu znaków 's' nawiasy okrągłe są poprawnie sparowane.

    Args:
        s (str): Ciąg znaków do analizy.

    Returns:
        bool: True jeśli nawiasy są poprawne, False w przeciwnym wypadku.
    """
    ### TUTAJ PODAJ ROZWIĄZANIE ZADANIA

    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
            ### return False - powinno być zmienione i zwrócić prawdziwy wynik (zgodny z oczekiwaniami)
                return False
            stack.pop()
    return len(stack) == 0

# Przykładowe wywołanie:
if __name__ == "__main__":
    examples = [
        "( if ( zero ? x ) max (/ 1 x ))",
        "I told ( that its not ( yet ) done ). (42)",
        ":-)",
        "Czesc (o kurcze, chyba niechcacy zamkne ten nawias dwa razy))",
        "())(("
    ]

    for example in examples:
         result = check_parentheses(example)
         message = "Nawiasy poprawne." if result else "Nawiasy niepoprawne."
         print(f"{example} -> {result} ({message})")

if __name__ == "__main__":
    sentence_input = input("Podaj ciąg znaków do analizy: ")

    result = check_parentheses(sentence_input)
    message = "Nawiasy poprawne." if result else "Nawiasy niepoprawne."
    print(f"{sentence_input} -> {result} ({message})")
