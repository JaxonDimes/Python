from users import Admin
from users import User
from users import Privileges

this = Admin('James', 'Dimes', 'Heath', 'Dr.Pepper')
that = User('John', 'Doe', '404', 'Missing Texture')


Privileges()
that.greet_user()
this.greet_user()
this.show_privileges()

