import random
import curses

# Setup the window
curses.initscr()
window = curses.newwin(20, 60, 0, 0)
window.keypad(1)
curses.noecho()
curses.curs_set(0)
window.border(0)
window.nodelay(1)

# Snake and food
snake = [[4,10], [4,9], [4,8]]
food = [10,20]
window.addch(food[0], food[1], '*')

score = 0
ESC = 27
key = curses.KEY_RIGHT

try:
    while key != ESC:
        window.addstr(0, 2, 'Score : ' + str(score) + ' ')
        window.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120)
        prev_key = key
        event = window.getch()
        key = event if event != -1 else prev_key

        if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
            key = prev_key

        # Calculate the next coordinates
        y = snake[0][0]
        x = snake[0][1]
        if key == curses.KEY_DOWN:
            y += 1
        if key == curses.KEY_UP:
            y -= 1
        if key == curses.KEY_LEFT:
            x -= 1
        if key == curses.KEY_RIGHT:
            x += 1
        snake.insert(0, [y, x])

        # Check if we hit the border
        if y == 0 or y == 19 or x == 0 or x == 59: break
        if snake[0] in snake[1:]: break

        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                nf = [
                    random.randint(1,18),
                    random.randint(1,58)
                ]
                food = nf if nf not in snake else None
            window.addch(food[0], food[1], '*')
        else:
            tail = snake.pop()
            window.addch(tail[0], tail[1], ' ')
        window.addch(snake[0][0], snake[0][1], '#')
finally:
    curses.endwin()
    print(f"Final score = {score}")