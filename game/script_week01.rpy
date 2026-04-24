label week01_start:
    call transition_week1 from _call_transition_week1
    jump jaewoo_wake_up

label jaewoo_wake_up:
    scene bg_house_day
    "오전 7시에 맞춘 알람이 울린다."
    "꿈을 꾸던 재우가 깨어나게 되었고 자신이 꾼 꿈에 대해 생각한다."
    j "그 꿈은 뭐였지.. 어제랑 이어지는 건가?"
    j "여자아이가 남자아이로 부터 도망치는 건가?"
    j "뭔가, 놓치는 게 있는 거 같은 데..."
    j "잘 생각해봐도 그게 누군지는 모르겠어."
    j "내가 모르는 뭔가가 있는걸까?"
    j "내가 잊으면 안되는 걸 잊은건가?"
    j "출근이나 해야겠다."
    "재우는 출근 준비를 하고 밖으로 나선다."
    jump street_day_commute

label street_day_commute:
    scene bg_street_day
    "재우는 집 근처의 역으로 향한다."
    j "역시 출근은 지하철이야."
    j "공사는 가급적 안 했으면 좋겠네"
    jump meet_seojin

label meet_seojin:
    scene bg_hospital
    show seojin_emotionless
    "병원에 도착하자 먼저 기다리던 서진이 보인다."
    hide seojin_emotionless
    show seojin_smile
    d "(손을 흔들며) 원장님 왔어?"
    j "어쩌서 나보다 항상 일찍 오는거지?"
    d "그러게요?"
    d "그건 원장님이 항상 늦게 오셔서 그런거 아니실까요?"
    j "(머리를 긁적이며) 응... 내가 미안해."
    d "잘 아네."
    j "그건 그렇고 하은씨는 어때?"
    d "우리 원장님 또 말 돌리시네."
    hide seojin_smile
    show seojin_emotionless
    d "안 그래도 하은씨에 대해서 얘기하려고 했어."
    j "왜? 무슨 문제라도 있었어?"
    d "응."
    j "(당황한다.) 큰 문제야?"
    d "응."
    j "뭔데? 빨리 말해봐."
    d "하은이 어머니께서 처음엔 조금씩 밝은 모습을 보여주었다고 하시더라고."
    d "근데 상담 이틀 뒤부터 갑자기 다시 어두워졌다고 하더라고."
    j "아직 문제 자체가 해결이 되진 않았으니까."
    d "그래도 단기적이더라도 밝은 모습은 보여줬으니까, 효과는 있는 거 같아."
    j "근데, 큰 문제라고 하기엔 상담 초기엔 대부분 이러지 않아?"
    d "응. 그게 말이야. 아무래도 하은씨가 전보다 더 어두워진거 같다고 하시더라고."
    j "더 어두워져?"
    d "어머니께서 걱정이 많다고 전화로 이야기 하시더라."
    j "하아... 일단 하은씨가 상담이 오늘이던가?"
    d "맞아. 아마 좀 있으면 상담시간이긴 한데, 여기에 오실 지 그게 걱정이야."
    hide seojin_emotionless
    show seojin_sad
    j "올 거라는 희망을 가져야지."
    d "그렇긴 하지. 솔직히 심각한 상태라곤 생각하지만..."
    d "난 우리 원장님 믿어."
    j "오실때 까지 얼마 남지 않은 거 같으니까. 미리 준비할게."
    d "응. 그럼 나도 준비해야겠다."
    hide seojin_sad
    "서진을 머리를 묶고 자신의 방으로 들어 갔다."
    j "오늘도 험난할 것 같네. 열심히 해야겠다."
    "재우도 준비를 마치고 상담실로 향한다."
    jump haeun_counseling

