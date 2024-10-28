import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# cards = [11, 10, 10, 11, 11]

def get_card(cards_list):
    card = [random.choice(cards_list)]
    return card


def get_cards_score(cards_list):
    cards_score = 0
    for i in cards_list:
        cards_score += i
    return cards_score

# def get_new_cards_list(cards_list):
#     cards_score = 0
#     for i in cards_list:
#         if cards_score > 10:
#             if i == 11:
#                 index = cards_list.index(i)
#                 cards_list[index] = 1
#                 i = 1
#                 cards_score += i
#             else:
#                 cards_score += i
#         else:
#             cards_score += i
#     return cards_list

def get_new_cards_list(cards_list):
    cards_score = 0
    for i in cards_list:
        cards_score += i
    for i in range(len(cards_list)):
        if cards_score > 21 and cards_list[i] == 11:
            cards_list[i] = 1
            cards_score -= 10
    return cards_list

def check_score(cards_score):
    if cards_score > 21:  # Add this check
        message = f'You went over and loose. \n Final score: {cards_score}. '
        return message


def print_cards_and_score(score, cards_to_print):
    print(f'Cards: {cards_to_print}, current score: {score}')
def main():
    # print(logo)
    print('==============')
    print("Let's play blackjack!")

    more_card_for_you = True
    cards_to_display = get_card(cards) + get_card(cards)
    cards_to_show = get_new_cards_list(cards_to_display)
    score_to_print = get_cards_score(cards_to_show)
    check_score(score_to_print)

    print('-=Yours=-')
    print_cards_and_score(score_to_print, cards_to_show)

    if score_to_print == 21:
        print("You've got a blackjack and win!")
        return

    new_card_list=cards_to_show
    computer_cards = get_card(cards)
    comp_cards_to_show = get_new_cards_list(computer_cards)
    comp_score_to_print = get_cards_score(comp_cards_to_show)
    check_score(comp_score_to_print)
    comp_new_card_list = comp_cards_to_show
    print("-=Computer's=-")
    print_cards_and_score(comp_score_to_print, comp_cards_to_show)
    new_score_to_print = score_to_print
    new_cards_to_show = new_card_list
    new_comp_score_to_print = comp_score_to_print
    while more_card_for_you:
        yes_or_no = input("\nType 'y' to get another card, type 'n' to pass: ")

        if yes_or_no == 'y':
            another_card = get_card(cards)
            new_card_list.extend(another_card)
            new_cards_to_show = get_new_cards_list(new_card_list)
            new_score_to_print = get_cards_score(new_cards_to_show)
            check_score(new_score_to_print)

            if check_score(new_score_to_print) is not None:
                print(check_score(new_score_to_print))
                more_card_for_you = False
            print()
            print('-=Yours=-')
            print_cards_and_score(new_score_to_print, new_cards_to_show)
            print()
            print("-=Computer's=-")
            print_cards_and_score(comp_score_to_print, comp_cards_to_show)


        elif yes_or_no == 'n':

            while new_comp_score_to_print < 21:
                comp_another_card = get_card(cards)
                comp_new_card_list.extend(comp_another_card)
                comp_new_card_to_show = get_new_cards_list(comp_new_card_list)
                new_comp_score_to_print = get_cards_score(comp_new_card_to_show)
                check_score(new_comp_score_to_print)

                if comp_new_card_to_show[0] + comp_new_card_to_show[1] == 21:
                    print()
                    print("Computer got a blackjack and win!")
                    break

                if check_score(new_score_to_print) is not None:
                    print(check_score(new_score_to_print))

                    break


                print("-=Computer's=-")
                print_cards_and_score(new_comp_score_to_print, comp_new_card_to_show)
                if new_comp_score_to_print > 13:
                    chance = random.randint(1,10)
                    print(f'chance {chance}')
                    if chance > 6:
                        # print('End')
                        break
            if new_comp_score_to_print > 21:
                print()
                print('Computer went over and loose. You win :)')
                break

            print()
            print('-=Yours=-')
            print_cards_and_score(new_score_to_print, new_cards_to_show)
            print()
            print("-=Computer's=-")
            print_cards_and_score(new_comp_score_to_print, comp_new_card_to_show)

            print()
            print(f'Computer score: {new_comp_score_to_print}')
            print(f'Your score: {new_score_to_print}')
            if new_score_to_print < new_comp_score_to_print:
                print()
                print('You loose (')
                return
            elif new_score_to_print == new_comp_score_to_print:
                print()
                print("It's a draw!")
                # quit()
                return
            else:
                print()
                print('You win!')
                # quit()
                return

def after_main():
    while True:
        waiting = input(f"\nIf you want to quit, press 1, if you "
                        f"want to play another game, press ENTER.")
        if len(waiting) < 1:
            main()
        else:
            print('Thx for the game. See you later )')
            quit()

print(logo)
main()
after_main()


