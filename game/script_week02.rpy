label week02_start:
    call transition_week2 from _call_transition_week2
    jump jaewoo_wakeup2

label jaewoo_wakeup2:
    scene bg_house_day
    "오전 7시의 알람이 울린다."

    j "뭔가가 이어지는 거 같아..."
    j "여자 아이와 남자아이는 왜 싸운걸까?"
    j "뭔가 어디서 보았던 것 같은데..."
    j "하은씨랑 겹쳐 보이는 건 기분 탓일까?"
    j "출근 해야지..."

    "재우는 출근 할 준비를 마치고 집을 나선다."
    # 출근길
    scene bg_street_day
    j "역시 출근길은 지하철이 최고야."
    j "오늘은 하은씨 상태가 나아졌으면 좋겠다."

    "재우는 지하철을 타고 병원으로 향했다."

    jump talk_with_seojin

label talk_with_seojin:
    scene bg_hospital
    "병원에 출근하자마자 재우는 서진에게 손이 잡힌 채 상담실로 끌려간다."
    show seojin_emotionless as actor
    d "재우야 어떻게 한 거야?"

    j "응? 왜 그래?"

    d "시치미 떼지 마, 하은씨한테 뭘 한 거야?"

    j "뭘 말하는 거야?"
    j "(설마 최악의 상황?)"
    hide actor
    show seojin_smile as actor
    d "어떻게 했길래 하은씨 상태가 좋아진 거야?"

    j "하은씨가?"

    d "응, 어머니께서 전화가 왔었는데 하은씨가 방에서 나온 거 뿐만 아니라!"

    d "하은씨가 어머니와 식사도 같이 하셨다는 거야!"

    j "기존엔 달랐었어?"

    d "응. 하은씨가 전에는 어머니 출퇴근 시간에 맞춰서 식사를 드시거나"

    d "어머니께서 방문 앞에 식사를 놓으면 방 안에서 드셨다고 하는데."

    d "지금은 하은씨가 직접 방에서 나와서 같이 식사하자고 이야기했다고 하시더라."

    d "어머니께서 이 정도로 상태가 나아질 지 몰랐다고 좋아하시더라고."

    d "대인 기피증이 있으셨던 하은씨가 스스로 방에서 나오다니 역시 원장님은 다르네."

    j "내가 뭘."

    "재우가 어깨를 으쓱인다."

    d "원장님 오늘만큼은 인정할게."

    d "어떻게 한 거야? 나도 배울래."

    d "설마 하은씨한테 손댄 건 아니겠지?"

    "재우는 손사래를 친다."

    j "설마 내가 그렇겠어? (일단 둘러대자.)"

    d "얼굴이 붉은데? 우리 원장님 원칙 잊은 거 아니지?"

    j "당연하지! 환자는 환자!"
    hide actor
    show seojin_emotionless as actor
    d "근데 왜 얼굴이 붉어지셨을까?"
    hide actor
    show seojin_smile as actor
    d "장난이야."

    "서진은 재우의 명치를 툭 친다."

    d "난 우리 원장님 믿고 있어."

    j "응. 그래. (잘 넘어간 거겠지?)"
    hide actor
    show seojin_sad as actor
    d "날 버린 건 아니지, 재우야? 흑흑."

    j "장난은 여기까지 해 줘. (얼굴이 붉어진다.)"
    hide actor
    show seojin_smile as actor
    d "그래. 우리 원장님이 원래부터 여자에 약하시긴 하셨지."

    j "뭐래?"

    d "난 먼저 상담실로 가볼게. 하은씨 밝아지신 거 진짜 보기 좋더라."

    j "응, 너도 힘내고."

    d "네, 원장님."

    jump talk_with_haeun1

