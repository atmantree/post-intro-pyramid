from pyramid.view import view_config

from pyramid.httpexceptions import HTTPFound    

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    WebFormData,
    )

@view_config(route_name='home', renderer='templates/home.pt')
def home(request):
    save_form = request.route_url('list')
    return {'save_form':save_form}

@view_config(route_name='list', renderer='templates/list.pt')
def list(request):
    if 'form.submitted' in request.params:
        title = request.params['title']
        comment_text = request.params['comment_text']
        comment = WebFormData(title, comment_text)
        DBSession.add(comment)
    data = DBSession.query(WebFormData).all()
    return {'data':data}

@view_config(route_name='show', renderer="templates/show.pt")
def show(request):
    uid = request.matchdict['uid']
    comment = DBSession.query(WebFormData).filter_by(id=uid).first()
    if comment is None:
        return HTTPFound(request.route_url('list'))
    return {'comment': comment}
    

