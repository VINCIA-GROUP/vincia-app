from enum import Enum

class AreasID(Enum):
   LANGUAGES = "76a3c2e5-8630-4607-af2d-68933a6dd13b"
   HUMANITIES = "13cd1299-5ebb-4fef-8d57-93db495cb170"
   NATURAL_SCIENCE = "7e6c2d22-a6bb-472a-ac86-a1c29b1658e7"
   MATHEMATICS = "dbb6cee7-3cba-49ca-84eb-b1204d670f89"

   @classmethod
   def get_index(cls, value):
      for index, member in enumerate(cls):
         if member.value == value:
            return index
      raise ValueError(f"{value} não encontrado no enum {cls.__name__}")
