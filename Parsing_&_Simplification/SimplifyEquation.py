import ui
import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mpl

init_text = 'This program allows you to test the homogeneity of your\rexpressions in physics problems. In larger scale you can\ruse it  to simplify any simple litteral equations.\rTo make sure to use it correctly, please\rlook at the usage conditions.'
conditions = 'This simple program is only accurate for processing common and simple equations.\r\rFor this reason , please respect the following conditions :\r\r- use standard computational math symbols ( * ; / ; ^ )\r\r- for non-integer exponents write them as a fraction and into brackets (instead of a^0.5 write a^(1/2))\r\r- for integer exponents put brackets only if negative or if it is followed by a "/" (e.g. : m^(2)/kg )\r\r- you can do a global division meaning dividing many units at the same time this way : a/(b*c*d), but cannot combine them in parallel as : a/(b*c/(d*e))\r\r- you can raise many units at the same time to the same power (e.g. : (a*b/(c*d))^(-3/4)), and include a global division within it as defined above but cannot combine them in parallel as : (a*b/(c*d)^2)^6\r\rHave fun !'

view = ui.View()



Init_text = ui.TextView(text = init_text, x= 350, y = 0, height = 200, width = 900, text_color='#00ac0f')
Init_text.font = ('Apple Color Emoji', 15)


expression= ui.TextField(height=35,width=200,x=150,y=50 )
lblexpression= ui.Label(text='expression',x=50,y=50,height=35,width=100,text_color='#000000')
lblexpression.font = ('Didot', 20)

btn = ui.Button(title='calculate', x=50 , y=150,height=35,width=100,tint_color='#ffffff',font=('Heiti TC',18),background_color='#00ff16',corner_radius=10)

getLaTex = ui.Button(title='LaTex', x=50 , y=200,height=35,width=100,tint_color='#ffffff',font=('Heiti TC',18),background_color='#00ff16',corner_radius=10)

Condition_btn = ui.Button(title='See Conditions', x=50 , y=250,height=35,width=100,tint_color='#ffffff',font=('Heiti TC',18),background_color='#00ff16',corner_radius=10)


view.bg_color='#ffffff'
result = ui.ImageView(x=100,y=200, height=600,width=828)

Conditions_view = ui.ScrollView(always_bounce_vertical = True)

Conditions = ui.TextView(text = conditions, x = 0, y=0, height = 1000, width = 1000, text_color='#dd0000', background_color= '#000000')
#x = 0, y=0, height = 500, width = 1000,
Conditions.font = ('Apple Color Emoji', 20)

