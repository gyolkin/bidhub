from dataclasses import dataclass

from bidhub.core.models import AuctionId


@dataclass(frozen=True, slots=True)
class ScheduleFinishAuctionRequest:
    auction_id: AuctionId
    mins_to_finish: int


@dataclass(frozen=True, slots=True)
class SendWelcomeEmailRequest:
    receiver: str
