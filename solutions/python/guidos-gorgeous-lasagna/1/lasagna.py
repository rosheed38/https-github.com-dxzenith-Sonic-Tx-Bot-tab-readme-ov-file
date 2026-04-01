"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# ---- Constants -------------------------------------------------------
# Total time (in minutes) the lasagna needs to bake in the oven.
EXPECTED_BAKE_TIME = 40

# Minutes of preparation needed per lasagna layer.
# Defined here (not inside functions) to avoid magic numbers.
PREPARATION_TIME = 2


# ---- Functions -------------------------------------------------------

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed (in minutes).
    :return: int - remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Takes the actual minutes the lasagna has been in the oven and returns
    how many minutes it still needs to bake.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time          # e.g. 40 - 15 = 25


def preparation_time_in_minutes(number_of_layers):
    """Calculate total preparation time for a given number of layers.

    :param number_of_layers: int - the number of layers added to the lasagna.
    :return: int - total preparation time (in minutes).

    Multiplies the number of layers by the constant PREPARATION_TIME
    (minutes per layer) to get the total prep time.
    """
    return number_of_layers * PREPARATION_TIME             # e.g. 3 layers × 2 = 6 mins


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time so far.

    :param number_of_layers: int - the number of layers added to the lasagna.
    :param elapsed_bake_time: int - how long the lasagna has been baking (in minutes).
    :return: int - total elapsed time (preparation + bake time so far).

    Combines preparation time for all layers with the time the lasagna
    has already spent in the oven.
    """
    prep_time = preparation_time_in_minutes(number_of_layers)  # reuse our function!
    return prep_time + elapsed_bake_time                        # e.g. 6 + 15 = 21 mins
