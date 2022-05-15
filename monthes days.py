from numpy import datetime64


def get_month_days(month: int, year: int) -> int:
    """
    The function counts and returns the number of days of specific month at a specific year.
    :param month: The wanted month.
    :param year: The wanted year.
    :return: The number of days of specific month at a specific year.
    """
    if month == 12:
        return datetime64(f"{year + 1}-0{(month % 12) + 1}-01") - datetime64(f"{year}-{month}-01")
    if month >= 10:
        return datetime64(f"{year}-{(month % 12) + 1}-01") - datetime64(f"{year}-{month}-01")
    return datetime64(f"{year}-0{(month % 12) + 1}-01") - datetime64(f"{year}-0{month}-01")


if __name__ == "__main__":
    print("Dec 2022: ", get_month_days(12, 2022))
    print("Oct 2022: ", get_month_days(11, 2022))
    print("Feb 2017:", get_month_days(2, 2017))
    print("Feb 2016:", get_month_days(2, 2016))
