label date_start:
    scene black with Fade(1.0, 2.0, 0.0)
    jump date_wake_up

label date_wake_up:
    scene bg_house_day with Fade(0.0, 0.0, 1.0)
    stop music fadeout 1.0
    play music "audio/bgm/date/date_wake_up.mp3" fadein 1.0
    "병원이 쉬는 날 오전 7시의 알람이 울린다."
    j "병원 쉬는 날이었구나... 오늘은 뭐 하지?"
    j "산책이나 할까? 운동을 안 한 지 너무 오래된 것 같아…"
    "재우는 간단하게 옷을 차려입고 커피를 마시며 밖으로 나선다."
    jump date_cafe

label date_cafe:
    scene bg_street_day
    stop music fadeout 1.0
    play music "audio/bgm/date/date_goto_cafe.mp3" fadein 1.0
    j "어딜 갈까? 흠...."
    j "그래. 오랜만에 근처 카페쪽으로 가보자."
    "재우는 카페로 향했다."
    scene bg_cafe
    stop music fadeout 1.0
    play music "audio/bgm/date/date_cafe.mp3" fadein 1.0
    "카페에 도착하자 향긋한 커피 냄새에 고개를 돌리자 예상치 못한 얼굴과 마주쳤다."
    show haeun_date_question as actor
    h "...선생님?"
    j "하은 씨. 여기는 자주 들리시나요?"
    show haeun_date_happy as actor
    h "아니요. 오늘 처음이에요. 근처 왔다가."
    j "하은 씨, 같이 들어갈까요?"
    show haeun_date_question as actor
    "하은은 짧게 눈을 깜빡였다. 아무래도 예상치 못한 모양이다."
    show haeun_date_happy as actor
    h "...같이요? 네. 좋아요."
    "하은과 같이 자리에 앉아 메뉴판을 본다."
    show haeun_date_default as actor
    j "뭐 마실지 정했어요?"
    show haeun_date_question as actor
    h "...음 선생님은요?"
    j "저는 아메리카노요. 하은 씨는 어떤 걸 좋아하시나요? 달달한 거?"
    show haeun_date_happy as actor
    h "...달달한 거 좋아해요. 저는 라떼로 할게요."
    "몇 분정도가 지난 후 음료가 나오고 약간의 어색한 침묵 후"
    show haeun_date_question as actor
    h "선생님은 어쩌다 이곳에?"
    j "(하은 씨가 먼저 말을 걸다니) 어쩌다보니?"
    show haeun_date_default as actor
    h "저는 서점에 들르는 길이였어요."
    "하은은 그렇게 말한뒤 라떼를 마시는 척 얼굴이 붉혀진 걸 감춘다."
    "하은은 뭔가를 기대하는 듯 하다."
    j "저도 같이 가도 될까요?"
    show haeun_date_happy as actor
    h "(고개를 끄덕이며) 네!"
    j "(정답이였던 모양이네...)"
    scene bg_street_day
    show haeun_date_happy as actor
    "하은과 재우는 카페를 나서 서점으로 향했다."
    show haeun_date_question as actor
    "길을 가던 도중, 하은이 재우를 올려다 보며 물어본다."
    menu:
        h "...선생님. 저희는 오늘 우연히 만난건가요?"
        "당연하죠. 왜요?":
            jump date_cafe_1
        "왜 그런 걸 물어보시나요?":
            jump date_cafe_2
        "...우연이 아니었으면 좋았나요?":
            jump date_cafe_3
    show haeun_date_default as actor
    "서점이 바로 앞에 보이는 듯하다."
    jump date_bookstore

label date_cafe_1:
    scene bg_street_day
    stop music fadeout 1.0
    play music "audio/bgm/date/date_cafe_1.mp3" fadein 1.0
    show haeun_date_question as actor
    j "당연하죠. 왜요?"
    show haeun_date_default as actor
    h "...아니요. 그냥. 확인하고 싶었어요."
    j "확인이요?"
    h "...네. 그냥요."
    j "(뭔가 마음에 걸리는 말이네.)"
    jump date_bookstore

