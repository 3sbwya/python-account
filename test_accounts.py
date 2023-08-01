from accounts import *

name = "Matt"
cc = "1234567890123"
invalidCC = "123456"
limit = 1000

def test_addAccount():
    testcases = [
        [[name, cc, limit], {name: Account(name, cc, limit)}],
        [[name, invalidCC, limit], {name: None}],
    ]
    for case in testcases:
        n, c, l = case[0]
        expected = case[1]
        assert addAccount(n, c, l, {}) == expected

def test_chargeAccount():
    testcases = [
        [[name, 100, {name: Account(name, cc, limit)}], {name: Account(name, cc, limit, balance=100)}],
        [[name, limit+100, {name: Account(name, cc, limit)}], {name: Account(name, cc, limit, balance=0)}],
        [[name, limit, {name: Account(name, cc, limit)}], {name: Account(name, cc, limit, balance=limit)}],
        [[name, 100, {name: None}], {name: None}],

    ]
    for case in testcases:
        n, a, accts = case[0]
        expected = case[1]
        actual = chargeAccount(n, a, accts)
        assert actual == expected

def test_creditAccount():
    testcases = [
        [[name, 100, {name: Account(name, cc, limit, balance=1000)}], {name: Account(name, cc, limit, balance=900)}],
        [[name, 100, {name: Account(name, cc, limit)}], {name: Account(name, cc, limit, balance=-100)}],
        [[name, 100, {name: None}], {name: None}],

    ]
    for case in testcases:
        n, a, accts = case[0]
        expected = case[1]
        actual = creditAccount(n, a, accts)
        assert actual == expected

def test_account_summary():
    testcases = [
        [{name: Account(name, cc, limit)}, [[name, "$0"]]],
        [{name: Account(name, cc, limit, balance=100)}, [[name, "$100"]]],
        [{name: Account(name, cc, limit, balance=-100)}, [[name, "-$100"]]],
        [{name: None}, [[name, "error"]]],
    ]
    for case in testcases:
        input, expected = case
        actual = accountSummary(input)
        assert actual == expected

def test_fromDollarStr():
    assert fromDollarStr("$100") == 100

def test_toDollarStr():
    testcases = [
        [100, "$100"],
        [-100, "-$100"]
    ]
    for case in testcases:
        input, expected = case
        assert toDollarStr(input) == expected

def test_isValidCC():
    testcases = [
        ["123456789012",        True],
        ["1234567890123456",    True],
        ["1234567",             False],
        ["1234567890123456789", False],
        ["1234567890ABCD",      False],
    ]
    for case in testcases:
        input, expected = case
        assert isValidCC(input) == expected