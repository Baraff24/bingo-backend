import random
import numpy as np

def gen_card():
    lista_numbers = []

    dummy_list = np.array([])
    pulled_numbers = np.array([])

    # Generate a variable size matrix to ease the extraction of numbers
    # Generate uneven matrix to ease the extraction of numbers

    for i in range(1, 91):
        if i % 10 == 0:
            if i == 90:
                dummy_list = np.append(dummy_list, i)
            lista_numbers.append(dummy_list)
            dummy_list = np.array([])

        dummy_list = np.append(dummy_list, i)

    card = []

    for i in range(0, 3):
        # Generate 5 random rows from lista_numbers
        random_rows = random.sample(range(0, 9), 5)

        card_row = np.zeros(shape=[1, 9])
        # Generate random index from the selected rows
        for j in range(0, 5):
            selected_row = random_rows[j]
            selected_row_length = len(lista_numbers[selected_row])
            random_index = random.sample(range(0, selected_row_length), 1)

            random_number = lista_numbers[random_rows[j]][random_index]

            while random_number in pulled_numbers:
                random_index = random.sample(range(0, selected_row_length), 1)
                random_number = lista_numbers[random_rows[j]][random_index]

            pulled_numbers = np.append(pulled_numbers, random_number)
            card_row[0, random_rows[j]] = random_number

        card.append(card_row[0])

    # Sort element by columns to have that nice cards effect where numbers are ordered in columns
    card = np.asarray(card)

    for i in range(0, 9):
        dummy_column = card[:, i]
        switch_index = []
        dummy_copy = []
        # If zero, shall remain in the same position

        for j in range(0, len(dummy_column)):
            if dummy_column[j] != 0:
                switch_index.append(j)
                dummy_copy.append(dummy_column[j])

        dummy_copy = np.asarray(dummy_copy)
        dummy_copy = np.sort(dummy_copy)

        for j in range(0, len(switch_index)):
            dummy_column_index = switch_index[j]
            dummy_column[dummy_column_index] = dummy_copy[j]

        card[:, i] = dummy_column

    return card


def serialize_card(card):
    new_card = []

    [new_card.append([{'number': str(int(number)), 'crossed_out': False} for number in card[j]]) for j in range(0, 3)]
    return new_card


def generate_card():
    card = gen_card()
    ser_card = serialize_card(card)
    return ser_card


def check_win_n(card, n):
    """
    Check if there are n numbers in the same row crossed out.
    2 <= n <= 5
    2 = ambo
    3 = terno
    4 = quaterna
    5 = cinquina
    """
    # check the numbers in the first row, if there are n numbers crossed out
    a = 0
    for element in card[0]:
        if element['crossed_out'] is True:
            a += 1
    if a == n:
        return True
    # check the numbers in the second row, if there are n numbers crossed out
    b = 0
    for element in card[1]:
        if element['crossed_out'] is True:
            b += 1
    if b == n:
        return True
    # check the numbers in the third row, if there are n numbers crossed out
    c = 0
    for element in card[2]:
        if element['crossed_out'] is True:
            c += 1
    if c == n:
        return True
    return False


def check_win_tombola(card):
    """
    Check if every number in the card is crossed out.
    """
    for row in card:
        for element in row:
            if element['crossed_out'] is False and element['number'] != "0":
                return False
    return True
