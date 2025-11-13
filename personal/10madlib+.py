"""
MAD LIB GENERATOR WITH ENHANCED WORD SELECTION

This program generates a classic Mad Lib story using random words from various categories.
The key improvement is using the NLTK library to access thousands of real English words,
ensuring much greater variety than manual lists alone.

The story format remains exactly the same as the original - only the word selection is enhanced.
"""

# Import the random module to generate random selections from our word lists
import random

"""
NLTK (Natural Language Toolkit) SETUP SECTION

NLTK is a powerful Python library for working with human language data.
It includes WordNet, a large lexical database of English words organized by meaning.
"""
try:
    # Try to import the NLTK library and its WordNet component
    import nltk
    from nltk.corpus import wordnet as wn  # WordNet is like a digital dictionary/thesaurus

    # Check if WordNet data is already downloaded on this computer
    try:
        nltk.data.find('corpora/wordnet')  # Looks for the WordNet data files
    except LookupError:
        # If WordNet isn't found, download it automatically (this only happens once)
        nltk.download('wordnet', quiet=True)  # quiet=True prevents download messages

    # Set a flag indicating NLTK is available for use
    NLTK_AVAILABLE = True

except ImportError:
    """
    FALLBACK MODE: If NLTK isn't installed, we'll use expanded manual word lists
    This ensures the program still works even without the external library
    """
    NLTK_AVAILABLE = False


