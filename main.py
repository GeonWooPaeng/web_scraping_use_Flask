from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("Job_Scrapper")


@app.route("/")
#"/"로 접속요청을 하면 파이썬 함수(home)로 실행
def home():
  #html을 사용자에게 보여주기 
  return render_template("home.html") #home.html내용 가져오기

@app.route("/report")
def report():
  # print(request.args) #모든 request 데이터가(url에 있는 글씨들) 우리한테 넘어온다
  word = request.args.get("word")
  if word: #글씨 없는 것 check
    word = word.lower() #모든 글자 소문자로 만들어주기
    jobs = get_jobs(word) #web_site url에서 오는 word를 받는다.
  else:
    return redirect("/") #아무 것도 없을 시 원래로 돌려주기(report)
  #report.html로 word데이터 넘겨주기
  #report.html의 {{searchingBy}} 에 word를 넣어준다.
  return render_template("report.html",searchingBy=word)


# @app.route("/<username>")
# #<>부분은 placeholder
# #url에서 뒤에 /username/paeng을 쳐주면
# # potato 함수가 paeng을 가지고 return 해준다.
# # 즉 paeng을 db에서 찾는 것
# def potato(username):
#   return "hello {username} " 



app.run(host="0.0.0.0") #새로운 window창이 뜬다./ host="0.0.0.0"은 repl.it에서 실행화면 보여주기 위해 사용하는 것