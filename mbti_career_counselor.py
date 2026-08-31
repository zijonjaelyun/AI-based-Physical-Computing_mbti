import random
import streamlit as st

st.set_page_config(page_title="MBTI 진로 상담소", page_icon="🧭", layout="centered")

# ============================================================
# 데이터
# ============================================================
mbti_data = {
    "ISTJ": {"emoji": "📋", "group": "SJ", "desc": "책임감 있고 꼼꼼하며, 규칙과 원칙을 중요하게 여기는 신뢰의 관리자 타입이에요.",
        "jobs": [("회계사", "💰", "숫자와 규정을 다루는 꼼꼼함이 빛을 발하는 직업이에요."),
                 ("공무원", "🏛️", "체계적이고 안정적인 업무 처리 능력이 잘 맞아요."),
                 ("품질관리 엔지니어", "🔧", "정확성과 절차 준수가 핵심인 분야예요.")]},
    "ISFJ": {"emoji": "🌷", "group": "SJ", "desc": "다정하고 헌신적이며, 주변 사람을 세심하게 챙기는 수호자 타입이에요.",
        "jobs": [("간호사", "💉", "타인을 돌보는 따뜻한 마음이 강점이 되는 직업이에요."),
                 ("초등학교 교사", "🍎", "아이들을 세심하게 보살피는 능력이 필요해요."),
                 ("사서", "📚", "차분하고 성실한 성향이 잘 어울리는 분야예요.")]},
    "INFJ": {"emoji": "🔮", "group": "NF", "desc": "통찰력이 뛰어나고 이상을 추구하는, 신비로운 조언자 타입이에요.",
        "jobs": [("심리상담사", "🧠", "타인의 마음을 깊이 이해하는 통찰력이 강점이에요."),
                 ("작가", "✍️", "내면의 깊은 생각을 표현하는 능력이 뛰어나요."),
                 ("사회복지사", "🤝", "이상을 실현하며 사람을 돕는 데 보람을 느껴요.")]},
    "INTJ": {"emoji": "♟️", "group": "NT", "desc": "전략적이고 독립적이며, 미래를 설계하는 전략가 타입이에요.",
        "jobs": [("데이터 과학자", "📊", "논리적 분석과 전략 수립 능력이 돋보여요."),
                 ("건축가", "🏗️", "장기적 비전과 설계 능력이 필요한 직업이에요."),
                 ("경영 컨설턴트", "💼", "체계적인 문제 해결 능력이 강점이 돼요.")]},
    "ISTP": {"emoji": "🛠️", "group": "SP", "desc": "논리적이고 손재주가 뛰어난, 실용적인 만능 재주꾼 타입이에요.",
        "jobs": [("정비 엔지니어", "🚗", "기계를 다루는 실용적 감각이 뛰어나요."),
                 ("프로그래머", "💻", "논리적 문제 해결을 즐기는 성향과 잘 맞아요."),
                 ("파일럿", "✈️", "위기 상황에서 침착하게 대응하는 능력이 강점이에요.")]},
    "ISFP": {"emoji": "🎨", "group": "SP", "desc": "온화하고 감성적이며, 예술적 감각이 뛰어난 호기심 많은 예술가 타입이에요.",
        "jobs": [("디자이너", "🖌️", "섬세한 미적 감각을 표현하는 데 강점이 있어요."),
                 ("사진작가", "📷", "순간의 아름다움을 포착하는 감성이 뛰어나요."),
                 ("플로리스트", "💐", "자연스럽고 부드러운 감성이 잘 드러나는 직업이에요.")]},
    "INFP": {"emoji": "🌈", "group": "NF", "desc": "따뜻한 마음과 풍부한 상상력을 지닌, 이상을 꿈꾸는 중재자 타입이에요.",
        "jobs": [("소설가", "📖", "풍부한 상상력을 글로 풀어내는 능력이 뛰어나요."),
                 ("영화감독", "🎬", "이상을 시각적으로 표현하는 창의력이 강점이에요."),
                 ("아동상담사", "🧸", "따뜻한 공감 능력으로 사람을 돕는 데 강해요.")]},
    "INTP": {"emoji": "🔬", "group": "NT", "desc": "논리적이고 호기심이 많은, 탐구를 즐기는 논리술사 타입이에요.",
        "jobs": [("연구원", "🧪", "깊이 있는 탐구와 분석을 즐기는 성향이에요."),
                 ("소프트웨어 개발자", "👨‍💻", "논리적 구조를 설계하는 능력이 뛰어나요."),
                 ("물리학자", "🌌", "이론적 원리를 탐구하는 데 강점이 있어요.")]},
    "ESTP": {"emoji": "⚡", "group": "SP", "desc": "활동적이고 현실적이며, 순발력이 뛰어난 모험가 타입이에요.",
        "jobs": [("스포츠 트레이너", "🏋️", "활동적이고 에너지 넘치는 성향이 강점이에요."),
                 ("영업 전문가", "🤝", "순발력과 대인관계 능력이 뛰어나요."),
                 ("응급구조사", "🚑", "빠른 판단력과 실행력이 필요한 직업이에요.")]},
    "ESFP": {"emoji": "🎉", "group": "SP", "desc": "명랑하고 사교적이며, 즐거움을 나누는 연예인 타입이에요.",
        "jobs": [("방송인", "🎤", "밝은 에너지로 사람들에게 즐거움을 주는 능력이 있어요."),
                 ("이벤트 플래너", "🎊", "사람들과 함께 즐거운 순간을 만드는 데 강점이 있어요."),
                 ("배우", "🎭", "감정 표현과 무대 위 매력이 뛰어나요.")]},
    "ENFP": {"emoji": "🌟", "group": "NF", "desc": "열정적이고 창의적이며, 사람들과의 교감을 즐기는 활동가 타입이에요.",
        "jobs": [("광고 기획자", "📢", "톡톡 튀는 아이디어와 열정이 강점이에요."),
                 ("유튜버/크리에이터", "🎥", "창의적 표현과 소통 능력이 뛰어나요."),
                 ("여행 기획자", "🧳", "새로운 경험을 향한 열정이 잘 드러나는 직업이에요.")]},
    "ENTP": {"emoji": "💡", "group": "NT", "desc": "재치있고 도전적이며, 새로운 아이디어를 즐기는 변론가 타입이에요.",
        "jobs": [("변호사", "⚖️", "논리적 설득력과 재치가 강점이 되는 직업이에요."),
                 ("스타트업 창업가", "🚀", "새로운 도전을 두려워하지 않는 성향과 잘 맞아요."),
                 ("마케팅 전략가", "📈", "창의적이고 유연한 사고가 필요한 분야예요.")]},
    "ESTJ": {"emoji": "📈", "group": "SJ", "desc": "체계적이고 리더십이 강한, 현실적인 관리자 타입이에요.",
        "jobs": [("경영자/관리자", "🏢", "조직을 체계적으로 이끄는 리더십이 강점이에요."),
                 ("군인/장교", "🎖️", "규율과 통솔력이 잘 발휘되는 직업이에요."),
                 ("프로젝트 매니저", "📅", "계획을 실행으로 옮기는 추진력이 뛰어나요.")]},
    "ESFJ": {"emoji": "🤗", "group": "SJ", "desc": "친절하고 협력적이며, 사람들을 잘 챙기는 사교적인 타입이에요.",
        "jobs": [("간호사", "🩺", "타인을 배려하는 마음이 자연스럽게 발휘돼요."),
                 ("인사(HR) 담당자", "🧑‍💼", "사람들과의 관계를 조율하는 능력이 강점이에요."),
                 ("호텔리어", "🛎️", "세심한 서비스 마인드가 잘 어울려요.")]},
    "ENFJ": {"emoji": "🌻", "group": "NF", "desc": "카리스마 있고 사람을 이끄는 것을 좋아하는 선도자 타입이에요.",
        "jobs": [("교사", "👩‍🏫", "사람들을 성장시키는 데서 보람을 느껴요."),
                 ("상담 심리사", "💬", "공감 능력과 리더십을 동시에 갖췄어요."),
                 ("NGO 활동가", "🌍", "사회적 가치를 실현하는 데 열정이 있어요.")]},
    "ENTJ": {"emoji": "👑", "group": "NT", "desc": "야심차고 결단력 있는, 타고난 리더 지휘관 타입이에요.",
        "jobs": [("CEO/경영자", "💼", "큰 그림을 그리고 조직을 이끄는 능력이 강점이에요."),
                 ("변호사", "⚖️", "논리와 추진력을 겸비한 직업이에요."),
                 ("정치인", "🏛️", "비전 제시와 결단력이 필요한 분야예요.")]},
}

