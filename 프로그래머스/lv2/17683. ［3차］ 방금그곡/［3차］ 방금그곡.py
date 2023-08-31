def convert(music):
    return music.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

def calc_time(start, end):
    st_hour, st_minute = map(int, start.split(":"))
    end_hour, end_minute = map(int, end.split(":"))
    return (end_hour * 60 + end_minute) - (st_hour * 60 + st_minute)

def solution(m, musicinfos):
    answer = []
    m = convert(m)
    for idx, info in enumerate(musicinfos):
        start, end, music_name, code = info.split(",")
        gap_time = calc_time(start, end)
        code = convert(code)
        listen_code = code * (gap_time // len(code)) + code[:gap_time % len(code)]
        if m in convert(listen_code):
            answer.append((-len(listen_code), idx, music_name))
    answer.sort()
    return answer[0][2] if answer else '(None)'