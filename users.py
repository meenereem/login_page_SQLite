class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

def create_user_account(db, email, password):
    q_str = "INSERT INTO users ({1}, {2}) values (?, ?)".format(TABLE_NAME, FIELD_EMAIL, FIELD_PASSHASH)
    c = db.cursor()
    c.execute(q_str, [email, password])
    db.commit()
    return get_one_by_email(db, email)

def create_session_token(db, email, token):
    q_str = "INSERT INTO user_sessions ({1}, {2}) values (?, ?)".format(TABLE_NAME, FIELD_EMAIL, FIELD_TOKEN)
    c = db.cursor()
    c.execute(q_str, [email, token])
    db.commit()

def get_one_by_email(db, email):
    if email is None:
        return None
    q_str = "SELECT {0}, {1} from {2} WHERE {3}=?".format(FIELD_EMAIL, FIELD_PASSHASH, TABLE_NAME, FIELD_EMAIL)
    c = db.cursor()
    c.execute(q_str, [email])
    users = [User(r[0], r[1]) for r in c.fetchall()]
    if len(users) < 1:
        return None
    return users[0]

def is_email_already_taken(db, email):
    user = get_one_by_email(db, email)
    if user is None:
        return False
    return True

########
# Defs #
########
TABLE_NAME = 'users'
FIELD_EMAIL = 'email'
FIELD_PASSHASH = 'password'
TABLE_NAME2 = 'user_sessions'
FIELD_EMAIL2 = 'email'
FIELD_TOKEN = 'token'

