ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# Printing "ramit's" email.
print(ramit["email"])

# Grabbing the first value of ramit's key interest
print(ramit["interests"][0])

#  Grabbing Jasmine's email address
print(ramit[3])
