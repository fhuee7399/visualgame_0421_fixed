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
define d = Character("서진")
define p = Character("준성")

# 여기에서부터 게임이 시작합니다.
label start:
# 과거회상_프롤로그
    "한 남자 아이가 도망가는 것이 보인다. 난 그 아이를 쫓고 있는 듯 하다."
   
    "늦게 온 사람이 음료수 사기."
    "야! 먼저 뛰면 어떡해."
    "나의 뒤엔 여자 아이 한명이 따라오고 있다."
    "잠깐만 같이 가."

# 재우파트_프롤로그
    "햇빛이 들어오는 방에서 오전 7시에 맞춘 알람이 울리며 재우가 깨어난다."
    j "오늘도 출근이네…"
    "재우는 병원에 갈 준비를 하면서 오늘 업무에 대해 정리한다."
    j "오늘 환자분은 8명 정도인가?"
    j "일단 서진이한테 4명 정도 넘겨야겠다."
    "그렇게 상담과 출근 준비를 끝낸 뒤 집을 나선다."

# 출근길_프롤로그
    "거리로 나선 재우는 평소와 같이 지하철을 타려간다."
    j "아 맞다 오늘 공사하는 날이였던가?"
    "재우는 집앞의 병원으로 향하는 버스 정류장으로 향한다."

menu:
    j "어떤 걸 타고 갈까?"
    "버스":
        jump bus_pro

    "택시":
        jump taxi_pro

    "걸어가기":
        jump walk_pro

label bus_pro:
    j "저기 버스가 오네. 딱 좋은 타이밍인걸?"
    "출근 시간의 버스 답게 많은 사람들이 타고 있다."
    "재우는 수많은 사람들에 끼이게 되었다."
    j "어우 내 병원 가는 것도 이렇게 고생해야 돼?"
    "누군가가 의도치 않게 재우의 명치를 친다."
    j "어억!!.."
    j "팔꿈치로 명치를 맞다니… 이래서 출근시간 버스는 지옥이라는 건가?"
    j "아프다… 언제 도착하지?"
    "때마침 버스가 병원에 서게 된다."
    j "드디어!"
    "재우는 빠르게 버스에서 내려 병원으로 향한다."
jump hospital_pro

label taxi_pro:
    j "오 택시는 오랜만인걸? 여기요!"
    "재우는 택시를 향해 손을 흔든다."
    "택시가 재우의 앞에 멈추고 재우는 택시에 탑승한다."
    j "OO병원으로 가주세요."
    "택시는 병원을 향했다."
    j "(기본요금 4800원?? 왜 이렇게 비싸?)"
    "재우는 자신의 지갑을 쳐다본 후 택시의 미터기를 확인한다."
    "재우의 애처로운 눈과 다르게 빠른 속도로 택시 금액이 오른다."
    j "(헉 설마 아니겠지? 카드에 얼마가 있었더라?)"
    "택시가 병원에 도착하고 재우가 결제를 하고 택시에서 내린다."
    j "휴 다행이다. 택시는 다시 못타겠는 걸…."
jump hospital_pro

label walk_pro:
    j "오랜만에 걸어가볼까?"
    "재우는 병원을 향해 걷기 시작했다."
    j "가끔씩을 걸어가볼까? 생각보다 좋다."
    "재우는 주변을 둘러보며 천천히 나아간다."
    "5분 정도 걷자 재우는 다리에 피로를 느낀다."
    j "어우 다리 아파… 운동 좀 할걸…"
    j "병원 가면 땀으로 젖는거 아니야?"
    "병원까지 남은 길을 보니 오르막길이 보인다."
    j "이것만 오르면…"
    "재우는 열심히 오르막길을 올랐다."
    j "어우 드디어 도착했다!!!"
    "주변 사람들이 재우를 바라본다."
    j "(뻘줌하네. 빨리 들어가야지.)"
    "재우는 건물에 들어가 자신의 병원인 3층으로 향한다."
jump hospital_pro

label hospital_pro:
    "3층의 병원에 들어가자 흰 가운에 네이비 색의 원피스를 입은 여성이 보인다."


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
