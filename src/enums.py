from enum import Enum


class TaskPriorityEnum(str, Enum):
    low = 'Low'
    medium = 'Medium'
    high = 'High'
    highest = 'Highest'
    expired = 'Expired'
    cancelled = 'Cancelled'


class TaskWhereEnum(str, Enum):
    home = 'Home'
    work = 'Work'
    sport = 'Sport'
    family = 'Family'
    study = 'Study'
    other = 'Other'
