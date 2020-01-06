class ShippingContainer:
    """A python program to model a shipping container.

       owner_code: the generic code of the container

       contents: the contents in the container"""

    next_serial = 1337

    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self,owner_code,content):
        self.owner_code = owner_code
        self.content = content
        self.serial = ShippingContainer._get_next_serial()