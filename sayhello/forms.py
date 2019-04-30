# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('发送者名字', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('要发送的消息', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField('提交')
