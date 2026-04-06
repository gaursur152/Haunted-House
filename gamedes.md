# Haunted House Game Design Document

## Overview
A text-based haunted house game written in Python. The player navigates through rooms, defeats monsters using weapons, and escapes through the final exit.

## Files
- `Room.py` — Inventory, Monster, Room classes
- `Player.py` — Player class
- `Game_func.py` — Game class (room setup, game loop, logic)
- `main.py` — entry point (to be created)
- `gamedes.md` — this file

## Room Layout
- **Living Room** — hub, player starts here, no monster, can always retreat here
- **Graveyard** — Zombie (maze stub for now)
- **Basement** — Ghost
- **Kitchen** — Witch
- **TV Room** — Ghostface
- **Resting Room** — Nosferatu (Vampire)
- **Backyard** — Werewolf
- **Exit** — final room, reaching here ends the game

## Movement Rules
- Player starts in the Living Room
- Moving forward into a room requires the monster in that room to be defeated first
- Player can always retreat to the previous room or Living Room
- Game ends when player passes through the Exit

## Monsters
| Room | Monster | HP | Speed | Attack |
|---|---|---|---|---|
| Graveyard | Zombie | never dies | 1 | 5 |
| Basement | Ghost | 150 | 9 | 10 |
| Kitchen | Witch | 75 | 3 | 10 |
| TV Room | Ghostface | 100 | 5 | 20 |
| Resting Room | Nosferatu | 200 | 8 | 25 |
| Backyard | Werewolf | 100 | 9 | 30 |

- Zombie cannot be killed — player must navigate a maze to escape the Graveyard (stubbed for baseline)
- All other monsters can be killed with the right weapons

## Weapons
| Weapon | Works On | Bonus Against |
|---|---|---|
| Garlic | Nosferatu only | — |
| Silver Sword | All killable monsters | Werewolf (extra damage) |
| Fire | All killable monsters | Witch, Ghost (extra damage) |
| Silver Bullet Gun | All killable monsters | Ghostface (extra damage) |

- "All killable" = Ghost, Witch, Ghostface, Nosferatu, Werewolf
- Bonus = extra damage (not instant kill)
- Weapons are randomly placed in rooms at game start

## Player
- Starts with 100 health
- Has an inventory
- Takes damage from monsters
- Can pick up weapons from rooms
- Can move between rooms

## TODO
- [done ] Call `__create_player__` in `__init__` in `Game_func.py`
- [done ] Fix trailing comma on `living_room` line 8 in `Game_func.py`
- [done] `move` method in `Game` — takes a direction, looks up next room via `current_room.exits[direction]`, allows forward only if monster is None or defeated, retreat always allowed to Living Room or previous room
- [done] `end_condition` — game ends when player reaches Exit
- [done] Game loop — text input/output loop (ask player for direction each turn, print room name and exits)
- [done ] `main.py` — entry point to start the game
- [done ] Zombie stub — placeholder message when player enters Graveyard
- [done] `__move__` edge case — handle retreat when `visited_rooms` is empty (first move)
- [done] create a method that just outputs a list of phrases saying they missed the monster
- [done] Fix exits display — show direction names only, not memory addresses
- [done] Check inventory command — let player see what's in their inventory
- [done] Display monster's current health each turn
- [ ] `use_weapon` — line 49 crashes if no monster in room, use `monster` parameter instead of `self.current_room.monster`
- [ ] Garlic against non-Nosferatu — add print message and fix silent string on line 56
- [ ] `__random_error__` — randint range is 0-5 but list has 7 items, change to randint(0, 6)
- [ ] Retreat bug — pop `visited_rooms[-1]` after retreating so repeated retreats work correctly


## Bugs
 if you enter an input thats wrong game just shuts down that needs to change
 display where the next exit is so they no to go to it and if they can pick up weapons
 when entering a room if there is a monster please state that there is one and they have to defeat it
 move function is not working
 when displaying exit should just display the one
 item is not updating
 need a check inventory
 display monsters health


## Future Plans
- Add graphics (Pygame)
- Implement zombie maze properly
- Expand weapon and item system
