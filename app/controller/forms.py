# -*- coding: utf-8 -*-

from flaskext.wtf import Form, TextField, TextAreaField, PasswordField, validators

class EntryForm(Form):
    title = TextField(u'タイトル', [validators.required(), validators.Length(max=255)])
    text = TextAreaField(u'内容', [validators.required()])