label date_cafe_2:
    scene bg_street_day
    stop music fadeout 1.0
    play music "audio/bgm/date/date_cafe_2.mp3" fadein 1.0
    show haeun_date_question as actor
    j "왜 그런 걸 물어보시나요?"
    show haeun_date_sad as actor
    h "...그냥...물어보면 안 되나요?"
    "하은은 재우를 올려다 본다. 어쩐지 눈물이 글썽이는 것처럼 보인다."
    j "아니에요. 아니에요. 장난이에요. 장난."
    j "(사고친 걸까...)"
    jump date_bookstore

label date_cafe_3:
    scene bg_street_day
    stop music fadeout 1.0
    play music "audio/bgm/date/date_cafe_3.mp3" fadein 1.0
    show haeun_date_question as actor
    j "...우연이 아니었으면 좋았나요?"
    show haeun_date_default as actor
    h "(귀가 붉어진다.) ...그, 그런게 아니라요."
    "하은이 고개를 푹 숙인다."
    j "알아요, 농담이에요. (...미안한데, 조금 귀엽다.)"
    jump date_bookstore

label date_bookstore:
    scene bg_bookstore
    stop music fadeout 1.0
    play music "audio/bgm/date/date_bookstore.mp3" fadein 1.0
    show haeun_date_default as actor
    h "여기에요. 서점..."
    show haeun_date_happy as actor
    "골목 안쪽에 자리한 작은 서점이였다. 간판도 수수하고, 문도 좁았다."
    j "자주 오시나요, 여기?"
    h "가끔씩이요. 작아서 좋아요..."
    j "작아도 감성적이어서 저도 좋은 거 같아요."
    "각자 천천히 책을 구경한다. 재우는 책을 구경하다 익숙한 책을 발견했다."
    j "이거 좋아하신다고 하셨죠?"
    show haeun_date_question as actor
    h "...기억 하시나요?"
    j "3번째 상담이였나요?"
    show haeun_date_happy as actor
    "하은은 눈을 한 번 깜빡였다. 그러고는 책 등을 살짝 건드린다."
    j "좋아하시는 대사 같은게 있으신가요?"
    show haeun_date_default as actor
    h "있어요. '사막이 아름다운 건 어딘가에 우물을 감추고 있기 때문'이라는 부분이요."
    j "왜 그 부분인가요?"
    h "음... 안 보여도 있는 거니까요, 그래서 좋은 거 같아요."
    show haeun_date_question as actor
    menu:
        h "선생님은요? '어린 왕자'에서 기억에 남는 대사가 있으신가요?"
        "\"가장 중요한 건 눈에 보이지 않아.\"일까요?":
            jump date_bookstore_1
        "대사는 아니지만... 마지막 장면이요.":
            jump date_bookstore_2
        "바로 대답하지 못하고 잠깐 생각한다.":
            jump date_bookstore_3
    show haeun_date_happy as actor
    "책을 고른 하은의 결제를 마친 후, 서점의 밖으로 나간다."
    show haeun_date_question as actor
    h "…공원, 지나서 가는 길이에요?"

label date_bookstore_end:
    scene bg_bookstore
    stop music fadeout 1.0
    play music "audio/bgm/date/date_bookstore_end.mp3" fadein 1.0
    show haeun_date_question as actor
    j "같이 바람 쐬다 갈까요?"
    show haeun_date_happy as actor
    h "네... 좋아요."
    j "(나도 그녀에게 길들여지고 있는 중인걸까?)"
    jump date_park

label date_bookstore_1:
    scene bg_bookstore
    stop music fadeout 1.0
    play music "audio/bgm/date/date_bookstore_1.mp3" fadein 1.0
    show haeun_date_question as actor
    j "\"가장 중요한 건 눈에 보이지 않아.\"일까요?"
    "그녀가 천천히 재우를 봤다."
    h "그렇네요... 선생님의 가장 중요한 건 무엇인가요?"
    j "(저 질문의 의도는 무엇일까...) 음... 잘 모르겠지만... 지금일까요?"
    show haeun_date_happy as actor
    h "그런가요? (방긋 웃는다.)"
    j "대답이 마음에 드셨다면 다행이네요. (어떤 생각을 하고 있을까?)"
    jump date_bookstore_end

