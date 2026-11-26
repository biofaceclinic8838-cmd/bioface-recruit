#!/usr/bin/env python3
"""Build the BIOFACE recruit page (860px) as inline-style HTML.
Usage: build.py <out_html> <image_base>   e.g. build.py index.html images/
"""
import sys, html

OUT, BASE = sys.argv[1], sys.argv[2]
if not BASE.endswith('/'):
    BASE += '/'

NG = "'Nanum Gothic','NanumGothic','나눔고딕','Malgun Gothic','맑은 고딕',sans-serif"
NS = "'Noto Sans KR','Malgun Gothic','맑은 고딕',sans-serif"
TEAL = '#5bb1b8'
LINE = '#b9dede'
e = html.escape


def img(name, w, h, extra=''):
    return (f'<img src="{BASE}{name}" width="{w}" height="{h}" alt="" '
            f'style="display:block;border:0;width:{w}px;height:{h}px;{extra}">')


def section(h, inner, name):
    return (f'<!-- {name} -->\n'
            f'<div style="position:relative;width:860px;height:{h}px;overflow:hidden;background:#fff;">\n{inner}\n</div>\n')


def title(text, top, ul_w, ul_top, bold_only=None):
    if bold_only:
        t = (f'<span style="font-weight:bold;letter-spacing:-0.029em;">{e(bold_only[0])}</span>'
             f'<span style="font-weight:normal;letter-spacing:-0.029em;">{e(bold_only[1])}</span>')
    else:
        t = e(text)
    return (f'<h2 style="position:absolute;left:52px;top:{top}px;margin:0;padding:0;font-family:{NG};'
            f'font-size:33px;line-height:33px;font-weight:bold;color:#000;letter-spacing:-0.06em;white-space:nowrap;">{t}</h2>\n'
            f'<div style="position:absolute;left:55px;top:{ul_top}px;width:{ul_w}px;height:4px;background:{TEAL};font-size:0;line-height:0;">&nbsp;</div>')


def paras(lines, left, top, size, lh, ls, bold=False, family=NG, color='#000'):
    body = '<br>'.join(e(x) for x in lines)
    return (f'<p style="position:absolute;left:{left}px;top:{top}px;margin:0;padding:0;font-family:{family};'
            f'font-size:{size}px;line-height:{lh}px;font-weight:{"bold" if bold else "normal"};color:{color};'
            f'letter-spacing:{ls}em;white-space:nowrap;">{body}</p>')


def bullet_list(items, left, top, item_h):
    rows = []
    for t in items:
        rows.append(
            f'<div style="position:relative;height:{item_h}px;padding-left:21px;font-family:{NG};font-size:19px;'
            f'line-height:{item_h}px;color:#000;letter-spacing:-0.067em;white-space:nowrap;">'
            f'<span style="position:absolute;left:1px;top:{(item_h-5)/2}px;width:5px;height:5px;border-radius:50%;'
            f'background:{TEAL};font-size:0;line-height:0;">&nbsp;</span>{e(t)}</div>')
    return f'<div style="position:absolute;left:{left}px;top:{top}px;">\n' + '\n'.join(rows) + '\n</div>'


S = []

# 01 상단 타이틀 -------------------------------------------------------
t_style = (f'position:absolute;left:52px;margin:0;padding:0;font-family:{NS};font-weight:500;'
           f'white-space:nowrap;line-height:1.2;')
S.append(section(844,
    f'{img("01_title.jpg", 860, 844)}\n'
    f'<p style="{t_style}top:50px;font-size:65px;color:#fff;letter-spacing:-0.024em;">(뷰티 선도 병원)</p>\n'
    f'<p style="{t_style}top:135px;font-size:65px;color:#fff;letter-spacing:-0.024em;">강남지역 클리닉 공채</p>\n'
    f'<p style="{t_style}top:228px;font-size:49px;color:#eec64c;letter-spacing:-0.031em;">(중국어 코디네이터)</p>',
    '01_상단 타이틀'))

