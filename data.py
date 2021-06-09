
from dataclasses import asdict, dataclass


@dataclass
class Test:
    test: str


print(asdict(Test("123")))
