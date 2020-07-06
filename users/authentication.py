from django.contrib.auth.models import User


class EmailAuthBackend():
	def authenticate(self, request, username, password):
		try:
			user = User.objects.get(email=username)
			success = user.check_password(password)
			if success:
				return user
			return None
		except User.DoesNotExist:
			return None

	def get_user(self, uid):
		try:
			return User.objects.get(pk=uid)
		except User.DoesNotExist:
			return None