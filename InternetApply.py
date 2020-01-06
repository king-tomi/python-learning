class InternetApply:
    """This is a class that simulates an internet application in which it continually checks if a person
    has packets to send and if so, sends it to another person."""

    def __init__(self,name,packets,internet = True):
        self.name = name
        self.packets = list(packets)
        self.internet = internet

    def __str__(self):
        return self.name

    def packets(self):
        return self.packets

    def check_internet(self):
        if not self.internet:
            return "You do not have internet please turn it on."
        else:
            return "You are logged in."

    def check_packets(self):
        if len(self.packets) == 0:
            return "Packets empty please fill."
        else:
            return "packets not empty and you have internet"

    def send_packets(self,receiver):
        """this checks first if the packets is empty and there is no internet.if not so, it returns none
        and does not implement but if so, it sends the packets to the receiver."""
        if len(self.packets) == 0 or not self.internet:
            return "Packets empty please fill and you do not have internet."
        else:
            sent = False
            received = []
            for item in self.packets:
                received.append(item)
            sent = True
            return "".join("Packets sent to {} and {}".format(receiver,sent))
        
        
    

class Receiver(InternetApply):
    
    def __init__(self,name,internet = True):
        super().__init__(name,packets=self,internet=True)
        self.name = name
        self.internet = internet

    def check_internet(self):
        super().check_internet()

    def receive_packets(self,sender):
        """this checks if the receiver has internet first and if he does not,it tells the receiver to turn it on.
        if true, it implements the superclass send_packets method."""
        super().send_packets("Bob")
        return "Packets received from {}".format(sender)




if __name__ == "__main__":
    Alice = InternetApply("Alice",[],True)
    print(str(Alice))
    print(Alice.check_internet())
    print(Alice.send_packets("Bob"))

    Bob = Receiver("Bob")
    print(Bob.receive_packets("Alice"))