group_data = {
    "NT": {"strengths": "논리적 분석력, 전략적 사고, 독립적 문제 해결 능력",
           "weaknesses": "감정 표현에 서툴 수 있고, 완벽주의로 스트레스를 받기 쉬워요",
           "majors": ["컴퓨터공학과", "경영학과", "물리학과", "산업공학과"],
           "books": ["『생각에 관한 생각』 - 대니얼 카너먼", "『사피엔스』 - 유발 하라리"],
           "certs": ["정보처리기사", "경영지도사", "데이터분석 준전문가(ADsP)"]},
    "NF": {"strengths": "공감 능력, 창의적 발상, 사람을 성장시키는 통찰력",
           "weaknesses": "현실적 문제보다 이상에 치우칠 수 있고, 갈등 상황에 예민해요",
           "majors": ["심리학과", "국어국문학과", "사회복지학과", "미디어커뮤니케이션학과"],
           "books": ["『데미안』 - 헤르만 헤세", "『죽고 싶지만 떡볶이는 먹고 싶어』 - 백세희"],
           "certs": ["청소년상담사", "사회복지사 2급", "평생교육사"]},
    "SJ": {"strengths": "책임감, 성실함, 체계적인 업무 처리 능력",
           "weaknesses": "변화에 적응하는 데 시간이 걸릴 수 있고, 융통성이 부족할 수 있어요",
           "majors": ["행정학과", "회계학과", "간호학과", "교육학과"],
           "books": ["『아주 작은 습관의 힘』 - 제임스 클리어", "『90년생이 온다』 - 임홍택"],
           "certs": ["전산회계자격증", "간호조무사", "공인중개사"]},
    "SP": {"strengths": "순발력, 실전 감각, 유연한 대처 능력",
           "weaknesses": "장기 계획보다 즉흥적인 선택을 선호할 수 있어요",
           "majors": ["체육학과", "실용음악과", "시각디자인학과", "항공서비스학과"],
           "books": ["『그릿(GRIT)』 - 앤절라 더크워스", "『프레임』 - 최인철"],
           "certs": ["바리스타자격증", "GTQ 그래픽기술자격", "생활스포츠지도사"]},
}

