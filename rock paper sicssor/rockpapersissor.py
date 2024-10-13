from tkinter import* 
import random
#design
root=Tk()
root.title('Rock Paper Scissor')
root.geometry("800x600")
canvas = Canvas(root, width=800, height=600,bg="white")
canvas.grid(row=0, column=0)

rock_img = PhotoImage(file=r"C:\Users\kriti\OneDrive\Desktop\rock.png")
paper_img = PhotoImage(file=r"C:\Users\kriti\OneDrive\Desktop\paper.png")
scissor_img = PhotoImage(file=r"C:\Users\kriti\OneDrive\Desktop\scissor.png")


rock=Button(root,
                    text="rock",anchor="center",cursor="hand2",height= 4,width= 8,command=lambda: game(1)
                    )
rock.place(x=40, y=450)


paper=Button(root,
                    text="paper",anchor="center",cursor="hand2",height= 4,width= 8,command=lambda: game(2)
                    )
paper.place(x=350, y=450)

sicssor=Button(root,
                    text="sicssor",anchor="center",cursor="hand2",height= 4,width= 8,command=lambda: game(3)
                    )
sicssor.place(x=700, y=450)

canvas.create_text(150, 50, text="COMPUTER", fill="black", font=('Algerian', 25))
canvas.create_text(600, 50, text="YOU", fill="black", font=('Algerian', 25))

#game
def game(player):
    canvas.delete("all")  # Clear the screen
    canvas.create_text(150, 50, text="COMPUTER", fill="black", font=('Algerian', 25))
    canvas.create_text(600, 50, text="YOU", fill="black", font=('Algerian', 25))

    x=(1,2,3)
    comp_choice=random.choice(x)
    #computer choice
    if(comp_choice==1):
        canvas.create_image(150, 200, image=rock_img)

    elif(comp_choice==2):
        canvas.create_image(150, 200, image=paper_img)

    elif(comp_choice==3):
        canvas.create_image(150, 200, image=scissor_img)
        
        #player choice
    if(player==1):
        canvas.create_image(600, 200, image=rock_img)

    elif(player==2):
        canvas.create_image(600, 200, image=paper_img)

    elif(player==3):
        canvas.create_image(600, 200, image=scissor_img)

    # Case of DRAW
    if(player == comp_choice): 
        res = 'Draw'
    # Case of player's win
    elif (player == 1 and comp_choice == 3) or (player == 2 and comp_choice == 1) or(player == 3 and comp_choice == 2):
        res = 'You won'
        
    # Case of computer's win
    else:
        res = 'Computer won'
    
    # Putting result on canvas
    canvas.create_text(390, 550, text='Result:- ' + res,
                        fill="black", font=('Algerian', 25), tag='result')
    
root.mainloop()