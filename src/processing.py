def filter_by_state(transactions: list, state: str = "EXECUTED") -> list:
    """Фильтрует транзакции по состоянию"""
    return [elem for elem in transactions if elem["state"] == state]


def filter_by_date(transactions: list, descending: bool = True) -> list:
    """Фильтрует транзакции по дате"""
    return sorted(transactions, key=lambda date: date.get("date"), reverse=descending)