quotes = [
    "길을 잃는 것도 결국 길을 찾는 과정이란다 🌱",
    "실패는 방향을 알려주는 나침반일 뿐이야 🍀",
    "오늘의 작은 선택이 3년 뒤의 너를 만든단다 🌤️",
    "모르는 건 부끄러운 게 아니야, 물어보지 않는 게 아쉬운 거지 📚",
    "열정은 재능보다 오래간다는 걸 잊지 마 🔥",
    "비교하지 마, 너의 속도로 걸어가면 돼 🕊️",
]

roadmap = [
    ("고1", "다양한 동아리·진로 체험으로 관심 분야 넓히기 🔭"),
    ("고1~2", "관심 과목 심화 학습 & 관련 대회·캠프 참여 🏆"),
    ("고2", "희망 학과 커리큘럼 조사 & 관련 자격증 알아보기 📑"),
    ("고2~3", "학생부 활동 정리 & 자기소개서 초안 작성 ✍️"),
    ("고3", "입시 전형 최종 선택 & 면접·서류 준비 🎓"),
]

# 진짜 성향검사 문항 (E/I, S/N, T/F, J/P 각 4문항, 5점 리커트)
test_items = [
    ("새로운 사람을 만나면 오히려 에너지가 난다", "E"),
    ("혼자만의 시간이 있어야 재충전이 된다", "I"),
    ("여럿이 함께 있는 자리가 편하고 즐겁다", "E"),
    ("생각을 말하기 전에 충분히 정리하는 편이다", "I"),
    ("구체적인 사실과 경험을 중요하게 여긴다", "S"),
    ("미래의 가능성과 새로운 아이디어에 끌린다", "N"),
    ("정해진 순서와 매뉴얼을 따르는 게 편하다", "S"),
    ("서로 다른 것들을 연결지어 상상하는 걸 좋아한다", "N"),
    ("결정할 때 논리와 원칙을 먼저 따진다", "T"),
    ("결정할 때 사람들의 감정을 먼저 고려한다", "F"),
    ("옳고 그름을 객관적 기준으로 판단하려 한다", "T"),
    ("주변 사람과의 조화를 중요하게 생각한다", "F"),
    ("계획을 세우고 그대로 실행하는 걸 좋아한다", "J"),
    ("상황에 따라 유연하게 바꾸는 게 편하다", "P"),
    ("마감 기한보다 미리 끝내야 마음이 편하다", "J"),
    ("마감이 다가와야 오히려 집중이 잘 된다", "P"),
]

