from main.db.data import get_db_connection
def get(name):
  conn = get_db_connection()
  users = conn.execute(f"SELECT id,nickname,email,created_at FROM USER where id='{name}'").fetchall()
  conn.close()
  return users

def get_all():
  conn = get_db_connection()
  users = conn.execute('SELECT  id,nickname,email,created_at FROM USER').fetchall()
  conn.close()
  return users

def insert_one(user_id, user_nickname, user_pw_hash, user_email, now):
  conn = get_db_connection()
  users = conn.execute(f"insert into USER (id, nickname, pw, email, created_at ) values ('{user_id}', '{user_nickname}', '{user_pw_hash}', '{user_email}', '{now}')").fetchall()
  conn.commit()
  conn.close()
  return users