label haeun_counseling:
    scene bg_counsel_day
    "재우는 걱정과 두려움 속에서 하은이가 오길 기다리고 있다."
    j "설마 안 오시는 건 아니겠지?"
    j "30분 정도 지난거 같은데..."
    scene bg_hospital
    show haeun_emotionless
    "재우에게 하은이 도착했다는 간호사의 말이 들린다."
    hide haeun_emotionless
    scene bg_counsel_day
    j "다행이다. 안 오시는 건 아닐까 했는데."
    j "이하은씨 들어오세요."
    show haeun_emotionless
    "하은이 문을 열고 들어온다."
    "하은은 왜 인지 재우와 눈을 맞추지 않는다."
    j "여기 앉으시면 됩니다."
    j "와 주셔서 감사합니다, 오시는 데 불편하신 건 없으셨나요?"
    h "네..."
    j "다행이네요. 오늘은 지하철로 오신건가요?"
    h "네..."
    j "저도 오늘 지하철로 왔거든요. 저는 지하철이 가장 편한거 같아요."
    hide haeun_emotionless
    show haeun_question
    h "그런가요?"
    j "네, 그리고 역 안에 있는 토스트를 좋아해요."
    h "토스트?"
    j "네, 저녁에 퇴근하면서 한번 씩 사먹는 데 맛있더라고요."
    hide haeun_question
    show haeun_emotionless
    j "하은씨한테도 사드리고 싶네요. 맛있는 건 다같이 먹는게 즐거우니까요."
    h "네에..."
    j "하은씨는 토스트 좋아하시나요?"
    h "저는 가끔씩 먹는 거 같아요..."
    j "토스트는 역시 햄 한 장과 양배추, 계란, 소스 딱 이렇게 들어가는 게 맛있죠."
    hide haeun_emotionless
    show haeun_happy
    h "저도 그렇게 생각해요."
    hide haeun_happy
    show haeun_question
    j "하은씨가 좋아하시는 음식은 무엇이신가요?"
    h "제가 좋아하는 음식이요?"
    j "네, 알려주실 수 있나요?"
    hide haeun_question
    show haeun_happy
    h "저는요... 메론빵을 좋아해요."
    j "메론빵 맛있죠."
    h "선생님도 좋아하시나요?"
    j "하은님, 메론빵엔 메론이 안 들어가는 거 아시나요?"
    hide haeun_happy
    show haeun_question
    h "에... 그런가요?"
    j "중학교때 친구가 알려줬거든요."
    j "그 친구도 메론빵을 좋아했던거 같아요."
    hide haeun_question
    show haeun_happy
    h "저랑 비슷하네요. 저도 어렸을 때부터 좋아했던 거 같은데.."
    j "어렸을 때부터면 언제부터 좋아하셨나요?"
    h "음... 정확하게는 모르겠어요."
    j "하은씨의 과거이야기 들어보고 싶어요."
    hide haeun_happy
    show haeun_question
    h "제 과거이야기요?"
    j "네, 저에게 이야기 해주실 수 있나요?"
    hide haeun_question
    show haeun_emotionless
    h "재미있으실 지는 모르겠어요..."
    j "괜찮아요. 말해 주실 수 있나요?"
    h "그럼... 말해드릴께요. 제 과거 이야기."
    j "감사해요."
    "하은이 잠시 생각을 한 뒤 재우를 바라보며 이야기 한다."
    h "잘 생각나진 않지만 가장 먼저 생각나는 건..."
    h "저는 꽤나 활발한 아이였던 거 같아요."
    j "흥미롭네요."
    h "네... 항상 '누군가'와 함께 떠들거나 돌아다니면서 지냈던거 같아요."
    j "'누군가' 말씀이신가요?"
    hide haeun_emotionless
    show haeun_sad
    h "정확하게는 기억나진 않지만..."
    h "누군지 모르겠지만... 그땐 즐거웠던 거 같아요."
    h "그때로 돌아가고 싶은 만큼."
    j "그 분은 한 분이신가요?"
    h "잘 모르겠지만... 그건 아닌거 같아요.."
    h "뭔지 모르게 떠올리면 떠올릴 수록 가슴이 먹먹해지는 기분이에요."
    j "어쩌면 그때의 일이 원인일 수 있겠네요."
    j "하은씨의 이유 모를 불안감 말이에요."
    "하은의 눈에서 매우 작은 물방울이 생긴다."
    "하은은 재우를 올려다 본다."
    h "그런거 같아요."
    j "무언가 사건이 있었던 게 아닐까요?"
    h "모르겠어요... 선생님..."
    menu:
        h "선생님도 힘드셨던 적이 있나요?"
        "어렸을 적 친구와 이별했던 적이 있어요.":
            jump haeun_counseling_memory_answer
        "서진 선생님이랑 힘든 일이 있었어요":
            jump haeun_counseling_seojin_answer
        "죄송하지만 그 대답은 하기 힘들 거 같아요":
            jump haeun_counseling_refusal_answer

