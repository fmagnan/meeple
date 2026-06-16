from typing import Any

from fantasy_realms.card import Card
from fantasy_realms.deck import deck
from fantasy_realms.glossary import Name, Suit
from fantasy_realms.hand import Hand


def init_hand(deck: dict[str, Any], names: list[Name]) -> Hand:
    hand :Hand = Hand(deck)
    for name in names:
        hand.add_card(name)
    return hand

def test_it_counts_cards_in_hand():
    hand = init_hand(deck, [Name.DRAGON, Name.BELL_TOWER, Name.MAGIC_WAND])
    assert hand.count_cards() == 3

def test_applies_penalty_when_dragon_has_not_a_wizard():
    hand = init_hand(deck, [Name.DRAGON])
    assert hand.get_total() == -10

def test_neutralizes_penalty_when_dragon_is_with_a_a_wizard():
    hand = init_hand(deck, [Name.DRAGON, Name.ELEMENTAL_ENCHANTRESS])
    assert hand.get_total() == 35

def test_gets_points_for_princess_with_elemental_enchantress():
    hand = init_hand(deck, [Name.PRINCESS, Name.ELEMENTAL_ENCHANTRESS])
    assert hand.get_total() == 15

def test_cancels_lightning_points_from_princess():
    hand = init_hand(deck, [Name.PRINCESS, Name.LIGHTNING])
    assert hand.get_total() == 13

def test_gets_lightning_points_with_rainstorm():
    hand = init_hand(deck, [Name.RAINSTORM, Name.LIGHTNING])
    assert hand.get_total() == 49

def test_gets_points_from_princess_and_loses_points_from_empress_when_they_are_together():
    hand = init_hand(deck, [Name.PRINCESS, Name.EMPRESS])
    assert hand.get_total() == 15

def test_adds_points_from_each_flood_for_rainstorm():
    hand = init_hand(deck, [Name.RAINSTORM, Name.SWAMP, Name.WATER_ELEMENTAL])
    assert hand.get_total() == 55

def test_does_nothing_when_island_is_with_dragon():
    hand = init_hand(deck, [Name.DRAGON, Name.ISLAND])
    assert hand.get_total() == 4

def test_clears_penalty_from_swamp_with_island():
    hand = init_hand(deck, [Name.SWAMP, Name.ISLAND, Name.DWARVISH_INFANTRY])
    assert hand.get_total() == 47

def test_adds_points_to_elven_archers_when_there_is_no_weather():
    hand = init_hand(deck, [Name.ELVEN_ARCHERS, Name.ISLAND])
    assert hand.get_total() == 29

def test_cancels_elven_archers_bonus_with_air_elemental():
    hand = init_hand(deck, [Name.ELVEN_ARCHERS, Name.AIR_ELEMENTAL])
    assert hand.get_total() == 14

def test_blanks_fire_elemental_with_rainstorm():
    hand = init_hand(deck, [Name.RAINSTORM, Name.FIRE_ELEMENTAL])
    assert hand.get_total() == 8

def test_blanks_hydra_with_wildfire():
    hand = init_hand(deck, [Name.WILDFIRE, Name.HYDRA])
    assert hand.get_total() == 40

def test_do_not_blank_dragon_with_wildfire():
    hand = init_hand(deck, [Name.WILDFIRE, Name.DRAGON])
    assert hand.get_total() == 30

def test_blanks_smoke_when_there_is_no_flame():
    hand = init_hand(deck, [Name.SMOKE, Name.AIR_ELEMENTAL])
    assert hand.get_total() == 4

def test_counts_smoke_with_fire_elemental():
    hand = init_hand(deck, [Name.SMOKE, Name.FIRE_ELEMENTAL])
    assert hand.get_total() == 31

def test_does_nothing_when_dragon_and_bell_tower_are_together():
    hand = init_hand(deck, [Name.DRAGON, Name.BELL_TOWER])
    assert hand.get_total() == -2

