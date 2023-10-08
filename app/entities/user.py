from dataclasses import dataclass


@dataclass
class User:
    id: int
    first_name: str
    middle_name: str
    last_name: str
    description: str

    def full_name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'
