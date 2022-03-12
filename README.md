# pgtd : programmer's thrill digger

PGTD mimics the old and almost impossible to find PGMS (Programmer's Minesweeper). PGMS was a Java project that implemented the Minesweeper game and allowed a person to code their favorite playing strategy while encouraging users to find better solutions to the game.

In this case we are implementing Thrill Digger, an incomplete information approach to minesweeper presented as a minigame in [The Legend of Zelda Skyward Sword](https://zelda.fandom.com/wiki/Thrill_Digger). The main difference from Thrill Digger and Minesweeper is that while in the later the goal is to clear the board without hitting any mine, in Thrill Digger the goal is to maximize the score regardless of winning or losing. There are additional rewards in the game for clearing each mode but since the information in Thrill Digger is incomplete, is even more luck dependant than the original Minesweeper.

## Rules and Hints

Thrill Digger presents a board in which we have to digout gemstones called rupees. In some holes there are bombs or rupoors (bad rupees) that either makes us lose the game or lose part of our score. Each difficulty mode presents a bigger board and an increaisng number of hazards.

Each type of rupee adds a different value to our score and hints us about the contents of its surroundings

| Color  | Name | Symbol | Value | Nearby Hazards |
|--------|------|--------|-------|----------------|
| 🟩 | Green | I | 1 | 0 |
| 🟦 | Blue | B | 5 | 1-2 |
| 🟥 | Red | R | 20 | 3-4 |
| 🥈 | Silver | S | 100 | 5-6 |
| 🥇 | Gold | G | 300 | 7-8 |
| ⬛️ | Rupoor | - | -20 | ? |
| 💣 | Bomb | X | 0 | ? |

## Programming a Digger

The game is implemented through the ThrillDigger class that uses a Board class to build and keep track of the game board and game state.
The user is tasked with implementing the ``execute_play_strategy()`` method by inheriting the ThrillDigger class. A sample digger is provided in ``strats/simpledigger.py``. By instancing the new digger and calling the ```play()`` method, the game will execute the strategy and check if the game has concluded afterwards. Users can collect data from the digger such as the score the board state or the game state in any moment, even when the game has concluded.

The simple provided script ``roi_digger.py`` uses an arbitrary custom digger to calculate the average Return on Investment of said digger and showcases how a digger can be called and used after defining its ``execute_play_strategy()`` method.

## The ThrillDigger API
