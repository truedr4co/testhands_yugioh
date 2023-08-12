import numpy as np

# empty deck
deck = []


# fill it with
def runick_generic_gen(n):
    for i in range(n):
        yield "Runick_QP_spell"


def level2_body_gen(n):
    for i in range(n):
        yield "Level_2_Body"


def other_card_gen(n):
    for i in range(n):
        yield "OtherCard"


for v in runick_generic_gen(16):
    deck.append(v)

for v in level2_body_gen(13):
    deck.append(v)

for v in other_card_gen(9):
    deck.append(v)

for card in range(2):
    deck.append("RunickFountain")

# check deck size
print("Deck size: " + str(len(deck)))

# check a sample hand
samplehand1 = np.random.choice(deck, size=5, replace=False)
samplehand1_list = list(samplehand1)
print("\nSample Hand")
print(samplehand1_list)



# score as follows
# get to fountain , empty emz, then activate a rqps
def score_hand(hand):
    fountains = hand.count("RunickFountain")
    rqps = hand.count("Runick_QP_spell")
    lvl2bodies = hand.count("Level_2_Body")
    if rqps >= 2 and lvl2bodies >= 1:
        return 1
    elif rqps == 1 and lvl2bodies >= 1 and fountains >= 1:
        return 1
    else:
        return 0


testscore = score_hand(samplehand1_list)
print("\n" + "Testhand success?: " + str(testscore))


def result_gen(n):
    for i in range(n):
        yield score_hand(list(np.random.choice(deck, size=5, replace=False)))


test_hand_list = []
for v in result_gen(100000):
    test_hand_list.append(v)

print("\nMean of 100k tests:")
print(np.mean(test_hand_list))