label haeun_counseling_memory_answer:
    scene bg_counsel_day
    hide haeun_sad
    show haeun_sad
    j "어렸을 적 친구와 이별했던 적이 있어요."
    j "저도 잘은 기억나지 않지만"
    j "어렸을 때부터 친했었던 친구가 있었어요."
    j "흔히 말하는 단짝 친구 같은 느낌이에요."
    h "그렇군요..."
    j "어느날 그 친구가 보이지 않았을 때가 있었는데..."
    j "주변에서 저에게 이야기하더라고요."
    h "어떤 이야기를요?"
    j "그 친구가 지금 해외유학을 갔다고요."
    j "그냥 저에겐 아무 말 없이 사라졌어요."
    h "정말이요?"
    j "네, 지금은 괜찮아 진 거 같아요."
    "재우의 표정이 조금 슬퍼보인다."
    jump haeun_counseling_part2

label haeun_counseling_seojin_answer:
    scene bg_counsel_day
    hide haeun_sad
    show haeun_emotionless
    j "서진 선생님이랑 힘든 일이 있었어요."
    h "서진 선생님이요?"
    j "네 서진 선생님이 저렇게 보여도 생각보다 놀리는 걸 좋아하시거든요."
    h "네...."
    j "가끔씩 심한 장난을 치셔서... 크게 싸우기도 하거든요."
    "하은이 침묵한다."
    j "답이 되었을까요?"
    h "네."
    hide haeun_emotionless
    jump haeun_bad_ending

label haeun_counseling_refusal_answer:
    scene bg_counsel_day
    hide haeun_sad
    show haeun_emotionless
    j "죄송하지만 그 대답은 하기 힘들 거 같아요."
    hide haeun_emotionless
    show haeun_mad
    h "재우 선생님도 똑같으시네요."
    j "네?"
    h "똑같다고요. 다른 선생님들과."
    hide haeun_mad
    jump haeun_bad_ending

label haeun_counseling_part2:
    scene bg_counsel_day
    j "그럼 이제 저도 하은씨의 과거 이야기를 들을 수 있나요?"
    hide haeun_sad
    show haeun_emotionless
    h "네..."
    j "떠올리시는 분들과 어떤 관계이셨나요?"
    h "평범한 친구 관계? 그런거 같아요."
    h "근데 뭔가 모르게 가슴이 뛰는 거 같은 느낌이 있어요."
    hide haeun_emotionless
    show haeun_question
    h "이건 좋아하는 감정일까요?"
    j "저도 잘 모르겠어요."
    h "그리고..."
    hide haeun_question
    show haeun_sad
    h "그리우면서 동시에 답답해요."
    j "답답하시다고 하신 건 어떤 느낌인가요?"
    h "잘 표현하진 못하겠지만... 후회하고 있는거 같아요."
    j "후회... 그렇군요."
    j "혹시 그 감정을 다른 상황에서도 느낀 적이 있나요?"
    h "네. 있어요."
    j "힘드신 건 알지만 이야기 해주세요."
    h "키우던 고양이가 있었어요."
    j "고양이 말씀이신가요?"
    h "어머니랑 같이 키우던 고양이인데..."
    h "좀 더 아껴주었으면 좋았을 텐데..."
    h "선생님도 주변에 죽음을 경험 해 보신 적이 있나요?"
    menu:
        j "(죽음이라...)"
        "...작년에 부모님이...":
            jump haeun_counseling_part2_parents_answer
        "지인은 아니지만 존경하시던 분이 올해 돌아가셨어요.":
            jump haeun_counseling_part2_celebrity_answer
        "죄송하지만... 그 대답은 너무 민감해요":
            jump haeun_counseling_part2_refusal_answer

label haeun_counseling_part2_parents_answer:
    scene bg_counsel_day
    hide haeun_sad
    show haeun_sad
    j "...작년에 부모님이..."
    h "제가 너무 민감한 걸 물어 본거 같아요..."
    j "아니에요. 최대한 극복할려고 노력하고 있어요."
    j "언젠가 일어날 일이였고, 언제 닥칠지 모르는 일이니까요..."
    j "아직도 후회하는 것이 남은 것 같아요."
    h "그게 무엇인가요?"
    j "전하지 못한 말이 너무 많은 것 같아서요."
    j "저는 그렇게 생각해요."
    hide haeun_sad
    show haeun_question
    h "어떻게요?"
    j "잠시 머나먼 여행길을 떠나신거라고요."
    j "하은씨의 고양이도 잠시 먼 여행을 떠난 것이 아닐까요?"
    hide haeun_question
    show haeun_sad
    h "...그랬으면 좋겠어요."
    j "이별은 나아가는 것이라 생각해요."
    h "좋은 말이라고 생각해요."
    jump haeun_counseling_wrap_up

