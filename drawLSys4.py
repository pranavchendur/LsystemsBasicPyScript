import turtle

def createLSystem(numIters,axiom):
	startString = axiom
	endString = ""
	for i in range(numIters):
		endString = processString(startString)
		startString = endString

	return endString

def processString(oldStr):
	newstr = ""
	for ch in oldStr:
		newstr = newstr + applyRules(ch)

	return newstr

def applyRules(ch):
	newstr = ""
	if ch == 'F':
		newstr = ''
	if ch == 'X':
		newstr = 'FX+FX+FXFY-FY-'
	if ch == 'Y':
		newstr = '+FX+FXFY-FY-FY'
	else:
		newstr = ch    # no rules apply so keep the character

	return newstr

def drawLsystem(aTurtle, instructions, angle, distance):
	# instructions = reversed(instructions)
	for cmd in instructions:
		if cmd == 'W':
			aTurtle.forward(distance)
		elif cmd == 'X':
			aTurtle.backward(distance)
		elif cmd == '+':
			aTurtle.right(angle)
		elif cmd == '-':
			aTurtle.left(angle)

def removeDuplicate(foo):  
    return ''.join([foo[i] for i in range(len(foo)-1) if foo[i+1]!= foo[i]]+[foo[-1]]) 

def main():
	inst = createLSystem(3, "XYXYXYX+XYXYXYX+XYXYXYX+XYXYXYX")   # create the string
	# inst = removeDuplicate(inst)
	print(inst)
	t = turtle.Turtle()            # create the turtle
	wn = turtle.Screen()

	t.up()
	t.goto(200, 0)
	t.right(180)
	t.pencolor("#f7491e")
	t.down()
	t.speed(0)
	drawLsystem(t, inst, 90, 5)   # draw the picture
								  # angle 60, segment length 5
	wn.exitonclick()

main()
