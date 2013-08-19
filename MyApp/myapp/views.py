from pyramid.response import Response
from pyramid.view import view_config

from pyramid.httpexceptions import HTTPFound    

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    WebFormData,
    )


# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
    # try:
        # one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
    # except DBAPIError:
        # return Response(conn_err_msg, content_type='text/plain', status_int=500)
    # return {'one': one, 'project': 'MyApp'}

# conn_err_msg = """\
# Pyramid is having a problem using your SQL database.  The problem
# might be caused by one of the following things:

# 1.  You may need to run the "initialize_MyApp_db" script
    # to initialize your database tables.  Check your virtual 
    # environment's "bin" directory for this script and try to run it.

# 2.  Your database server may not be running.  Check that the
    # database server referred to by the "sqlalchemy.url" setting in
    # your "development.ini" file is running.

# After you fix the problem, please restart the Pyramid application to
# try it again.
# """

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
    

