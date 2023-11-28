from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse

from src.models.candidate import CandidateInfo
from src.utils.connector import Session, get_db

from .api import api_router
from .ws import ws_router

main_router = APIRouter()

main_router.include_router(api_router, prefix="/api")
main_router.include_router(ws_router, prefix="/ws")


@main_router.get("/candidate/{name}")
def get_candidate(
    name: str,
    db: Session = Depends(get_db),
):
    stored_candidate = db.query(CandidateInfo).filter_by(name=name).first()

    if stored_candidate is None:
        return HTMLResponse(
            content="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
        }

        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            text-align: center;
        }

        h1 {
            font-size: 5em;
            margin: 0;
            color: #333;
        }

        p {
            font-size: 1.5em;
            color: #555;
        }

        a {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #3498db;
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s;
        }

        a:hover {
            background-color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>404</h1>
        <p>找不到該簡歷表</p>
        <p>很抱歉，該簡歷表可能不存在.</p>
        <a href="/">回首頁</a>
    </div>
</body>
</html>

"""
        )

    # fmt: off
    html_content = (
'<!DOCTYPE html>'
'<html lang="zh_TW">'
'<head>'
    '<meta charset="UTF-8">'
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    '<title>簡歷</title>'
    '<style>'
        'body {'
            'font-family: Arial, sans-serif;'
            'margin: 0;'
            'padding: 0;'
            'background-color: #ececec;'
            'color: #222;'
        '}'
        'header {'
            'background-color: #2c3e50;'
            'color: #fff;'
            'padding: 20px;'
            'text-align: center;'
        '}'
        'section {'
            'margin: 20px;'
            'background-color: #fff;'
            'padding: 15px;'
            'border-radius: 8px;'
            'box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);'
        '}'
        'h2 {'
            'color: #2c3e50;'
        '}'
        'ul {'
            'list-style: disc;'
            'padding: 0;'
        '}'
        'li {'
            'margin-left: 40px;'
            'margin-bottom: 10px;'
        '}'
        '.container {'
            'max-width: 800px;'
            'margin: 0 auto;'
        '}'
        '.add-button {'
            'background-color: #3498db;'
            'color: #fff;'
            'border: none;'
            'padding: 8px 12px;'
            'border-radius: 4px;'
            'cursor: pointer;'
        '}'
        '.input-field {'
            'margin-bottom: 10px;'
        '}'
        'footer {'
            'background-color: #2c3e50;'
            'color: #fff;'
            'padding: 20px;'
            'text-align: center;'
            'margin-top: 20px;'
        '}'

        '@media print {'
        '    /* 在列印時隱藏的樣式 */'
        '    .no-print {'
        '        display: none;'
        '    }'
        '}'
    '</style>'
'</head>'
'<body>'
    '<header>'
        f'<h1> {name}的簡歷</h1>'
    '</header>'
    '<div class="container">'
        '<section>'
            '<h2>基本資訊</h2>'
            '<ul id="info">'
                '<li id="info-name"><strong>姓名：</strong> {stored_candidate.name}</li>'
                '<li id="info-phone"><strong>電話：</strong> </li>'
                '<li id="info-email"><strong>信箱：</strong> </li>'
                '<li id="info-address"><strong>地址：</strong> </li>'
                '<li id="info-about"><strong>關於：</strong> </li>'
            '</ul>'
        '</section>'
        '<section>'
            '<h2>主要技能</h2>'
            '<ul id="skills"></ul>'
        '</section>'
        '<section>'
            '<h2>工作經驗</h2>'
            '<ul id="experiences"></ul>'
        '</section>'
        '<section>'
            '<h2>學歷</h2>'
            '<ul id="educations"></ul>'
        '</section>'
    '</div>'

    '<footer class="no-print" >'
        '<p> 感謝您的閱讀 </p>'
        '<a href="/" style="color: #fff; text-decoration: none;">回首頁</a>'
    '</footer>'

    '<script>'


        'const host = window.location.host;'
        'fetch(`http://${host}/api/candidates/' + f'{name}`)'
            '.then(res => res.json())'
            '.then(raw_data => {'
                'const data = raw_data.data;'
                'const info = data.info;'
                'const infoName = document.querySelector("#info-name");'
                'const infoPhone = document.querySelector("#info-phone");'
                'const infoEmail = document.querySelector("#info-email");'
                'const infoAddress = document.querySelector("#info-address");'
                'const infoAbout = document.querySelector("#info-about");'
                'infoName.innerHTML = `<strong>姓名：</strong> ${info.name}`;'
                'infoPhone.innerHTML = `<strong>電話：</strong> ${info.phone}`;'
                'infoEmail.innerHTML = `<strong>信箱：</strong> ${info.email}`;'
                'infoAddress.innerHTML = `<strong>地址：</strong> ${info.address}`;'
                'infoAbout.innerHTML = `<strong>關於：</strong> ${info.about}`;'


                'const convertDateToYYYYMM = (dateStr) => {'
                    'const date = new Date(dateStr);'
                    'const year = date.getFullYear();'
                    'const month = date.getMonth() + 1;'
                    'return `${year}-${month.toString().padStart(2, "0")}`;'
                '};'

                'const skills = data.skills;'
                'const skillsList = document.querySelector("#skills");'
                'skills.forEach(skill => {'
                    'const skillItem = document.createElement("li");'
                    'skillItem.textContent = skill.name;'
                    'skillsList.appendChild(skillItem);'
                '});'


                'const experiences = data.experiences;'
                'const experiencesList = document.querySelector("#experiences");'
                'experiences.forEach(experience => {'
                    'const experienceItem = document.createElement("li");'
                    'experienceItem.innerHTML = '
                        '`<strong>${experience.company}</strong> ${experience.position} ${convertDateToYYYYMM(experience.start_date)} - ${experience.end_date ? convertDateToYYYYMM(experience.end_date) : "今"}'
                        '<p>${experience.description}</p>`;'
                    'experiencesList.appendChild(experienceItem);'
                '});'

                'const educations = data.educations;'
                'const educationsList = document.querySelector("#educations");'
                'educations.forEach(education => {'
                    'const educationItem = document.createElement("li");'
                    'educationItem.innerHTML = '
                        '`<strong>${education.school}</strong> ${education.major} ${convertDateToYYYYMM(education.start_date)} - ${convertDateToYYYYMM(education.end_date)}'
                        '<p>${education.description}</p>`;'
                    'educationsList.appendChild(educationItem);'
                '});'

            '})'
    '</script>'
'</body>'
'</html>'
)
    # fmt: on
    return HTMLResponse(content=html_content)
