from tkinter import*
import os
from tkinter import messagebox
import wolframalpha
class Main_Code:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768")
        self.root.title("AI Virtual Assistance | Developed By:Abdul Ali")
        Ressultpr=Label(self.root,text="I am Your Virtual Assistance?",bg="white",fg="green",font=("times new roman",20,"bold")).place(x=0,y=0,relwidth=1)
        Ressultpr=Label(self.root,text="What Do You Want To Do?",fg="red",bg="white",font=("times new roman",20,"bold")).place(x=0,y=39,relwidth=1)

        # Info-----------
        

        Question=Label(self.root,text="Question:",font=("times new roman",15)).place(x=683,y=80)
        self.Question=Entry(root,font=("times new roman",16))
        self.Question.place(x=679,y=80)

        self.btn_Button=Button(self.root,bg="white",text="Find Answer",font=("Impact",15),command=self.Answer)
        self.btn_Button.place(x=700,y=120)
        


        


    def Answer(self):
        question = self.Question.get()
        
        if question=="":
            messagebox.showinfo("Error","Please Enter Something")
        AnswerText=Label(self.root,text="Please Wait.....",fg="green",font=("times new roman",15)).place(x=0,y=180,relwidth=1)

        # Enter Your App Id Below

        app_id = "  "
        client = wolframalpha.Client(app_id) 
        res = client.query(question) 
        answer = next(res.results).text 
        print(answer)
        
        AnswerText=Label(self.root,text=answer,fg="green",font=("times new roman",15)).place(x=0,y=180,relwidth=1)
        


root=Tk()
obj=Main_Code(root)
root.mainloop()