def get_word_list(category, count=20):
    """
    GET WORDS FOR A SPECIFIC CATEGORY (nouns, verbs, adjectives, etc.)

    This is the core improvement - instead of small manual lists, we can access
    thousands of real English words categorized by their grammatical function.

    Parameters:
    - category (string): What type of words we need ('adj', 'noun', 'verb', etc.)
    - count (integer): How many words to return in the list

    Returns:
    - list: A list of random words from the specified category
    """

    # ATTEMPT 1: Use NLTK WordNet for unlimited word variety
    if NLTK_AVAILABLE:
        try:
            """
            MAPPING OUR CATEGORIES TO WORDNET TYPES

            WordNet organizes words by their part of speech using single-letter codes:
            - 'n' = noun (person, place, thing)
            - 'v' = verb (action words) 
            - 'a' = adjective (describing words)
            - 'r' = adverb (how actions are done)

            We map our friendly category names to WordNet's codes.
            """
            wordnet_map = {
                'adj': 'a',  # Adjectives -> WordNet adjective type
                'noun': 'n',  # Nouns -> WordNet noun type
                'pluralNoun': 'n',  # Plural nouns are still nouns in WordNet
                'ingVerb': 'v', #-ing verbs come from regular verbs
            'game': 'n',  # Games are specific types of nouns
            'plant': 'n',  # Plants are nouns
            'bodyPart': 'n',  # Body parts are nouns
            'place': 'n'  # Places are nouns
            }

            # Get the WordNet code for our category, default to nouns if unknown
            pos_code = wordnet_map.get(category, 'n')

            """
            UNDERSTANDING WORDNET SYNSETS

            In WordNet, words are grouped into 'synsets' (synonym sets) - groups of 
            words that share the same meaning. For example: {'car', 'auto', 'automobile'}

            wn.all_synsets(pos_code) returns ALL synsets for our part of speech.
            We convert it to a list so we can work with it.
            """
            all_synsets = list(wn.all_synsets(pos_code))

            """
            SHUFFLING FOR RANDOMNESS

            WordNet returns words in a fixed order. By shuffling, we ensure we get
            different words each time the program runs, making each Mad Lib unique.
            """
            random.shuffle(all_synsets)

            # We'll collect our filtered words in this list
            words = []

            """
            PROCESSING EACH SYNSET

            We loop through the synsets to extract individual words. We take more
            than we need (count * 3) because some words will be filtered out.
            """
            for synset in all_synsets[:count * 3]:
                """
                EXTRACTING AND CLEANING WORDS

                Each synset has multiple 'lemmas' (word forms). We take the first one.
                Some words in WordNet have underscores (like 'base_ball') so we 
                replace them with spaces to make them more natural.
                """
                word = synset.lemmas()[0].name().replace('_', ' ')

                """
                FILTERING WORDS FOR QUALITY

                We only want words that:
                1. Are alphabetic (no numbers or symbols)
                2. Are between 3-14 characters (not too short, not too long)
                3. Don't contain digits

                This ensures we get clean, appropriate words for our Mad Lib.
                """
                if (word.isalpha() and 2 < len(word) < 15 and
                        not any(char.isdigit() for char in word)):

                    """
                    CATEGORY-SPECIFIC FORMATTING

                    Depending on the category, we may need to modify the words:
                    - Plural nouns should end with 's'
                    - -ing verbs should end with 'ing'
                    """
                    if category == 'pluralNoun':
                        # Simple pluralization - just add 's' if not already plural
                        if not word.endswith('s'):
                            word = word + 's'
                    elif category == 'ingVerb':
                        # Add -ing ending to verbs
                        if not word.endswith('ing'):
                            word = word + 'ing'

                    # Convert to lowercase for consistency and add to our collection
                    words.append(word.lower())

            """
            REMOVING DUPLICATES AND TRIMMING

            We might have collected duplicate words from different synsets.
            set(words) removes duplicates, then we convert back to a list
            and return only the number of words requested.
            """
            unique_words = list(set(words))
            return unique_words[:count]

        except Exception:
            """
            NLTK FAILOVER

            If anything goes wrong with NLTK (network issues, corrupted data, etc.),
            we silently fall through to use our manual word lists instead.
            This makes the program robust and reliable.
            """
            pass

    """
    ATTEMPT 2: MANUAL WORD LISTS (FALLBACK)

    If NLTK isn't available or fails, we use these expanded manual lists.
    These are much larger than the original lists but still finite.
    """
    manual_lists = {
        # Adjectives - words that describe nouns (big, small, colorful, etc.)
        'adj': ["funny", "big", "small", "loud", "quiet", "red", "green", "blue",
                "black", "white", "happy", "sad", "fast", "slow", "tall", "short",
                "bright", "dark", "young", "old", "hot", "cold", "wet", "dry"],

        # Nouns - people, places, things, or ideas
        'noun': ["car", "cat", "dog", "ball", "shoe", "plane", "house", "book",
                 "computer", "tree", "flower", "river", "mountain", "ocean", "city",
                 "school", "park", "beach", "forest", "desert", "island", "castle"],

        # Plural nouns - more than one of something
        'pluralNoun': ["toys", "apples", "bananas", "socks", "pencils", "books",
                       "cars", "dogs", "cats", "houses", "trees", "flowers", "rivers",
                       "mountains", "oceans", "cities", "schools", "parks", "beaches"],

        # Games - activities for fun and play
        'game': ["Chess", "Tic-Tac-Toe", "Rock-Paper-Scissors", "I-Spy", "Hop-Scotch",
                 "Checkers", "Monopoly", "Uno", "Poker", "Bingo", "Twister", "Jenga"],

        # -ing verbs - actions happening now (present participle)
        'ingVerb': ["running", "playing", "reading", "dancing", "jumping", "swimming",
                    "singing", "writing", "drawing", "painting", "cooking", "eating",
                    "sleeping", "walking", "talking", "laughing", "thinking"],

        # Plants - living organisms that grow in soil
        'plant': ["grass", "shrub", "tree", "vine", "moss", "flower", "fern", "cactus",
                  "bush", "weed", "mushroom", "algae", "lichen", "ivy", "bamboo"],

        # Body parts - components of the human body
        'bodyPart': ["foot", "face", "hand", "arm", "leg", "head", "nose", "ear",
                     "eye", "mouth", "shoulder", "knee", "elbow", "finger", "toe"],

        # Places - specific locations
        'place': ["Melbourne High School", "Mr. Gornto's house", "McDonald's",
                  "The Melbourne Causeway", "Palm Bay High School", "Disney World",
                  "New York City", "Grand Canyon", "Paris", "London", "Tokyo"]
    }

    # Return the manual list for our category, or nouns if category isn't found
    return manual_lists.get(category, manual_lists['noun'])[:count]


def get_unique_word(word_list):
    """
    GET A RANDOM WORD AND REMOVE IT TO PREVENT REPEATS

    This function ensures that no word is used more than once in the Mad Lib.
    It works by:
    1. Randomly selecting a word from the list
    2. Removing that word from the list
    3. Returning the selected word

    Parameters:
    - word_list (list): The list of words to choose from

    Returns:
    - string: A randomly selected word
    """
    # random.choice() picks one random item from a list
    word = random.choice(word_list)

    # list.remove() deletes the first occurrence of an item from the list
    word_list.remove(word)

    return word


"""
WORD LIST GENERATION SECTION

Here we create our word banks for each category needed in the Mad Lib.
We request more words than we need (15 instead of 3-4) to ensure we have
enough unique words and to make each run more varied.
"""

# Adjectives - words that describe things (3 needed for story)
adj = get_word_list('adj', 15)

