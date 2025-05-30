import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Крестики-Нолики")
        self.window.resizable(False, False)
        
        self.current_player = 'X'
        self.game_board = [[' ' for _ in range(3)] for _ in range(3)]
        self.move_count = 0
        
        self.create_widgets()
        self.setup_board()
        
    def create_widgets(self):
        # Настройка стилей
        self.button_style = {
            'font': ('Arial', 32, 'bold'),
            'width': 5,
            'height': 2,
            'bg': '#f0f0f0',
            'activebackground': '#e0e0e0'
        }
        
        # Статусная строка
        self.status_label = tk.Label(
            self.window,
            text=f"Ход игрока: {self.current_player}",
            font=('Arial', 14),
            bg='#333',
            fg='white',
            padx=10,
            pady=5
        )
        self.status_label.grid(row=3, column=0, columnspan=3, sticky='we')
        
        # Кнопка новой игры
        self.restart_btn = tk.Button(
            self.window,
            text='Новая игра',
            command=self.reset_game,
            font=('Arial', 12),
            bg='#4CAF50',
            fg='white',
            activebackground='#45a049'
        )
        self.restart_btn.grid(row=4, column=0, columnspan=3, pady=10, sticky='we')
        
    def setup_board(self):
        self.cells = []
        for row in range(3):
            cell_row = []
            for col in range(3):
                cell = tk.Button(self.window, **self.button_style)
                cell.config(command=lambda r=row, c=col: self.make_move(r, c))
                cell.grid(row=row, column=col, padx=5, pady=5)
                cell_row.append(cell)
            self.cells.append(cell_row)
            
    def make_move(self, row, col):
        if self.game_board[row][col] == ' ':
            self.game_board[row][col] = self.current_player
            self.cells[row][col].config(
                text=self.current_player,
                fg='red' if self.current_player == 'X' else 'blue',
                disabledforeground='red' if self.current_player == 'X' else 'blue',
                state='disabled'
            )
            self.move_count += 1
            
            if self.check_winner():
                self.show_winner()
            elif self.move_count == 9:
                if self.current_player == 'X':
                    self.show_draw()
                    self.reset_game(0)
                else:
                    self.show_draw()
                    self.reset_game(1)
            else:
                self.switch_player()
                
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.status_label.config(text=f"Ход игрока: {self.current_player}")
        
    def check_winner(self):
        # Проверка строк
        for row in range(3):
            if self.game_board[row][0] == self.game_board[row][1] == self.game_board[row][2] != ' ':
                self.highlight_winner(row, 0, row, 2)
                return True
        
        # Проверка столбцов
        for col in range(3):
            if self.game_board[0][col] == self.game_board[1][col] == self.game_board[2][col] != ' ':
                self.highlight_winner(0, col, 2, col)
                return True
        
        # Проверка диагоналей
        if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] != ' ':
            self.highlight_winner(0, 0, 2, 2)
            return True
        if self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] != ' ':
            self.highlight_winner(0, 2, 2, 0)
            return True
        
        return False

    def highlight_winner(self, start_row, start_col, end_row, end_col):
    # Горизонтальная линия
        if start_row == end_row:
            for col in range(3):
                self.cells[start_row][col].config(bg='#a5d6a7')
        
        # Вертикальная линия
        elif start_col == end_col:
            for row in range(3):
                self.cells[row][start_col].config(bg='#a5d6a7')
        
        # Диагонали
        else:
            # Главная диагональ (0,0)-(1,1)-(2,2)
            if (start_row, start_col, end_row, end_col) == (0, 0, 2, 2) or \
            (start_row, start_col, end_row, end_col) == (2, 2, 0, 0):
                for i in range(3):
                    self.cells[i][i].config(bg='#a5d6a7')
            
            # Обратная диагональ (0,2)-(1,1)-(2,0)
            elif (start_row, start_col, end_row, end_col) == (0, 2, 2, 0) or \
                (start_row, start_col, end_row, end_col) == (2, 0, 0, 2):
                for i in range(3):
                    self.cells[i][2-i].config(bg='#a5d6a7')
    
    def show_winner(self):
        for row in self.cells:
            for cell in row:
                cell.config(state='disabled')
        messagebox.showinfo(
            "Победа!",
            f"Игрок {self.current_player} победил!",
            parent=self.window
        )
        
    def show_draw(self):
        messagebox.showinfo(
            "Ничья!",
            "Игра завершилась вничью!",
            parent=self.window 
        )

    def reset_game(self, vs):
        self.current_player = 'O' if vs == 0 else 'X'
        self.game_board = [[' ' for _ in range(3)] for _ in range(3)]
        self.move_count = 0
        
        for row in range(3):
            for col in range(3):
                self.cells[row][col].config(
                    text=' ',
                    state='normal',
                    bg='#f0f0f0',
                    fg='black'
                )
                
        self.status_label.config(text=f"Ход игрока: {self.current_player}")
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
