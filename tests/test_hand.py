from typing import Any

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

def test_gets_full_points_when_candle_has_bell_tower_and_book_of_changes_and_any_wizard():
    hand = init_hand(deck, [Card.BEASTMASTER, Card.BELL_TOWER, Card.CANDLE])
    hand.add_card(Card.BOOK_OF_CHANGES, { 'card': Card.CANDLE, 'suit': Suit.WEAPON})
    assert hand.get_total() == 137

def test_does_not_get_candle_bonus_without_a_wizard():
    hand = init_hand(deck, [Card.SWORD_OF_KETH, Card.BELL_TOWER, Card.CANDLE])
    hand.add_card(Card.BOOK_OF_CHANGES, { 'card': Card.CANDLE, 'suit': Suit.WEAPON})
    assert hand.get_total() == 20

def test_does_not_get_full_points_from_whirlwind_when_rainstorm_is_missing():
    hand = init_hand(deck, [Card.BLIZZARD, Card.GREAT_FLOOD, Card.WHIRLWIND])
    assert hand.get_total() == 43

def test_gets_whirlwind_bonus_when_rainstorm_and_blizzard_are_together():
    hand = init_hand(deck, [Card.BLIZZARD, Card.RAINSTORM, Card.WHIRLWIND])
    assert hand.get_total() == 91

def test_cancels_swamp_penalty_with_rangers_bonus():
    hand = init_hand(deck, [Card.SWAMP, Card.RANGERS])
    assert hand.get_total() == 23



