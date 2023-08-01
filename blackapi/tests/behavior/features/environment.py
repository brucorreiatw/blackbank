# import ipdb
from blackapi import create_app

def before_all(context):
    context.base_url = context.config.userdata.get('base_url')
    
def before_feature(context, feature):
    context.flask = create_app()
    context.flask.testing = True
    context.flask_context = context.flask.test_request_context()
    context.flask_context.push()
    context.client = context.flask.test_client()

# def after_step(context, step):
#     if step.status == 'failed':
#         ipdb.spost_mortem(step.exc_traceback)