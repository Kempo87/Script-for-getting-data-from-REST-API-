# Opis programu "KALKULATOR WALUT":

Program służy do pobierania kursu waluty z danego dnia z Narodowego Banku Polskiego (NBP). Użytkownik może podać nazwę waluty (np. EUR, USD) oraz datę, dla której chce poznać kurs waluty. Program korzysta z API NBP, aby uzyskać kursy walut na podstawie podanych parametrów.

## Opis działania programu krok po kroku:

Program rozpoczyna się od wyświetlenia komunikatu "KALKULATOR WALUT".

Następnie sprawdza, czy użytkownik podał nazwę waluty jako argument wywołania programu. Jeśli nie, to prosi użytkownika o wprowadzenie nazwy waluty.

Program przekształca nazwę waluty na wielkie litery, co pozwala uniknąć problemów z rozpoznaniem waluty.

Program podobnie jak w przypadku waluty, sprawdza, czy użytkownik podał datę jako argument wywołania programu. Jeśli nie, to prosi użytkownika o wprowadzenie daty.

Następnie program próbuje sparsować datę, aby upewnić się, że ma ona właściwy format.

Po poprawnym odczytaniu waluty i daty, program tworzy adres URL, który zawiera te dane, aby odpytać API NBP o kurs waluty na daną datę.

Następnie program wysyła zapytanie do API NBP o kurs waluty.

Jeśli serwer zwraca kod 404 (brak danych), program wyświetla odpowiedni komunikat i kończy działanie z kodem błędu 2.

Jeśli odpowiedź od serwera jest nieprawidłowa, program wyświetla komunikat o nieoczekiwanym błędzie serwera i kończy działanie z kodem błędu 3.

Jeśli odpowiedź od serwera jest prawidłowa, program parsuje ją jako dane w formacie JSON.

Następnie program próbuje wyodrębnić kurs waluty z danych JSON. Wartość ta jest średnim kursem ("mid").

Jeśli parsowanie lub wyodrębnienie kursu nie powiedzie się, program wyświetla komunikat o błędzie w odpowiedzi serwera i kończy działanie z kodem błędu 4.

W przeciwnym przypadku program wyświetla informację o kursie waluty w danym dniu oraz wybranej dacie.

### Ten program jest przykładem prostego kalkulatora walut, który można dostosować do swoich potrzeb i używać do sprawdzania kursów walut z NBP.