# 02 BIOFACE CLINIC 소개 ------------------------------------------------
S.append(section(471,
    title('BIOFACE CLINIC', 37, 208, 86) + '\n' +
    paras(['“직원이 행복해야 병원도 성장할 수 있다”',
           '[최첨단 의료장비, 두발 앞선 시술법, 수술 없는 아름다움]'], 52, 115.5, 20.9, 36, -0.048, bold=True) + '\n' +
    paras(['또 한번 앞서 가며, 빠르게 성장하고 있는 비오페이스에서 함께 할 직원을 모십니다.',
           '비오페이스는 강남 위치, 아름다움을 추구하는 미용 시술 전문 병원입니다.'], 52, 216.5, 19, 33, -0.067) + '\n' +
    bullet_list(['2013년 8월 서면 비오페이스의원 오픈',
                 '2015년 8월 신사 비오페이스의원 본점 오픈',
                 '2021년 4월 신사 비오페이스의원 확장 이전'], 52, 307, 38),
    '02_BIOFACE CLINIC 소개'))

# 03 병원 전경 ----------------------------------------------------------
S.append(section(303, img('03_hospital.jpg', 860, 303), '03_병원 전경'))

# 04 About ----------------------------------------------------------------
S.append(section(261,
    title('About BIOFACE', 38, 203, 85) + '\n' +
    paras(['비오페이스는 뷰티·피부 미용의 메카 강남·신사에 위치한,',
           '쁘띠·리프팅·피부 관리에 특화된 피부과 브랜드입니다.',
           '비오페이스만의 특별한 “시그니처 시술”로 높은 만족과 사랑을 받아 눈에 띄게 성장하고 있습니다.'],
          52, 118.75, 18.8, 33, -0.056),
    '04_About BIOFACE'))

# 05 직원 사진 및 소개 -------------------------------------------------
S.append(section(607,
    f'<div style="position:absolute;left:0;top:0;">{img("05_staff.jpg", 440, 302)}</div>\n'
    f'<div style="position:absolute;left:439px;top:0;">{img("05_group.jpg", 421, 302)}</div>\n' +
    paras(['또한 전문 경영진과 의료진을 중심으로,',
           '체계적인 조직 운영과 정도 경영을 실현하고 있습니다.'], 52, 356.5, 18.8, 33, -0.056) + '\n' +
    paras(['비오페이스는 전 세계가 주목하는 K-뷰티 및 코리아 메디컬 트렌드에 발맞춰',
           '의료관광 유치사업을 기반으로 태국·중국·일본 등 아시아를 넘어,',
           '글로벌 메디컬 넘버원을 목표로 다양한 사업 확장을 이어가고 있습니다.'], 52, 454.5, 18.8, 33, -0.056),
    '05_직원 사진 및 소개'))

# 06 4S 시그니처 --------------------------------------------------------
S.append(section(363, img('06_4s.jpg', 860, 363), '06_4S 시그니처'))

# 07 Trust ----------------------------------------------------------------
S.append(section(249,
    title('Trust BIOFACE', 51, 203, 99) + '\n' +
    paras(['외면의 아름다움을 넘어, 삶의 질까지 향상시키는 ANTI-AGING 및 Marketing 노하우로',
           '10년 이상의 지속적인 성장 및 MSO를 앞둔 실력과 전문성이 겸비된 탄탄한 조직입니다.'],
          52, 129.5, 19, 39, -0.067),
    '07_Trust BIOFACE'))

# 08 원장님 10년 노하우 ---------------------------------------------------
S.append(section(363, img('08_director.jpg', 860, 363), '08_원장님 10년 노하우'))

# 09 모집요강 (실제 table) -------------------------------------------------
cell = f'border:1px solid {LINE};font-family:{NG};color:#000;padding:0;'
th = cell + 'font-size:18px;font-weight:bold;text-align:center;letter-spacing:-0.053em;height:42px;'
li = ('font-size:16.6px;line-height:43px;letter-spacing:-0.072em;text-align:left;white-space:nowrap;')
def ul(lines, bold_first=False):
    out = []
    for i, l in enumerate(lines):
        w = 'bold' if (bold_first and i == 0) else 'normal'
        out.append(f'<div style="{li}font-weight:{w};">{e(l)}</div>')
    return ''.join(out)

