from django.shortcuts import render

# Create your views here.

def index(request):
    myinfo = '''
    김민수
    순천향대학교
    컴퓨터소프트웨어공학과
    20174444
    22살
    '''

    myinfo = myinfo.split("\n")
    # ['', '김민수', '순천향대학교', '컴퓨터소프트웨어공학과', '20174444', '22살', '']

    myinfo = list(filter(lambda data: data != '', myinfo))
    # ['김민수', '순천향대학교', '컴퓨터소프트웨어공학과', '20174444', '22살']
    # 데이터가 ''인 것은 필터링해서 다시 저장

    return render(request, "index.html", {
        "name": myinfo[0],
        "university": myinfo[1],
        "department": myinfo[2],
        "student_number": myinfo[3],
        "age": myinfo[4],
        "myinfo": myinfo,
    })
