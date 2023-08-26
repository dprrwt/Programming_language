"""Introduction to Python Dictionaries
A dictionary is an unordered set of key: value pairs.

It provides us with a way to map pieces of data to each other so that we can quickly find values that are associated with one another.

Suppose we want to store the prices of various items sold at a cafe:

Avocado Toast is 6 dollars
Carrot Juice is 5 dollars
Blueberry Muffin is 2 dollars
In Python, we can create a dictionary called menu to store this data:

menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

Notice that:

A dictionary begins and ends with curly braces { and }.
Each item consists of a key ("avocado toast") and a value (6).
Each key: value pair is separated by a comma.
It’s considered good practice to insert a space ( ) after each comma, but our code will still run without the space."""


sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)

"""Make a Dictionary
In the previous exercise, we saw a dictionary that maps strings to numbers (i.e., "avocado toast": 6). However, the keys can be numbers as well.

For example, if we were mapping restaurant bill subtotals to the bill total after tip, a dictionary could look like:

subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}

Values can be of any type. We can use a string, a number, a list, or even another dictionary as the value associated with a key!

For example:

students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

The list ["Aaron", "Delila", "Samson"], which is the value for the key "software design", represents the students in that class.

We can also mix and match key and value types. For example:

person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}
"""

"""Add Multiple Keys
If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.

Looking at our sensors object from a previous exercise:

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}

If we wanted to add 3 new rooms, we could use:

sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

This would add all three items to the sensors dictionary.

Now, sensors looks like:

{"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}"""


#Overwrite values
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

#GetAllKeys
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)

#GetAllValues
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0
for num in num_exercises.values():
  total_exercises += num

print(total_exercises)

#GetAllItems
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0
for num in num_exercises.values():
  total_exercises += num

print(total_exercises)



#ProjectScrabble
"""Scrabble Theory
In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points.

There are many ways you can extend this project on your own if you finish and want to get more practice!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

Tasks
14/15 Complete
Mark the tasks as complete by checking them off
Build your Point Dictionary
1.
We have provided you with two lists, letters and points. We would like to combine these two into a dictionary that would map a letter to its point value.

Using a list comprehension and zip, create a dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values.


Stuck? Get a hint
2.
Our letters list did not take into account blank tiles. Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.


Stuck? Get a hint
Score a Word
3.
We want to create a function that will take in a word and return how many points that word is worth.

Define a function called score_word that takes in a parameter word.


Stuck? Get a hint
4.
Inside score_word, create a variable called point_total and set it to 0.

5.
After defining point_total, create a for loop that goes through the letters in word and adds the point value of each letter to point_total.

You should get the point value from the letter_to_points dictionary. If the letter you are checking for is not in letter_to_points, add 0 to the point_total.


Stuck? Get a hint
6.
After the for loop is finished, return point_total.

7.
Let’s test this function! Create a variable called brownie_points and set it equal to the value returned by the score_word() function with an input of "BROWNIE".

8.
We expect the word BROWNIE to earn 15 points:

(B + R + O + W + N + I + E)

(3 + 1 + 1 + 4 + 4 + 1 + 1) = 15

Let’s print out brownie_points to make sure we got it right.

Score a Game
9.
Create a dictionary called player_to_words that maps players to a list of the words they have played. This table represents the data to transcribe into your dictionary:

player1	wordNerd	Lexi Con	Prof Reader
BLUE	EARTH	ERASER	ZAP
TENNIS	EYES	BELLY	COMA
EXIT	MACHINE	HUSKY	PERIOD

Stuck? Get a hint
10.
Create an empty dictionary called player_to_points.


Stuck? Get a hint
11.
Iterate through the items in player_to_words. Call each player player and each list of words words.

Within your loop, create a variable called player_points and set it to 0.


Stuck? Get a hint
12.
Within the loop, create another loop that goes through each word in words and adds the value of score_word() with word as an input.


Stuck? Get a hint
13.
After the inner loop ends, set the current player value to be a key of player_to_points, with a value of player_points.


Hint
To set a key:value pair in a dictionary, use the syntax:

my_dict[key_to_add] = value_to_add

14.
player_to_points should now contain the mapping of players to how many points they’ve scored. Print this out to see the current standings for this game!

If you’ve calculated correctly, wordNerd should be winning by 1 point.

Ideas for Further Practice!
15.
If you want extended practice, try to implement some of these ideas with the Python you’ve learned:

play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played
update_point_totals() — turn your nested loops into a function that you can call any time a word is played
make your letter_to_points dictionary able to handle lowercase inputs as well"""