label date_bookstore_2:
    scene bg_bookstore
    stop music fadeout 1.0
    play music "audio/bgm/date/date_bookstore_2.mp3" fadein 1.0
    show haeun_date_question as actor
    j "\"네 장미를 소중하게 만드는 건 그 장미를 위해 네가 쓴 시간이야.\"라는 대사가 생각나요."
    h "...왜 그 부분이에요?"
    j "관계라는 것이 따로 있지 않다는 것을 보여주는 것이 좋아요."
    h "무슨 의미 인가요?"
    j "저의 시간을 누군가에게 바친다면 그것이 관계로써 꽃피우는 것이라는 의미라고 생각해요."
    show haeun_date_default as actor
    h "...저는 그 부분, 좀 무서울지도 모르겠어요."
    j "왜요?"
    h "...시간을 써도, 꽃피우지 못한다면요?"
    j "저는 그렇더라도 꽃을 피우기 위해 노력할 것 같아요."
    h "하은은 괜히 자신의 옷을 매만졌다."
    jump date_bookstore_end

label date_bookstore_3:
    scene bg_bookstore
    stop music fadeout 1.0
    play music "audio/bgm/date/date_bookstore_3.mp3" fadein 1.0
    show haeun_date_default as actor
    h "...아, 없으시면 괜찮아요. 갑자기 이상한 걸 물어봤네요."
    show haeun_date_question as actor
    j "당신은 나에게 이 세상에 하나뿐인 존재가 되는 거야."
    h "그게요?"
    j "네, 여우가 어린 왕자에게 이야기 하는 장면이 기억에 남아요."
    show haeun_date_default as actor
    h "그렇군요..."
    jump date_bookstore_end

label date_park:
    scene bg_street_afternoon
    stop music fadeout 1.0
    play music "audio/bgm/date/date_park.mp3" fadein 1.0
    show haeun_date_happy as actor
    "서점에서 나와 골목을 돌자 공원이 나왔다."
    hide actor
    "공원 입구에 들어서는 순간, 발걸음이 잠깐 무거워졌다."
    scene bg_park_afternoon
    j "(...이상하다)"
    "이유가 없었다. 그냥 뭔가가 가슴 아래쪽에 살짝 걸리는 것 같은 느낌이었다."
    j "(피곤한가? 일단 넘어가자.)"
    show haeun_date_default as actor
    h "…저 여기 와본 적 있어요."
    j "저도요."
    "둘은 나란히 걷기 시작했다."
    h "...선생님은 여기 자주 오시나요?"
    j "가끔요. 별 이유 없이 오게 되는 거 같아요."
    "잠깐의 침묵의 이후"
    h "...이상하죠. 같은 곳인데 오늘이 뭔가 달라 보여요."
    j "이상하지 않아요. 같이 있는 사람이 다르니까요."
    "걷다 보니 어느새 그녀의 어깨가 재우의 팔쪽에 닿을 듯 말 듯 한 거리가 되었다."
    hide actor
    "둘은 공원의 벤치에 앉았다."
    show haeun_date_question as actor
    h "...선생님은 오늘 어떠셨나요?"
    j "그게 무슨 말씀이신가요?"
    h "저도 잘 모르겠어요..."
    show haeun_date_default as actor
    "어느정도의 시간이 흐르자 공원이 노을빛으로 물들었다."
    show haeun_date_happy as actor
    h "(하늘을 바라본다.)...예쁘다."
    "재우도 하늘을 쳐다봤다. 하지만 왠지 모르게 시선은 옆을 향한다."
    menu:
        j "(무슨 말을 꺼내야 할까?)"
        "하늘 얘기를 꺼낸다.":
            jump date_park_1
        "그냥 옆에 있는다.":
            jump date_park_2
        "\"하은 씨도 예쁘네요\"라고 말할 뻔한다.":
            jump date_park_3
    h "슬슬 가봐야겠네요."
    j "네."

