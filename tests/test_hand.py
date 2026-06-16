from typing import Any

from fantasy_realms.card import Card as CardClass
from fantasy_realms.deck import deck
from fantasy_realms.glossary import Card, Suit
from fantasy_realms.hand import Hand


def init_hand(deck: dict[str, Any], cards: list[Card]) -> Hand:
    hand :Hand = Hand(deck)
    for card in cards:
        hand.add_card(card)
    return hand

def test_it_counts_cards_in_hand():
    hand = init_hand(deck, [Card.DRAGON, Card.BELL_TOWER, Card.MAGIC_WAND])
    assert hand.count_cards() == 3

def test_applies_penalty_when_dragon_has_not_a_wizard():
    hand = init_hand(deck, [Card.DRAGON])
    assert hand.get_total() == -10

def test_neutralizes_penalty_when_dragon_is_with_a_a_wizard():
    hand = init_hand(deck, [Card.DRAGON, Card.ELEMENTAL_ENCHANTRESS])
    assert hand.get_total() == 35

def test_gets_points_for_princess_with_elemental_enchantress():
    hand = init_hand(deck, [Card.PRINCESS, Card.ELEMENTAL_ENCHANTRESS])
    assert hand.get_total() == 15

def test_cancels_lightning_points_from_princess():
    hand = init_hand(deck, [Card.PRINCESS, Card.LIGHTNING])
    assert hand.get_total() == 13

def test_gets_lightning_points_with_rainstorm():
    hand = init_hand(deck, [Card.RAINSTORM, Card.LIGHTNING])
    assert hand.get_total() == 49

def test_gets_points_from_princess_and_loses_points_from_empress_when_they_are_together():
    hand = init_hand(deck, [Card.PRINCESS, Card.EMPRESS])
    assert hand.get_total() == 15

def test_adds_points_from_each_flood_for_rainstorm():
    hand = init_hand(deck, [Card.RAINSTORM, Card.SWAMP, Card.WATER_ELEMENTAL])
    assert hand.get_total() == 55

def test_does_nothing_when_island_is_with_dragon():
    hand = init_hand(deck, [Card.DRAGON, Card.ISLAND])
    assert hand.get_total() == 4

def test_clears_penalty_from_swamp_with_island():
    hand = init_hand(deck, [Card.SWAMP, Card.ISLAND, Card.DWARVISH_INFANTRY])
    assert hand.get_total() == 47

def test_adds_points_to_elven_archers_when_there_is_no_weather():
    hand = init_hand(deck, [Card.ELVEN_ARCHERS, Card.ISLAND])
    assert hand.get_total() == 29

def test_cancels_elven_archers_bonus_with_air_elemental():
    hand = init_hand(deck, [Card.ELVEN_ARCHERS, Card.AIR_ELEMENTAL])
    assert hand.get_total() == 14

def test_blanks_fire_elemental_with_rainstorm():
    hand = init_hand(deck, [Card.RAINSTORM, Card.FIRE_ELEMENTAL])
    assert hand.get_total() == 8

def test_blanks_hydra_with_wildfire():
    hand = init_hand(deck, [Card.WILDFIRE, Card.HYDRA])
    assert hand.get_total() == 40

def test_do_not_blank_dragon_with_wildfire():
    hand = init_hand(deck, [Card.WILDFIRE, Card.DRAGON])
    assert hand.get_total() == 30

def test_blanks_smoke_when_there_is_no_flame():
    hand = init_hand(deck, [Card.SMOKE, Card.AIR_ELEMENTAL])
    assert hand.get_total() == 4

def test_counts_smoke_with_fire_elemental():
    hand = init_hand(deck, [Card.SMOKE, Card.FIRE_ELEMENTAL])
    assert hand.get_total() == 31

def test_does_nothing_when_dragon_and_bell_tower_are_together():
    hand = init_hand(deck, [Card.DRAGON, Card.BELL_TOWER])
    assert hand.get_total() == -2