table = (
f'<table cellpadding="0" cellspacing="0" border="0" width="754" style="position:absolute;left:52px;top:157px;'
f'width:754px;border-collapse:collapse;table-layout:fixed;">\n'
f'<colgroup><col width="133"><col width="279"><col width="288"><col width="54"></colgroup>\n'
f'<tr style="height:43px;">'
f'<td style="{th}background:#4db5b5;">{img("logo_white.png", 77, 24, "margin:0 auto;")}</td>'
f'<td style="{th}">주요업무</td><td style="{th}">자격요건</td><td style="{th}">인원</td></tr>\n'
f'<tr style="height:229px;">'
f'<td rowspan="3" style="{cell}font-size:18px;font-weight:bold;text-align:center;vertical-align:middle;letter-spacing:-0.053em;">코디네이터</td>'
f'<td rowspan="3" style="{cell}padding-left:28px;vertical-align:middle;">'
f'{ul(["- 언어 통역","- 병원 코디네이터","- 데스크 업무","- 고객응대, 고객배분, 리셉션","- 중국어 채널 포스팅 작업","- 그외 관련 제반 업무"])}</td>'
f'<td style="{cell}padding-left:28px;vertical-align:middle;">'
f'{ul(["- 학력 무관","- 경력 무관","- 성별 : 무관","- 코디네이터 자격증 보유자","- 비즈니스 중국어 회화 가능"])}</td>'
f'<td rowspan="3" style="{cell}font-size:16px;font-weight:bold;text-align:center;vertical-align:middle;letter-spacing:-0.053em;">0명</td></tr>\n'
f'<tr style="height:42px;"><td style="{cell}font-size:18px;font-weight:bold;text-align:center;vertical-align:middle;letter-spacing:-0.053em;">우대사항</td></tr>\n'
f'<tr style="height:241px;"><td style="{cell}padding-left:28px;vertical-align:middle;">'
f'{ul(["- 경력자 우대","- 외국어 가능자 우대 (영어,일본어 등)","- 책임감, 주도적 업무 수행자","- 진실되고 긍정적인 인성 보유자 우대","- 고객만족 서비스 마인드 보유자 우대"], bold_first=True)}</td></tr>\n'
f'</table>')
S.append(section(769, title('모집요강', 64, 110, 108) + '\n' + table, '09_모집요강'))

# 10 급여조건 -------------------------------------------------------------
S.append(section(185, title('급여조건', 36, 110, 79) + '\n' + bullet_list(['면접 시 협의'], 52, 107, 38), '10_급여조건'))

# 11 근무조건 -------------------------------------------------------------
S.append(section(315,
    title('근무조건', 35, 110, 79) + '\n' +
    bullet_list(['근무형태 : 정규직 (팀원)',
                 '근무지 : 서울 강남구 강남대로 605 휴먼타워 10층 (신사역 4번 출구, 바로 앞)',
                 '근무부서 : 코디팀',
                 '근무시간 : 주 5일제, 주당 40시간, 10시~8시 순환'], 52, 114, 38),
    '11_근무조건'))

# 12 복리후생 -------------------------------------------------------------
ben = [('ben_01_insurance.png', '4대보험', 97), ('ben_02_pension.png', '퇴직연금', 97),
       ('ben_03_meal.png', '중식 제공', 97), ('ben_04_leave.png', '연차 휴가', 97),
       ('ben_05_leave_pay.png', '연차 수당', 98), ('ben_06_birthday.png', '생일 수당', 98),
       ('ben_07_bonus.png', '상여금', 98), ('ben_08_lounge.png', '휴게실', 98),
       ('ben_09_discount.png', '직원 할인', 107), ('ben_10_events.png', '각종 행사', 107),
       ('ben_11_gift.png', '명절 선물', 107), ('ben_12_incentive.png', '인센티브', 107),
       ('ben_13_overtime.png', '오버타임 보상', 104), ('ben_14_uniform.png', '유니폼 지급', 104)]
