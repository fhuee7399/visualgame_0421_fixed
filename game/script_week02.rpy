# define j = Character("재우", show_box_kind="jaeu")
# define j_hidden = Character("???", kind=j)

# define h = Character("하은", show_box_kind="haeun")
# define h_hidden = Character("???", kind=h)

# define d = Character("서진", show_box_kind="doctor")
# define d_hidden = Character("???", kind=d)

#define p = Character("준성", show_box_kind="junsung")
# define p_hidden = Character("???", kind=p)

label week02_start:
    call transition_week2 from _call_transition_week2
    "오전 7시의 알람이 울린다."
    j "뭔가가 이어지는 거 같아..."
    j "여자 아이와 남자아이는 왜 싸운걸까?"
    j "뭔가 어디서 보았던 것 같은데..."
    j "하은씨랑 겹쳐 보이는 건 기분 탓일까?"
    j "출근 해야지..."
    "재우는 출근 할 준비를 마치고 집을 나선다."
    j "역시 출근길은 지하철이 최고야."
    j "오늘은 하은씨 상태가 나아졌으면 좋겠다."
    "재우는 지하철을 타고 병원으로 향했다."
return