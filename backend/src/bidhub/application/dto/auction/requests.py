from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CreateAuctionInput:
    title: str
    description: str
    start_price: int
    mins_to_finish: int
