#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import app

app.secret_key = '123123123'
app.run(host=app.config.get('HOST'), port=app.config.get('PORT'), debug=True)
