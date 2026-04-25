default week03_first_choice = 0

label week03_start:
    $ week03_first_choice = 0
    call transition_week3 from _call_transition_week3
    jump jaewoo_wake_up_week03

label jaewoo_wake_up_week03:
    scene bg_house_day
    hide actor
    "오전 7시의 알람이 울리지만, 이미 재우는 깨어있었다."
    j "뭔가 이어진 거 같아."
    j "나랑 하은 씨, 그리고 다른 한 명이 있었던 거 같아."
    j "...이준성 이였던가?"
    j "혹시 나 역시 기억하지 못하고 있었던 건가..."
    j "그것이 하은 씨를 만나고 부터 조금씩 떠오르는 것 같아."
    j "오늘 하은 씨와의 상담이 있으니까... 이야기 해볼까..."
    "재우는 출근 할 준비를 마치고 병원으로 향한다."
    jump commute_to_hospital_week03

label commute_to_hospital_week03:
    scene bg_street_day
    hide actor
    "평소와 다름이 없는 지하철을 타고 병원으로 향한다."
    j "하은 씨와 무슨 대화를 나누게 될까?"
    "재우는 의식하지 않은 채 하은에 대한 생각을 하게 된다."
    jump talk_with_seojin_week03

label talk_with_seojin_week03:
    scene bg_counsel_day
    hide actor
    "재우가 병원에 들어서자. 서진이 손을 흔들며 반긴다."
    show seojin_smile as actor
    d "재우야, 왔어? 얼굴이 밝아졌는 걸? 너 하은 씨 상담있는 날이 면 항상 그렇게 밝더라."
    j "(설마 알아차린건가? 어느새?)"
    d "너 사귀어? 하은 씨랑?"
    show seojin_sad as actor
    d "나는 버려진거야? 흑흑. 김재우 나쁜남자네."
    j "아... 아니야. (아직은)"
    show seojin_emotionless as actor
    d "흠흠 (목을 풀면서) 원장님 하은 씨에 대한 경과 보고를 해도 될까요?"
    d "하은 씨가 아르바이트를 스스로 구할 정도로 많이 나아졌다고 하네요."
    j "그 정도까지요?"
    d "네. 심지어 지난 주에는 혼자서 밖에 나갔다 왔다고 해요."
    j "(설마 그날 말하는 건가...)"
    d "아마 이번이 마지막 상담이 될 수도 있을 꺼 같아요."
    show seojin_mad as actor
    "서진이 재우를 빤히 바라본다."
    d "근데, 재우야, 너 스스로를 의사라고 자각하고 있는거지?"
    j "그게 무슨 소리야...?"
    d "너가 하은 씨랑 어떤 관계로 나아가고 싶은 지는 모르겠지만..."
    d "지금 하은 씨가 보여주는 모습이 과연 너 그 자체를 좋아하시는 건지."
    d "아니면 너가 일하면서 의도적으로 보여준 너의 모습을 좋아하는 건지."
    d "착각하면 안 된다고 생각해. 적어도."
    show seojin_smile as actor
    j "으...응. 고마워."
    d "하은 씨가 이쁘긴 하시지. 너 자신의 감정도 다시 한번 생각해봐."
    d "하은 씨의 치료 과정 중에 생긴 일시적인 감정은 아닐지."
    j "그래, 생각해 볼께."
    d "김재우 이 녀석 부정하질 않네, 하은 씨랑 데이트 잘 하시고요. 원장님~."
    j "야!!"
    d "농담이고~ 상담 잘 해요. 전 먼저 가볼께요. 원장님"
    hide actor
    "서진은 상담실로 들어갔다."
    "재우는 서진이 한 말을 곱씹으며 자신의 상담실로 가 하은이 올 때까지 기다린다."
    j "(아직 잘 모르겠어. 최선을 다해보자.)"
    jump counseling_with_haeun_week03

