import datetime


def count_days(date1: str, date2: str) -> datetime.timedelta:
    """Return number of days between two dates.
    
    Parameters
    ----------
    date1 : str
        First date given in following format: YYYY-MM-DDD (ISO 8601)
    date2 : str
        Second date given in following format: YYYY-MM-DDD (ISO 8601)
        
    Returns
    -------
    datetime.timedelta
        a timedelta object representing number of days between two dates
    """

    return (datetime.date.fromisoformat(date2) -
            datetime.date.fromisoformat(date1))

def date_from(given_date: str, number_of_days: int):
    """Return a date that differs from the given date by the given number of 
    days.
    
    Parameters
    ----------
    given_date : str
        A date given in following format: YYYY-MM-DDD (ISO 8601)
    number_of_days : int
        Given number of days (if positive, function returns future date;
        if negative, function returns past date)
    
    Returns:
        date
        a date object representing new future or past date
    """

    return (datetime.date.fromisoformat(given_date) +
            datetime.timedelta(days=number_of_days))