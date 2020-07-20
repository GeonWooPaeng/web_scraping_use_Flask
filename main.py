from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("Job_Scrapper")

db = {}#계속 찾으면 시간이 많이 걸리기 때문에 fake db를 만들어 준다.

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
    existingJobs = db.get(word) #db에서 먼저 찾아본다.

    if existingJobs: 
      jobs = existingJobs

    else:
      jobs = get_jobs(word) #web_site url에서 오는 word를 받는다.
      db[word] = jobs

  else:
    return redirect("/") #아무 것도 없을 시 원래로 돌려주기(report)
  #report.html로 word데이터 넘겨주기
  #report.html의 {{searchingBy}} 에 word를 넣어준다.
  return render_template("report.html", searchingBy=word, resultsNumber = len(jobs), jobs = jobs) #jobs = jobs는 렌더링 하는 것이다.(모두 보내주는 일)


# @app.route("/<username>")
# #<>부분은 placeholder
# #url에서 뒤에 /username/paeng을 쳐주면
# # potato 함수가 paeng을 가지고 return 해준다.
# # 즉 paeng을 db에서 찾는 것
# def potato(username):
#   return "hello {username} " 

@app.route("/export")
def export():
  #error가 나면 except으로 간다.
  try:
    word = request.args.get('word')
    if not word:
      raise Exception() #에러발생시 except부분으로 간다.
    
    word = word.lower()
    jobs = db.get(word)
    if not jobs:
      raise Exception() 
    save_to_file(jobs)
    return send_file("jobs.csv")

  except:
    return redirect("/")


app.run(host="0.0.0.0") #새로운 window창이 뜬다./ host="0.0.0.0"은 repl.it에서 실행화면 보여주기 위해 사용하는 것