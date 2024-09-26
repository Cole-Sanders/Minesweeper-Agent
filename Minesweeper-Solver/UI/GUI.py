import tkinter as tk
from tkinter import ttk

#Pass in a 2D array of the board configuration to display it.
def display(board):
    root = tk.Tk()
    root.title("Minesweeper")
    
    frm = ttk.Frame(root, padding=20)
    frm.grid()
    blankTile = tk.PhotoImage(file="blank.png")
    blankTile = blankTile.subsample(4,4)
    oneTile = tk.PhotoImage(file="one.png")
    oneTile = oneTile.subsample(4,4)
    twoTile = tk.PhotoImage(file="two.png")
    twoTile = twoTile.subsample(4,4)
    threeTile = tk.PhotoImage(file="three.png")
    threeTile = threeTile.subsample(4,4)
    flagTile = tk.PhotoImage(file="flag.png")
    flagTile = flagTile.subsample(4,4)
    
    for row in range(len(board)):
        for col in range(len(board[0])):
            #If it's a blank square.
            if board[row][col] == ' ':
                ttk.Label(frm, image=blankTile).grid(column=col, row=row)

            #If it's a one square.
            if board[row][col] == '1':
                ttk.Label(frm, image=oneTile).grid(column=col, row=row)
            #If it's a two square.
            if board[row][col] == '2':
                ttk.Label(frm, image=twoTile).grid(column=col, row=row)
            #If it's a three square.
            if board[row][col] == '3':
                ttk.Label(frm, image=threeTile).grid(column=col, row=row)
            #If it's a flag square.
            if board[row][col] == 'F':
                ttk.Label(frm, image=flagTile).grid(column=col, row=row)
    
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=len(board), row=0) 
    root.mainloop()

#Enter real vals here.
display([[' ', '1'],['2','F']])