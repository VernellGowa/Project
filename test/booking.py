from dataclasses import dataclass, field

@dataclass
class Booking():
    service: any = field(default=None)
    date: any = field(default=None)
    time: any = field(default=None)
    stylist_id: any = field(default=None)