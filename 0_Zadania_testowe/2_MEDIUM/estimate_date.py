import datetime
import math


def estimate_date(start_date: str, estimated_hours: int):
    """Return number of workdays needed to get task done and estimated end date
    od task.

    Parameters
    ----------
    start_date : str
        Task start date
    estimated_hours : int
        Estimated number of hours to complete the task

    Returns
    -------
    estimated_workdays : int
        estimated int number of workdays to get task done
    end_date.date() : date
        estimated end date of completing the task

    Raises
    ------
        ValueError - if start_date is given in incorrect format
    """

    try:
        start_date_ = datetime.datetime.strptime(start_date, "%d-%m-%Y")
    except ValueError:
        raise ValueError("Wrong date format - the correct one is 'DD-MM-YYYY'.")
    estimated_workdays = math.ceil(estimated_hours / 8)
    workdays = estimated_workdays
    end_date = start_date_
    while workdays > 0:
        end_date += datetime.timedelta(days=1)
        weekday = end_date.weekday()
        if weekday >= 5:
            continue
        workdays -= 1
    return estimated_workdays, end_date.date()
