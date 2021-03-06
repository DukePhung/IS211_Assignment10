DROP TABLE IF EXISTS artist;
DROP TABLE IF EXISTS album;
DROP TABLE IF EXISTS song;

CREATE TABLE artist (
	Artist_ID INTEGER PRIMARY KEY,
	Name TEXT);
	
CREATE TABLE album (
	Album_ID INTEGER PRIMARY KEY,
	Title TEXT,
	Artist_ID INTEGER);

CREATE TABLE song (
	Song_ID INTEGER PRIMARY KEY,
	Name TEXT,
	Track_Num INTEGER,
	song_length INTEGER,
	Album_ID INTEGER);
	
	