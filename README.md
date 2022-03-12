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

### ThrillDigger class

#### ThrillDigger and Digger instances
To instantiate the ThrillDigger class or any custom Digger that inherits from it, the only parameter needed is a Difficulty (see below)

#### play()
Executes the defined strategy and checks for the final game and board states afterwards

#### dig(x,y)
Digs up and returns the item at coordinate x,y. Changes board and game states accordingly. 
Raises ``GameIsOverException`` if attempting to dig when the game has finished either by winning or by having dug up a bomb previously.

#### get_price()
Returns the cost of playing this game of Thrill Digger. This is specified by the difficulty but is useful sometimes to have the digger know the cost itself.

#### get_score()
Returns the current game's score. Note that even though Rupoors substract score, the score can never be less than 0.
    
#### get_play_state()
Returns the game's state by the PlayState enumerator (see below)
    
#### get_board()
Returns a representation of the board in the form of a two dimensional array of tuples (CellState, Item).
It's updated each time the ``dig(x,y)`` method is called and can be checked at any time.
    
#### get_pretty_board()
Provides a simple string representation of the board using letters and symbols to be able to easily visualize the current state of the board.
    
#### get_board_shape()
Returns a tuple (width:int, height:int) that indicates the shape of the board. 
    
#### get_board_hazards()
Returns a tuple (bombs:int, rupoors:int) that indicates the initial amount of hazards in the board. These values are not updated while playing to indicate the remaining hazards.

#### execute_play_strategy()
The main method a Digger should implement by using all and any of the above methods, enumerators and properties to try and solve a Thrill Digger's game.

### Difficulties
Standard difficulties are provided through the ``lib.difficulties.Difficulty`` enumerator. These are:

| Difficulty | Width | Height | Bombs | Rupoors | Cost |
|------------|-------|--------|-------|---------|------|
| BEGINNER | 5 | 4 | 4 | 0 | 30 |
| INTERMEDIATE | 6 | 5 | 4 | 4 | 50 |
| EXPERT | 6 | 5 | 8 | 8 | 70 |
| CUSTOM | 0 | 0 | 0 | 0 | 0 |

The default values for CUSTOM difficulty are zeroes, but they can be specified as optional parameters in the Digger's constructor. Specifying these values while using standard Difficulties will have no effect.

### PlayState
PlayState represents the different possible states of a Thrill Digger game and are provided by the ``lib.thrilldigger.PlayState`` enumerator.
- MAKE_MOVE: User can keep digging.
- FAILED: Game has finished because user has dug up a bomb.
- VICTORY: Game has finished because user has dug up every rupee without hitting any bombs.

### Item
Enum that represents all the possible items. It's provided by ``lib.board.Item``. A caveat about this enum is that its integer values correspond with the score value of the item in the game.
- BLANK: Empty or Unknown Item.
- BOMB: A bomb. Ends the game.
- RUPOOR: A bad rupee. Substracts 20 points from the score.
- GREEN: A green rupee. Adds 1 to the score.
- BLUE: A blue rupee. Adds 5 to the score.
- RED: A red rupee. Adds 20 to the score.
- SILVER: A silver rupee. Adds 100 to the score.
- GOLDEN: A golden rupee. Adds 300 to the score.

### CellState
CellState represents the perceived state of a given cell of the board. It's provided by ``lib.board.CellState`` and can either be:
- COVERED: Cell has been dug up and its contents are known.
- UNCOVERED: Cell hasn't been dug up and its contents are unknown.

### Exceptions

#### IncorrectStateError
Custom Exception to notify that the action we are trying to perfom can't be executed due to the Board or Game being in an incorrect state for it

#### GameIsOverException
A subclass of IncorrectStateError. Indicates that the game is already over, either by Victory or by Defeat.

#### UnfinishedGameException
A subclass of IncorrectStateError. Indicates that the play method has finished executing the strategy but the game can still be played. For example if the strategy consists in digging up a single tile and nothing else, in which case the game only would be in a proper end state if the arbitrary tile contained a bomb.
