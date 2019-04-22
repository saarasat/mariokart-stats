# User manual

## 1. Logging in & creating an account

Before logging in, you need to register https://mario-kart-stats.herokuapp.com/users/new/. For creating a user account, you need to give your name, username and a password of your choice. 
Logging happens with username and password at https://mario-kart-stats.herokuapp.com/.

## 2. Adding statistics

There are two kinds of information that can be added to the Mario Kart Statistics -database. 

### 2.1 Adding new players:
 
Firstly, create a player: https://mario-kart-stats.herokuapp.com/players. Player can be you or all people in the group playing the game. 

For each player you need to specify a unique player handle, define two favorite tracks for the player and the favorite character they like to play with.

For example:

- Player handle: “Player1”
- Your favorite track: “Mario Raceway”
- Add another favorite track: “Luigi Raceway”
- Favorite character: “Mario”. 

This information is needed to compare how the player is doing in their favorite tracks and with their favorite character. All tracks and characters are pre-defined, as they are in the game. In order to add another favorite track, you need to choose the first track field first. The same track cannot be added twice. 

### 2.2. Adding new races: 

After creating the player information, you can start adding individual races at: https://mario-kart-stats.herokuapp.com/races/new/

For each race you need to add the player playing, name of the track played, character played, at what place the player finished and finish time in minutes and seconds (in the form mm:ss)

For example:

- Player handle: “Player1”
- Track: “Mario Raceway
- Character: "Mario"
- Placement: "1:
- FinishTime: "03:02"


## 3. Checking statistics 

The application stores three different kind of information. Statistics by race, by track and by player. 

### 3.1 Stats by race

Lists all data of all races in the order they were added. All races for all players in this account are shown. The newest can be found last on the list. Each race can be deleted in this view. 

### 3.2 Stats by track

Lists all data of all tracks. The list shows the name of the track, the times each track has been played, the fastest time for each track and the player who has the fastest time. 

### 3.3 Stats by player

Statistics of individual players can be found here. Each user can find the stats of the players they have registered. 

#### "Races played in total":
Shows all the races this player has ever played.

#### "Races won":
Shows the races where this player won (finished in first place).

#### "Results by character":
Shows the favorite character defined for this player. Shows how many times each character was played by this player and how many times player has won with that character. Therefore the user can compare the results of their favorite character and other characters.

#### "Results by track":
Shows the favorite tracks of the player. Shows how many times each track was played by this player and how many times player has won in that track. Therefore the user can compare the results of their favorite tracks and other tracks.

#### "All races":
Shows all race stats by this player in ascending order by placement. Eg. the fastest times for each track can be seen here. 

## 4. Manage players

A place for adding new players (see 2.1. "Adding new players")
Player handles can be updated or individual players can be deleted. Please note that deleting a player will delete all data relating to them.