# 성향 기반 궁합 참고표 (재미로 보는 지표)
best_matches = {
    "INFP": ["ENFJ", "ENTJ"], "ENFJ": ["INFP", "ISFP"], "INFJ": ["ENFP", "ENTP"], "ENFP": ["INFJ", "INTJ"],
    "INTJ": ["ENFP", "ENTP"], "ENTP": ["INFJ", "INTJ"], "INTP": ["ENTJ", "ENFJ"], "ENTJ": ["INFP", "INTP"],
    "ISTJ": ["ESFP", "ESTP"], "ESTP": ["ISFJ", "ISTJ"], "ISFJ": ["ESTP", "ESFP"], "ESFP": ["ISTJ", "ISFJ"],
    "ESTJ": ["ISFP", "INFP"], "ISFP": ["ESTJ", "ENFJ"], "ESFJ": ["ISFP", "ISTP"], "ISTP": ["ESFJ", "ESTJ"],
}


def analyze_compatibility(a, b):
    if a == b:
        tier = ("이란성 쌍둥이 👯", "같은 유형이라 서로를 정말 잘 이해하겠지만, 비슷한 약점도 함께 가질 수 있어요.")
    elif b in best_matches.get(a, []):
        tier = ("찰떡궁합 💛", "성향 이론상 서로의 부족한 부분을 채워주는 대표적인 궁합이에요.")
    else:
        tier = ("무난하게 지낼 수 있는 사이 🙂", "노력하기에 따라 충분히 좋은 관계를 만들어갈 수 있어요.")

    reasons = []
    if a[0] == b[0]:
        reasons.append("에너지를 얻는 방식이 비슷해서 함께 있는 리듬이 잘 맞아요." if a[0] == "E"
                        else "둘 다 조용한 시간을 존중해줘서 편안한 사이가 될 수 있어요.")
    else:
        reasons.append("한 명은 활발하게, 한 명은 차분하게 — 서로의 에너지를 보완해줄 수 있어요.")

    if a[1] == b[1]:
        reasons.append("정보를 받아들이는 방식이 같아서 대화 코드가 잘 통해요." if a[1] == "S"
                        else "둘 다 아이디어와 가능성 이야기를 좋아해서 대화가 끊이지 않아요.")
    else:
        reasons.append("한 명은 현실적으로, 한 명은 상상력 풍부하게 생각해서 서로의 시야를 넓혀줄 수 있어요.")

    if a[2] == b[2]:
        reasons.append("결정 기준이 비슷해서 갈등이 적은 편이에요." if a[2] == "T"
                        else "서로의 감정을 잘 이해해줘서 마음이 편한 사이예요.")
    else:
        reasons.append("한 명은 논리로, 한 명은 마음으로 판단해서 균형 잡힌 결정을 내릴 수 있어요.")

    if a[3] == b[3]:
        reasons.append("계획을 대하는 태도가 비슷해서 일정 맞추기가 수월해요." if a[3] == "J"
                        else "둘 다 즉흥적인 걸 즐겨서 함께 다니면 재밌을 거예요.")
    else:
        reasons.append("계획파와 즉흥파의 조합이라 처음엔 부딪혀도 서로 다른 매력에 이끌릴 수 있어요.")

    return tier, reasons