"""



it('cancels swamp penalty with rangers bonus', function (): void {
    hand = init_hand(this->deck, [
        Glossary::CARD_SWAMP,
        Glossary::CARD_RANGERS,
    ])
    expect(hand->getTotal())->toBe(23)
})

it('gets no points from collector when all cards have different suits', function (): void {
    hand = init_hand(this->deck, [
        Glossary::CARD_COLLECTOR,
        Glossary::CARD_RANGERS,
        Glossary::CARD_SWAMP,
        Glossary::CARD_DRAGON,
        Glossary::CARD_PRINCESS,
        Glossary::CARD_FORGE,
        Glossary::CARD_FOREST,
    ])
    expect(hand->getTotal())->toBe(113)
})

it('gets points from collector when three cards have same suit', function (): void {
    hand = init_hand(this->deck, [
        Glossary::CARD_COLLECTOR,
        Glossary::CARD_BEASTMASTER,
        Glossary::CARD_HYDRA,
        Glossary::CARD_DRAGON,
        Glossary::CARD_UNICORN,
        Glossary::CARD_FORGE,
        Glossary::CARD_FOREST,
    ])
    expect(hand->getTotal())->toBe(156)
})

it('gets points from collector when four cards have same suit', function (): void {
    hand = init_hand(this->deck, [
        Glossary::CARD_BASILISK,
        Glossary::CARD_BEASTMASTER,
        Glossary::CARD_COLLECTOR,
        Glossary::CARD_DRAGON,
        Glossary::CARD_FOREST,
        Glossary::CARD_HYDRA,
        Glossary::CARD_UNICORN,
    ])
    expect(hand->getTotal())->toBe(233)
})

it('gets maximum points from collector when five cards have same suit', function (): void {
    hand = init_hand(this->deck, [
        Glossary::CARD_BASILISK,
        Glossary::CARD_BEASTMASTER,
        Glossary::CARD_COLLECTOR,
        Glossary::CARD_DRAGON,
        Glossary::CARD_HYDRA,
        Glossary::CARD_UNICORN,
        Glossary::CARD_WARHORSE,
    ])
    expect(hand->getTotal())->toBe(267)
})

it('gets world tree bonus if each active card has a different suit', function (): void {
    hand = init_hand(this->deck, [
        Glossary::CARD_COLLECTOR,
        Glossary::CARD_WORLD_TREE,
    ])
    expect(hand->getTotal())->toBe(59)
})

it('gets no points from world tree if at least two active card have same suit', function (): void {
    hand = init_hand(this->deck, [
        Glossary::CARD_COLLECTOR,
        Glossary::CARD_WORLD_TREE,
    ])
    hand->addCard(Glossary::CARD_BOOK_OF_CHANGES, [
        'card' => Glossary::CARD_COLLECTOR,
        'suit' => Glossary::SUIT_WEAPON,
    ])
    expect(hand->getTotal())->toBe(12)
})

it('cannot choose any card with fountain of life and only artifacts', function (): void {
    hand = init_hand(this->deck, [
        Glossary::CARD_FOUNTAIN_OF_LIFE,
        Glossary::CARD_GEM_OF_ORDER,
        Glossary::CARD_PROTECTION_RUNE,
        Glossary::CARD_SHIELD_OF_KETH,
        Glossary::CARD_WORLD_TREE,
    ])
    hand->addCard(Glossary::CARD_BOOK_OF_CHANGES, [
        'card' => Glossary::CARD_PROTECTION_RUNE,
        'suit' => Glossary::SUIT_WILD,
    ])
    expect(hand->getTotal())->toBe(76)
})

it('gains maximum value among various flood cards with fountain of life', function (): void {
    hand = init_hand(this->deck, [
        Glossary::CARD_FOUNTAIN_OF_LIFE,
        Glossary::CARD_GREAT_FLOOD,
        Glossary::CARD_PROTECTION_RUNE,
        Glossary::CARD_WAR_DIRIGIBLE,
        Glossary::CARD_WORLD_TREE,
    ])
    expect(hand->getTotal())->toBe(93)
})

it('gains minimum points when only three cards are in run with gem of order', function (): void {
    hand = init_hand(this->deck, [
        Glossary::CARD_COLLECTOR,
        Glossary::CARD_GEM_OF_ORDER,
        Glossary::CARD_QUEEN,
    ])
    expect(hand->getTotal())->toBe(28)
})

it('can change suit card with book of changes', function (): void {
    hand = init_hand(this->deck, [
        Glossary::CARD_DRAGON,
        Glossary::CARD_QUEEN,
    ])
    hand->addCard(Glossary::CARD_BOOK_OF_CHANGES, [
        'card' => Glossary::CARD_QUEEN,
        'suit' => Glossary::SUIT_WIZARD,
    ])
    expect(hand->getTotal())->toBe(39)
})

it('can add a last card with necromancer', function (): void {
    hand = init_hand(this->deck, [
        Glossary::CARD_DRAGON,
        Glossary::CARD_EARTH_ELEMENTAL,
    ])
    hand->addCard(Glossary::CARD_NECROMANCER, [
        'card' => Glossary::CARD_UNICORN
    ])
    expect(hand->getTotal())->toBe(46)
})

it('can have two times the same card because of the doppelganger', function (): void {
    hand = init_hand(this->deck, [
        Glossary::CARD_DRAGON,
        Glossary::CARD_WARLOCK_LORD,
    ])
    hand->addCard(Glossary::CARD_DOPPELGANGER, [
        'card' => Glossary::CARD_DRAGON
    ])
    expect(hand->getTotal())->toBe(85)
})

it('can get penalties twice if doppelganger is misused', function (): void {
    hand = init_hand(this->deck, [
        Glossary::CARD_DRAGON,
        Glossary::CARD_CANDLE,
    ])
    hand->addCard(Glossary::CARD_DOPPELGANGER, [
        'card' => Glossary::CARD_DRAGON
    ])
    expect(hand->getTotal())->toBe(-18)
})

it('can get bonuses from shapeshifter', function (): void {
    hand = init_hand(this->deck, [
        Glossary::CARD_SWORD_OF_KETH,
        Glossary::CARD_PRINCESS,
    ])
    hand->addCard(Glossary::CARD_SHAPESHIFTER, [
        'card' => Card::fromDeck(Glossary::CARD_SHIELD_OF_KETH, this->deck),
    ])
    expect(hand->getTotal())->toBe(49)
})


"""
