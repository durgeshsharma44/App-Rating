

class AuthRouter:
    
    def db_for_read(self, model, **hints):
       
        if model._meta.app_label == 'accounts':
            if model.__name__ == 'Admin':
                return 'admin_db'
            if model.__name__ == 'User':
                return 'user_db'
        return None

    def db_for_write(self, model, **hints):
       
        if model._meta.app_label == 'accounts':
            if model.__name__ == 'Admin':
                return 'admin_db'
            if model.__name__ == 'User':
                return 'user_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
       
        if obj1._state.db in ('admin_db', 'user_db') and obj2._state.db in ('admin_db', 'user_db'):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
       
        if app_label == 'accounts':
            if model_name == 'admin':
                return db == 'admin_db'
            if model_name == 'user':
                return db == 'user_db'
        return None
