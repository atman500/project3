print('welcom to  our a  new  website ', 'if  you  want  to  get  access to the  website you need to  complete  your  information', sep= '$')
correct_first_name= 'medini'
correct_second_name='atmane'
correct_afiliation='eloued'
#attemps  statement###

attempts = 3
for i in range(attempts):
  first_name=input('enter you  first name :').strip().lower()
  second_name=input('enter your  second name :').strip().lower()
  afiliation=input(' enter  your afiliation :').strip().lower()
  if first_name==correct_first_name and second_name==correct_second_name and afiliation==correct_afiliation:
      print('you answers are correct you  can acsess to the web_page')
    
  elif first_name== correct_first_name and second_name==correct_second_name  and afiliation !=correct_afiliation:
        print(' you can try  a gain')
        
  else:
      print('wrong answer you are not the  correct  user')
  if i ==attempts-1:
      print('you are reach the limite  you cant  acsse to  the  page')


 
