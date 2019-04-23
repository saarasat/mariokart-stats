# User stories

The idea is that anyone can update racing statistics from Mario Kart 64. The person (scorekeeper) can be either the player themselves, or a someone who keeps the score players playing the game. The concept “race” includes the performance of one player in one track. That way the app can contain either the statistics of only one player who wants to follow his progress or for instance the results of a group of friends playing the game.


## Scorekeeper

1. Adding stats: As a scorekeeper I can insert the game statistics of a single race

*SQL (example):*

<code>"INSERT INTO race"
        " (date_created, date_modified, finish_time, placement," 
        " player_id, character_id, track_id, account_id) "
        " VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?,?,?,?,?,?)", 
        ('01:22:00', '1', 5, 2, 4, 2);</code>

2. Removing stats: As a scorekeeper I can remove records of one or all races

*SQL (example):*  

<code>"DELETE FROM race WHERE race.id = ?", (2);</code>


### Track-specific records: 

1. As a scorekeeper I can find out how many times each track has been played by my players
2. As a scorekeeper I can find out what is the best finish time for a certain track 

*SQL for both 1 and 2:*

<code>"SELECT Track.name AS Track,"
        " COUNT(Race.track_id) AS Races,"
        " MIN(Race.finish_time) AS BestTime,"
        " Player.handle AS Player FROM Track" 
        " LEFT JOIN Race ON Track.id = Race.track_id "
        " LEFT JOIN Player ON Race.player_id = Player.id"
        " GROUP BY Track.name, Player.handle ORDER BY Races, Player.handle"</code>
        
### Player-specific records: 

1. As a scorekeeper I can search for all the races where a certain player has won

*SQL*

<code>"SELECT SUM(Race.placement) AS Wins FROM Player"
        " JOIN Race ON Player.id = Race.player_id"
        " WHERE Race.placement = 1 AND Player.id = :id").params(id=id)</code>

2. As a scorekeeper I can search for all the races where a certain player was last

*SQL (included in this query in the actual application)*

<code>"SELECT Track.name AS Track,"
        " Race.finish_time AS FinishTime, Character.name AS Character, Race.placement AS Placement FROM Race"
        " JOIN Track ON Race.track_id = Track.id"
        " JOIN Character ON Race.character_id = Character.id"
        " WHERE player_id = :id"
        " GROUP BY Track, Race.finish_time, Race.placement, Character.name"
        " ORDER BY Race.placement, Race.finish_time").params(id=id)</code>

3. As a scorekeeper I can find out which has been the most successful character for a certain player (character with most first places)

*SQL*

<code>"SELECT Character.name AS Character,"
        " COUNT(Race.id) AS Wins FROM Player"
        " JOIN Race ON Player.id = Race.player_id"
        " JOIN Character ON Race.character_id = Character.id"
        " WHERE Player.id = :id AND Race.placement = 1"
        " GROUP BY Character"
        " ORDER BY Wins DESC").params(id=id)</code>

4. As a scorekeeper I can find out in which track a certain player has performed the best (most first places out of all tracks played)

*SQL*

<code>"SELECT Track.name AS Track, COUNT(Race.track_id) AS Races FROM Race"
        " JOIN Track ON Race.track_id = Track.id"
        " WHERE player_id = :id AND Race.placement = 1"
        " GROUP BY Track"
        " ORDER BY Races DESC").params(id=id)</code>

5. As a scorekeeper I can find out how many times a certain player has played a single track

*SQL (included in this query in the actual application)*

"SELECT Track.name AS Track,"
        " Race.finish_time AS FinishTime, Character.name AS Character, Race.placement AS Placement FROM Race"
        " JOIN Track ON Race.track_id = Track.id"
        " JOIN Character ON Race.character_id = Character.id"
        " WHERE player_id = :id"
        " GROUP BY Track, Race.finish_time, Race.placement, Character.name"
        " ORDER BY Race.placement, Race.finish_time").params(id=id)

### Character-specific records: 

1. As a scorekeeper I can search how many times a certain player has played with a single character