label haeun_counseling_part2_celebrity_answer:
    scene bg_counsel_day
    hide haeun_sad
    show haeun_sad
    j "제가 존경하는 유명인이 최근에 돌아 가셨어요."
    hide haeun_sad
    show haeun_emotionless
    h "아...네."
    j "네, 김XX라고 하시는 분인데 알고 계신가요?"
    h "네..."
    j "저가 그분 영화를 보고 자랐거든요..."
    h "아...네."
    hide haeun_emotionless
    jump haeun_bad_ending

label haeun_counseling_part2_refusal_answer:
    scene bg_counsel_day
    hide haeun_sad
    show haeun_sad
    j "죄송하지만 그 대답은 너무 민감해요."
    hide haeun_sad
    show haeun_mad
    h "선생님..."
    j "(어 왜 그러시지?)"
    h "안녕히 계세요."
    "하은이 자리를 박차고 나간다."
    hide haeun_mad
    jump haeun_bad_ending

label haeun_counseling_wrap_up:
    scene bg_counsel_day
    "하은과의 상담이 끝나고 재우는 하은이의 마중을 나간다."
    scene bg_hospital
    hide haeun_sad
    show haeun_happy
    j "다음에도 볼 수 있었으면 좋겠어요."
    "재우는 하은에게 손을 흔든다."
    h "네. 오늘 상담 감사합니다."
    j "(많이 나아지신 거 같아.)"
    jump jaewoo_return_home

label jaewoo_return_home:
    scene bg_street_night
    hide haeun_happy
    j "너무 개인적인 이야기를 많이 한 걸까?"
    j "오늘은 오랜만에 토스트를 먹어야겠다."
    "재우는 토스트를 먹으며 부모님을 떠올리며 집으로 향했다."
    scene bg_house_night
    "재우는 집에 돌아와 잘 준비를 한 뒤 잠을 잠을 청한다."
    "재우는 하은에 대해 떠올린다."
    show haeun_happy
    j "(웃는 하은씨도 예쁘시네.)"
    j "허걱, 내가 무슨 생각을."
    hide haeun_happy
    show seojin_smile
    "귓 속에서 서진의 말이 들려 오는 것 같다."
    d "반하시면 안 되는거 아시죠?"
    hide seojin_smile
    "재우는 머리를 흔든다."
    j "잠 자야지..."
    jump past_flashback_2

label past_flashback_2:
    show dim_past
    scene bg_class_day
    "남자 아이와 여자 아이가 싸우는 듯한 소리가 들린다."
    show haeun_sil
    h_hidden "너무한거 아니야?"
    hide haeun_sil
    show junsung_sil
    p_hidden "잠깐만 기다려. 오해하고 있는 거 같아."
    hide junsung_sil
    show haeun_sil
    h_hidden "넌 \%\$\#\$는 친구도 아니야?"
    hide haeun_sil
    show junsung_sil
    p_hidden "그런게 아니야. 난 그저..."
    hide junsung_sil
    show haeun_sil
    h_hidden "어떻게 그렇게 중요한 걸 소중한 친구에게 말하지 않을 수가 있어?"
    h_hidden "내가 뭘 오해 하고 있는 건데!"
    h_hidden "넌 친구도 아니야."
    hide haeun_sil
    "남자아이가 여자아이를 붙잡는다."
    show haeun_sil
    "여자아이가 남자아이를 뿌리치고 달려나간다."
    h_hidden "붙잡지마! 그냥 내 앞에서 사라져!"
    hide haeun_sil
    "남자아이가 여자아이를 뒤따라 달린다."
    hide dim_past
    jump week02_start


label haeun_bad_ending:
    scene bg_counsel_day
    show haeun_emotionless
    "이후 몇번의 대화가 오간 후."
    h "수고하셨습니다."
    j "수고하셨습니다."
    hide haeun_emotionless
    scene bg_hospital
    "하은은 빠르게 병원을 벗어났다."
    scene bg_street_night
    j "뭔가 불안하다."
    scene bg_house_night
    "재우는 잘 준비를 마치고 잠에 들었다."
    scene bg_house_day
    "재우는 기상 후 병원으로 향했다."
    window hide
    scene bg_street_day
    pause 2.0
    window show
    scene bg_hospital
    "하은의 다음 상담이 되었다."
    show seojin_sad
    d "재우야... 하은이 어머니한테 연락이 왔는데..."
    d "하은이가 이제 우리 병원에 안 가겠다고 하셔..."
    j "그렇구나..."
    "Bad Ending"
    hide seojin_sad
    return