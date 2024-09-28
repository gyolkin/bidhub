from dataclasses import dataclass

from bidhub.core.models import AuctionId


@dataclass(frozen=True, slots=True)
class ScheduleFinishAuctionInput:
    auction_id: AuctionId
    days_to_finish: int


@dataclass(frozen=True, slots=True)
class SendWelcomeEmailInput:
    receiver: str
