In this exercise, we are using a points dictinary, with each character as a key in the alphabet corresponding to a numeric point assigned as the value for each key. 

The exercise is straigh forward, in which there is a words variable and that is compared against the dictionary. A for loop is used to iterate over words, in which then a conditional statement is used to compare the characters (char) against the char in the dictionary:

    if char in points:
        point += points[char]

The breakdown here is that for each char in the words variable, the total points should be based on the key to which each points are assigned its value. For example, if we assigned the word "Lay" to the word variable.

    word = "Lay"

Now we iterate over the word:
    for char in word.lower():
        if char in points:
            point += points[char]

Lets evaluate how we total the points:
    point = Lay
    l = 12
    a = 1
    y = 25
    point = Lay
    Lay.lower() = lay
    point = l   +a  +y
    point = 12  +1  +25
    point = 38