label talk_with_haeun1:
    scene bg_counsel_day
    show haeun_emotionless as actor
    "재우가 상담실로 이동해 상담 준비를 마칠 무렵 하은씨가 도착했다."
    hide actor
    j "흠흠... (목을 풀면서) 하은씨 들어오세요."
    show haeun_emotionless
    "하은이 방으로 들어온다. 하은의 상태가 무척이나 괜찮아진 것처럼 보인다."

    j "안녕하세요, 하은씨."
    hide haeun_emotionless
    show haeun_happy as actor
    h "안녕하세요, 선생님."

    j "오늘은 뭔가 적극적이시네요."

    h "그런가요? 헤헤."

    "하은이 자리에 앉아 손을 만지작거린다."

    j "오늘 기분이 좋으신 것 같아요."

    h "뭔가... 표현하기 어려운 것 같아요..."

    j "그러시군요. 일단 상담을 진행하기에 앞서 간단한 이야기를 나누죠."
    hide actor
    show haeun_question as actor
    h "네. 무슨 이야기를 나누면 좋을까요?"

    "하은은 고개를 갸우뚱거리며 재우를 쳐다본다."

    j "하은님은 보통 방에서 어떤 걸 하시나요?"
    hide actor
    show haeun_emotionless
    h "...음, 저는요... 책을 읽는 것 같아요."

    j "어떤 책을 좋아하시나요?"

    h "소설책을 주로 읽고 있어요."

    j "특별히 좋아하시는 책이 있으신가요?"

    h "어... '어린 왕자'를 가장 좋아하는 것 같아요."

    j "좋아하시는 이유가 있으신가요?"

    h "좋아하는 이유라... 글쎄요..."

    h "장미꽃 때문일까요?"

    j "어린 왕자가 키우던 장미꽃이요?"
    hide actor
    show haeun_happy as actor
    h "어려운 환경 속에서도 예쁘게 피어 있잖아요."

    h "저도 그런 장미꽃이 되고 싶어요."

    "하은의 두 눈이 반짝이는 것 같다."

    j "슬슬 상담을 시작해 볼까요?"

    h "네. 좋아요."

    j "상태가 많이 좋아지신 것 같아서 다행인 것 같아요. 계기가 있으셨나요?"

    h "저번에 선생님이랑 상담을 하고 나서 스스로 생각을 좀 해봤어요."

    h "이별에 관한 이야기를 듣고 나서 우울감이 조금씩 줄어드는 듯한 느낌이 들어요."
    hide actor
    show haeun_sad as actor
    h "아직은 가끔씩 이유 모를 우울감이 찾아오긴 하지만 많이 괜찮아진 것 같아요."

    j "일단 저번에 이어서 상담을 해보도록 하죠."
    hide actor
    show haeun_emotionless as actor
    j "하은씨의 과거 이야기를 더 듣고 싶어요."

    h "친구에 관한 이야기였나요? 네."

    h "음... 정확하지는 않지만... 아마 중학교 때일 거예요."

    h "중학교 때 3명이서 같이 공원을 돌아다니는 꿈을 꿔요."

    h "저의 앞에 두 명의 남자아이들이 달려가는 것이 보여요."
    hide actor
    show haeun_cured_sad as actor
    h "동시에 가슴이 먹먹거리면서 동시에 두근두근거리는 것 같아요."

    j "힘드시면 천천히 하셔도..."

    h "괜찮아요, 선생님."

    j "(뭔가 어디서 본 것 같은 꿈이다. 설마...)"

    h "선생님. 이 감정은 무엇일까요? 이게 사랑인가요?"

    h "선생님은 사랑을 하신 적이 있나요?"

    "갑작스러운 질문에 재우는 당황한다."

    menu:
        h "대답해 주세요."

        "저희 어머니를 사랑합니다.":
            show haeun_question as actor
            j "저희 어머니를 사랑합니다."
            h "...선생님?"
            j "네?"
            hide actor
            show haeun_mad as actor
            h "아니에요." 
            hide actor
            jump haeun_bad_ending

        "저도 프라이버시가 있어요.":
            show haeun_sad as actor
            j "저도 프라이버시가 있어요."
            hide actor
            show haeun_mad as actor
            h "...저랑 상담을 하고 있던 게 맞나요?"
            j "죄송합니다."
            hide actor
            jump haeun_bad_ending

        "글쎄요... 중학교 때 있었던 거 같아요.":
            show haeun_sad as actor
            j "글쎄요... 중학교 때 있었던 거 같아요."
            hide actor
            show haeun_emotionless as actor
            h "더 이야기해 주실 수 있나요?"
            j "네, 저도 정확하게는 기억나지 않지만..."
            j "무언가 그 시절을 생각하면 '사랑이란 게 이런 게 아닐까?'라는 생각을 해요."
            hide actor
            show haeun_question as actor
            h "선생님은 그게 사랑인지 어떻게 아시는 건가요?"
            j "잘은 설명하지 못하겠지만..."
            j "볼수록 더 보고 싶고, 생각할수록 더 생각나는 그런 게 아닐까요?"
            hide actor 
            show haeun_happy as actor
            h "네... 어느 정도 알 것 같아요." 
            hide actor
            jump talk_with_haeun2

