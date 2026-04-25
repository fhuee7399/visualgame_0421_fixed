label haeun_bad_ending:
    scene bg_counsel_day
    stop music fadeout 1.0
    play music "audio/bgm/ending/bad_ending.mp3" 
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
    "Bad Ending" with hpunch
    hide seojin_sad
    stop music fadeout 1.0
    return