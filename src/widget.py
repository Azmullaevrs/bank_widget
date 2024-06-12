from src.masks import mask_account, mask_card


def mask_card_and_account(acc_number: str) -> str:
    """Возвращет исходную строку с замаскированным номером карты/счета"""
    if acc_number.lower().startswith("счет"):
        parts = acc_number.split(" ")
        account = parts[-1]
        return f"Счет {mask_account(account)}"
    else:
        card_name = " ".join([i for i in acc_number.split() if i.isalpha()])
        card_number = mask_card("".join([i for i in acc_number.split() if i.isdigit()]))
        return f"{card_name + " " + card_number}"


if __name__ == "__main__":
    print(mask_card_and_account("Visa Platinum 7000 7922 8960 6361"))
    print(mask_card_and_account("Счет 73654108430135874305"))