def test_does_nothing_when_celestial_knights_and_beast_master_are_together():
    hand = init_hand(deck, [Card.CELESTIAL_KNIGHTS, Card.BEASTMASTER])
    assert hand.get_total() == 21

def test_add_points_when_unicorn_meets_beast_master():
    hand = init_hand(deck, [Card.UNICORN, Card.BEASTMASTER])
    assert hand.get_total() == 27

def test_add_maximum_points_for_unicorn_with_princess():
    hand = init_hand(deck, [Card.UNICORN, Card.PRINCESS])
    assert hand.get_total() == 41

def test_add_less_points_when_unicorn_has_no_princess_but_empress():
    hand = init_hand(deck, [Card.UNICORN, Card.EMPRESS])
    assert hand.get_total() == 34

def test_does_nothing_when_magic_wand_and_shield_of_keth_are_together():
    hand = init_hand(deck, [Card.SHIELD_OF_KETH, Card.MAGIC_WAND])
    assert hand.get_total() == 5

def test_adds_points_when_shield_of_keth_is_handled_by_a_leader():
    hand = init_hand(deck, [Card.SHIELD_OF_KETH, Card.PRINCESS])
    assert hand.get_total() == 21

def test_combines_when_king_has_shield_and_sword_of_keth():
    hand = init_hand(deck, [Card.SHIELD_OF_KETH, Card.KING, Card.SWORD_OF_KETH])
    assert hand.get_total() == 99

def test_does_not_get_full_points_from_whirlwind_when_rainstorm_is_missing():
    hand = init_hand(deck, [Card.BLIZZARD, Card.GREAT_FLOOD, Card.WHIRLWIND])
    assert hand.get_total() == 43

def test_gets_whirlwind_bonus_when_rainstorm_and_blizzard_are_together():
    hand = init_hand(deck, [Card.BLIZZARD, Card.RAINSTORM, Card.WHIRLWIND])
    assert hand.get_total() == 91

def test_cancels_swamp_penalty_with_rangers_bonus():
    hand = init_hand(deck, [Card.SWAMP, Card.RANGERS])
    assert hand.get_total() == 23

def test_gets_no_points_from_collector_when_all_cards_have_different_suits():
    hand = init_hand(deck, [Card.COLLECTOR, Card.RANGERS, Card.SWAMP, Card.DRAGON, Card.PRINCESS, Card.FORGE, Card.FOREST])
    assert hand.get_total() == 113

def test_points_from_collector_when_three_cards_have_same_suit():
    hand = init_hand(deck, [Card.COLLECTOR, Card.BEASTMASTER, Card.HYDRA, Card.DRAGON, Card.UNICORN, Card.FORGE, Card.FOREST])
    assert hand.get_total() == 156

def test_gets_points_from_collector_when_four_cards_have_same_suit():
    hand = init_hand(deck, [Card.COLLECTOR, Card.BEASTMASTER, Card.HYDRA, Card.DRAGON, Card.UNICORN, Card.BASILISK, Card.FOREST])
    assert hand.get_total() == 233

def test_gets_points_from_collector_when_five_cards_have_same_suit():
    hand = init_hand(deck, [Card.COLLECTOR, Card.BEASTMASTER, Card.HYDRA, Card.DRAGON, Card.UNICORN, Card.BASILISK, Card.WARHORSE])
    assert hand.get_total() == 267

def test_gets_world_tree_bonus_if_each_active_card_has_a_different_suit():
    hand = init_hand(deck, [Card.COLLECTOR, Card.WORLD_TREE])
    assert hand.get_total() == 59

def test_gets_no_points_from_world_tree_if_at_least_two_active_cards_have_same_suit():
    hand = init_hand(deck, [Card.PROTECTION_RUNE, Card.WORLD_TREE])
    assert hand.get_total() == 3

def test_gains_maximum_value_among_various_flood_cards_with_fountain_of_life():
    hand = init_hand(deck, [Card.FOUNTAIN_OF_LIFE, Card.GREAT_FLOOD, Card.PROTECTION_RUNE, Card.WAR_DIRIGIBLE, Card.WORLD_TREE])
    assert hand.get_total() == 93

