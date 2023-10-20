1. Umiesić wszystkie pliki w dowolnej, tej samej lokalizacji
2. Otworzyć plik exe.py w dowolnym programie tekstowym lub do obslugi programów Python
3. Zmienić ścieżki tam gdzie jest to niezbędne (zaznaczone w skrypcie)na scięzkę gdzie zostały umieszczone pliki w pkt 1.
4. Zapisać i zamknąć plik exec.py
5. Otworzyć plik czas_pr_v1.2.py (z czasem przy aktualizacjach może być inna wersja pliku) tak samo jak exec.py w pkt.2
6. Na początku skryptu wstawić taką samą scieżkę jak w pliku exec.py (zmienna pt)
7. Na końcu pliku zdefiniować ścięzkę do zapisu pliku, zapisać i zamknąć plik.
8. W pliku classes.py znajduje się zmienna file_n, w której należy ustawić lokalizację pliku roboczo godziny (file_n = "/path_to_your_file/file_name.xlsx")
8a. Poprzednich kroków nie trzeba powtarzać. W kolejnych miesiącach należy jedynie uwzględnić czy zmienniły się nazwy plików i w razie czego zaktualizować również nazwy w wymiennionych zmiennych
9. W terminalu przejść do lokalizacji plików i wpisać komendę: python exe.py
Ewentualnie: python3 exe.py
Następnie podać ścięzkę do pliku dla którego mają być wygenerowane godziny (program sam zażąda), a następnie imię i nazwisko takie samo jak w Excelu
10. Gotowy plik excel powinnien się pojawić w lokalizacji ustawionej na koncu programu czas_pr_v1.2.py


Aktualizacja:
W pliku Roboczogodziny powinna znajdować się jedna zakładka, bez sumy godzin w ostatniej kolumnie. Jeśli będzie więcej niż jedna zakładka program wyświetli powiadomienie, że nie udało się dodać podsumowania w pliku.

Program jest napisany z założeniem, że jego uruchomienie następuje w miesiącu następującym po rozliczeniu, tzn. arkusze z godzinami są np. dla miesiąca czerwca, a plik powinnien zostać uruchomiony w lipcu. Uruchomienie w czerwcu spowoduje błędną datę w pliku końcowym.