def Units(z):
	Units = {}
	
	GlobExp = re.findall(r'(\/)?(\((([^a-zA-Z0-9_])?\(?([A-Za-z]+)(\^\(?(-?\d+\/?\d*)\)?)?\)?)+\))(\^\(?(-?\d+\/?\d*)\)?)', z , 0)
			
	for i in range(len(GlobExp)):
		inside = GlobExp[i][1]	
		glob = GlobExp[i][8]
		
		insidePar = re.findall(r'\/\((([A-Za-z]+)(\^\(?(-?\d+\/?\d*)\)?)?(([^a-zA-Z0-9_])([A-Za-z]+)(\^\(?(-?\d+\/?\d*)\)?)?)+)\)', inside, 0)
	
		for j in range(len(insidePar)):		
			in_insidePar = insidePar[j][0]	
			SimpExp = re.findall(r'([^a-zA-Z0-9_])?([A-Za-z]+)(\^\(?(-?\d+\/?\d*)\)?)?', in_insidePar , 0)
			for k in range(len(SimpExp)):			
				if SimpExp[k][3] == '':
					if SimpExp[k][0] == '/' :
						Unit_Exp = eval(glob)
						
					else :
						Unit_Exp = eval('-'+glob)
						
				else :
					if SimpExp[j][0] == '/' :
						Unit_Exp = eval(str(SimpExp[k][3])+'*'+glob)
						
					else :
						Unit_Exp = eval('-'+str(SimpExp[j][3])+'*'+glob)
						
				if GlobExp[i][0] == '/':
					Unit_Exp = -Unit_Exp
				if SimpExp[k][1] in Units :
					Units[SimpExp[k][1]] += Unit_Exp
				else:
					Units[SimpExp[k][1]]= Unit_Exp
			
		rest = re.sub(r'\/\((([A-Za-z]+)(\^\(?(-?\d+\/?\d*)\)?)?(([^a-zA-Z0-9_])([A-Za-z]+)(\^\(?(-?\d+\/?\d*)\)?)?)+)\)','',inside)
		SimpExp = re.findall(r'([^a-zA-Z0-9_])?([A-Za-z]+)(\^\(?(-?\d+\/?\d*)\)?)?', rest , 0)
		for j in range(len(SimpExp)):
			
			if SimpExp[j][3] == '':
				if SimpExp[j][0] == '/' :
					Unit_Exp = eval('-'+glob) 
					
				else :
					Unit_Exp = eval(glob) 
					
			else :
				if SimpExp[j][0] == '/' :
					Unit_Exp = eval('-'+glob+'*'+str(SimpExp[j][3]))  
					
				else :
					Unit_Exp = eval(glob+'*'+str(SimpExp[j][3])) 
					
			if GlobExp[i][0] == '/':
				Unit_Exp = -Unit_Exp 
			if SimpExp[j][1] in Units :
				Units[SimpExp[j][1]] += Unit_Exp 
			else:
				Units[SimpExp[j][1]]= Unit_Exp 
				
				
	
	surroundings = re.sub(r'(\/)?(\((([^a-zA-Z0-9_])?\(?([A-Za-z]+)(\^\(?(-?\d+\/?\d*)\)?)?\)?)+\))(\^\(?(-?\d+\/?\d*)\)?)', '',z)
	
	parentheses2 = re.findall(r'\/\((([A-Za-z]+)(\^\(?(-?\d+\/?\d*)\)?)?(([^a-zA-Z0-9_])([A-Za-z]+)(\^\(?(-?\d+\/?\d*)\)?)?)+)\)', surroundings , 0)
	
	for i in range(len(parentheses2)):
		SimpExp = re.findall(r'([^a-zA-Z0-9_])?([A-Za-z]+)(\^\(?(-?\d+\/?\d*)\)?)?', parentheses2[i][0] , 0)
		for j in range(len(SimpExp)):
			if SimpExp[j][3] == '':
				if SimpExp[j][0] == '/' :
					Unit_Exp = 1
					
				else :
					Unit_Exp = -1
					
			else :
				if SimpExp[j][0] == '/' :
					Unit_Exp = eval(str(SimpExp[j][3]))
					
				else :
					Unit_Exp = eval('-'+str(SimpExp[j][3]))
					
			if SimpExp[j][1] in Units :
				Units[SimpExp[j][1]] += Unit_Exp
			else:
				Units[SimpExp[j][1]]= Unit_Exp
				
				
	
	reste2 = re.sub(r'\/\((([A-Za-z]+)(\^\(?(-?\d+\/?\d*)\)?)?(([^a-zA-Z0-9_])([A-Za-z]+)(\^\(?(-?\d+\/?\d*)\)?)?)+)\)','',surroundings)
	
	SimpExp = re.findall(r'([^a-zA-Z0-9_])?([A-Za-z]+)(\^\(?(-?\d+\/?\d*)\)?)?', reste2 , 0)
	for j in range(len(SimpExp)):
		if SimpExp[j][3] == '':
			if SimpExp[j][0] == '/' :
				Unit_Exp = -1
				
			else :
				Unit_Exp = 1
				
		else :
			if SimpExp[j][0] == '/' :
				Unit_Exp = eval('-'+str(SimpExp[j][3]))
				
			else :
				print(SimpExp[j][3])
				Unit_Exp = eval(str(SimpExp[j][3]))
				
		if SimpExp[j][1] in Units :
			Units[SimpExp[j][1]] += Unit_Exp
		else:
			Units[SimpExp[j][1]]= Unit_Exp
			
	print(Units)
	# this following list is to complete with composed units
	extraunits = [('N', (('kg', 1), ('m', 1), ('s', -2))), ('A', (('C', 1), ('s', -1))), ('Pa', (('kg', 1), ('m', -1), ('s', -2))), ('V', (('kg', 1), ('m', 2), ('s', -2), ('C', -1))),('R', (('J',1),('K',-1),('mol',-1)))]
	for i in extraunits:
		if i[0] in Units:
			for j in i[1] :
				if j[0] in Units:
					
					Units[j[0]] = Units[j[0]] + Units[i[0]]*j[1]
				else:
					Units[j[0]] = Units[i[0]]*j[1]
			del Units[i[0]]
	print(list(Units.items()))
	return Units
	
	
	
	
