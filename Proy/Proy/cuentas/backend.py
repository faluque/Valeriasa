from cuentas.models import usuarios
from django.db import connection
import logging


class MyAuthBackend(object):
    def authenticate(self, username, password):    
        try:
            user = usuarios.objects.get(username=username)
            if user.check_password(password):
                return user
            else:
                return None
        except usuarios.DoesNotExist:
            logging.getLogger("error_logger").error("usuario %s no existe " % login)
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None

   

    def get_user(self, user_id):
        try:
            user = usuarios.objects.get(id=user_id)
            if user.is_active:
                return user
            return None
        except UserModel.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(user_id)d not found")
            return None

        