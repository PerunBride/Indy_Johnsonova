[
    {
        "name": "dungeon",
        "description": "Tmavá a stuchnutá miestnosť. Každé okno je zvonku zabarikádované a do miestnosti preniká len úzky prameň svetla. Masívne drevené dvere sú jediným východom z miestnosti.",
        "items": [
            {
                "name": "kanister",
                "description": "Kanister plný benzínu.",
                "features": [
                    1,
                    2
                ]
            },
            {
                "name": "hasiaci pristroj",
                "description": "Ručný hasiaci prístroj plný. Značka - červený.",
                "features": [
                    1,
                    2
                ]
            },
            {
                "name": "zapalky",
                "description": "Krabička zápaliek vyrobená ešte v Československu. Kvalitka.",
                "features": [
                    1,
                    2
                ],
                "total": 3
            },
            {
                "name": "dvere",
                "description": "Veľké masívne drevené dvere. Zamknuté.",
                "features": [],
                "state": "zamknute"
            }
        ],
        "exits": {
            "west": null,
            "east": null,
            "south": null,
            "north": null
        }
    },
    {
        "name": "garden",
        "description": "Pomerne zarastené hriadky niečoho, čo by sa dalo voľne nazvať záhradkou. Darí sa tu skorocelu a inej burine.",
        "items": [],
        "exits": {
            "east": "dungeon",
            "west": null,
            "north": null,
            "south": null
        }
    }
]