label counseling_with_haeun_week03:
    scene bg_counsel_day
    hide actor
    "재우는 상담에 대해 생각하면서 멍하니 앉아 있다보니, 간호사 분이 하은씨가 왔다고 한다."
    j "(…왔구나)"
    j "네, 들어오시라고 해주세요."
    show haeun_cured_happy as actor
    "문이 열리고 하은이 들어온다. 표정이 밝아 보인다, 걸음에 망설임이 없었다."
    j "하은씨, 잘 왔어요. 오는 데 불편한 건 없었죠?"
    h "네, 지하철 타고 편하게 왔어요."
    "침묵이 흐른다. 예전의 어색함이 아니었다."
    "재우는 그 침묵이 오히려 편했고, 동시에 그게 무섭기도 했다."
    j "(이게 진짜인지 아직도 모르겠다. 내가 하은씨를 좋아하는 건지, 아니면 이 사람이 나아가는 걸 곁에서 지켜보면서 생긴 감정인지)"
    j "지켜보니까 확실히 좋아진 것 같네요. 저번엔 의자에 앉아 있어도 어딘가 불편해 보였거든요."
    h "네, 지금은 불편함이 많이 사라진 것 같아요. 저를 괴롭혔던 우울감에서 해방된 느낌이에요"
    j "저번 데이트는 재밌었어요. 우연히 만났는데 뭔가 많은 걸 느꼈다고 할까요"
    h "저도요. 얼마 만에 그렇게 재밌게 놀았는지 모를 정도였어요"
    j "(웃으면서 얘기하는 모습이 좋다. 근데 서진이 한 말이 자꾸 맴돈다. 하은씨가 나를 좋아하는 건지, 아니면 힘들 때 손 잡아준 사람을 좋아하는 건지. 그게 구분이 되어야 한다고)"
    show haeun_cured_default as actor
    j "그럼 이제 트라우마에 대해 얘기해 봐도 될까요?"
    h "네, 지금이라면 할 수 있을 것 같아요."
    j "혹시 중학교가 어디였어요?"
    show haeun_cured_question as actor
    h "서현중학교요. 왜요?"
    j "(…서현중. 나랑 같다)"
    j "아, 저도 서현중 출신이에요"
    h "어, 진짜요?"
    show haeun_cured_default as actor
    j "네. 그래서 물어본 거예요. 혹시 학교 다닐 때 가까이 지내던 친구들 기억나는 사람 있어요?"
    h "딱히… 별로 없었어요. 몇 명이랑 어울리긴 했는데 지금은 잘 기억이 안 나요"
    j "몇 명이요?"
    h "두 명이었던 것 같아요. 근데 얼굴이나 이름이 잘 떠오르질 않아요"
    j "(두 명. 그 말을 듣는 순간 뭔가 가슴 언저리가 조여드는 느낌이 든다.)"
    j "(나도 그 시절에 둘이랑 어울렸는데. 한 명은 해외로 갔다고 들었고.)"
    j "(근데 왜 지금 이 얘기를 들으니까 그 기억이 이상하게 흔들리는 거지.)"
    j "혹시 그 시절에 자주 갔던 장소 같은 게 기억나요?"
    h "…공원이요. 학교 근처에 있던 공원에 자주 갔던 것 같아요."
    j "거기서 무슨 일이 있었던 건 기억하세요?"
    show haeun_cured_concerned as actor
    h "……트럭이요."
    h "트럭이 갑자기 달려왔고, 저는 피하지 못했어요"
    h "근데 누군가가 저를 밀어냈어요. 그리고 그 사람이…"
    menu:
        "하은의 말이 멈췄다. 재우는 서두르지 않고 기다렸다"
        "그 사람이 대신 치인 건가요?":
            $ week03_first_choice += 1
            jump counseling_with_haeun_first_choice_1
        "그 사람이 다쳤나요?":
            jump counseling_with_haeun_first_choice_2
        "괜찮아요, 천천히 해요":
            jump counseling_with_haeun_first_choice_3

label counseling_with_haeun_first_choice_1:
    scene bg_counsel_day
    hide actor
    j "그 사람이… 대신 치인 건가요?"
    show haeun_cured_concerned as actor
    h "네"
    show haeun_cured_sad as actor
    h "저를 구하려다가 그만…"
    j "(…뭔가 머릿속에서 스치는 게 있다. 공원. 트럭. 누군가를 밀어낸 사람. 왜 이게 낯설지가 않지)"
    jump week03_row_92

label counseling_with_haeun_first_choice_2:
    scene bg_counsel_day
    show haeun_cured_concerned as actor
    j "그 사람이 다쳤나요?"
    show haeun_cured_sad as actor
    h "…다친 게 아니에요"
    h "죽었어요. 저를 구하려다가"
    j "(…그 말이 예상보다 훨씬 크게 들어온다. 왜지)"
    jump week03_row_92

label counseling_with_haeun_first_choice_3:
    scene bg_counsel_day
    show haeun_cured_concerned as actor
    j "괜찮아요, 천천히 해도 돼요"
    show haeun_cured_sad as actor
    h "…그 사람이 대신 치였어요. 저를 구하려다가 죽었어요"
    j "(…말을 잇지 못한다. 이 얘기가 왜 이렇게 낯설지가 않은 거지)"
    jump week03_row_92

