import pytest

from login import SocialNetwork

@pytest.fixture
def social_network():
    return SocialNetwork()

def test_login(social_network: SocialNetwork):
    social_network.create_account("pepe123@gmail.com", "potencia123")
    assert social_network.login("pepe123@gmail.com", "potencia123")

def test_failed_login(social_network: SocialNetwork):
    social_network.create_account("juanfdez@hotmail.com", "fdez1234")
    assert not social_network.login("juanfdez@hotmail.com", "fdez4567")