# app/routes.py
import os
import random
import string
from datetime import datetime
from flask import render_template, Blueprint, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from app.models import JobApplication, Template, db

main_bp = Blueprint('main', __name__)

def generate_unique_filename(original_name, template_type):
    # Generates a unique filename by appending the type, date, and a random uppercase letter
    name, ext = os.path.splitext(original_name)
    date_str = datetime.utcnow().strftime("%Y%m%d")
    rand_char = random.choice(string.ascii_uppercase)
    unique_name = f"{name}_{template_type}_{date_str}_{rand_char}{ext}"
    return secure_filename(unique_name)

@main_bp.route('/')
def dashboard():
    # Calculate stats for display on the home/dashboard page
    total_jobs = JobApplication.query.count()
    # Count jobs that have been updated from the default "Applied" status
    applied_jobs = JobApplication.query.filter(JobApplication.status != "Applied").count()
    cv_templates = Template.query.filter_by(type='CV').count()
    coverletter_templates = Template.query.filter_by(type='CoverLetter').count()
    return render_template('dashboard.html', total_jobs=total_jobs, applied_jobs=applied_jobs,
                           cv_templates=cv_templates, coverletter_templates=coverletter_templates)

@main_bp.route('/templates', methods=['GET', 'POST'])
def templates_page():
    if request.method == 'POST':
        # Handle file upload for a template
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        template_type = request.form.get('template_type')
        if file and template_type in ['CV', 'CoverLetter']:
            unique_filename = generate_unique_filename(file.filename, template_type)
            upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(upload_path)
            # Save the uploaded template info to the database
            new_template = Template(type=template_type, filename=unique_filename)
            db.session.add(new_template)
            db.session.commit()
            flash('Template uploaded successfully')
            return redirect(url_for('main.templates_page'))
    # For GET, list the uploaded templates
    cv_templates = Template.query.filter_by(type='CV').all()
    coverletter_templates = Template.query.filter_by(type='CoverLetter').all()
    return render_template('templates.html', cv_templates=cv_templates, coverletter_templates=coverletter_templates)

@main_bp.route('/add-job', methods=['GET', 'POST'])
def add_job():
    if request.method == 'POST':
        # Gather data from the form
        url_ref = request.form.get('job_url')
        title = request.form.get('job_title')
        company = request.form.get('company')
        description = request.form.get('description')
        # Create a new JobApplication record
        new_job = JobApplication(title=title, company=company, description=description)
        db.session.add(new_job)
        db.session.commit()
        flash('Job added successfully')
        return redirect(url_for('main.add_job'))
    return render_template('add_job.html')

@main_bp.route('/apply-job', methods=['GET'])
def apply_job_list():
    # List all jobs so the user can choose one to apply for
    jobs = JobApplication.query.all()
    return render_template('apply_job_list.html', jobs=jobs)

@main_bp.route('/apply-job/<int:job_id>', methods=['GET'])
def apply_job_detail(job_id):
    # Show details for a selected job, with a placeholder for future matching analysis
    job = JobApplication.query.get_or_404(job_id)
    return render_template('apply_job_detail.html', job=job)

@main_bp.route('/status', methods=['GET', 'POST'])
def status_page():
    if request.method == 'POST':
        job_id = request.form.get('job_id')
        new_status = request.form.get('status')
        job = JobApplication.query.get(job_id)
        if job:
            job.status = new_status
            db.session.commit()
            flash('Job status updated')
        return redirect(url_for('main.status_page'))
    jobs = JobApplication.query.all()
    return render_template('status.html', jobs=jobs)
