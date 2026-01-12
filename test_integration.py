import pytest
from bank_app import transfer, calculate_interest


# ---------------- Integration: Transfer ----------------
def test_transfer_success():
    balance_from, balance_to = transfer(1000, 500, 300)

    # validate both accounts after transfer
    assert balance_from == 700
    assert balance_to == 800


# ---------------- Integration: Failure Scenario ----------------
def test_transfer_insufficient_balance():
    # transfer internally uses withdraw + deposit
    with pytest.raises(ValueError):
        transfer(200, 500, 400)


# ---------------- Integration: Combined Workflow ----------------
def test_transfer_then_interest():
    # Step 1: Transfer money
    balance_from, balance_to = transfer(5000, 2000, 1000)

    # Step 2: Apply interest on receiving account
    new_balance = calculate_interest(balance_to, 10, 1)

    # After transfer: 2000 + 1000 = 3000
    # After interest (10% for 1 year): 3000 * 1.10 = 3300
    assert new_balance == pytest.approx(3300)
