from flask import render_template, redirect, url_for
from app import app
from app.forms import EditProfileForm

@app.route('/')
def index():
    return "Главная страница. Перейдите на <a href='/edit_profile'>редактирование профиля</a>."

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        # Обработка сохранения изменений профиля (добавьте свою логику здесь)
        return redirect(url_for('index'))  # Перенаправление на главную страницу после сохранения
    return render_template('edit_profile.html', form=form)
