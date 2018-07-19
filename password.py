# 密碼重試程式
# passwor = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入 3次
# 如果正確就印出"登入成功"
# 如果不正確就印出"密碼錯誤! 還有幾次機會!"

password = 'a123456'
i = 3 # 最多3次機會
while i > 0:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break # 跳出迴圈
	else:
		i = i - 1
		print('密碼錯誤! 還有', i, '次機會')
		


