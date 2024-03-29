"""Model for aircraft flights. """

class Flight:

    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in {}.".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code {}.".format(number))

        if not (number[2:].isdigit() and int(number[2:])):
            raise ValueError("Invalid route number {}.".format(number))

        self._number = number
        self._aircraft = aircraft
        rows,seats = self._aircraft.seating_plan()
        self.seating = [None] + [{letter: None for letter in seats} for _ in rows]


    def number(self):
        return self._number


    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()


class Aircraft:

    def __init__(self,registration,model,num_rows,num_seats_per_row):
        self._registration = registration
        self._model = model
        self.num_rows = num_rows
        self.num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self.num_rows + 1),
                "ABCDEFGHJK"[:self.num_seats_per_row])