def Dico2LaTex2(z):
	dico = list(z.items())
	isFirst = True
	print(dico)
	positiv = []
	negativ = []
	Psquared = []
	Nsquared = []
	num = ''
	denom = ''
	sqrtnum = ''
	sqrtdenom = ''
	final=''
	for i in dico:		
		if i[1] < 0:
			if i[1] - int(i[1]) == -0.5 :
				Nsquared.append(i)
			else :
				negativ.append(i)
		else :
			if i[1] - int(i[1]) == 0.5 :
				Psquared.append(i)
			else :
				positiv.append(i)
			
	for j in positiv :
		if isFirst:
			num = num + '{' + j[0] + '}' + '^' + '{' + str(j[1]) + '}'
			isFirst = False
		else :
			num = num + '\cdot' + '{' + j[0] + '}' + '^' + '{' + str(j[1]) + '}'

	isFirst = True
	for h in negativ :
		if isFirst:
			denom = denom + '{' + h[0] + '}' + '^' + '{' + str(-h[1]) + '}'
			isFirst = False
		else:
			denom = denom + '\cdot' + '{' + h[0] + '}' + '^' + '{' + str(-h[1]) + '}'
				
				
	isFirst = True
	for k in Psquared:
		if isFirst:
			sqrtnum = 	sqrtnum + '{' + k[0] + '}' + '^' + '{' + str(2*k[1]) + '}'
			isFirst = False
		else :
			sqrtnum = 	sqrtnum + '\cdot' + '{' + k[0] + '}' + '^' + '{' + str(2*k[1]) + '}'
	
	isFirst = True
	for l in Nsquared:
		if isFirst:
			sqrtdenom = 	sqrtdenom + '{' + l[0] + '}' + '^' + '{' + str(-2*l[1]) + '}'
			isFirst = False
		else :
			sqrtdenom = 	sqrtdenom + '\cdot' + '{' + l[0] + '}' + '^' + '{' + str(-2*l[1]) + '}'
			
	if len(negativ)>0 :	
		if len(positiv)>0 :
			final = '\\frac{' + num + '}' + '{' + denom + '}'
		else :
			final = '\\frac{1}' + '{' + denom + '}'
	else :
		final = num
		
	if len(negativ)>0 or len(positiv)>0 :
		if len(Psquared) > 0 :
			if len(Nsquared) > 0 :
				final = final + '\cdot\sqrt{\\frac{' + sqrtnum + '}' + '{' + sqrtdenom + '}}'
			else :
				final = final + '\cdot\sqrt{' + sqrtnum + '}'
		else:
			if len(Nsquared) > 0 :
				final = final + '\cdot\sqrt{\\frac{1}' + '{' + sqrtdenom + '}}'
						
	else:
		if len(Psquared) > 0 :
			if len(Nsquared) > 0 :
				final = final + '\sqrt{\\frac{' + sqrtnum + '}' + '{' + sqrtdenom + '}}'
			else :
				final = final + '\sqrt{' + sqrtnum + '}'
		else:
			if len(Nsquared) > 0 :
				final = final + '\sqrt{\\frac{1}' + '{' + sqrtdenom + '}}'
				
	return final




def LaTex2Image(equation, file_name):
	plt.text(0.1,0.7,r'$%s$' % equation, fontsize = 50)
	plt.axis('off')
	plt.savefig(file_name, bbox_inches='tight')
	plt.show()
	img = mpimg.imread(file_name)
	return img
	
file_name = "result.png"



def btn_tapped(sender):	
	plt.clf()
	z = LaTex2Image(Dico2LaTex2(Units(expression.text)),file_name)
	result.image = ui.Image(file_name)
	
def getLaTex_tapped(sender):
	with open('LaTex.txt', 'w') as LaTex:
		LaTex.writelines(Dico2LaTex2(Units(expression.text)))		
		
def Conditions_btn_tapped(sender):
	Conditions_view.add_subview(Conditions)
	Conditions_view.present()
	
btn.action = btn_tapped
getLaTex.action = getLaTex_tapped
Condition_btn.action = Conditions_btn_tapped

for subview in (expression,lblexpression,btn,result,getLaTex, Init_text, Condition_btn):
	view.add_subview (subview)
view.present()





