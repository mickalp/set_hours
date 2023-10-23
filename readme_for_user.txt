1. Umiesić wszystkie pliki w dowolnej, tej samej lokalizacji
2. W pliku classes.py znajduje się zmienna file_n, w której należy ustawić lokalizację pliku roboczo godziny (file_n = "/path_to_your_file/file_name.xlsx"). Pozostałe zmienne, które należy zmienić znajdują się również w pliku classes.py, więc użytkownik powinnien zmiany wprowadzać jedynie w tym pliku.
3. Poprzednich kroków nie trzeba powtarzać. W kolejnych miesiącach należy jedynie uwzględnić czy zmienniły się nazwy plików i w razie czego zaktualizować również nazwy w wymiennionych zmiennych
4. W terminalu przejść do lokalizacji plików i wpisać komendę: python exec.py
Ewentualnie: python3 exec.py
Następnie podać ścięzkę do pliku dla którego mają być wygenerowane godziny (program sam zażąda), a następnie imię i nazwisko takie samo jak w Excelu.



Aktualizacja:
W pliku Roboczogodziny powinna znajdować się jedna zakładka, bez sumy godzin w ostatniej kolumnie. Jeśli będzie więcej niż jedna zakładka program wyświetli powiadomienie, że nie udało się dodać podsumowania w pliku. Jeżeli ta zakładka to już jest pdosumowanie wtedy program po prostu nie doda więcej zakładek, jeżeli jest to jakaś inna zakładka nie z podsumowaniem godzin, użytkownik powinnien ją usunąć.

Program jest napisany z założeniem, że jego uruchomienie odbywa się w miesiącu następującym po rozliczeniu, tzn. arkusze z godzinami są np. dla miesiąca czerwca, a plik powinnien zostać uruchomiony w lipcu. Uruchomienie w czerwcu spowoduje błędną datę w pliku końcowym. Została dodana opcja, w której użythownik może sam wybrać datę. W tym celu należy otworzyć plik classes.py i w zmiennej def_mnth zastąpić 0 na 1. W takim wypadku, po uruchomieniu programu exec.py pojawi się komunikat aby podać miesiąc i rok w formie "miesiąc rok" bez cudzysłowia, np 3 2023 lub 12 2022.

WAŻNE w pliku roboczogodziny nie powinna się znajdować kolumna z sumą godzin dla projektu, ponieważ będzie ona dodana w oddzielnym arkuszu w tym samym pliku. Obecność kolumny z sumą godzin w pierwszym arkuszu spowoduje błędny wynik w nowym arkuszu.




