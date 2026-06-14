from fantasy_realms.glossary import Action, Card, Suit

deck = {
      Card.AIR_ELEMENTAL: {
            'suit' : Suit.WEATHER,
            'base_strength': 4,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 15,
                'suits': [
                    Suit.WEATHER
                ]
            }
      },
       Card.BASILISK: {
            'suit': Suit.BEAST,
            'base_strength': 35,
            'penalty': {
                'action': Action.BLANKS,
                'targets': {
                    'suits': [
                        Suit.ARMY,
                        Suit.LEADER,
                        Suit.BEAST
                    ]
                }
            }
        },
        Card.BEASTMASTER: {
            'suit': Suit.WIZARD,
            'base_strength': 9,
            'bonus': {
                'and': [
                    {
                        'action': Action.FOR_EACH,
                        'value': 9,
                        'suits': [
                            Suit.BEAST
                        ]
                    },
                    {
                        'action': Action.CLEARS_PENALTY,
                        'suits': [
                            Suit.BEAST
                        ]
                    }
                ]
            }
        },
        Card.BELL_TOWER: {
            'suit': Suit.LAND,
            'base_strength': 8,
            'bonus': {
                'action': Action.WITH_ANY_ONE_SUIT,
                'value': 15,
                'suits': [
                    Suit.WIZARD
                ]
            },
        },
        Card.BLIZZARD: {
            'suit': Suit.WEATHER,
            'base_strength': 30,
            'penalty': {
                'and': [
                    {
                        'action': Action.BLANKS,
                        'targets': {
                            'suits': [
                                Suit.FLOOD
                            ]
                        }
                    },
                    {
                        'action': Action.FOR_EACH,
                        'value': 5,
                        'suits': [
                            Suit.ARMY,
                            Suit.BEAST,
                            Suit.FLAME,
                            Suit.LEADER,
                        ]
                    }
                ]
            }
        },
        Card.BOOK_OF_CHANGES: {
            'suit': Suit.ARTIFACT,
            'base_strength': 3,
            'bonus': {
                'action': Action.CHANGE_SUIT
            }
        },
        Card.CANDLE: {
            'suit': Suit.FLAME,
            'base_strength': 2,
            'bonus': {
                'action': Action.WITH_BOTH_CARDS,
                'value': 100,
                'cards': [
                    Card.BELL_TOWER,
                    Card.BOOK_OF_CHANGES,
                ],
                'suits': [
                    Suit.WIZARD
                ]
            }
        },
        Card.CELESTIAL_KNIGHTS: {
            'suit': Suit.ARMY,
            'base_strength': 20,
            'penalty': {
                'action': Action.UNLESS_AT_LEAST,
                'value': 8,
                'suits': [
                    Suit.LEADER
                ]
            },
        },
        Card.COLLECTOR: {
            'suit': Suit.WIZARD,
            'base_strength': 7,
            'bonus': {
                'or': [
                    {
                        'action': Action.DIFFERENT_CARDS_IN_SAME_SUIT,
                        'value': 100,
                        'cards': 5
                    },
                    {
                        'action': Action.DIFFERENT_CARDS_IN_SAME_SUIT,
                        'value': 40,
                        'cards': 4
                    },
                    {
                        'action': Action.DIFFERENT_CARDS_IN_SAME_SUIT,
                        'value': 10,
                        'cards': 3
                    },
                ]
            }
        },
        Card.DOPPELGANGER: {
            'suit': Suit.WILD,
            'base_strength': 0,
            'bonus': {
                'action': Action.DUPLICATE
            }
        },
        Card.DRAGON: {
            'suit': Suit.BEAST,
            'base_strength': 30,
            'penalty': {
                'action': Action.UNLESS_AT_LEAST,
                'value': 40,
                'suits': [
                    Suit.WIZARD
                ]
            },
        },
        Card.DWARVISH_INFANTRY: {
            'suit': Suit.ARMY,
            'base_strength': 15,
            'penalty': {
                'action': Action.FOR_EACH,
                'value': 2,
                'suits': [
                    Suit.ARMY
                ]
            },
        },
        Card.EARTH_ELEMENTAL: {
            'suit': Suit.LAND,
            'base_strength': 4,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 15,
                'suits': [
                    Suit.LAND
                ]
            },
        },
        Card.ELEMENTAL_ENCHANTRESS: {
            'suit': Suit.WIZARD,
            'base_strength': 5,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 5,
                'suits': [
                    Suit.FLAME,
                    Suit.FLOOD,
                    Suit.LAND,
                    Suit.WEATHER,
                ]
            },
        },
        Card.ELVEN_ARCHERS: {
            'suit': Suit.ARMY,
            'base_strength': 10,
            'bonus': {
                'action': Action.IF_NO,
                'value': 5,
                'suits': [
                    Suit.WEATHER
                ]
            }
        },
        Card.ELVEN_LONGBOW: {
            'suit': Suit.WEAPON,
            'base_strength': 3,
            'bonus': {
                'action': Action.WITH_ANY_ONE_CARD,
                'value': 30,
                'cards': [
                    Card.ELVEN_ARCHERS,
                    Card.WARLORD,
                    Card.BEASTMASTER
                ]
            },
        },
        Card.EMPRESS: {
            'suit': Suit.LEADER,
            'base_strength': 10,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 10,
                'suits': [
                    Suit.ARMY
                ]
            },
            'penalty': {
                'action': Action.FOR_EACH,
                'value': 5,
                'suits': [
                    Suit.LEADER
                ]
            },
        },
        Card.FIRE_ELEMENTAL: {
            'suit': Suit.FLAME,
            'base_strength': 4,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 15,
                'suits': [
                    Suit.FLAME
                ]
            },
        },
        Card.FOREST: {
            'suit': Suit.LAND,
            'base_strength': 7,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 12,
                'suits': [
                    Suit.BEAST
                ],
                'cards': [
                    Card.ELVEN_ARCHERS
                ]
            }
        },
        Card.FORGE: {
            'suit': Suit.FLAME,
            'base_strength': 9,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 9,
                'suits': [
                    Suit.WEAPON,
                    Suit.ARTIFACT
                ]
            },
        },
        Card.FOUNTAIN_OF_LIFE: {
            'suit': Suit.FLOOD,
            'base_strength': 1,
            'bonus': {
                'action': Action.ADD_BASE_STRENGTH_AMONG,
                'suits': [
                    Suit.FLAME,
                    Suit.FLOOD,
                    Suit.LAND,
                    Suit.WEAPON,
                    Suit.WEATHER
                ]
            }
        },
        Card.GEM_OF_ORDER: {
            'suit': Suit.ARTIFACT,
            'base_strength': 5,
            'bonus': {
                'or': [
                    {
                        'action': Action.CARD_RUN,
                        'value': 150,
                        'cards': 7
                    },
                    {
                        'action': Action.CARD_RUN,
                        'value': 100,
                        'cards': 6
                    },
                    {
                        'action': Action.CARD_RUN,
                        'value': 60,
                        'cards': 5
                    },
                    {
                        'action': Action.CARD_RUN,
                        'value': 30,
                        'cards': 4
                    },
                    {
                        'action': Action.CARD_RUN,
                        'value': 10,
                        'cards': 3
                    },
                ]
            }
        },
        Card.GREAT_FLOOD: {
            'suit': Suit.FLOOD,
            'base_strength': 32,
            'penalty': {
                'action': Action.BLANKS,
                'targets': {
                    'suits': [
                        Suit.ARMY,
                        Suit.LAND,
                        Suit.FLAME
                    ],
                },
                'excludes': {
                    'cards': [
                        Card.MOUNTAIN,
                       Card.LIGHTNING
                    ]
                }
            }
        },
        Card.HYDRA: {
            'suit': Suit.BEAST,
            'base_strength': 12,
            'bonus': {
                'action': Action.WITH_CARD,
                'value': 28,
                'cards': [

                             Card.SWAMP
                ]
            },
        },
        Card.KING: {
            'suit': Suit.LEADER,
            'base_strength': 8,
            'bonus': {
                'or': [
                    {
                        'action': Action.FOR_EACH,
                        'value': 20,
                        'suits': [
                            Suit.ARMY
                        ],
                        'cards': [
                            Card.QUEEN
                        ]
                    },
                    {
                        'action': Action.FOR_EACH,
                        'value': 5,
                        'suits': [
                            Suit.ARMY
                        ]
                    }
                ]
            }
        },
        Card.ISLAND: {
            'suit': Suit.FLOOD,
            'base_strength': 14,
            'bonus': {
                'action': Action.CLEARS_PENALTY,
                'suits': [
                    Suit.FLOOD,
                    Suit.FLAME
                ]
            }
        },
        Card.LIGHT_CALVARY: {
            'suit': Suit.ARMY,
            'base_strength': 17,
            'penalty': {
                'action': Action.FOR_EACH,
                'value': 2,
                'suits': [
                    Suit.LAND
                ]
            },
        },
        Card.LIGHTNING: {
            'suit': Suit.FLAME,
            'base_strength': 11,
            'bonus': {
                'action': Action.WITH_CARD,
                'value': 30,
                'cards': [
                    Card.RAINSTORM
                ]
            },
        },
        Card.MAGIC_WAND: {
            'suit': Suit.WEAPON,
            'base_strength': 1,
            'bonus': {
                'action': Action.WITH_ANY_ONE_SUIT,
                'value': 25,
                'suits': [
                    Suit.WIZARD
                ]
            },
        },
        Card.MIRAGE: {
            'suit': Suit.WILD,
            'base_strength': 0,
            'bonus': {
                'action': Action.TAKE_ON_NAME_AND_SUIT,
                'suits': [
                    Suit.ARMY,
                    Suit.FLAME,
                    Suit.FLOOD,
                    Suit.LAND,
                    Suit.WEATHER,
                ]
            }
        },
        Card.MOUNTAIN: {
            'suit': Suit.LAND,
            'base_strength': 9,
            'bonus': {
                'and': [
                    {
                        'action': Action.WITH_BOTH_CARDS,
                        'value': 50,
                        'cards': [
                            Card.SMOKE,
                            Card.WILDFIRE
                        ]
                    },
                    {
                        'action': Action.CLEARS_PENALTY,
                        'suits': [
                            Suit.FLOOD
                        ]
                    }
                ]
            }
        },
        Card.NECROMANCER: {
            'suit': Suit.WIZARD,
            'base_strength': 3,
            'bonus': {
                'action': Action.TAKE_ONE_MORE_CARD_AT_THE_END,
                'suits': [
                    Suit.ARMY,
                    Suit.BEAST,
                    Suit.LEADER,
                    Suit.WIZARD,
                ]
            }
        },
        Card.PRINCESS: {
            'suit': Suit.LEADER,
            'base_strength': 2,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 8,
                'suits': [
                    Suit.ARMY,
                    Suit.LEADER,
                    Suit.WIZARD,
                ]
            },
        },
        Card.PROTECTION_RUNE: {
            'suit': Suit.ARTIFACT,
            'base_strength': 1,
            'bonus': {
                'action': Action.CLEARS_PENALTY,
                'suits': [
                    Suit.ARMY,
                    Suit.ARTIFACT,
                    Suit.BEAST,
                    Suit.FLAME,
                    Suit.FLOOD,
                    Suit.LAND,
                    Suit.LEADER,
                    Suit.WEAPON,
                    Suit.WEATHER,
                    Suit.WILD,
                    Suit.WIZARD,
                ]
            },
        },
        Card.QUEEN: {
            'suit': Suit.LEADER,
            'base_strength': 6,
            'bonus': {
                'or': [
                    {
                        'action': Action.FOR_EACH,
                        'value': 20,
                        'suits': [
                            Suit.ARMY
                ],
                        'cards': [
                            Card.KING
                ]
                    },
                    {
                        'action': Action.FOR_EACH,
                        'value': 5,
                        'suits': [
                            Suit.ARMY
                        ]
                    },
                ]
            }
        },
        Card.RAINSTORM: {
            'suit': Suit.WEATHER,
            'base_strength': 8,
            'bonus': {
                'action': Action.WITH_ANY_ONE_SUIT,
                'value': 10,
                'suits': [
                    Suit.FLOOD
                ]
            },
            'penalty': {
                'action': Action.BLANKS,
                'targets': {
                    'suits': [
                        Suit.FLAME
                    ],
                },
                'excludes': {
                    'cards': [
                        Card.LIGHTNING
                    ]
                }
            }
        },
        Card.RANGERS: {
            'suit': Suit.ARMY,
            'base_strength': 5,
            'bonus': {
                'and': [
                    {
                        'action': Action.FOR_EACH,
                        'value': 10,
                        'suits': [
                            Suit.LAND
                        ]
                    },
                    {
                        'action': Action.CLEARS_WORD_FROM_PENALTY,
                        'word': Suit.ARMY
                    }
                ]
            }
        },
        Card.SHAPESHIFTER: {
            'suit': Suit.WILD,
            'base_strength': 0,
            'bonus': {
                'action': Action.TAKE_ON_NAME_AND_SUIT,
                'suits': [
                    Suit.ARTIFACT,
                    Suit.BEAST,
                    Suit.LEADER,
                    Suit.WEAPON,
                    Suit.WIZARD,
                ]
            },
        },
        Card.SHIELD_OF_KETH: {
            'suit': Suit.ARTIFACT,
            'base_strength': 4,
            'bonus': {
                'or': [
                    {
                        'action': Action.WITH_BOTH_CARDS,
                        'value': 40,
                        'suits': [
                            Suit.LEADER
                        ],
                        'cards': [
                            Card.SWORD_OF_KETH
                        ]
                    },
                    {
                        'action': Action.WITH_ANY_ONE_SUIT,
                        'value': 15,
                        'suits': [
                            Suit.LEADER
                        ],
                    },
                ]
            }
        },
        Card.SMOKE: {
            'suit': Suit.WEATHER,
            'base_strength': 27,
            'penalty': {
                'action': Action.BLANKED_UNLESS,
                'suits': [
                    Suit.FLAME
                ]
            },
        },
        Card.SWAMP: {
            'suit': Suit.FLOOD,
            'base_strength': 18,
            'penalty': {
                'action': Action.FOR_EACH,
                'value': 3,
                'suits': [
                    Suit.ARMY,
                    Suit.FLAME
                ]
            },
        },
        Card.SWORD_OF_KETH: {
            'suit': Suit.WEAPON,
            'base_strength': 7,
            'bonus': {
                'or': [
                    {
                        'action': Action.WITH_BOTH_CARDS,
                        'value': 40,
                        'suits': [
                            Suit.LEADER
                        ],
                        'cards': [
                            Card.SHIELD_OF_KETH
                        ]
                    },
                    {
                        'action': Action.WITH_ANY_ONE_SUIT,
                        'value': 10,
                        'suits': [
                            Suit.LEADER
                        ]
                    },
                ]
            }
        },
        Card.UNDERGROUND_CAVERNS: {
            'suit': Suit.LAND,
            'base_strength': 6,
            'bonus': {
                'and': [
                    {
                        'action': Action.WITH_CARD,
                        'value': 25,
                        'cards': [
                            Card.DRAGON,
                            Card.DWARVISH_INFANTRY
                        ]
                    },
                    {
                        'action': Action.CLEARS_PENALTY,
                        'suits': [
                            Suit.WEATHER
                        ]
                    }
                ]
            }
        },
        Card.UNICORN: {
            'suit': Suit.BEAST,
            'base_strength': 9,
            'bonus': {
                'or': [
                    {
                        'action': Action.WITH_CARD,
                        'value': 30,
                        'cards': [
                            Card.PRINCESS
                        ]
                    },
                    {
                        'action': Action.WITH_CARD,
                        'value': 15,
                        'cards': [
                            Card.ELEMENTAL_ENCHANTRESS,
                            Card.EMPRESS,
                            Card.QUEEN,
                        ]
                    }
                ]
            }
        },
        Card.WAR_DIRIGIBLE: {
            'suit': Suit.WEAPON,
            'base_strength': 25,
            'penalty': [
                {
                    'action': Action.BLANKED_UNLESS,
                    'suits': [
                        Suit.ARMY
                    ]
                },
                {
                    'action': Action.BLANKED_WITH,
                    'suits': [
                        Suit.WEATHER
                    ]
                },
            ]
        },
        Card.WARHORSE: {
            'suit': Suit.BEAST,
            'base_strength': 6,
            'bonus': {
                'action': Action.WITH_ANY_ONE_SUIT,
                'value': 14,
                'suits': [
                    Suit.LEADER,
                    Suit.WIZARD
                ]
            }
        },
        Card.WARLOCK_LORD: {
            'suit': Suit.WIZARD,
            'base_strength': 25,
            'penalty': {
                'action': Action.FOR_EACH,
                'value': 10,
                'suits': [
                    Suit.LEADER,
                    Suit.WIZARD
                ]
            },
        },
        Card.WARSHIP: {
            'suit': Suit.WEAPON,
            'base_strength': 23,
            'bonus': {
                'action': Action.CLEARS_WORD_FROM_PENALTY,
                'word': Suit.ARMY,
                'suits': [
                    Suit.FLOOD
                ]
            },
            'penalty': {
                'action': Action.BLANKED_UNLESS,
                'suits': [
                    Suit.FLOOD
                ],
            }
        },
        Card.WATER_ELEMENTAL: {
            'suit': Suit.FLOOD,
            'base_strength': 4,
            'bonus': {
                'action': Action.FOR_EACH,
                'value': 15,
                'suits': [
                    Suit.FLOOD
                ]
            }
        },
        Card.WHIRLWIND: {
            'suit': Suit.WEATHER,
            'base_strength': 13,
            'bonus': {
                'action': Action.WITH_CARD_AND_EITHER,
                'value': 40,
                'cards': [
                    Card.RAINSTORM
                ],
                'either': [
                    Card.BLIZZARD,
                    Card.GREAT_FLOOD
                ]
            }
        },
        Card.WILDFIRE: {
            'suit': Suit.FLAME,
            'base_strength': 40,
            'penalty': {
                'action': Action.BLANKS,
                'targets': {},
                'excludes': {
                    'suits': [
                        Suit.ARTIFACT,
                        Suit.FLAME,
                        Suit.WEAPON,
                        Suit.WEATHER,
                        Suit.WIZARD,
                    ],
                    'cards': [
                        Card.GREAT_FLOOD,
                        Card.DRAGON,
                        Card.ISLAND,
                        Card.MOUNTAIN,
                        Card.UNICORN,
                    ]
                }
            }
        },
        Card.WORLD_TREE: {
            'suit': Suit.ARTIFACT,
            'base_strength': 2,
            'bonus': {
                'action': Action.EACH_ACTIVE_CARD_IS_FROM_DIFFERENT_SUIT,
                'value': 50
            },
        },
    }
