from flask import Blueprint

blueprint = Blueprint('comment',__name__,url_prefix='/comment')

@blueprint.route('/read')
def get():
  return '읽기'

@blueprint.route('/save')
def create():
  return '저장'