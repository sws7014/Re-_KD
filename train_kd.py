import requests

# 엔드포인트 URL
url = "https://underwood1.yonsei.ac.kr/sch/shtl/ShtlrmCtr/saveShtlbusResveList.do"

# 요청에 필요한 쿠키들
cookies = {
    '_ga': 'GA1.3.212837407.1724393688',
    '_ga_71LBQKDHJ2': 'GS1.1.1719778847.2.0.1719778847.60.0.0',
    '_ga_E0C08CRK91': 'GS1.1.1724393687.1.0.1724393687.0.0.0',
    '_INSIGHT_CK_8301': 'ba5d6d23abaee04622c2214e03636c65_93686|218d6316bde1e1d9f342214e03636c65_93686:1724395486000',
    'cugubun': 'JauOfOhyWuoegiIkKDoeghJlLAdS',
    'JSESSIONID': 'AzI9RCR3zQQl6dYQG1ylRB1i1VEQE2ExraT9ez1tP0dakrPPzdhNPAeqp19ua1da.amV1c19kb21haW4vaGFrc2ExXzE=',
    'UbiResult': 'dRchIPuszt+gQBOSR2yh+A==',
    'WMONID': 'MSss53WA03E'
}

# 요청 데이터
data = {
    "_findSavedRow": "areaDivCd, busCd, seatNo, stdrDt, beginTm",
    "_menuId": "MTA3NDkwNzI0MDIyNjk1MTQwMDA=",
    "_pgmId": "MzI5MzAyNzI4NzE=",
    "@d1#areaDivCd": "I",
    "@d1#busCd": "I1",
    "@d1#busNm": "1호차",
    "@d1#stdrDt": "20240828",
    "@d1#beginTm": "1230",
    "@d1#endTm": "1330",
    "@d1#tm": "12:30 ~ 13:30",
    "@d1#thrstNm": "영종대교(Yeongjong Bridge), 인천대교(Incheon Bridge)",
    "@d1#remndSeat": "18",
    "@d1#resveWaitPcnt": "5",
    "@d1#resveYn": "0",
    "@d1#resveWaitYn": "0",
    "@d1#resveResnDivCd": "1",
    "@d1#dailResvePosblYn": "1",
    "@d1#sts": "u",
    "@d1#tp": "ds",
    "@d1#dsShtl110": "@d1#"
}

# 요청 보내기
response = requests.post(url, cookies=cookies, data=data)

# 응답 확인
print("응답 상태 코드:", response.status_code)
print("응답 본문:", response.text)