label date_park_end:
    scene bg_park_afternoon
    stop music fadeout 1.0
    play music "audio/bgm/date/date_park_end.mp3" fadein 1.0
    show haeun_date_happy as actor
    "둘은 같이 일어서서 출구 쪽으로 걸었다."
    "갑자기 하은이 재우의 앞쪽으로 살짝 뛰었다."
    "흝날리는 옷의 소매와 작은 등이 눈에 보인다."
    j "(...어디선가 봤었던거 같아.)"
    hide actor
    "하은은 길 건너까지 달려갔다."
    show haeun_date_happy as actor
    "길 건너 편에서 하은이 크게 손을 흔들었다."
    h "오늘 즐거웠어요."
    j "네. 조심히 들어가세요."
    hide actor
    "하은이 멀어져 간다. 하지만 재우는 그 자리에 서서 가만히 그 모습을 지켜본다."
    j "(더 보고 싶다.)"
    j "아ㅡ, 그런가."
    j "내가 하은 씨를 좋아하는구나."
    show haeun_date_default as actor
    "도로를 건넌 하은은 자신의 얼굴과 귀가 붉어진 느낌이 들었다."
    h "(왜 인지, 달려야만 할 것 같았어... 뭔가 떠오르는 것 같기도 하지만... 잘 모르겠어...)"
    jump date_return_home

label date_park_1:
    scene bg_park_afternoon
    stop music fadeout 1.0
    play music "audio/bgm/date/date_park_1.mp3" fadein 1.0
    show haeun_date_default as actor
    j "노을 자주 봐요?"
    h "가끔요. 혼자 볼 때랑은 다르네요."
    j "뭐가요?"
    h "같이 보면 더 오래 보게 돼요."
    jump date_park_end

label date_park_2:
    scene bg_park_afternoon
    stop music fadeout 1.0
    play music "audio/bgm/date/date_park_2.mp3" fadein 1.0
    show haeun_date_default as actor
    "두명 다 아무 말도 하지 않는다. 하은의 어깨가 재우의 팔에 살짝 닿았다."
    show haeun_date_happy as actor
    h "좋네요."
    show haeun_date_default as actor
    j "(무엇이 좋다는 걸까...)"
    jump date_park_end

label date_park_3:
    scene bg_park_afternoon
    stop music fadeout 1.0
    play music "audio/bgm/date/date_park_3.mp3" fadein 1.0
    show haeun_date_default as actor
    j "(하은 씨도 예쁘네요, 라고 할 뻔했다.)"
    show haeun_date_happy as actor
    j "...노을이 오래 가네요, 오늘."
    "재우가 하은을 바라보자, 하은이 자신을 보고 있다는 것을 깨달았다."
    show haeun_date_default as actor
    "둘의 눈이 마주쳤다. 1초, 2초, 그녀가 먼저 앞을 봤다."
    jump date_park_end

label date_return_home:
    scene bg_street_night
    stop music fadeout 1.0
    play music "audio/bgm/date/date_return_home.mp3" fadein 1.0
    j "(집에 돌아가자.)"
    "재우는 집으로 돌아가며 오늘의 일을 생각 해본다."
    "계획되지 않았던 일들로 가득 찬 날이었지만 그렇기에 더 기억에 남는다."
    j "나는 의사야. 하은 씨는 환자고, 우리는 이어질 수 없는 사이야."
    "재우는 씁쓸하게 말을 뱉으며 하늘을 바라보다가 집으로 들어갔다."
    scene bg_house_night
    "재우는 잠을 잘 준비를 마친 후 잠자리에 들었다."
    jump date_past_flashback_4

label date_past_flashback_4:
    scene bg_funeral_hall
    show dim_past
    stop music fadeout 1.0
    play music "audio/bgm/date/date_past_flashback_4.mp3" fadein 1.0
    "재우는 지금 장례식장에 있는 것 같다. 분명히 많은 사람이 곁에 있으나 느껴지지는 않는다."
    "그저 허망하게 앞의 사진을 바라만 보고 있을 뿐."
    "사진을 보고 있자 점점 땅이 가까워 진다."
    "부모님이 나의 이름을 부르는 소리가 들리지만 몸이 말을 듣지 않는다."
    scene bg_hospital_bed
    "눈을 떠보니 나는 병원 1인실에 있었다."
    "친구들과의 기억은 사라진 상태로."
    "거짓된 기억이 덧씌워지는 것조차 모르는 상태로."
    hide dim_past
    stop music fadeout 1.0
    jump week03_start
