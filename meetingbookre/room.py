from database import CursorFromConnectionPool


class Room:
    def __init__(self, capacity, projector, wifi, price,  id=None):
        self.capacity = capacity
        self.projector = projector
        self.wifi = wifi
        self.price = price
