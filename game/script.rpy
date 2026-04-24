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

# 연출 메서드입니다.

# 전환 애니메이션 출력
label transition_week1:
    window hide

    show week1_transition_anim zorder 100
    pause 2.0
    hide week1_transition_anim

    window show
    return

label transition_week2:
    window hide

    show week2_transition_anim zorder 100
    pause 2.0
    hide week2_transition_anim

    window show
    return

label transition_week3:
    window hide

    show week3_transition_anim zorder 100
    pause 2.0
    hide week3_transition_anim

    window show
    return

# 여기에서부터 게임이 시작합니다.
label start:
# 과거회상_프롤로그
    scene bg_park_day
    "한 남자 아이가 도망가는 것이 보인다. 난 그 아이를 쫓고 있는 듯 하다."   
    show junsung_sil
    "늦게 온 사람이 음료수 사기!"
    hide junsung_sil
    show haeun_sil
    "야! 먼저 뛰면 어떡해."
    show haeun_sil
    "나의 뒤엔 여자 아이 한명이 따라오고 있다."
    "잠깐만 같이 가."

# 재우파트_프롤로그
    scene bg_house_day
    "햇빛이 들어오는 방에서 오전 7시에 맞춘 알람이 울리며 재우가 깨어난다."
    j "오늘도 출근이네…"
    "재우는 병원에 갈 준비를 하면서 오늘 업무에 대해 정리한다."
    j "오늘 환자분은 8명 정도인가?"
    j "일단 서진이한테 4명 정도 넘겨야겠다."
    "그렇게 상담과 출근 준비를 끝낸 뒤 집을 나선다."

