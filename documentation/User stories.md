# User stories

The idea is that anyone can update racing statistics from Mario Kart 64. The person (scorekeeper) can be either the player themselves, or a someone who keeps the score players playing the game. The concept “race” includes the performance of one player in one track. That way the app can contain either the statistics of only one player who wants to follow his progress or for instance the results of a group of friends playing the game.

## User

1. A new account can be created:

<pre>
SQL (example):

<code>
"INSERT INTO account" 
        " (date_created, date_modified, name, username, password)"
        " VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)", 
        ('New name', 'new user', 'password');</code>
</pre>

2. A user can login:

<pre>
SQL (example):

<code>
"SELECT account.id AS account_id," 
        " account.date_created AS account_date_created," 
        " account.date_modified AS account_date_modified," 
        " account.name AS account_name," 
        " account.username AS account_username," 
        " account.password AS account_password" 
        " FROM account WHERE account.id = ?", (1);</code> 
</pre>
      
3. User can update their account information:

<pre>
SQL (example):

<code>
"UPDATE account SET date_modified=CURRENT_TIMESTAMP,"
        "name=? WHERE account.id = ?", ('Updated Name', 1);</code>
</pre>


## Scorekeeper

1. Adding stats: As a scorekeeper I can insert the game statistics of a single race

<pre>
SQL (example):

<code>"INSERT INTO race"
        " (date_created, date_modified, finish_time, placement," 
        " player_id, character_id, track_id, account_id) "
        " VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?,?,?,?,?,?)", 
        ('01:22:00', '1', 5, 2, 4, 2);</code>
</pre>


2. Removing stats: As a scorekeeper I can remove records of one or all races

<pre>
SQL (example):

<code>"DELETE FROM race WHERE race.id = ?", (2);</code>
</pre>


### Track-specific records: 

1. As a scorekeeper I can find out how many times each track has been played by my players
2. As a scorekeeper I can find out what is the best finish time for a certain track 

<pre>
SQL for both 1 and 2:

<code>
("SELECT Track.name AS Track,"
       " COUNT(Race.track_id) AS Races,"
       " MIN(Race.finish_time) AS BestTime FROM Track" 
       " LEFT JOIN Race ON Track.id = Race.track_id "
       " LEFT JOIN Player ON Race.player_id = Player.id"
       " WHERE Race.account_id = :id"
       " GROUP BY Track.name ORDER BY Races"
       " DESC").params(id=id)</code>
</pre>


### Player-specific records: 

1. As a scorekeeper I can search for all the races where a certain player has won

<pre>
SQL

<code>("SELECT SUM(Race.placement) AS Wins FROM Player"
        " JOIN Race ON Player.id = Race.player_id"
        " WHERE Race.placement = 1 AND Player.id = :id").params(id=id)</code>
</pre>


2. As a scorekeeper I can search for all the races where a certain player was last

<pre>
SQL (included in this query in the actual application)

<code>("SELECT Track.name AS Track,"
        " Race.finish_time AS FinishTime, Character.name AS Character,"
        " Race.placement AS Placement FROM Race"
        " JOIN Track ON Race.track_id = Track.id"
        " JOIN Character ON Race.character_id = Character.id"
        " WHERE player_id = :id"
        " GROUP BY Track, Race.finish_time, Race.placement, Character.name"
        " ORDER BY Race.placement, Race.finish_time").params(id=id)</code>
</pre>


3. As a scorekeeper I can find out which has been the most successful character for a certain player (character with most first places)

<pre>
SQL

<code>
("SELECT Character.name AS Character," 
        " COUNT(Race.character_id) AS Races FROM Race"
        " JOIN Character ON Race.character_id = Character.id"
        " WHERE player_id = :id AND Race.placement = 1"
        " GROUP BY Character"
        " ORDER BY Character").params(id=id)</code>
</pre>


4. As a scorekeeper I can find out in which track a certain player has performed the best (most first places out of all tracks played)

<pre>
SQL

<code>
("SELECT Track.name AS Track, COUNT(Race.track_id) AS Races FROM Race"
        " JOIN Track ON Race.track_id = Track.id"
        " WHERE player_id = :id AND Race.placement = 1"
        " GROUP BY Track"
        " ORDER BY Races DESC").params(id=id)</code>
</pre>


5. As a scorekeeper I can find out how many times a certain player has played a single track

<pre>
SQL (included in this query in the actual application)

<code>
("SELECT Track.name AS Track, COUNT(Race.track_id) AS Races FROM Race"
        " JOIN Track ON Race.track_id = Track.id"
        " WHERE player_id = :id"
        " GROUP BY Track"
        " ORDER BY Track.name DESC").params(id=id)</code>
</pre>

### Character-specific records: 

1. As a scorekeeper I can search how many times a certain player has played with a single character

<pre>
SQL (included in this query in the actual application)

<code>
("SELECT Character.name AS Character, COUNT(Race.character_id) AS Races FROM Race"
        " JOIN Character ON Race.character_id = Character.id"
        " WHERE player_id = :id AND Race.placement = 1"
        " GROUP BY Character"
        " ORDER BY Character").params(id=id)</code>
</pre>
