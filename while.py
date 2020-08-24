num_of_tries = 0

while num_of_tries != 3:

    
 username = input('Please Enter Your Username: ')
 password = input('Pleae Enter Your Password:  ')
 if  username == 'Ahmed' and password == '123':
  print('Welcome')
  num_of_tries = 0
  exit()
 else:
      print('error')
      num_of_tries += 1
      print('you have ' + str(3 - num_of_tries)+ ' tries left')