label talk_with_haeun2:
    scene bg_counsel_day
    show haeun_happy as actor
    j "이어서 상담을 진행해 볼까요?"
    hide actor
    show haeun_emotionless as actor
    h "네, 선생님. 어쩌면 이 답답함이 우울함의 원인일 수도 있을 것 같아요."

    j "비슷한 감정을 느끼는 대상이 있으신가요?"

    h "음... 비슷하진 않지만 트럭을 볼 때마다 조금씩 답답한 게 있는 것 같아요."

    j "트럭이라... 사고가 있으셨던 건가요?"
    hide actor
    show haeun_sad as actor
    h "어... (머리를 쥔다.)"

    "하은이 괴로운 신음 소리를 낸다."

    j "괜찮으신가요?"

    h "뭔가 잊으면 안 되는 걸 잊은 것 같아요."

    j "힘드시면 그만두셔도 괜찮아요."

    h "선생님..."

    "하은이 재우를 향해 손을 뻗는다."

    h "손을 잡아주실 수 있나요?"

    menu:
        j "(이래도 되는 걸까?)"
       
        "고소가 무서워 서진이를 불러 대신 안심시킨다.":
            show haeun_sad as actor
            j "(잠깐만... 고소당하는 거 아니야?)"
            j "안 됩니다."
            h "...그러시겠죠."
            hide actor
            jump haeun_bad_ending

        "하은의 손을 잡는다.":
            show haeun_sad as actor
            j "(이래도 되는 걸까?)"
            "재우가 하은의 손을 잡는다."
            "하은의 신음 소리가 줄어든다."
            h "감사합니다..."
            hide actor
            jump talk_with_haeun3

        "하은을 멈춘다.":
            show haeun_sad as actor
            j "(아무래도 신체 접촉은 좀 부담스럽지.)"
            j "하은님, 괜찮아요. 무리하지 않아도 돼요."
            h "그렇지만... 앞으로 조금 남은 것 같은데..."
            j "괜찮다니까요?"
            hide actor
            jump haeun_bad_ending
    
label talk_with_haeun3:
    scene bg_counsel_day
    show haeun_emotionless as actor
    h "선생님, 이제 괜찮아요..."
    hide actor
    show haeun_happy as actor
    h "다시 한번 감사합니다."

    "마침 상담을 마칠 시간이 되었다."

    j "수고하셨어요, 하은씨."

    h "선생님도요."
    scene bg_hospital
    "재우는 하은의 배웅을 나가 손을 흔든다."

    h "(손을 흔들며) 다음에 뵐게요, 선생님."

    "재우는 엘리베이터 문이 닫힐 때까지 손을 흔들었다."
    hide actor
    jump jaewoo_return_home

label jaewoo_return_home:
    scene bg_street_night
    "재우도 마무리를 한 뒤 집으로 향하자 밤이 되었다."

    j "오늘도 수고했다, 나 자신."
    scene bg_house_night
    "재우는 집으로 돌아와 잘 준비를 마치고 잠자리에 든다."
    show haeun_happy as actor
    j "하은씨 보기 좋아져서 다행이다."
    hide actor
    "재우는 하은에 대한 생각을 하며 잠에 들었다."
    jump past_event3

label past_event3:
    scene bg_street_afternoon
    show dim_past
    "울면서 달리고 있는 여자아이의 실루엣이 보인다."
    show junsung_mad as actor
    p_hidden "멈춰! 이하은!"
    hide actor
    show haeun_past_mad as actor
    "남자아이의 소리에 소녀(하은)가 멈춰 선다."
    hide actor
    show junsung_surprised as actor
    p_hidden "안 돼!"
    "남자아이가 하은을 밀친다."
    hide actor
    show haeun_past_surprised as actor
    h "준성아!!!"
    hide actor
    hide dim_past
    jump date_start