def test_does_nothing_when_celestial_knights_and_beast_master_are_together():
    hand = init_hand(deck, [Name.CELESTIAL_KNIGHTS, Name.BEASTMASTER])
    assert hand.get_total() == 21

def test_add_points_when_unicorn_meets_beast_master():
    hand = init_hand(deck, [Name.UNICORN, Name.BEASTMASTER])
    assert hand.get_total() == 27

def test_add_maximum_points_for_unicorn_with_princess():
    hand = init_hand(deck, [Name.UNICORN, Name.PRINCESS])
    assert hand.get_total() == 41

def test_add_less_points_when_unicorn_has_no_princess_but_empress():
    hand = init_hand(deck, [Name.UNICORN, Name.EMPRESS])
    assert hand.get_total() == 34

def test_does_nothing_when_magic_wand_and_shield_of_keth_are_together():
    hand = init_hand(deck, [Name.SHIELD_OF_KETH, Name.MAGIC_WAND])
    assert hand.get_total() == 5

def test_adds_points_when_shield_of_keth_is_handled_by_a_leader():
    hand = init_hand(deck, [Name.SHIELD_OF_KETH, Name.PRINCESS])
    assert hand.get_total() == 21

def test_combines_when_king_has_shield_and_sword_of_keth():
    hand = init_hand(deck, [Name.SHIELD_OF_KETH, Name.KING, Name.SWORD_OF_KETH])
    assert hand.get_total() == 99

def test_does_not_get_full_points_from_whirlwind_when_rainstorm_is_missing():
    hand = init_hand(deck, [Name.BLIZZARD, Name.GREAT_FLOOD, Name.WHIRLWIND])
    assert hand.get_total() == 43

def test_gets_whirlwind_bonus_when_rainstorm_and_blizzard_are_together():
    hand = init_hand(deck, [Name.BLIZZARD, Name.RAINSTORM, Name.WHIRLWIND])
    assert hand.get_total() == 91

def test_cancels_swamp_penalty_with_rangers_bonus():
    hand = init_hand(deck, [Name.SWAMP, Name.RANGERS])
    assert hand.get_total() == 23

def test_gets_no_points_from_collector_when_all_cards_have_different_suits():
    hand = init_hand(deck, [Name.COLLECTOR, Name.RANGERS, Name.SWAMP, Name.DRAGON, Name.PRINCESS, Name.FORGE, Name.FOREST])
    assert hand.get_total() == 113

def test_points_from_collector_when_three_cards_have_same_suit():
    hand = init_hand(deck, [Name.COLLECTOR, Name.BEASTMASTER, Name.HYDRA, Name.DRAGON, Name.UNICORN, Name.FORGE, Name.FOREST])
    assert hand.get_total() == 156

def test_gets_points_from_collector_when_four_cards_have_same_suit():
    hand = init_hand(deck, [Name.COLLECTOR, Name.BEASTMASTER, Name.HYDRA, Name.DRAGON, Name.UNICORN, Name.BASILISK, Name.FOREST])
    assert hand.get_total() == 233

def test_gets_points_from_collector_when_five_cards_have_same_suit():
    hand = init_hand(deck, [Name.COLLECTOR, Name.BEASTMASTER, Name.HYDRA, Name.DRAGON, Name.UNICORN, Name.BASILISK, Name.WARHORSE])
    assert hand.get_total() == 267

def test_gets_world_tree_bonus_if_each_active_card_has_a_different_suit():
    hand = init_hand(deck, [Name.COLLECTOR, Name.WORLD_TREE])
    assert hand.get_total() == 59

def test_gets_no_points_from_world_tree_if_at_least_two_active_cards_have_same_suit():
    hand = init_hand(deck, [Name.PROTECTION_RUNE, Name.WORLD_TREE])
    assert hand.get_total() == 3

