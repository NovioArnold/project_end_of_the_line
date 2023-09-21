
def sub_stock(amount: int, quantity: int) -> int:
    count = amount - quantity
    if count < 0:
        return amount
    else:
        return count


def add_stock(amount: int, quantity: int) -> int:
    amount = amount + quantity
    print(amount)
    return amount


def product_to_self(stock: int, quantity: int, max_store: int) -> int:
    l_stock = add_stock(stock, quantity)

    if l_stock <= max_store:
        return l_stock
    else:
        return max_store


def product_from_self(stock: int, quantity: int) -> int:
    s_stock = sub_stock(amount=stock, quantity=quantity)
    print(s_stock)
    if s_stock > 0:
        return s_stock
    else:
        return 0


def eval_bool(x: bool, y: bool) -> bool:
    return x == y


def eval_str(x: str, y: str) -> bool:
    return x == y


def eval_int(x: int, y: int) -> bool:
    return x == y


def greater_int(x: int, y: int) -> bool:
    return x > y
