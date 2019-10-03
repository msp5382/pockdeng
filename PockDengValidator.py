def getNum(n):
    if n in '1234567890':
        return int(n)
    else:
        if n == 'A':
            return 1
        else:
            return 0


def validate(cards, cards_jaomue):
    finalizeState = {}
    # schema = winner, paying
    card1 = {
        'card': cards[0],
        'num': getNum(cards[0][0]),
        'dog': cards[0][1]
    }
    card2 = {
        'card': cards[1],
        'num': getNum(cards[1][0]),
        'dog': cards[1][1]
    }
    card3 = {
        'card': '',
        'num': 0,
        'dog': ''
    }
    if len(cards) > 2:
        card3 = {
            'card': cards[2],
            'num': getNum(cards[2][0]),
            'dog': cards[2][1]
        }
    card1_jaomue = {
        'card': cards_jaomue[0],
        'num': getNum(cards_jaomue[0][0]),
        'dog': cards_jaomue[0][1]
    }
    card2_jaomue = {
        'card': cards_jaomue[1],
        'num': getNum(cards_jaomue[1][0]),
        'dog': cards_jaomue[1][1]
    }
    card3_jaomue = {
        'card': '',
        'num': 0,
        'dog': ''
    }
    if len(cards_jaomue) > 2:
        card3_jaomue = {
            'card': cards_jaomue[2],
            'num': getNum(cards_jaomue[2][0]),
            'dog': cards_jaomue[2][1]
        }
    print(card1, card2, card3)

    tame = card1['num'] + card2['num'] + card3['num']
    
    if tame >= 10:
        tame = tame - 10
    print('total_player = ', tame)
    tame_jaomue = card1_jaomue['num']+card2_jaomue['num']+card3_jaomue['num']
    if tame_jaomue >= 10:
        tame_jaomue = tame_jaomue - 10
        #'total_jaomue = ',tame_jaomue
    if tame_jaomue > tame:
        finalizeState['winner'] = 'jaomue'
        print("jaomue_win")
        if card1_jaomue['dog'] == card2_jaomue['dog']:
            print('2deng')  # จ่าย *2
            finalizeState['paying'] = '2'
        elif card1_jaomue['dog'] == card2_jaomue['dog'] == card3_jaomue['dog']:
            print('3deng')  # จ่าย *3
            finalizeState['paying'] = '3'
        elif card1_jaomue['num'] == card2_jaomue['num'] == card3_jaomue['num']:
            print('tong')  # จ่าย *5
            finalizeState['paying'] = '5'
    if tame_jaomue < tame:
        finalizeState['winner'] = 'player'
        print("player_win")
        if card1['dog'] == card2['dog']:
            finalizeState['paying'] = '2'
            print('2deng')
        elif card1['dog'] == card2['dog'] == card3['dog']:
            finalizeState['paying'] = '3'
            print('3deng')
        elif card1['num'] == card2['num'] == card3['num']:
            finalizeState['paying'] = '5'
            print('tong')
    elif tame == 9 or tame == 8:
        if tame == tame_jaomue:
            finalizeState['winner'] = 'jaomue'
            print('เจ้ามือชนะ', 'คนอื่นที่ได้ แต้ม 9 แต้ม 8 ไม่เสียเงิน')
            finalizeState['paying'] = '0'
        else:
            finalizeState['winner'] = 'jaomue'
            finalizeState['paying'] = '1'

    return finalizeState

# print(validate(['9H','8H'],['9H','9H']))
