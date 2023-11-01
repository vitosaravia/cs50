from jar import Jar
import pytest

# Test the __init__ method
def test_init():
    jar = Jar()  # Create a new instance of Jar
    assert jar.capacity == 12  # Check if it has the default capacity

# Test the __str__ method
def test_str():
    jar = Jar()
    jar.deposit(3)  # Deposit 3 cookies
    assert str(jar) == "aaa"  # Check if str(jar) displays the correct number of cookies

# Test the deposit method
def test_deposit():
    jar = Jar()
    jar.deposit(5)  # Deposit 5 cookies
    assert jar.size == 5  # Check if jar's size attribute is correct

    with pytest.raises(ValueError):
        jar.deposit(10)  # Try to deposit more cookies than the jar's capacity

# Test the withdraw method
def test_withdraw():
    jar = Jar()
    jar.deposit(5)  # Deposit 5 cookies
    jar.withdraw(3)  # Withdraw 3 cookies
    assert jar.size == 2  # Check if jar's size attribute is updated correctly

    with pytest.raises(ValueError):
        jar.withdraw(4)  # Try to withdraw more cookies than are available in the jar

if __name__ == "__main":
    pytest.main()