# 출근길_프롤로그
    scene bg_street_day
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
    scene bg_bus
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
    scene bg_taxi
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
    scene bg_street_day
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
    scene bg_hospital
    show seojin_emotionless
    "3층의 병원에 들어가자 흰 가운에 네이비 색의 원피스를 입은 여성이 보인다."
    show seojin_emotionless
    hide seojin_emotionless
    j "뭐야, 먼저 왔네? 지하철 공사 때문에 늦을 줄 알았더니."
    show seojin_smile
    d "난 자차로 왔지, 우리 원장님께선 차가 없던가? 하하"
    show seojin_smile
    j "아침부터 활기차네… 부럽다."
    show seojin_smile
    d "근데 너는 아직도 칠칠 맞게 옷에 커피를 흘려?"
    show seojin_smile
    "재우는 옷에 커피가 묻었는지 확인한다."
    show seojin_smile
    j "야! 너 진짜?"
    show seojin_smile
    d "야가 아니라 누나 해봐 누나."
    show seojin_smile
    "여성의 이름은 윤서진, 재우보다 1살 연상이지만 재우의 대학교 시절 친구이자 같은 대학 병원의 동료로 현재는 재우의 병원에서 일하고 있다."
    show seojin_smile
    j "서진씨, 예약하신 분 오실 시간이 되지 않았나요?"
    show seojin_smile
    d "원장님은 불리하실 때 꼭 환자 얘기 하시네요?"
    show seojin_smile
    hide seojin_smile
    j "서진씨?"
    show seojin_emotionless
    hide seojin_emotionless
    d "네네 알겠어요. 원장님. 일단 상담실에 가서 이야기 하죠?"
    
    # 백그라운드 상담실
    scene bg_counsel_day
    show seojin_emotionless
    "서진은 머리를 묶고, 재우와 상담실로 이동해 이야기를 이어간다."
    show seojin_emotionless
    "서진은 머리를 묶고 차트를 가져와 브리핑을 시작한다."
    show seojin_emotionless
    d "아침에 오시는 분들은 여성분 한 분, 남성분 한 분, 총 2분이네요."
    show seojin_emotionless
    j "이 남성분은 저번에 오셨던 분이네요. 서진씨 담당이였나요?"
    show seojin_emotionless
    d "네, 제가 맡을 거 같아요."
    show seojin_emotionless
    d "여성분 쪽은 원래 제가 주치의를 맡고 있던 환자인데 이 분을 원장님이 맡아주세요."
    show seojin_emotionless
    j "네, 그럼 여성분에 대해 브리핑 해주세요."
    show seojin_emotionless
    d "이 분 같은 경우 조금 특이케이스이신 거 같아요."
    show seojin_emotionless
    j "어떤 점에서요?"
    show seojin_emotionless
    d "보통의 환자들은 대부분 틀리더라도 원인을 지목하시는데 이 분은 모르겠다고 하시더라고요."
    show seojin_emotionless 
    d "아예 원인 자체를 잊은 거 같아요. 아무래도 기억장애라고 생각돼요."
    show seojin_emotionless
    j "해리성 기억장애가 의심되는 거 같네요? 정신적으로 큰 충격을 받게 될 때 당시의 기억을 자기방어의 수단으로 잊어버리는 정신 질환이요."
    show seojin_emotionless
    d "네, 저도 그 질환을 의심하고 있어요."
    show seojin_emotionless
    d "처음에 원인의 이유를 모른다고 하셨을 때 다른 환자들처럼 둘러대시는 줄 알았는데"
    show seojin_emotionless
    d "몇 번의 질문에 대해서 답을 하는 모습을 보고 정말로 기억을 잊은 거 같으셨어요."
    show seojin_emotionless
    j "근데 그럼 이분이 내원하신 이유는 무엇 때문이라고 하셨나요?"
    show seojin_emotionless
    d "원인 모를 답답함? 그런 게 있다고 하시더라고요."
    show seojin_emotionless
    j "과거의 기억에서 감정만 그대로 남아 있을 수 있겠네요."
    show seojin_emotionless
    d "그리고 약간의 우울증과 대인기피증의 증상을 보였어요."
    show seojin_emotionless
    hide seojin_emotionless
    j "그렇군요. 서진씨가 상담하셨을 땐 어떤 느낌이였나요?"
    show seojin_sad
    d "음, 그렇네요… 조금 무반응을 하시는 경우가 많았던 거 같아요."
    show seojin_sad
    hide seojin_sad
    d "대답을 해주셔도 단답형이셨고.."
    show seojin_smile
    j "참고해서 상담 진행 해볼게요. 여성분 성함은 어떻게 되시죠?"
    show seojin_smile
    d "\"이하은\"이라고 하셔요. 동갑이신 거 같은데 반하시면 안 되는 거 아시죠?"
    show seojin_smile
    j "서진씨, 걱정마세요. 저는 서진씨처럼 이상한 로맨스 영화 안 보니까요."
    show seojin_smile
    d "그게 무슨 말이죠? 원장님?"
    show seojin_smile
    j "아니에요. 서진씨도 준비하셔야죠."
    show seojin_smile
    d "마음의 준비 하셔야 할 거예요. 제가 봐도 이쁘더라고요."
    show seojin_smile
    j "걱정도 많으시다. 제가 그럴 사람으로 보여요?"
    show seojin_smile
    hide seojin_smile
    d "네." 

    "재우를 놀리며 서진이 상담실을 빠져나간다."

    j "나라도 일해야지. (한숨을 쉰다.)"

    j "(어디선가 들어봤던 거 같은 이름인데… 기분 탓이려나?)"

    "혼자 남은 재우는 환자가 오기 전에 질문 거리를 생각하면서 상담 준비를 한다."

    "상담의 준비를 하던 도중 서진에게서 메일 하나가 왔다."

    j "여성 분에 대한 정보와 함께 상담 당시 작성한 문진표인가?"

    "재우는 전달 받은 문서를 확인한다."

    "신상 정보, 이름, 성별, 나이를 알 수 있었지만 사진의 누락으로 생김새를 알 수 없었고"

    "하은이 작성한 문진표에는 질문과 맞지 않는 답변들로 채워져 있다."

    d "잠을 제대로 주무시지 못하나요?"

    h "...집에 가고 싶어요."

    d "식사에 대해 불편함이 있으신가요?"

    h "...이런 거 그만 하고 싶어요."

    d "지난 한 달 동안 정신적 혹은 육체적으로 감당하기 힘들다고 느낀 적이 있으신가요?"

    h "...지겨워 그만 할래요."

    "객관식이라 체크만 하면 되는 문항에도 불구하고 이런 답변을 하는 것을 보고 재우는 답답함에 한숨을 짓는다."

    j "하아.. 왜 맡겼는지 알겠는데.. 이분 상담은 좀 힘들겠다."

    j "일단 일상 대화 위주로 질문하면서 하은씨의 얘기를 걸어봐야겠다."

    "그렇게 문진표를 보면서 방법을 생각하던 중 하은이의 상담 시간에 맞춘 알람 소리가 상담실을 채웠고"

    "재우는 상담 준비를 마저 끝낸 다음 하은이를 부르며 상담실에 들어오길 기다린다."

    j "이하은씨 들어오세요."
    #하은_첫_상담
    show haeun_emotionless
    "하은이 상담실에 들어오자 백발과 다르게 붉은 눈이 눈에 들어온다."
    show haeun_emotionless
    j "안녕하세요? (어디서 본 거 같은데)"
    show haeun_emotionless
    j "여기 의자에 앉으시죠."
    show haeun_emotionless
    "하은이 의자에 앉았다."
    show haeun_emotionless
    j "안녕하세요. 하은씨, 저는 오늘부터 하은씨의 상담을 맡게 된 김재우라고 합니다."
    show haeun_emotionless
    h "전에 상담하신 분은요?"
    show haeun_emotionless
    hide haeun_emotionless
    j "그분은 다른 업무가 생기셔서요. 아무래도 검진만 맡으실 거 같아요."
    show haeun_mad
    h "거짓말. 날 피하려고 핑계 대는 거지."
    show haeun_mad
    "서진의 문진표와 같이 하은은 잘 협조하지 않는 성격인 듯 하다."
    show haeun_mad
    "하지만 재우는 노련하게 상담을 이어간다."
    show haeun_mad
    hide haeun_mad
    j "정말이에요, 서진 선생님이 일이 많아지셔서 제가 하은씨의 상담을 맡게 된 거예요."
    show haeun_question
    h "정말요?"
    show haeun_question
    hide haeun_question
    j "그럼요. 하은씨가 싫어서가 아니라 서진 선생님이 바쁘셔서 그런 거예요."
    show haeun_emotionless
    h "믿어드릴게요."
    show haeun_emotionless
    j "(휴, 넘어간 건가?)"
    show haeun_emotionless
    j "그럼 소개는 여기까지 하고 이제 상담을 시작할게요."
    show haeun_emotionless
    "재우는 준비했던 질문들로 편안한 분위기를 구성하려 한다."
    show haeun_emotionless
    hide haeun_emotionless
    j "오늘 지하철 공사 때문에 오기 불편하셨을 거 같아요. 어떤 방법으로 오셨나요?"
    show haeun_question
    h "그게 무슨 의미가 있죠?"
    show haeun_question
    hide haeun_question
    j "순수하게 궁금해서요. 저는 보통 지하철을 타고 다니거든요."
    show haeun_emotionless
    j "그런데 오늘 공사를 한다고 해서 다른 방식으로 왔거든요."
    show haeun_emotionless
    h "그게 저와의 상담에 무슨 도움이 되는지 모르겠네요."
    show haeun_emotionless
    "예상은 했으나 더 철벽 같은 대답이 돌아왔다."
    show haeun_emotionless
    j "그럼 좀 더 도움이 될 만한 질문을 할게요."
    show haeun_emotionless
    h "네, 그러시죠."
    show haeun_emotionless
    j "서진씨한테 듣기론 이유 모를 우울감 때문에 오신 건가요?"
    show haeun_emotionless
    h "맞는데요?"
    show haeun_emotionless
    hide haeun_emotionless
    j "혹시 이것 이외에 따로 오시게 된 계기가 있나요? 심적인 변화나 다른 이유 같은 거요."
    show haeun_sad
    h "말하기 싫어요."
    show haeun_sad
    "재우는 하은의 반응에 개인적인 물음을 시도해 본다."
    show haeun_sad
    j "그래도 얘기해주시면 안 될까요?"
    show haeun_sad
    j "어떤 이유로 그런 아픔을 가지셨는지 알아야 할 거 같아요."
    show haeun_sad
    j "(너무 공격적으로 물어본 걸까?)"
    show haeun_sad
    menu:
        h "왜 그렇게 날 도와주려는 거야?"
        "모르겠어요. 하지만 하은씨를 볼 때 마다 도와주고 싶다는 생각이 들어요.":
                hide haeun_sad
                show haeun_question
                j "저도 왜 그랬는지는 모르겠지만"
                show haeun_question
                j "하은씨를 볼 때마다 저도 뭔가 모를 감정이 떠올라요."
                show haeun_question
                j "하은씨는 이 감정이 우울감이신 거니까... 하은씨를 더욱 도와드리고 싶네요."
                show haeun_question
                hide haeun_question
                "재우는 하고 싶은 말을 하고 얼굴이 붉어진 것을 느낀다."
                show haeun_happy 
                h "선생님은 솔직하신 분이시군요."
                show haeun_happy
                h "말해드릴게요."
                show haeun_happy
                j "고마워요."
                show haeun_happy
                h "우울감에서 벗어나서 자유로워지고 싶어요."
                show haeun_happy
                hide haeun_happy
                h "우울한 이유를 몰라요. 그걸 알고 싶어요."
                show haeun_emotionless
                hide haeun_emotionless
                j "대답하시기 힘드셨을 텐데 이야기해주셔서 감사합니다."
                jump firstmeeting_pro

        "의사니까요. 저는 하은씨를 도와드리고 싶어요.":
                hide haeun_sad
                show haeun_emotionless
                h "감사합니다. 그냥 우울했어요."
                show haeun_emotionless
                j "그 이유를 알고 계신가요?"
                show haeun_emotionless
                h "몰라요. 그걸 알려주세요."
                show haeun_emotionless
                hide haeun_emotionless
                j "고마워요."
                jump firstmeeting_pro

        "죄송합니다. 그래도 저는 알아야 할 의무가 있어요.":
                show haeun_sad
                hide haeun_sad 
                h "의무니까 알고 싶으신 건가요?"
                show haeun_emotionless
                j "너무 말이 강했던 거 같네요. 하지만 저도 하은씨를 돕고 싶어요."
                show haeun_emotionless
                h "뭔가 우울했어요. 이유는 모르겠네요."
                show haeun_emotionless
                j "그 이유를 알고 싶어서 오신 건가요?"
                show haeun_emotionless
                hide haeun_emotionless
                h "네."
                jump firstmeeting_pro