# Regular nouns - people, places, things (3 needed for story)
noun = get_word_list('noun', 15)

# Plural nouns - multiple items (4 needed for story)
pluralNoun = get_word_list('pluralNoun', 15)

# Games - activities (1 needed for story)
game = get_word_list('game', 10)

# -ing verbs - actions in progress (4 needed for story)
ingVerb = get_word_list('ingVerb', 15)

# Plants - flora (1 needed for story)
plant = get_word_list('plant', 10)

# Body parts - anatomy (1 needed for story)
bodyPart = get_word_list('bodyPart', 10)

# Places - locations (1 needed for story)
place = get_word_list('place', 10)

"""
WORD SELECTION SECTION

Now we select specific words for each slot in the Mad Lib story.
We use our get_unique_word() function to ensure no word repeats.
Each call to get_unique_word() removes the selected word from its list.
"""

# Select 3 unique adjectives for the story
adj1 = get_unique_word(adj)  # First adjective
adj2 = get_unique_word(adj)  # Second adjective
adj3 = get_unique_word(adj)  # Third adjective

# Select 3 unique nouns (note: noun1 isn't used in the original story)
noun2 = get_unique_word(noun)  # Second noun
noun3 = get_unique_word(noun)  # Third noun
noun4 = get_unique_word(noun)  # Fourth noun

# Select 4 unique plural nouns
pluralNoun1 = get_unique_word(pluralNoun)  # First plural noun
pluralNoun2 = get_unique_word(pluralNoun)  # Second plural noun
pluralNoun3 = get_unique_word(pluralNoun)  # Third plural noun
pluralNoun4 = get_unique_word(pluralNoun)  # Fourth plural noun

# Select 1 game
game1 = get_unique_word(game)

# Select 4 unique -ing verbs
ingVerb1 = get_unique_word(ingVerb)  # First -ing verb
ingVerb2 = get_unique_word(ingVerb)  # Second -ing verb
ingVerb3 = get_unique_word(ingVerb)  # Third -ing verb
ingVerb4 = get_unique_word(ingVerb)  # Fourth -ing verb

# Select 1 plant
plant1 = get_unique_word(plant)

# Select 1 body part
bodyPart1 = get_unique_word(bodyPart)

# Select 1 place
place1 = get_unique_word(place)

# Generate a random number between 2-24 for the hours worked
hours = str(random.randint(2, 24))

"""
STORY OUTPUT SECTION

This is the original Mad Lib story format - completely unchanged from the original.
The only difference is that the words are now selected from much larger, more varied pools.

The story uses string concatenation (+) to build each line by combining fixed text
with our randomly selected words.
"""

print()  # Empty line for spacing
print("-------------My Mad Lib-------------")
print()  # Another empty line

# Line 1: Introduces the vacation concept with first adjective
print("A vacation is when you take a trip to some " + adj1 + " place")

# Line 2: Describes who you go with using second adjective
print("with your " + adj2 + " family. Usually you go to some place ")

# Line 3: Describes location near specific nouns
print("that is near a/an " + noun2 + " or up on a/an " + noun3)

# Line 4: Describes activities at vacation place
print("A good vacation place is one where you can ride " + pluralNoun1)

# Line 5: More activities including a game and hunting
print("or play " + game1 + " or go hunting for " + pluralNoun2 + ".  I like ")

# Line 6: Personal preferences for time spending
print("to spend my time " + ingVerb1 + " or " + ingVerb2 + ".")

# Line 7: Describes parent activities on vacation
print("When parents go on a vacation, they spend their time eating")

# Line 8: Specific eating habits and gender-specific activities
print("three " + pluralNoun3 + " a day, and fathers play golf, and mothers ")

# Line 9: Mother's activity and brother's accident setup
print("sit around " + ingVerb3 + ". Last summer, my little brother ")

# Line 10: Brother's accident with noun and plant
print("fell in a/an " + noun4 + " and got poison " + plant1 + " all")

# Line 11: Location of poison on body
print("over his " + bodyPart1 + ".  My family is going to go to (the) ")

# Line 12: Future vacation plans and personal practice
print(place1 + " , and I will practice " + ingVerb4 + ".  Parents")

# Line 13: Reason parents need vacations more
print("need vacations more than kids because parents are always very ")

# Line 14: Third adjective describing parents and work hours
print(adj3 + " and because they have to work ", hours)

# Line 15: Concludes with work purpose and final plural noun
print("hours every day all year making enough " + pluralNoun4 + " to pay ")

# Final line: Purpose of the money
print("for the vacation.")