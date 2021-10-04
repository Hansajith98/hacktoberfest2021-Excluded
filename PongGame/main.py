# Pong Game using tkinter canvas python
# credits: nanorex07

from tkinter import *
from tkinter import messagebox
import random
import os
import time

# Initialise Window And Set's Useful Properties 
tk = Tk()
tk.title('Pong Game!')
tk.geometry('+300+100')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1) # Keeps Window always on top of desktop

#Creates Canvas
canvas = Canvas(tk,width=700,height=500,bd=0,highlightthickness=0)
canvas.config(bg='black')
canvas.pack()

tk.update()

# Creates mid line
canvas.create_line(350,0,350,500,fill='white')

# Ball Class
class Ball:
	#constructer
	def __init__(self,canvas,paddle1,paddle,color):
		self.canvas = canvas
		self.paddle = paddle
		self.paddle1 = paddle1
		self.pS = 0
		self.p1S = 0
		self.drawP1 = None
		self.drawP = None
		self.id = self.canvas.create_oval(10,10,35,35,fill = color)
		self.canvas.move(self.id,327,220)
		self.canvas_height=self.canvas.winfo_height()
		self.canvas_width=self.canvas.winfo_width()
		self.x = random.choice([-2.5,2.5])
		self.y = -2.5
		
	#check for score crossing 10 (win!)
	def checkwin(self):
		winner = None
		if self.pS == 10:
			winner = 'Player Left'
		if self.p1S == 10:
			winner = 'Player Right'
			
		return winner
	
	#Update Left Paddle Score 
	def updatep(self,val):
		self.canvas.delete(self.drawP)
		self.drawP = self.canvas.create_text(170,50,
		font=('',40),text=str(val),fill='white')
		
	#Update Right Paddle Score
	def updatep1(self,val):
		self.canvas.delete(self.drawP1)
		self.drawP1 = self.canvas.create_text(550,50,
		font=('',40),text=str(val),fill='white')		
	
	#Checks for collision of paddle and ball for paddle left	
	def hit_paddle(self,pos):
		
		paddle_pos = self.canvas.coords(self.paddle.id)
		
		if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
			if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
				return True	
				
			return False
	
	#Checks for collision of paddle and ball for paddle right		
	def hit_paddle1(self,pos):
		
		paddle_pos = self.canvas.coords(self.paddle1.id)
		
		if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
			if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
				return True	
				
			return False
			
	# Draw Ball and Check for all collisions
	def draw(self):
		self.canvas.move(self.id,self.x,self.y)
		pos = self.canvas.coords(self.id)
		if pos[1] <= 0:
			self.y = 4
		if pos[3] >= self.canvas_height:
			self.y =-4
		if pos[0] <= 0:
			self.p1S += 1
			#for mac : os.system('afplay {}&'.format('Beep2.wav'))
			#for windows: import winsound ; winsound.PlaySound('Beep2.wav')
			#os.system('aplay {}&'.format('Beep2.wav'))# for linux
			self.canvas.move(self.id,327,220)
			self.x = 4
			self.updatep1(self.p1S)
		if pos[2] >= self.canvas_width:
			self.pS += 1
			#os.system('aplay {}&'.format('Beep2.wav'))
			self.canvas.move(self.id,-327,-220)
			self.x = -4
			self.updatep(self.pS)
		if self.hit_paddle(pos):
			#os.system('aplay {}&'.format('Beep1.wav'))
			self.x = 4
		if self.hit_paddle1(pos):
			#os.system('aplay {}&'.format('Beep1.wav'))
			self.x = -4
		
		
# paddle class	
class Paddle:
	def __init__(self,canvas,color):
		self.canvas = canvas
		self.id = self.canvas.create_rectangle(0,200,20,310,fill=color)
		self.y = 0
		self.canvas_height=self.canvas.winfo_height()
		self.canvas_width=self.canvas.winfo_width()
		#Binding
		self.canvas.bind_all('a',self.left)
		self.canvas.bind_all('d',self.right)	
		
	#moving paddle
	def left(self,e):
		self.y = -5
		
	def right(self,e):
		self.y = 5
	
	# Drawing 
	def draw(self):
		self.canvas.move(self.id,0,self.y)
		pos = self.canvas.coords(self.id)
		if pos[1] <= 0:
			self.y = 0
		if pos[3] >= 500:
			self.y = -0

# paddle right
class Paddle1:
	def __init__(self,canvas,color):
		self.canvas = canvas
		self.id = self.canvas.create_rectangle(680,200,710,310,fill=color)
		self.y = 0
		self.canvas_height=self.canvas.winfo_height()
		self.canvas_width=self.canvas.winfo_width()
		self.canvas.bind_all('<KeyPress-Left>',self.left)
		self.canvas.bind_all('<KeyPress-Right>',self.right)	
		
	def left(self,e):
		self.y = -5
		
	def right(self,e):
		self.y = 5
	
	def draw(self):
		self.canvas.move(self.id,0,self.y)
		pos = self.canvas.coords(self.id)
		if pos[1] <= 0:
			self.y = 0
		if pos[3] >= 500:
			self.y = 0
			

#objects
paddle = Paddle(canvas,'white')
paddle1 = Paddle1(canvas,'white')		
ball = Ball(canvas,paddle1,paddle,'white')

#game loop
while 1:

	ball.draw()
	paddle.draw()
	paddle1.draw()
	if ball.checkwin():
		messagebox.showinfo('Game End',ball.checkwin()+' won!!')
		break
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)

	
quit()
tk.mainloop()
