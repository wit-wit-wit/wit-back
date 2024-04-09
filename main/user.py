from flask import Blueprint, request, jsonify,json
from main import now
from main.db.sql import user_sql as user
import hashlib

blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route('/check', methods=['GET'])
def id_check():
  result = user.get(request.args.get('id'))
  if len(result):
    return json.dumps({'result': 'fail', 'msg': '이미 존재 하는 ID 입니다!'}, ensure_ascii=False)
  else:
    return json.dumps({'result': 'success', 'msg': '생성 가능한 ID 입니다.'}, ensure_ascii=False)


@blueprint.route('/register',methods=['POST'])
def register():
  user_nickname = request.form['nickname']
  user_email = request.form['email']
  user_id = request.form['id']
  user_pw = request.form['pw']
  user_pw_hash = hashlib.sha256(user_pw.encode('utf-8')).hexdigest()

  # 이미 존재하는 아이디면 패스!
  result = user.get(user_id)
  if len(result):
    return jsonify({'result': 'fail', 'msg': '이미 존재 하는 ID 입니다!'})
  else:
    user.insert_one(user_id, user_nickname, user_pw_hash, user_email, now)
  return jsonify({'result': 'success'})



@blueprint.route('/get')
def get_all_user():
  all_data = user.get_all()
  print(all_data)
  return all_data
#
# @blueprint.route('/login', methods=['POST'])
# def login():
#   user_id = request.form['id']
#   user_pw = request.form['pw']
#
#   # 회원가입 때와 같은 방법으로 pw를 암호화합니다.
#   user_pw_hash = hashlib.sha256(user_pw.encode('utf-8')).hexdigest()
#
#   # id, 암호화된pw을 가지고 해당 유저를 찾습니다.
#   result = db.user.find_one({'id': user_id, 'pw': user_pw_hash})
#   print(user_pw_hash)
#
#   # 찾으면 JWT 토큰을 만들어 발급합니다.
#   if result is not None:
#     # # JWT 토큰 생성
#     # payload = {
#     #   'id': id_receive,
#     #   'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=100)
#     # }
#     # token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
#     #
#     # # token을 줍니다.
#     return jsonify({'result': 'success', 'id':user_id})
#   else:
#     return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

@blueprint.route('/edit')
def edit():
  return '수정'