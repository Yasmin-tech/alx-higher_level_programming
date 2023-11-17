-- a script that lists all records of the table second_table of the database hbtn_0c_0 in my MySQL server.
-- rows without a name value will not be listed
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score
SELECT score, name FROM second_table
	WHERE name IS NOT NULL 
	ORDER BY score DESC, name;
