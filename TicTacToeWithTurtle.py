def main():
    import random
    import math
    import string
    import turtle
    
    spota = 1
    spotb = 2
    spotc = 3
    spotd = 4
    spote = 5
    spotf = 6
    spotg = 7
    spoth = 8
    spoti = 9
    turna = 0
    turnb = 0
    turnc = 0
    turnd = 0
    turne = 0
    turnf = 0
    turng = 0
    turnh = 0
    turni = 0
    alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]



    def welcome():
        print("*" * 60)
        print("Welcome to Tic-Tac-Toe!".center(60))
        print("You will choose a gamemode type from the main menu.".center(60))
        print("*" * 60)


    def get_choice_from_menu():
        print("Here are your choices: ")
        print("1. Play against a Human")
        print("2. Play against an A.I.")
        print("3. Quit")
        try:
            choice = int(input("Enter the number of your choice: "))
        except:
            print("You have entered an invalid response.")
            choice = 0
        return choice

    def draw_board():
        screen = turtle.Screen()
        screen.setup(500,500)
        screen.title("Tic Tac Toe")
        screen.setworldcoordinates(-5,-5,5,5)
        screen.bgcolor('black')
        turtle.hideturtle()
        turtle.pencolor('yellow')
        turtle.pensize(5)
        turtle.up()
        turtle.goto(-3,-1)
        turtle.seth(0)
        turtle.down()
        turtle.fd(6)
        turtle.up()
        turtle.goto(-3,1)
        turtle.seth(0)
        turtle.down()
        turtle.fd(6)
        turtle.up()
        turtle.goto(-1,-3)
        turtle.seth(90)
        turtle.down()
        turtle.fd(6)
        turtle.up()
        turtle.goto(1,-3)
        turtle.seth(90)
        turtle.down()
        turtle.fd(6)
        

        
    def draw_o(x,y):
        turtle.speed(20)
        turtle.up()
        turtle.goto(x,y-0.75)
        turtle.seth(0)
        turtle.color('red')
        turtle.down()
        turtle.circle(0.75, steps=100)

    def draw_x(x,y):
        turtle.color('blue')
        turtle.up()
        turtle.goto(x-0.75,y-0.75)
        turtle.down()
        turtle.goto(x+0.75,y+0.75)
        turtle.up()
        turtle.goto(x-0.75,y+0.75)
        turtle.down()
        turtle.goto(x+0.75,y-0.75)

    def check_win():
        if spota == 'X' and spotb == 'X' and spotc == 'X':
            print("Player One Wins\n ")
            turtle.clear()
            main()
        if spotd == 'X' and spote == 'X' and spotf == 'X':
            print("Player One Wins\n ")
            turtle.clear()
            main()
        if spotg == 'X' and spoth == 'X' and spoti == 'X':
            print("Player One Wins\n ")
            turtle.clear()
            main()
        if spota == 'X' and spotd == 'X' and spotg == 'X':
            print("Player One Wins\n ")
            turtle.clear()
            main()
        if spotb == 'X' and spote == 'X' and spoth == 'X':
            print("Player One Wins\n ")
            turtle.clear()
            main()
        if spotc == 'X' and spotf == 'X' and spoti == 'X':
            print("Player One Wins\n ")
            turtle.clear()
            main()
        if spota == 'X' and spote == 'X' and spoti == 'X':
            print("Player One Wins\n ")
            turtle.clear()
            main()
        if spotc == 'X' and spote == 'X' and spotg == 'X':
            print("Player One Wins\n ")
            turtle.clear()
            main()
        if spota == 'O' and spotb == 'O' and spotc == 'O':
            print("Player Two Wins\n ")
            turtle.clear()
            main()
        if spotd == 'O' and spote == 'O' and spotf == 'O':
            print("Player Two Wins\n ")
            turtle.clear()
            main()
        if spotg == 'O' and spoth == 'O' and spoti == 'O':
            print("Player Two Wins\n ")
            turtle.clear()
            main()
        if spota == 'O' and spotd == 'O' and spotg == 'O':
            print("Player Two Wins\n ")
            turtle.clear()
            main()
        if spotb == 'O' and spote == 'O' and spoth == 'O':
            print("Player Two Wins\n ")
            turtle.clear()
            main()
        if spotc == 'O' and spotf == 'O' and spoti == 'O':
            print("Player Two Wins\n ")
            turtle.clear()
            main()
        if spota == 'O' and spote == 'O' and spoti == 'O':
            print("Player Two Wins\n ")
            turtle.clear()
            main()
        if spotc == 'O' and spote == 'O' and spotg == 'O':
            print("Player Two Wins\n ")
            turtle.clear()
            main()
        else:
            return 'Tie'

    def check_tie():
        if check_win() == "Tie":
            print("The Match is a Draw!")
            turtle.clear()
            main()

    def tictactoe():
        print (" %s | %s | %s \n-----------\n %s | %s | %s \n-----------\n %s | %s | %s \n " % (spota,spotb,spotc,spotd,spote,spotf,spotg,spoth,spoti))

    welcome()
    choice = get_choice_from_menu()
    while choice !=3:
        if choice == 1:
            print("*" * 60)
            print("Player #1".center(60))
            print("=========".center(60))
            draw_board()
            tictactoe()
            while True:
                try:
                    turna = int(input("Enter the location: "))
                    if turna in alist:
                        raise ValueError
                    if turna > 9:
                        raise ValueError
                    if turna < 1:
                        raise ValueError
                except:
                    tictactoe()
                    print("You have entered an invalid response.")
                else:
                    break
            if turna == 1:
                spota = "X"
                draw_x(-2,2)
            if turna == 2:
                spotb = "X"
                draw_x(0,2)
            if turna == 3:
                spotc = "X"
                draw_x(2,2)
            if turna == 4:
                spotd = "X"
                draw_x(-2,0)
            if turna == 5:
                spote = "X"
                draw_x(0,0)
            if turna == 6:
                spotf = "X"
                draw_x(2,0)
            if turna == 7:
                spotg = "X"
                draw_x(-2,-2)
            if turna == 8:
                spoth = "X"
                draw_x(0,-2)
            if turna == 9:
                spoti = "X"
                draw_x(2,-2)
            print("")
            print("*" * 60)
            print("Player #2".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()
            
            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turnb = int(input("Enter the location: "))
                    if turnb in alist:
                        raise ValueError
                    if turnb > 9:
                        raise ValueError
                    if turnb < 1:
                        raise ValueError
                except:
                    tictactoe()
                    print("You have entered an invalid response.")
                else:
                    break
            if turnb == 1:
                spota = "O"
                draw_o(-2,2)
            if turnb == 2:
                spotb = "O"
                draw_o(0,2)
            if turnb == 3:
                spotc = "O"
                draw_o(2,2)
            if turnb == 4:
                spotd = "O"
                draw_o(-2,0)
            if turnb == 5:
                spote = "O"
                draw_o(0,0)
            if turnb == 6:
                spotf = "O"
                draw_o(2,0)
            if turnb == 7:
                spotg = "O"
                draw_o(-2,-2)
            if turnb == 8:
                spoth = "O"
                draw_o(0,-2)
            if turnb == 9:
                spoti = "O"
                draw_o(2,-2)
            print("")
            print("*" * 60)
            print("Player #1".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()

            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turnc = int(input("Enter the location: "))
                    if turnc in alist:
                        raise ValueError
                    if turnc > 9:
                        raise ValueError
                    if turnc < 1:
                        raise ValueError
                except:
                    tictactoe()
                    print("You have entered an invalid response.")
                else:
                    break
            if turnc == 1:
                spota = "X"
                draw_x(-2,2)
            if turnc == 2:
                spotb = "X"
                draw_x(0,2)
            if turnc == 3:
                spotc = "X"
                draw_x(2,2)
            if turnc == 4:
                spotd = "X"
                draw_x(-2,0)
            if turnc == 5:
                spote = "X"
                draw_x(0,0)
            if turnc == 6:
                spotf = "X"
                draw_x(2,0)
            if turnc == 7:
                spotg = "X"
                draw_x(-2,-2)
            if turnc == 8:
                spoth = "X"
                draw_x(0,-2)
            if turnc == 9:
                spoti = "X"
                draw_x(2,-2)
            print("")
            print("*" * 60)
            print("Player #2".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()

            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turnd = int(input("Enter the location: "))
                    if turnd in alist:
                        raise ValueError
                    if turnd > 9:
                        raise ValueError
                    if turnd < 1:
                        raise ValueError
                except:
                    tictactoe()
                    print("You have entered an invalid response.")
                else:
                    break
            if turnd == 1:
                spota = "O"
                draw_o(-2,2)
            if turnd == 2:
                spotb = "O"
                draw_o(0,2)
            if turnd == 3:
                spotc = "O"
                draw_o(2,2)
            if turnd == 4:
                spotd = "O"
                draw_o(-2,0)
            if turnd == 5:
                spote = "O"
                draw_o(0,0)
            if turnd == 6:
                spotf = "O"
                draw_o(2,0)
            if turnd == 7:
                spotg = "O"
                draw_o(-2,-2)
            if turnd == 8:
                spoth = "O"
                draw_o(0,-2)
            if turnd == 9:
                spoti = "O"
                draw_o(2,-2)
            print("")
            print("*" * 60)
            print("Player #1".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()

            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turne = int(input("Enter the location: "))
                    if turne in alist:
                        raise ValueError
                    if turne > 9:
                        raise ValueError
                    if turne < 1:
                        raise ValueError
                except:
                    tictactoe()
                    print("You have entered an invalid response.")
                else:
                    break
            if turne == 1:
                spota = "X"
                draw_x(-2,2)
            if turne == 2:
                spotb = "X"
                draw_x(0,2)
            if turne == 3:
                spotc = "X"
                draw_x(2,2)
            if turne == 4:
                spotd = "X"
                draw_x(-2,0)
            if turne == 5:
                spote = "X"
                draw_x(0,0)
            if turne == 6:
                spotf = "X"
                draw_x(2,0)
            if turne == 7:
                spotg = "X"
                draw_x(-2,-2)
            if turne == 8:
                spoth = "X"
                draw_x(0,-2)
            if turne == 9:
                spoti = "X"
                draw_x(2,-2)
            print("")
            print("*" * 60)
            print("Player #2".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()

            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turnf = int(input("Enter the location: "))
                    if turnf in alist:
                        raise ValueError
                    if turnf > 9:
                        raise ValueError
                    if turnf < 1:
                        raise ValueError
                except:
                    tictactoe()
                    print("You have entered an invalid response.")
                else:
                    break
            if turnf == 1:
                spota = "O"
                draw_o(-2,2)
            if turnf == 2:
                spotb = "O"
                draw_o(0,2)
            if turnf == 3:
                spotc = "O"
                draw_o(2,2)
            if turnf == 4:
                spotd = "O"
                draw_o(-2,0)
            if turnf == 5:
                spote = "O"
                draw_o(0,0)
            if turnf == 6:
                spotf = "O"
                draw_o(2,0)
            if turnf == 7:
                spotg = "O"
                draw_o(-2,-2)
            if turnf == 8:
                spoth = "O"
                draw_o(0,-2)
            if turnf == 9:
                spoti = "O"
                draw_o(2,-2)
            print("")
            print("*" * 60)
            print("Player #1".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()

            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turng = int(input("Enter the location: "))
                    if turng in alist:
                        raise ValueError
                    if turng > 9:
                        raise ValueError
                    if turng < 1:
                        raise ValueError
                except:
                    tictactoe()
                    print("You have entered an invalid response.")
                else:
                    break
            if turng == 1:
                spota = "X"
                draw_x(-2,2)
            if turng == 2:
                spotb = "X"
                draw_x(0,2)
            if turng == 3:
                spotc = "X"
                draw_x(2,2)
            if turng == 4:
                spotd = "X"
                draw_x(-2,0)
            if turng == 5:
                spote = "X"
                draw_x(0,0)
            if turng == 6:
                spotf = "X"
                draw_x(2,0)
            if turng == 7:
                spotg = "X"
                draw_x(-2,-2)
            if turng == 8:
                spoth = "X"
                draw_x(0,-2)
            if turng == 9:
                spoti = "X"
                draw_x(2,-2)
            print("")
            print("*" * 60)
            print("Player #2".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()

            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turnh = int(input("Enter the location: "))
                    if turnh in alist:
                        raise ValueError
                    if turnh > 9:
                        raise ValueError
                    if turnh < 1:
                        raise ValueError
                except:
                    tictactoe()
                    print("You have entered an invalid response.")
                else:
                    break
            if turnh == 1:
                spota = "O"
                draw_o(-2,2)
            if turnh == 2:
                spotb = "O"
                draw_o(0,2)
            if turnh == 3:
                spotc = "O"
                draw_o(2,2)
            if turnh == 4:
                spotd = "O"
                draw_o(-2,0)
            if turnh == 5:
                spote = "O"
                draw_o(0,0)
            if turnh == 6:
                spotf = "O"
                draw_o(2,0)
            if turnh == 7:
                spotg = "O"
                draw_o(-2,-2)
            if turnh == 8:
                spoth = "O"
                draw_o(0,-2)
            if turnh == 9:
                spoti = "O"
                draw_o(2,-2)
            print("")
            print("*" * 60)
            print("Player #1".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()

            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turni = int(input("Enter the location: "))
                    if turni in alist:
                        raise ValueError
                    if turni > 9:
                        raise ValueError
                    if turni < 1:
                        raise ValueError
                except:
                    tictactoe()
                    print("You have entered an invalid response.")
                else:
                    break
            if turni == 1:
                spota = "X"
                draw_x(-2,2)
            if turni == 2:
                spotb = "X"
                draw_x(0,2)
            if turni == 3:
                spotc = "X"
                draw_x(2,2)
            if turni == 4:
                spotd = "X"
                draw_x(-2,0)
            if turni == 5:
                spote = "X"
                draw_x(0,0)
            if turni == 6:
                spotf = "X"
                draw_x(2,0)
            if turni == 7:
                spotg = "X"
                draw_x(-2,-2)
            if turni == 8:
                spoth = "X"
                draw_x(0,-2)
            if turni == 9:
                spoti = "X"
                draw_x(2,-2)
            print("")
            print("*" * 60)
            print("Results".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()
            check_tie()
        if choice == 2:
            print("*" * 60)
            print("Player #1".center(60))
            print("=========".center(60))
            tictactoe()
            draw_board()
            while True:
                try:
                    turna = int(input("Enter the location: "))
                    if turna in alist:
                        raise ValueError
                    if turna > 9:
                        raise ValueError
                    if turna < 1:
                        raise ValueError
                except:
                    tictactoe()
                    print("You have entered an invalid response.")
                else:
                    break
            if turna == 1:
                spota = "X"
                draw_x(-2,2)
            if turna == 2:
                spotb = "X"
                draw_x(0,2)
            if turna == 3:
                spotc = "X"
                draw_x(2,2)
            if turna == 4:
                spotd = "X"
                draw_x(-2,0)
            if turna == 5:
                spote = "X"
                draw_x(0,0)
            if turna == 6:
                spotf = "X"
                draw_x(2,0)
            if turna == 7:
                spotg = "X"
                draw_x(-2,-2)
            if turna == 8:
                spoth = "X"
                draw_x(0,-2)
            if turna == 9:
                spoti = "X"
                draw_x(2,-2)
            print("")
            print("*" * 60)
            print("Player #2".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()
            
            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turnb = random.randint(1,9)
                    if turnb in alist:
                        raise ValueError
                    if turnb > 9:
                        raise ValueError
                    if turnb < 1:
                        raise ValueError
                except:
                    print("")
                else:
                    break
            if turnb == 1:
                spota = "O"
                draw_o(-2,2)
            if turnb == 2:
                spotb = "O"
                draw_o(0,2)
            if turnb == 3:
                spotc = "O"
                draw_o(2,2)
            if turnb == 4:
                spotd = "O"
                draw_o(-2,0)
            if turnb == 5:
                spote = "O"
                draw_o(0,0)
            if turnb == 6:
                spotf = "O"
                draw_o(2,0)
            if turnb == 7:
                spotg = "O"
                draw_o(-2,-2)
            if turnb == 8:
                spoth = "O"
                draw_o(0,-2)
            if turnb == 9:
                spoti = "O"
                draw_o(2,-2)
            print("")
            print("*" * 60)
            print("Player #1".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()

            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turnc = int(input("Enter the location: "))
                    if turnc in alist:
                        raise ValueError
                    if turnc > 9:
                        raise ValueError
                    if turnc < 1:
                        raise ValueError
                except:
                    tictactoe()
                    print("You have entered an invalid response.")
                else:
                    break
            if turnc == 1:
                spota = "X"
                draw_x(-2,2)
            if turnc == 2:
                spotb = "X"
                draw_x(0,2)
            if turnc == 3:
                spotc = "X"
                draw_x(2,2)
            if turnc == 4:
                spotd = "X"
                draw_x(-2,0)
            if turnc == 5:
                spote = "X"
                draw_x(0,0)
            if turnc == 6:
                spotf = "X"
                draw_x(2,0)
            if turnc == 7:
                spotg = "X"
                draw_x(-2,-2)
            if turnc == 8:
                spoth = "X"
                draw_x(0,-2)
            if turnc == 9:
                spoti = "X"
                draw_x(2,-2)
            print("")
            print("*" * 60)
            print("Player #2".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()

            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turnd = random.randint(1,9)
                    if turnd in alist:
                        raise ValueError
                    if turnd > 9:
                        raise ValueError
                    if turnd < 1:
                        raise ValueError
                except:
                    print("")
                else:
                    break
            if turnd == 1:
                spota = "O"
                draw_o(-2,2)
            if turnd == 2:
                spotb = "O"
                draw_o(0,2)
            if turnd == 3:
                spotc = "O"
                draw_o(2,2)
            if turnd == 4:
                spotd = "O"
                draw_o(-2,0)
            if turnd == 5:
                spote = "O"
                draw_o(0,0)
            if turnd == 6:
                spotf = "O"
                draw_o(2,0)
            if turnd == 7:
                spotg = "O"
                draw_o(-2,-2)
            if turnd == 8:
                spoth = "O"
                draw_o(0,-2)
            if turnd == 9:
                spoti = "O"
                draw_o(2,-2)
            print("")
            print("*" * 60)
            print("Player #1".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()

            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turne = int(input("Enter the location: "))
                    if turne in alist:
                        raise ValueError
                    if turne > 9:
                        raise ValueError
                    if turne < 1:
                        raise ValueError
                except:
                    tictactoe()
                    print("You have entered an invalid response.")
                else:
                    break
            if turne == 1:
                spota = "X"
                draw_x(-2,2)
            if turne == 2:
                spotb = "X"
                draw_x(0,2)
            if turne == 3:
                spotc = "X"
                draw_x(2,2)
            if turne == 4:
                spotd = "X"
                draw_x(-2,0)
            if turne == 5:
                spote = "X"
                draw_x(0,0)
            if turne == 6:
                spotf = "X"
                draw_x(2,0)
            if turne == 7:
                spotg = "X"
                draw_x(-2,-2)
            if turne == 8:
                spoth = "X"
                draw_x(0,-2)
            if turne == 9:
                spoti = "X"
                draw_x(2,-2)
            print("")
            print("*" * 60)
            print("Player #2".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()

            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turnf = random.randint(1,9)
                    if turnf in alist:
                        raise ValueError
                    if turnf > 9:
                        raise ValueError
                    if turnf < 1:
                        raise ValueError
                except:
                    tictactoe()
                    print("")
                else:
                    break
            if turnf == 1:
                spota = "O"
                draw_o(-2,2)
            if turnf == 2:
                spotb = "O"
                draw_o(0,2)
            if turnf == 3:
                spotc = "O"
                draw_o(2,2)
            if turnf == 4:
                spotd = "O"
                draw_o(-2,0)
            if turnf == 5:
                spote = "O"
                draw_o(0,0)
            if turnf == 6:
                spotf = "O"
                draw_o(2,0)
            if turnf == 7:
                spotg = "O"
                draw_o(-2,-2)
            if turnf == 8:
                spoth = "O"
                draw_o(0,-2)
            if turnf == 9:
                spoti = "O"
                draw_o(2,-2)
            print("")
            print("*" * 60)
            print("Player #1".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()

            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turng = int(input("Enter the location: "))
                    if turng in alist:
                        raise ValueError
                    if turng > 9:
                        raise ValueError
                    if turng < 1:
                        raise ValueError
                except:
                    tictactoe()
                    print("You have entered an invalid response.")
                else:
                    break
            if turng == 1:
                spota = "X"
                draw_x(-2,2)
            if turng == 2:
                spotb = "X"
                draw_x(0,2)
            if turng == 3:
                spotc = "X"
                draw_x(2,2)
            if turng == 4:
                spotd = "X"
                draw_x(-2,0)
            if turng == 5:
                spote = "X"
                draw_x(0,0)
            if turng == 6:
                spotf = "X"
                draw_x(2,0)
            if turng == 7:
                spotg = "X"
                draw_x(-2,-2)
            if turng == 8:
                spoth = "X"
                draw_x(0,-2)
            if turng == 9:
                spoti = "X"
                draw_x(2,-2)
            print("")
            print("*" * 60)
            print("Player #2".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()

            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turnh = random.randint(1,9)
                    if turnh in alist:
                        raise ValueError
                    if turnh > 9:
                        raise ValueError
                    if turnh < 1:
                        raise ValueError
                except:
                    print("")
                else:
                    break
            if turnh == 1:
                spota = "O"
                draw_o(-2,2)
            if turnh == 2:
                spotb = "O"
                draw_o(0,2)
            if turnh == 3:
                spotc = "O"
                draw_o(2,2)
            if turnh == 4:
                spotd = "O"
                draw_o(-2,0)
            if turnh == 5:
                spote = "O"
                draw_o(0,0)
            if turnh == 6:
                spotf = "O"
                draw_o(2,0)
            if turnh == 7:
                spotg = "O"
                draw_o(-2,-2)
            if turnh == 8:
                spoth = "O"
                draw_o(0,-2)
            if turnh == 9:
                spoti = "O"
                draw_o(2,-2)
            print("")
            print("*" * 60)
            print("Player #1".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()

            alist = [turna,turnb,turnc,turnd,turne,turnf,turng,turnh,turni]
            while True:
                try:
                    turni = int(input("Enter the location: "))
                    if turni in alist:
                        raise ValueError
                    if turni > 9:
                        raise ValueError
                    if turni < 1:
                        raise ValueError
                except:
                    tictactoe()
                    print("You have entered an invalid response.")
                else:
                    break
            if turni == 1:
                spota = "X"
                draw_x(-2,2)
            if turni == 2:
                spotb = "X"
                draw_x(0,2)
            if turni == 3:
                spotc = "X"
                draw_x(2,2)
            if turni == 4:
                spotd = "X"
                draw_x(-2,0)
            if turni == 5:
                spote = "X"
                draw_x(0,0)
            if turni == 6:
                spotf = "X"
                draw_x(2,0)
            if turni == 7:
                spotg = "X"
                draw_x(-2,-2)
            if turni == 8:
                spoth = "X"
                draw_x(0,-2)
            if turni == 9:
                spoti = "X"
                draw_x(2,-2)
            print("")
            print("*" * 60)
            print("Results".center(60))
            print("=========".center(60))
            tictactoe()
            check_win()
            check_tie()
    print("*" * 60)
    print("Thank you for using this program!")

    print("""
░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌ 
░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐ 
░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐ 
░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐ 
░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌ 
░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌ 
░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐ 
░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌ 
░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌ 
▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐ 
▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌ 
▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐ 
░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌ 
░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐ 
░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌ 
░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀ 
░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄— 

DOGECOIN TO THE MOOOOON""")

main()

