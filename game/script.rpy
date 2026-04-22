# 이 파일에 게임 스크립트를 입력합니다.

default week = 1
default affection = 0
default saw_date_event = False

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('아이린', color="#c8ffc8")

# 여기에서부터 게임이 시작합니다.
label start:

    e "프롤로그입니다."
   
    e "너 나 좋아해?"

menu:
    "1.응 좋아해":
        e "우와 기뻐"

    "2.그럭저럭":
        e "너무해"

    "3.아니 전혀":
        e "흠"
    
    e "그럼그럼 너 나 좋아해?"
    
menu:
    "1.응 좋아해":
        e "우와 기뻐"

    "2.그럭저럭":
        e "너무해"

    "3.아니 전혀":
        e "흠"

jump week1

label week1:
    $ affection = 0

    "1주차 시작"

e "나는 귀여워?"

menu:
    "1.응 귀여워":
        $ affection += 2
        e "우와 기뻐"

    "2.그럭저럭":
        $ affection += 1
        e "너무해"

    "3.아니 전혀":
        $ affection += 0
        e "흠"

e "귀여워어어?"

menu:
    "1.응 귀여워":
        $ affection += 2
        e "우와 기뻐"

    "2.그럭저럭":
        $ affection += 1
        e "너무해"

    "3.아니 전혀":
        $ affection += 0
        e "흠"
    
if affection >= 2:
        "회상 1 해금!"

jump week2

if affection < 2:
    jump week2

label week2:
    $ affection = 0

    "2주차 시작"

    e "나는 멋있어?"

menu:
    "1.응":
        $ affection += 2
        e "우와 기뻐"

    "2.뭐 그냥 그래":
        $ affection += 1
        e "너무해"

    "3.놉":
        $ affection += 0
        e "흠"

e "너를 좋아하는 것 같아."

menu:
    "1.응":
        $ affection += 2
        e "우와 기뻐"

    "2.뭐 그냥 그래":
        $ affection += 1
        e "너무해"

    "3.놉":
        $ affection += 0
        e "흠"
    
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

    e "안녕"

menu:
    "1.응 반가워":
        $ affection += 2
        e "우와 기뻐"

    "2.응":
        $ affection += 1
        e "너무해"

    "3.안 반가움":
        $ affection += 0
        e "흠"

menu:
    "1.응 반가워":
        $ affection += 2
        e "우와 기뻐"

    "2.응":
        $ affection += 1
        e "너무해"

    "3.안 반가움":
        $ affection += 0
        e "흠"
    
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
