correct_password = 'owo123456'
x = 3
while x > 0:
	password = input('請輸入您にゃんこ大戦争的密碼:')
	if password == correct_password:
		print('登入成功!開始遊戲owo+')
		break
	else:
		x = x-1
		if x == 0:
			print('登入失敗，將強制登出!' )
		elif x > 0:
			print('密碼錯誤!還有', x, '次機會' )