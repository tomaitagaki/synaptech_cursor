from enum import Enum
from dataclasses import dataclass

@dataclass
class BandType:
	freq_start: float
	freq_stop: float

class Band(Enum):
	MU = BandType(8.0, 12.0)
	BETA = BandType(18.0, 26.0)