label week03_row_92:
    scene bg_counsel_day
    show haeun_cured_concerned as actor
    j "그 사람이 어떤 사람이었는지 기억해요?"
    h "저랑 사이가 좋지 않았어요. 근데 이상하게 싫지는 않았던 사람이에요"
    h "말이 거칠고 행동이 맘에 안 들었는데… 나쁜 사람은 아니었거든요"
    j "이름이 기억나요?"
    h "…준. 준이 들어갔던 것 같아요"
    menu:
        j "(해외 갔다고 들었던 애. 언제 들었더라. 기억이 잘 안 난다)"
        "이준성?":
            $ week03_first_choice += 1
            jump counseling_with_haeun_second_choice_1
        "이준혁?":
            jump counseling_with_haeun_second_choice_2
        "기억이 안 나요?":
            jump counseling_with_haeun_second_choice_3

label counseling_with_haeun_second_choice_1:
    scene bg_counsel_day
    show haeun_cured_concerned as actor
    j "이준성?"
    "그 이름을 입 밖에 내는 순간 재우의 머릿속에서 뭔가 툭 하고 끊어지는 느낌이 들었다"
    h "…네. 맞아요. 이준성이요"
    show haeun_cured_question as actor
    h "근데 선생님, 어떻게 아셨어요? 제가 말씀드린 적 없는데요"
    j "(어떻게 알았지. 추측이 아니었다. 그냥 알고 있었다)"
    j "…저도 잘 모르겠어요. 그냥 나왔어요"
    jump week03_row_114

label counseling_with_haeun_second_choice_2:
    scene bg_counsel_day
    show haeun_cured_concerned as actor
    j "이준혁?"
    h "…아뇨, 그 이름은 아닌 것 같아요"
    h "준성. 이준성이요"
    j "(이준성. 그 이름을 하은씨 입에서 듣는 순간 뭔가 머릿속에서 흔들리는 게 있다)"
    jump week03_row_114

label counseling_with_haeun_second_choice_3:
    scene bg_counsel_day
    show haeun_cured_concerned as actor
    j "그 이상은 기억이 안 나요?"
    h "…이준성이요. 갑자기 떠올랐어요"
    j "(이준성. 그 이름이 낯설지 않다. 왜 내가 먼저 말하지 않았지)"
    jump week03_row_114

label week03_row_114:
    scene bg_counsel_day
    show haeun_cured_concerned as actor
    "이름이 확인된 후 재우는 잠시 말을 잃었다"
    j "(이준성. 해외 갔다고 들었는데. 근데 지금 하은씨 표정을 보면 그게 아니라는 걸 이미 알 것 같다)"
    show haeun_cured_sad as actor
    h "이준성은요… 결국 그 자리에서 죽었어요. 저를 구하려다가"
    j "(죽었다. 해외가 아니라. 죽은 거였다. 근데 왜 나는 그걸 지금에서야 듣는 것처럼 느끼는 거지. 이미 알고 있었던 것 같기도 한데. 아니, 알고 싶지 않아서 그냥 믿어버린 건지)"
    "재우는 잠시 말을 잃었다. 아무렇지 않은 척 하려고 했는데 그게 잘 안 됐다"
    j "…그렇군요"
    h "괜찮으세요?"
    j "네, 괜찮아요. 계속 얘기해줘요"
    j "(괜찮지 않다. 지금 머릿속에서 뭔가 계속 뒤집어지고 있다)"
    h "준성이는 말도 거칠고 행동이 맘에 안 들어도"
    h "이타적이고 착한 친구라서 싫진 않았어요"
    j "(착한 친구. 맞다. 그 애는 그런 애였다. 근데 이걸 내가 왜 알고 있지)"
    "두 사람 사이에 잠시 침묵이 흘렀다. 재우는 조용히 숨을 골랐다"
    show haeun_cured_concerned as actor
    j "저도 서현중 출신이라고 했잖아요. 같은 학년이었어요"
    h "…네?"
    j "그 공원도 알고, 그 사고도 알아요"
    j "저도 거기 있었거든요"
    "하은은 재우를 바라보았다. 말이 없었다"
    j "저는 그 이후로 준성이가 해외로 갔다고 알고 있었어요"
    j "그렇게 들었거든요"
    j "근데 지금 하은씨 얘기를 들으면서… 그게 아니었다는 걸 알겠어요"
    j "(그리고 그 말을 누가 했는지도, 왜 내가 그걸 그대로 믿었는지도 이제는 모르겠다. 아니, 알고 싶지 않아서 그냥 믿어버린 것 같기도 하다)"
    "한동안 침묵이 흘렀다"
    if week03_first_choice == 2:
        jump week03_true_ending
    jump week03_good_ending