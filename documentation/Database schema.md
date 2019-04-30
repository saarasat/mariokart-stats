# Structure of the database

There are six tables in the database. For each table id, creation and modification timestamps are created automatically. 

### 1. Account
Account-table holds the information regarding an individual user. For account-table each user inserts their name, chosen username and password. 

### 2. Player
Each account can hold the information of only one or multiple players. This choice of separating the player-table from account-table has been made so that one person can act also as a “scorekeeper” if a group of friends playing, as Mario Kart is many times played in a group.  

For each player there is a player handle defined as well as their favorite character and two favorite tracks. 

### 3. Character
Character-table includes the 8 characters that are readily defined in the game. In case there would be changes to these characters (eg. the database would be used for a different MK-game besides Mario Kart 64), the admin can add new characters.

### 4. Track
Track-table includes the 16 tracks that are readily defined in the game. In case there would be changes to these tracks (eg. the database would be used for a different MK-game besides Mario Kart 64), the admin can add new tracks. 

### 5. favoriteTracks
Acts as a many-to-many association-table between player-table and track-table.

### 6. Race 
Includes the main data of the app, the actual racing data. A single entry to this table includes the results of an individual race, in a single track by a single player.


## Database schema

![Database](https://github.com/saarasat/mariokart-stats/blob/master/documentation/Database%20schema%20-%20Mario%20Kart%20Statistics%20v.4.0.png)




## SQL for creating the tables

### 1. Account
<pre><code>
CREATE TABLE Account (
    id SERIAL,
    date_created TIMESTAMP,
    date_modified TIMESTAMP,
    name VARCHAR(100),
    username VARCHAR (60),
    password VARCHAR(60),
    PRIMARY KEY (id)
);
</code></pre>

### 2. Player
<pre><code>
CREATE TABLE Player(
    id SERIAL,
    character_id INTEGER,
    account_id INTEGER,
    date_created TIMESTAMP,
    date_modified TIMESTAMP,
    handle VARCHAR(100),
    PRIMARY KEY (id),
    FOREIGN KEY (character_id) REFERENCES Character(id),
    FOREIGN KEY (account_id) REFERENCES Account(id)
);
</code></pre>

### 3. Character
<pre><code>
CREATE TABLE Character(
    id SERIAL,
    date_created TIMESTAMP,
    date_modified TIMESTAMP,
    name VARCHAR(100),
    PRIMARY KEY (id),
);
</code></pre>

### 4. Track
<pre><code>
CREATE TABLE Track(
    id SERIAL,
    date_created TIMESTAMP,
    date_modified TIMESTAMP,
    name VARCHAR(100),
    PRIMARY KEY (id),
);
</code></pre>

### 5. Favoritetracks
<pre><code>
CREATE TABLE favoritetracks(
    player_id INTEGER,
    track_id INTEGER,
    PRIMARY KEY (player_id, track_id),
    FOREIGN KEY (player_id) REFERENCES Player(id),
    FOREIGN KEY (track_id) REFERENCES Track(id)
);
</code></pre>

### 6. Race
<pre><code>
CREATE TABLE Race(
    id SERIAL,
    account_id INTEGER,
    player_id INTEGER,
    track_id INTEGER,
    character_id INTEGER,
    date_created TIMESTAMP,
    date_modified TIMESTAMP,
    placement INTEGER,
    finish_time TIME,
    PRIMARY KEY (id),
    FOREIGN KEY (account_id) REFERENCES Account(id),
    FOREIGN KEY (player_id) REFERENCES Player(id),
    FOREIGN KEY (track_id) REFERENCES Track(id),
    FOREIGN KEY (character_id) REFERENCES Character(id),
);
</code></pre>
