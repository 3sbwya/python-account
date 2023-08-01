inputs = [
    ["ADD", "Matt", "123456789012", "$1000"],
    ["ADD", "Kirstin", "1234567890123456", "$1500"],
    ["ADD", "John", "123456789", "$2000"],
    ["CHARGE", "Matt", "$500"],
    ["CHARGE", "John", "$1000"],
    ["CREDIT", "Kirstin", "$750"],
]

'''
    ADD:    Validate cc number: 12-16 digits long
    CHARGE: If charge does not put balance over limit, apply charge
    CREDIT: apply credit, negative balance is allowed

    END: Print account summary
'''

class Account:
    def __init__(self, name: str, cc: str, limit: int, balance: int = 0) -> None:
        self.name = name
        self.cc = cc
        self.limit = limit
        self.balance = balance

    def __eq__(self, __value: object) -> bool:
        return self.name == __value.name and self.cc == __value.cc, self.limit == __value.limit and self.balance == __value.balance

    def sumamry(self):
        return [self.name, toDollarStr(self.balance)]

def solution(opts):
    accounts = {}
    for input in opts:
        action = input[0]
        if action == "ADD":
            name, cc, limit = input[1:]
            accounts = addAccount(name, cc, fromDollarStr(limit), accounts)
        elif action == "CHARGE":
            name, amt = input[1:]
            accounts = chargeAccount(name, fromDollarStr(amt), accounts)
        elif action == "CREDIT":
            name, amt = input[1:]
            accounts = creditAccount(name, fromDollarStr(amt), accounts)
        
    # Print summary
    return accountSummary(accounts)


def addAccount(name: str, cc: str, limit: int, accts: dict):
    accts[name] = Account(name, cc, limit) if isValidCC(cc) else None
    return accts

def chargeAccount(name: str, amount: int, accts: dict):
    if accts[name]:
        account: Account = accts[name]
        newBalance = account.balance + amount
        if newBalance <= account.limit:
            account.balance = newBalance
            accts[name] = account
    return accts

def creditAccount(name: str, amount: int, accts: dict):
    if accts[name]:
        account: Account = accts[name]
        account.balance -= amount
        accts[name] = account
    return accts

def accountSummary(accts: dict):
    names = sorted(accts.keys())
    result = []
    for name in names:
        account: Account = accts[name]
        result.append(account.sumamry() if account else [name, "error"])
    return result

def fromDollarStr(amtStr: str) -> int:
    return int(amtStr[1:])

def toDollarStr(amt: int) -> str:
    return f"${amt}" if amt >= 0 else f"-${abs(amt)}"

def isValidCC(cc: str) -> bool:
    return (12 <= len(cc) <= 16) and cc.isdigit()


print(solution(inputs))