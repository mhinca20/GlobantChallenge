#!/usr/bin/env python
import os
from app import blueprint
from app.main import create_app, db

if __name__ == '__main__':
    app = create_app('dev')
    app.register_blueprint(blueprint)
    app.app_context().push()
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0') 
 