rows = []
for r in range(4):
    tds = []
    for c in range(4):
        i = r * 4 + c
        if i < len(ben):
            f, label, ih = ben[i]
            # 160x100 박스 안 가운데 정렬 (Figma의 object-contain)
            pad = (100 - ih) / 2
            tds.append(
                f'<td width="197" valign="top" align="center" style="width:197px;padding:0;">'
                f'<div style="width:160px;height:100px;margin:0 auto;text-align:center;">'
                f'<img src="{BASE}{f}" width="160" height="{ih}" alt="{e(label)}" style="display:block;border:0;margin:{pad}px auto 0;"></div>'
                f'<div style="margin-top:1px;font-family:{NG};font-size:15px;line-height:18px;color:#333;'
                f'letter-spacing:-0.04em;text-align:center;white-space:nowrap;">{e(label)}</div></td>')
        else:
            tds.append('<td width="197" style="width:197px;padding:0;">&nbsp;</td>')
    pt = 25 if r == 0 else 0
    rows.append(f'<tr style="height:{162 if r<3 else 140}px;"><td colspan="0" style="display:none"></td>' + ''.join(tds) + '</tr>')
# (colspan hack 제거: 위 빈 td 는 사용하지 않음)
rows = [x.replace('<td colspan="0" style="display:none"></td>', '') for x in rows]
panel = (
f'<table cellpadding="0" cellspacing="0" border="0" width="788" style="position:absolute;left:36px;top:114px;'
f'width:788px;height:651px;background:#daf1f1;border-collapse:collapse;table-layout:fixed;">\n'
f'<tr style="height:25px;"><td colspan="4" style="padding:0;font-size:0;line-height:0;">&nbsp;</td></tr>\n' +
'\n'.join(rows) + '\n</table>')
S.append(section(800, title('', 31, 110, 75, bold_only=('복리후생', ' (확대 예정)')) + '\n' + panel, '12_복리후생'))

# 13 제출서류 -------------------------------------------------------------
S.append(section(220,
    title('제출서류', 41, 110, 88) + '\n' +
    bullet_list(['이력서 및 자기소개서 : 온라인 이력서 양식 (해당 취업 포털) 또는 자유 양식',
                 '(사진 및 희망 연봉 기재)'], 52, 116.5, 39),
    '13_제출서류'))

# 14 지원 방법 및 절차 ----------------------------------------------------
S.append(section(320,
    title('지원 방법 및 절차', 46, 211, 92) + '\n' +
    bullet_list(['지원 방법 : 온라인 입사지원 (해당 취업 포털) 또는 이메일 (service@bioface.kr) 접수',
                 '접수 기간 : 채용 시, 접수 마감',
                 '전형 절차 : 지원서 접수 ▶ 서류 합격자 통보 ▶ 면접 ▶ 최종 합격자 통보',
                 '서류 합격자 통보 : 개별 연락 (면접 일정 협의)'], 52, 127.5, 39),
    '14_지원 방법 및 절차'))

# 15 문의 -----------------------------------------------------------------
S.append(section(230,
    title('문의', 37, 52, 80) + '\n' +
    bullet_list(['연락처 : 1833-8838, 010-4163-8839',
                 '(입사지원 서류에 허위사실이 발견될 경우, 채용확정 이후라도 채용이 취소될 수 있습니다.)'],
                52, 114.5, 39),
    '15_문의'))

# 16 P.S 및 로고 ----------------------------------------------------------
S.append(section(428,
    title('P.S', 36, 40, 78) + '\n'
    f'<div style="position:absolute;left:53px;top:127.5px;width:5px;height:5px;border-radius:50%;background:{TEAL};font-size:0;line-height:0;">&nbsp;</div>\n' +
    paras(['잠깐 거쳐가는 직장이 아닌, 오랜 시간 같이 근무할 분을 찾습니다.',
           '열정적이고 주인의식이 있는 분이면 더욱 좋겠습니다.',
           '저희 병원과 함께 비전을 펼치고자 하는 분의 적극 지원 바랍니다.'],
          73, 109.25, 25, 43, -0.027, family=NS, color='#000').replace('font-weight:normal', 'font-weight:500') + '\n'
    f'<div style="position:absolute;left:323px;top:307px;">{img("logo.png", 214, 66)}</div>',
    '16_P.S 및 로고'))

doc = f'''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=860">
<title>비오페이스의원 채용공고 - 중국어 코디네이터</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700&family=Noto+Sans+KR:wght@500&display=swap" rel="stylesheet">
</head>
<body style="margin:0;padding:0;background:#fff;">
<div style="width:860px;margin:0 auto;background:#fff;">
{''.join(S)}</div>
</body>
</html>
'''
open(OUT, 'w', encoding='utf-8').write(doc)
print('wrote', OUT, len(doc), 'bytes')
