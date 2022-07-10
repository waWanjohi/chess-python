from typing import List


def create_message(detail, messages):
    """
    This is a service method to create any kind of message within the game.
    It only returns a stringified version of the input
    """
    messages.append(detail)
    return str(detail)