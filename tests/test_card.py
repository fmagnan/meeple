from fantasy_realms.card import Card
from fantasy_realms.glossary import Action, Suit


def test_card_does_not_trigger_bonus_with_empty_hand():
    bonus =  {
            'action': Action.WITH_ANY_ONE_SUIT,
            'value': 10,
            'suits': [Suit.ARTIFACT]
        }
    magic_carpet = Card('magic carpet', Suit.ARTIFACT, 12, bonus)
    assert magic_carpet.base_strength == 12
    assert magic_carpet.value == 12
