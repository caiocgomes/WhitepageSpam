# -*- coding: utf-8 -*-

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, _app_ctx_stack

app = Flask(__name__)

@app.route('/')
def input():
    return "Hello World"
