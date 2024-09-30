import pytest
from src.masks import get_mask_account, get_mask_card_number

@pytest.mark.parametrize('numbers, masks', [('7000792289606361', '7000 79** **** 6361'),
                                            ('4571354875129009', '4571 35** **** 9009'),
                                            (2504706942057145, '2504 70** **** 7145')])

def test_get_mask_card_number(numbers, masks):
    assert get_mask_card_number(numbers) == masks


def test_get_mask_card_number_len():
    assert get_mask_card_number('700079228960636125') == 'Проверьте длину номера карты'
    assert get_mask_card_number('') == 'Проверьте длину номера карты'


@pytest.mark.parametrize('account, masks', [('64686473678894779589', '**9589'),
                                            ('35383033474447895560', '**5560'),
                                            (73654108430135874305, '**4305')])

def test_get_mask_account(account, masks):
    assert get_mask_account(account) == masks


def test_get_mask_account_len():
    assert get_mask_account('7000792289606361254578') == 'Проверьте длину номера счета'
    assert get_mask_account('') == 'Проверьте длину номера счета'