def test_gains_minimum_points_when_only_three_cards_are_in_run_with_gem_of_order():
    hand = init_hand(deck, [Card.COLLECTOR, Card.GEM_OF_ORDER, Card.QUEEN])
    assert hand.get_total() == 28

def test_can_change_suit_card_with_book_of_changes():
    hand = init_hand(deck, [Card.DRAGON, Card.QUEEN])
    hand.add_card(Card.BOOK_OF_CHANGES, { 'card': Card.QUEEN, 'suit': Suit.WIZARD})
    assert hand.get_total() == 39

def test_gets_full_points_when_candle_has_bell_tower_and_book_of_changes_and_any_wizard():
    hand = init_hand(deck, [Card.BEASTMASTER, Card.BELL_TOWER, Card.CANDLE])
    hand.add_card(Card.BOOK_OF_CHANGES, { 'card': Card.CANDLE, 'suit': Suit.WEAPON})
    assert hand.get_total() == 137

def test_does_not_get_candle_bonus_without_a_wizard():
    hand = init_hand(deck, [Card.SWORD_OF_KETH, Card.BELL_TOWER, Card.CANDLE])
    hand.add_card(Card.BOOK_OF_CHANGES, { 'card': Card.CANDLE, 'suit': Suit.WEAPON})
    assert hand.get_total() == 20

def test_gets_no_points_from_world_tree_if_at_least_two_active_cards_have_same_suit_cause_of_book_of_changes():
    hand = init_hand(deck, [Card.COLLECTOR, Card.WORLD_TREE])
    hand.add_card(Card.BOOK_OF_CHANGES, { 'card': Card.COLLECTOR, 'suit': Suit.WEAPON})
    assert hand.get_total() == 12

def test_cannot_choose_any_card_with_fountain_of_life_and_only_artifacts():
    hand = init_hand(deck, [Card.FOUNTAIN_OF_LIFE, Card.GEM_OF_ORDER, Card.PROTECTION_RUNE, Card.SHIELD_OF_KETH, Card.WORLD_TREE])
    hand.add_card(Card.BOOK_OF_CHANGES, { 'card': Card.PROTECTION_RUNE, 'suit': Suit.WILD})
    assert hand.get_total() == 76

def test_add_a_last_card_with_necromancer():
    hand = init_hand(deck, [Card.DRAGON, Card.EARTH_ELEMENTAL])
    hand.add_card(Card.NECROMANCER, { 'card': Card.UNICORN })
    assert hand.get_total() == 46

def test_can_have_two_times_the_same_card_because_of_the_doppelganger():
    hand = init_hand(deck, [Card.DRAGON, Card.WARLOCK_LORD])
    hand.add_card(Card.DOPPELGANGER, { 'card': Card.DRAGON })
    assert hand.get_total() == 85

def test_can_get_penalties_twice_if_doppelganger_is_misused():
    hand = init_hand(deck, [Card.DRAGON, Card.CANDLE])
    hand.add_card(Card.DOPPELGANGER, { 'card': Card.DRAGON })
    assert hand.get_total() == -18

def test_can_get_bonuses_from_shapeshifter():
    hand = init_hand(deck, [Card.SWORD_OF_KETH, Card.PRINCESS])
    hand.add_card(Card.SHAPESHIFTER, { 'card': CardClass.from_conf(Card.SHIELD_OF_KETH, deck[Card.SHIELD_OF_KETH]) })
    assert hand.get_total() == 49

def test_elven_long_bow_fits_well_with_elven_archers():
    hand = init_hand(deck, [Card.ELVEN_LONGBOW, Card.ELVEN_ARCHERS])
    assert hand.get_total() == 48

def test_princess_cannot_handle_elven_long_bow():
    hand = init_hand(deck, [Card.ELVEN_LONGBOW, Card.PRINCESS])
    assert hand.get_total() == 5
