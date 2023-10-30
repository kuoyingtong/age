driving = input('你有開過車嗎?')
if driving != '有' and driving != '沒有':
	print('只能輸入有或沒有')
	raise SystemExit

age = input('請問你的年齡:')
age = int(age)
if driving == '有' :
	if age >= 18:
		print('ok')
	else:
		print('有問題喔')
elif driving == '沒有':
	if age >= 18:
		print('怎麼不考駕照?')
	else:
		print('沒關係再等幾年')
