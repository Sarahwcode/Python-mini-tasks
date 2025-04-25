from userperson import person_user


class french_user(person_user):

  def french(self):
    print(f"Bonjour {self.name}")
