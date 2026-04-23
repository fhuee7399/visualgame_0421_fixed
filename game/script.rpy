# 이 파일에 게임 스크립트를 입력합니다.

default week = 1
default affection = 0
default expaffection = 0
default saw_date_event = False

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define j = Character("재우")
define h = Character("하은")
define d = Character("주치의")
define p = Character("준성")

# 여기에서부터 게임이 시작합니다.
label start:

    p "프롤로그입니다."
   
    h "너 나 좋아해?"

menu:
    "1.응 좋아해":
        d "우와 기뻐"

    "2.그럭저럭":
        j "너무해"

    "3.아니 전혀":
        j "흠"
    
    h "그럼그럼 너 나 좋아해?"
    
menu:
    "1.응 좋아해":
        h "우와 기뻐"

    "2.그럭저럭":
        h "너무해"

    "3.아니 전혀":
        h "흠"

jump week1

label week1:
    $ affection = 0

    "1주차 시작"

h "나는 귀여워?"

menu:
    "1.응 귀여워":
        $ affection += 2
        $ expaffection += 2
        h "우와 기뻐"

    "2.그럭저럭":
        $ affection += 1
        $ expaffection += 1
        h "너무해"

    "3.아니 전혀":
        $ affection += 0
        $ expaffection += 0
        h "흠"

h "귀여워어어?"

menu:
    "1.응 귀여워":
        $ affection += 2
        $ expaffection += 2
        h "우와 기뻐"

    "2.그럭저럭":
        $ affection += 1
        $ expaffection += 1
        h "너무해"

    "3.아니 전혀":
        $ affection += 0
        $ expaffection += 0
        h "흠"
    
if affection >= 2:
        "회상 1 해금!"

        jump week1feedback


if affection < 2:

    jump week1feedback

label week1feedback:
if affection <= 1:
    j "낮은 피드백"


elif 1 < affection < 4:
    j "중간 피드백"


else:
    j "높은 피드백"

jump week2

label week2:
    $ affection = 0

    "2주차 시작"

    d "나는 멋있어?"

menu:
    "1.응":
        $ affection += 2
        d "우와 기뻐"

    "2.뭐 그냥 그래":
        $ affection += 1
        d "너무해"

    "3.놉":
        $ affection += 0
        d "흠"

j "너를 좋아하는 것 같아."

menu:
    "1.응":
        $ affection += 2
        j "우와 기뻐"

    "2.뭐 그냥 그래":
        $ affection += 1
        j "너무해"

    "3.놉":
        $ affection += 0
        j "흠"
    
if affection < 3:
        jump bad_ending

if affection >= 5:
        "회상 2 해금"

if affection >= 7:
        $ saw_date_event = True
        jump date_event

jump week3

label week3:
    $ affection = 0

    "3주차 시작"

    h "안녕"

menu:
    "1.응 반가워":
        $ affection += 2
        h "우와 기뻐"

    "2.응":
        $ affection += 1
        h "너무해"

    "3.안 반가움":
        $ affection += 0
        h "흠"

menu:
    "1.응 반가워":
        $ affection += 2
        d "우와 기뻐"

    "2.응":
        $ affection += 1
        d "너무해"

    "3.안 반가움":
        $ affection += 0
        d "흠"
    
if affection >= 9:
    "회상 3 해금"

jump final_branch

if affection < 9:
    jump final_branch

label final_branch:

    if affection < 5:
        jump bad_ending

    if not saw_date_event:
        jump normal_ending

    if final_piece:
        jump true_ending

    jump good_ending

label bad_ending:
    "배드 엔딩"
    return

label normal_ending:
    "노멀 엔딩"
    return

label good_ending:
    "굿 엔딩"
    return

label true_ending:
    "트루 엔딩"
    return