def test_gains_maximum_value_among_various_flood_cards_with_fountain_of_life():
    hand = init_hand(deck, [Name.FOUNTAIN_OF_LIFE, Name.GREAT_FLOOD, Name.PROTECTION_RUNE, Name.WAR_DIRIGIBLE, Name.WORLD_TREE])
    assert hand.get_total() == 93

def test_gains_minimum_points_when_only_three_cards_are_in_run_with_gem_of_order():
    hand = init_hand(deck, [Name.COLLECTOR, Name.GEM_OF_ORDER, Name.QUEEN])
    assert hand.get_total() == 28

def test_can_change_suit_card_with_book_of_changes():
    hand = init_hand(deck, [Name.DRAGON, Name.QUEEN])
    hand.add_card(Name.BOOK_OF_CHANGES, { 'card': Name.QUEEN, 'suit': Suit.WIZARD})
    assert hand.get_total() == 39

def test_gets_full_points_when_candle_has_bell_tower_and_book_of_changes_and_any_wizard():
    hand = init_hand(deck, [Name.BEASTMASTER, Name.BELL_TOWER, Name.CANDLE])
    hand.add_card(Name.BOOK_OF_CHANGES, { 'card': Name.CANDLE, 'suit': Suit.WEAPON})
    assert hand.get_total() == 137

def test_does_not_get_candle_bonus_without_a_wizard():
    hand = init_hand(deck, [Name.SWORD_OF_KETH, Name.BELL_TOWER, Name.CANDLE])
    hand.add_card(Name.BOOK_OF_CHANGES, { 'card': Name.CANDLE, 'suit': Suit.WEAPON})
    assert hand.get_total() == 20

def test_gets_no_points_from_world_tree_if_at_least_two_active_cards_have_same_suit_cause_of_book_of_changes():
    hand = init_hand(deck, [Name.COLLECTOR, Name.WORLD_TREE])
    hand.add_card(Name.BOOK_OF_CHANGES, { 'card': Name.COLLECTOR, 'suit': Suit.WEAPON})
    assert hand.get_total() == 12

def test_cannot_choose_any_card_with_fountain_of_life_and_only_artifacts():
    hand = init_hand(deck, [Name.FOUNTAIN_OF_LIFE, Name.GEM_OF_ORDER, Name.PROTECTION_RUNE, Name.SHIELD_OF_KETH, Name.WORLD_TREE])
    hand.add_card(Name.BOOK_OF_CHANGES, { 'card': Name.PROTECTION_RUNE, 'suit': Suit.WILD})
    assert hand.get_total() == 76

def test_add_a_last_card_with_necromancer():
    hand = init_hand(deck, [Name.DRAGON, Name.EARTH_ELEMENTAL])
    hand.add_card(Name.NECROMANCER, { 'card': Name.UNICORN })
    assert hand.get_total() == 46

def test_can_have_two_times_the_same_card_because_of_the_doppelganger():
    hand = init_hand(deck, [Name.DRAGON, Name.WARLOCK_LORD])
    hand.add_card(Name.DOPPELGANGER, { 'card': Name.DRAGON })
    assert hand.get_total() == 85

def test_can_get_penalties_twice_if_doppelganger_is_misused():
    hand = init_hand(deck, [Name.DRAGON, Name.CANDLE])
    hand.add_card(Name.DOPPELGANGER, { 'card': Name.DRAGON })
    assert hand.get_total() == -18

def test_can_get_bonuses_from_shapeshifter():
    hand = init_hand(deck, [Name.SWORD_OF_KETH, Name.PRINCESS])
    hand.add_card(Name.SHAPESHIFTER, { 'card': Name.SHIELD_OF_KETH })
    assert hand.get_total() == 49

def test_elven_long_bow_fits_well_with_elven_archers():
    hand = init_hand(deck, [Name.ELVEN_LONGBOW, Name.ELVEN_ARCHERS])
    assert hand.get_total() == 48

def test_princess_cannot_handle_elven_long_bow():
    hand = init_hand(deck, [Name.ELVEN_LONGBOW, Name.PRINCESS])
    assert hand.get_total() == 5