# ============================================================
# 세션 상태 초기화
# ============================================================
defaults = {
    "bookmarks": set(), "board_text": "안녕! 궁금한 걸 아래에서 물어보면 여기 칠판에 답을 적어줄게 😊",
    "time_of_day": "낮", "checklist": {}, "rating": None, "last_result": None,
    "show_test": False, "last_question": "",
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ============================================================
# 전체 화면 교실 컨셉 스타일
# ============================================================
if st.session_state.time_of_day == "낮":
    wall_top, wall_bot, floor_c = "#dff1ff", "#fdf3d8", "#caa06b"
else:
    wall_top, wall_bot, floor_c = "#0f1830", "#241f3a", "#4a3c2a"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gaegu:wght@700&family=Nanum+Pen+Script&display=swap');

.stApp {{
    background:
        linear-gradient(180deg, {wall_top} 0%, {wall_bot} 72%, {floor_c} 72%, {floor_c} 100%);
    background-attachment: fixed;
}}
.block-container {{ position: relative; z-index: 1; padding-top: 200px; max-width: 760px; }}

.side-deco {{
    position: fixed; top: 90px; pointer-events: none; z-index: 0; opacity: 0.85;
}}
.deco-left {{ left: 6px; }}
.deco-right {{ right: 6px; }}
.desk-row {{
    position: fixed; bottom: 0; left: 0; width: 100%; z-index: 0; pointer-events: none; opacity: 0.9;
}}

.blackboard {{
    position: fixed; top: 12px; left: 50%; transform: translateX(-50%);
    width: min(760px, 92vw); max-height: 150px; overflow-y: auto;
    z-index: 999999;
    background: radial-gradient(ellipse at top, #2f4f3f 0%, #24382c 100%);
    border: 14px solid #8a6d3b; border-radius: 10px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.45);
    padding: 18px 22px;
}}
.board-title {{
    font-family: 'Gaegu', sans-serif; color: #fdf6e3; font-size: 1.1rem; opacity: 0.85; margin-bottom: 6px;
}}
.chalk-text {{
    font-family: 'Nanum Pen Script', cursive; color: #ffffff; font-size: 1.7rem; line-height: 1.5;
    text-shadow: 0 0 2px rgba(255,255,255,0.25);
}}

.main-title {{ text-align:center; font-size:2.0rem; font-weight:800; margin: 4px 0 2px 0; }}
.sub-title {{ text-align:center; color:#5b5b6b; margin-bottom: 1.0rem; }}

.notebook-card {{
    background-color: rgba(255,254,248,0.94); border-radius:14px; padding:16px 20px; margin-bottom:12px;
    border:1px solid #e6e2cf; box-shadow: 2px 3px 0px rgba(0,0,0,0.08);
}}

.student-bubble-wrap {{ display:flex; align-items:flex-end; gap:10px; margin: 10px 0 4px 0; }}
.student-emoji {{ font-size: 2.2rem; }}
.student-bubble {{
    position: relative; background:#fff7d6; border:2px solid #b8952f; border-radius:14px;
    padding:10px 14px; font-size:0.95rem; max-width: 80%;
}}
</style>

<div class="side-deco deco-left">
<svg width="70" height="140" viewBox="0 0 70 140" xmlns="http://www.w3.org/2000/svg">
  <rect x="5" y="5" width="60" height="90" rx="4" fill="#a9d6e5" stroke="#6b8f9e" stroke-width="5"/>
  <line x1="35" y1="5" x2="35" y2="95" stroke="#6b8f9e" stroke-width="4"/>
  <line x1="5" y1="50" x2="65" y2="50" stroke="#6b8f9e" stroke-width="4"/>
  <rect x="0" y="110" width="70" height="10" fill="#8a6d3b"/>
</svg>
</div>
<div class="side-deco deco-right">
<svg width="80" height="140" viewBox="0 0 80 140" xmlns="http://www.w3.org/2000/svg">
  <rect x="5" y="10" width="70" height="120" fill="#8a6d3b"/>
  <rect x="10" y="15" width="60" height="25" fill="#f2e2c4"/>
  <rect x="10" y="45" width="60" height="25" fill="#f2e2c4"/>
  <rect x="10" y="75" width="60" height="25" fill="#f2e2c4"/>
  <rect x="10" y="105" width="60" height="25" fill="#f2e2c4"/>
</svg>
</div>
<div class="desk-row">
<svg width="100%" height="70" viewBox="0 0 800 70" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="30" y="25" width="90" height="35" rx="6" fill="#c48a4d"/>
  <rect x="45" y="10" width="60" height="18" rx="4" fill="#e6cfa3"/>
  <rect x="200" y="25" width="90" height="35" rx="6" fill="#c48a4d"/>
  <rect x="215" y="10" width="60" height="18" rx="4" fill="#e6cfa3"/>
  <rect x="370" y="25" width="90" height="35" rx="6" fill="#c48a4d"/>
  <rect x="385" y="10" width="60" height="18" rx="4" fill="#e6cfa3"/>
  <rect x="540" y="25" width="90" height="35" rx="6" fill="#c48a4d"/>
  <rect x="555" y="10" width="60" height="18" rx="4" fill="#e6cfa3"/>
  <rect x="680" y="25" width="90" height="35" rx="6" fill="#c48a4d"/>
  <rect x="695" y="10" width="60" height="18" rx="4" fill="#e6cfa3"/>
</svg>
</div>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="blackboard">
  <div class="board-title">👩‍🏫 상담 선생님의 칠판</div>
  <div class="chalk-text">{st.session_state.board_text}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🧭 청소년 MBTI 진로 상담소</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">교실에 앉아 선생님과 함께, 나에게 맞는 진로를 찾아보아요 🍎</div>', unsafe_allow_html=True)

# ============================================================
# 사이드바
# ============================================================
with st.sidebar:
    st.markdown("### 🪪 나의 학생증")
    name = st.text_input("이름", placeholder="홍길동")
    grade = st.selectbox("학년", ["고1", "고2", "고3"])
    if name:
        st.markdown(f"**{grade} {name}** 학생, 환영해요! 🌼")

    st.markdown("---")
    st.markdown("### 🌗 교실 시간대")
    tod = st.radio("배경 분위기 선택", ["낮", "밤"], horizontal=True,
                    index=0 if st.session_state.time_of_day == "낮" else 1)
    if tod != st.session_state.time_of_day:
        st.session_state.time_of_day = tod
        st.rerun()

    st.markdown("---")
    st.markdown("### ⭐ 즐겨찾기 직업")
    if st.session_state.bookmarks:
        for b in st.session_state.bookmarks:
            st.write(f"- {b}")
    else:
        st.caption("아직 즐겨찾기한 직업이 없어요.")

    st.markdown("---")
    if st.button("🔄 전체 초기화"):
        for k, v in defaults.items():
            st.session_state[k] = v
        st.rerun()

# ============================================================
# 1. MBTI 확인 (선택 또는 정식 검사)
# ============================================================
st.markdown("### 1️⃣ 나의 MBTI 확인하기")
col1, col2 = st.columns([3, 1])
with col1:
    mbti_type = st.selectbox("🔍 나의 MBTI 유형을 선택하세요", options=list(mbti_data.keys()))
with col2:
    st.write("")
    st.write("")
    if st.button("📝 정식 검사하기" if not st.session_state.show_test else "❌ 검사지 접기"):
        st.session_state.show_test = not st.session_state.show_test
        st.rerun()

if st.session_state.show_test:
    st.markdown('<div class="notebook-card">', unsafe_allow_html=True)
    top_l, top_r = st.columns([5, 1])
    with top_l:
        st.markdown("#### 📝 간이 성향 검사 (16문항)")
    with top_r:
        if st.button("✖ 접기", key="close_test_inner"):
            st.session_state.show_test = False
            st.rerun()
    st.caption("각 문항에 얼마나 동의하는지 선택해주세요. (원하지 않으면 접기를 눌러 닫을 수 있어요)")
    with st.form("mbti_real_test"):
        scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
        for idx, (q, letter) in enumerate(test_items):
            v = st.select_slider(
                q, options=["전혀 아니다", "아니다", "보통이다", "그렇다", "매우 그렇다"],
                value="보통이다", key=f"t{idx}",
            )
            weight = {"전혀 아니다": -2, "아니다": -1, "보통이다": 0, "그렇다": 1, "매우 그렇다": 2}[v]
            scores[letter] += weight
        submitted = st.form_submit_button("결과 보기 ➡️")
        if submitted:
            result = ""
            result += "E" if scores["E"] >= scores["I"] else "I"
            result += "S" if scores["S"] >= scores["N"] else "N"
            result += "T" if scores["T"] >= scores["F"] else "F"
            result += "J" if scores["J"] >= scores["P"] else "P"
            st.session_state.board_text = f"검사 결과 너는 {result} 유형에 가까운 것 같아! 위에서 {result}로 선택해볼래? 😉"
            st.session_state.show_test = False
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 2️⃣ 추천 진로 확인하기")

c1, c2 = st.columns(2)
with c1:
    check_result = st.button("✨ 나의 추천 진로 확인하기", use_container_width=True)
with c2:
    random_pick = st.button("🎲 랜덤 직업 뽑기 (고민될 때!)", use_container_width=True)

if check_result:
    st.session_state.last_result = mbti_type
    st.balloons()

if random_pick:
    info = mbti_data[mbti_type]
    picked = random.choice(info["jobs"])
    st.info(f"🎲 랜덤으로 뽑은 직업은... {picked[1]} {picked[0]}! {picked[2]}")

if st.session_state.last_result:
    info = mbti_data[st.session_state.last_result]
    st.markdown("---")
    st.subheader(f"{info['emoji']} {st.session_state.last_result} 유형 분석 결과")
    st.write(info["desc"])

    st.markdown("#### 🎯 추천 직업 3가지")
    for job_name, job_emoji, job_desc in info["jobs"]:
        with st.container():
            st.markdown(
                f"""<div class="notebook-card"><b>{job_emoji} {job_name}</b><br>
                <span style="color:#555;">{job_desc}</span></div>""",
                unsafe_allow_html=True,
            )
            if job_name not in st.session_state.bookmarks:
                if st.button("⭐ 즐겨찾기", key=f"bm_{job_name}"):
                    st.session_state.bookmarks.add(job_name)
                    st.rerun()
            else:
                if st.button("💔 즐겨찾기 취소", key=f"unbm_{job_name}"):
                    st.session_state.bookmarks.discard(job_name)
                    st.rerun()

    g = group_data[info["group"]]
    tabs = st.tabs(["💪 강점/약점", "🏫 추천 학과", "📖 추천 도서", "📜 관련 자격증", "🗓️ 진로 로드맵"])
    with tabs[0]:
        st.success(f"강점: {g['strengths']}")
        st.warning(f"보완하면 좋은 점: {g['weaknesses']}")
    with tabs[1]:
        for m in g["majors"]:
            st.write(f"- 🏛️ {m}")
    with tabs[2]:
        for b in g["books"]:
            st.write(f"- 📗 {b}")
    with tabs[3]:
        for c in g["certs"]:
            st.write(f"- 📄 {c}")
    with tabs[4]:
        for stage, todo in roadmap:
            st.markdown(f"**{stage}** — {todo}")

# ============================================================
# 3. 궁합 & 명언 & 체크리스트
# ============================================================
st.markdown("---")
st.markdown("### 3️⃣ 더 알아보고 상담해요")

d1, d2 = st.columns(2)
with d1:
    st.markdown("#### 💌 오늘의 명언")
    if st.button("한마디 뽑기"):
        st.info(random.choice(quotes))

with d2:
    st.markdown("#### 🤝 MBTI 성향 궁합 보기")
    friend_type = st.selectbox("친구의 MBTI", options=list(mbti_data.keys()), key="friend_mbti")

if st.button("궁합 자세히 분석하기"):
    (tier_label, tier_reason), reasons = analyze_compatibility(mbti_type, friend_type)
    st.markdown(f"##### {mbti_type} ↔ {friend_type} : **{tier_label}**")
    st.write(tier_reason)
    for r in reasons:
        st.write(f"- {r}")
    st.caption("※ 성향 이론을 참고한 재미용 결과예요. 실제 관계는 더 다양한 요인으로 결정돼요!")

st.markdown("#### ✅ 이번 주 진로 체크리스트")
checklist_items = ["관심 학과 홈페이지 방문하기", "진로 관련 유튜브 영상 1개 보기",
                    "선생님/부모님과 진로 이야기 나누기", "희망 직업 하루 일과 검색해보기"]
done_count = 0
for item in checklist_items:
    checked = st.checkbox(item, key=f"chk_{item}", value=st.session_state.checklist.get(item, False))
    st.session_state.checklist[item] = checked
    if checked:
        done_count += 1
st.progress(done_count / len(checklist_items))
st.caption(f"{done_count}/{len(checklist_items)} 완료했어요!")

# ============================================================
# 4. 질문하기 (학생 말풍선 → 칠판 답변)
# ============================================================
st.markdown("#### 💬 선생님께 질문하기")

if st.session_state.last_question:
    st.markdown(
        f"""<div class="student-bubble-wrap">
        <span class="student-emoji">🧑‍🎓</span>
        <div class="student-bubble">{st.session_state.last_question}</div>
        </div>""",
        unsafe_allow_html=True,
    )

question = st.text_input("궁금한 점을 적어보세요", placeholder="예: 문과인데 개발자 될 수 있나요?", key="q_input")
if st.button("✋ 손들고 질문하기"):
    if not question.strip():
        reply = "질문을 먼저 적고 손을 들어줘! 😊"
        st.session_state.last_question = ""
    else:
        st.session_state.last_question = question
        if "문과" in question or "복수전공" in question:
            reply = "물론이지! 요즘은 전공보다 실제 역량과 포트폴리오가 더 중요한 시대야. 관련 부트캠프나 온라인 강의부터 시작해봐 💻"
        elif "돈" in question or "연봉" in question:
            reply = "연봉도 중요하지만, 오래 즐길 수 있는 일인지도 함께 고민해보면 좋겠어 💰"
        elif "몰라" in question or "모르" in question:
            reply = "괜찮아, 진로는 원래 여러 번 바뀌기도 해! 위에 있는 정식 검사부터 차근차근 해보자 🍀"
        else:
            reply = "좋은 질문이야! 그 고민은 담임 선생님이나 진로상담 선생님과 함께 더 깊이 이야기해보면 좋겠다 🍀"
    st.session_state.board_text = reply
    st.rerun()

st.markdown("#### 🌟 오늘 상담은 어땠나요?")
rating = st.slider("만족도", 1, 5, st.session_state.rating or 3)
if st.button("평가 제출"):
    st.session_state.rating = rating
    st.success("소중한 의견 고마워! 다음에 또 만나자 👋" if rating >= 4 else "의견 고마워! 더 나은 상담이 되도록 노력할게 🙏")

st.markdown("#### 📤 상담 요약 저장하기")
if st.session_state.last_result:
    bm_text = ", ".join(st.session_state.bookmarks) if st.session_state.bookmarks else "없음"
    summary_lines = ["[MBTI 진로상담 요약]", f"이름: {name or '학생'} ({grade})",
                      f"MBTI: {st.session_state.last_result}",
                      "추천 직업: " + ", ".join(j[0] for j in mbti_data[st.session_state.last_result]["jobs"]),
                      f"즐겨찾기: {bm_text}",
                      f"체크리스트 완료: {done_count}/{len(checklist_items)}"]
    summary = "\n".join(summary_lines)
    st.download_button("💾 요약 다운로드 (txt)", data=summary, file_name="진로상담_요약.txt")
    with st.expander("🔗 친구에게 공유할 문구 보기"):
        st.code(f"나는 {st.session_state.last_result} 유형! 추천 진로는 {mbti_data[st.session_state.last_result]['jobs'][0][0]} 등이래 😄", language=None)
else:
    st.caption("먼저 위에서 '추천 진로 확인하기'를 눌러주세요!")

if st.button("❄️ 방학이다!! (이스터에그)"):
    st.snow()

st.markdown("---")
st.caption("🧡 Made with Streamlit | 청소년 진로상담 프로그램 · 전체 화면 교실 컨셉")
