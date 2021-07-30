from abc import ABC, abstractmethod


class Piece(ABC):
    name = "piece"
    description = "description"

    @abstractmethod
    def possible_moves(self, size_x, size_y, pos_x, pos_y):
        pass
