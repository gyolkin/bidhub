from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CreateBidRequest:
    amount: int