label firstmeeting_pro:
    scene bg_counsel_day
    show haeun_emotionless
    j "시간이 된 거 같네요."
    show haeun_emotionless
    h "그렇네요."
    show haeun_emotionless
    j "다음 상담 시간은 몇 시로 할까요? 지금 시간처럼 할까요?"
    show haeun_emotionless
    h "지금 시간으로 할게요."
    show haeun_emotionless
    j "네, 알겠습니다."
    show haeun_emotionless
    j "오늘 상담 고생하셨어요."
    show haeun_emotionless
    h "네."
    show haeun_emotionless
    "두 명은 상담실에서 같이 나왔다."
    show haeun_emotionless
    "재우는 하은이가 엘리베이터를 타고 나가는 모습을 보면서 손을 흔들며 인사한다."
    show haeun_emotionless
    hide haeun_emotionless
    "하은이는 재우의 인사를 무시한 채 내려갔다."

    j "휴, 생각보다 힘들었다."

    "재우는 마무리를 한 뒤 귀가 준비를 한다."
    scene bg_street_night
    "재우는 업무를 마치고 집으로 향한다."

    j "다행이다. 공사가 끝났네."

    "재우는 지하철을 타고 집으로 향했다."
    scene bg_house_night
    j "드디어 집이다..."

    "재우는 저녁을 먹고 씻은 뒤 소파에 눕는다."

    j "상상 이상의 강적이었다, 날 돌발 행동을 하게 할 줄이야."

    j "서진이한테 들키면 혼날 거 같은데..."

    "하은과의 상담을 생각하다 재우는 잠에 든다."
jump pastevent1

label pastevent1:
    scene bg_class_day
    show dim_past
    "지지직..."

    "교실의 창문 밖으로 두 명의 학생이 뛰어가는 것이 보인다."
    show haeun_sil
    hide haeun_sil
    "쫓아오지 마!!!"
    show junsung_sil
    hide junsung_sil
    "잠깐만! 내 말 좀 들어봐!"
    show haeun_sil
    hide haeun_sil
    "싫어!"
    show junsung_sil
    hide junsung_sil
    "야! 기다려봐! 잠깐만!"
    hide dim_past
    jump week01_start



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
