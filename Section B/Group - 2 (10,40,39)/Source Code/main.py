from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
# Add your own database name and password here to reflect in the code
mypass = "student"
mydatabase = "library_xiib"

con = pymysql.connect(host="localhost", user="root",
                      password=mypass, database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=1300, height=700)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same = True
n = 0.53

# Adding a background image
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n)
else:
    newImageSizeHeight = int(imageSizeHeight/n)

background_image = background_image.resize(
    (newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300, 340, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root, bg="#FFD700", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.25)

headingLabel = Label(headingFrame1, text='''WELCOME TO e-LIBRARY
Developed by:-
Jayachandra B.
Amith S Kumar
P.Sai Ganesh''', bg='black', fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Book Details",
              bg='BLACK', fg='WHITE', command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='BLACK', fg='WHITE', command=delete)
btn2.place(relx=0.28, rely=0.52, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List",
              bg='BLACK', fg='WHITE', command=View)
btn3.place(relx=0.28, rely=0.64, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student",
              bg='BLACK', fg='WHITE', command=issueBook)
btn4.place(relx=0.28, rely=0.76, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='BLACK',
              fg='WHITE', command=returnBook)
btn5.place(relx=0.28, rely=0.88, relwidth=0.45, relheight=0.1)

root.mainloop()
