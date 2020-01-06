class Translate:
    """A python program that models a game for translating between languages.
    
       Last Modified: 13 - 12 - 2019
       
       Author: Ayodabo Tomisin"""                                                                     #class
    score = 0                                                                                         #attributes
    group = {"Baby" : "Omo",
             "Car" : "Moto",
             "House" : "Ile",
             "Book" : "Iwe",
             "Shoe": "Bata",
             "Plate" : "Abo",
             "Boy" : "Omodekunrin",
             "Girl" : "Omodebinrin",
             "Father" : "Baba",
             "Mother" : "Iya"}


    def play_game(self):
        """This gives the user the chance to play the game."""

        for k,v in Translate.group.items():      #repeatedly prompts the user for input
            prompt = str(k)  # returns the key v in the group dictionary
            print("can you guess the Yoruba meaning of {}?".format(prompt))
            response = input("> ")
            if response.isnumeric():
                raise ValueError("Expected str, got int instead.")
            else:
                if response == v:         #checks if the response is equal to the value at the index in the dictionary
                    Translate.score += 5                 #adds five to the score
                    print("Wow! you got that right.now try the next question.")
                else:
                    Translate.score += 0                     #adds zero to the score
                    print("Sorry you did not get it right, the correct answer is \"{}\" maybe you will in the next question".format(v))

        self._check_result()

    def _check_result(self):
        #This is a private method
        print("Game completed. time to know how well you performed.")
        print("")
        """This checks for the rating based on the user's score"""
        if Translate.score >= 40:
            print("You are very good!, you score is  {}.".format(self.score))
        elif Translate.score >= 30:
            print("You are almost there. You got a score of {}".format(self.score))
        elif Translate.score >= 20:
            print("You still got a long way to go. your score is {}".format(self.score))
        else:
            print("You need to work harder next time. your score is {}".format(self.score))


if __name__ == "__main__":
    translate = Translate()
    translate.play_game()
