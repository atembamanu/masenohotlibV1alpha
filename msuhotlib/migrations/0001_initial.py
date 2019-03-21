# Generated by Django 2.1.7 on 2019-03-21 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminChallenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_name', models.CharField(max_length=255)),
                ('challenge_category', models.CharField(choices=[('prog', 'Programming'), ('net', 'Networking'), ('blockc', 'Blockchain'), ('datasc', 'Data Science'), ('webdev', 'Web Development'), ('script', 'Scripting'), ('intell', 'Artificial Intelligence')], max_length=6)),
                ('challenge_level', models.CharField(choices=[('beginner', 'Beginner Level'), ('intermediate', 'Intermediate Level'), ('advanced', 'Advanced Level')], max_length=12)),
                ('challenge_url', models.URLField()),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Admin Challenge Uploads',
            },
        ),
        migrations.CreateModel(
            name='AdminResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_type', models.CharField(choices=[('prog', 'Programming'), ('net', 'Networking'), ('blockc', 'Blockchain'), ('datasc', 'Data Science'), ('webdev', 'Web Development'), ('script', 'Scripting'), ('intell', 'Artificial Intelligence')], max_length=6)),
                ('resource_name', models.CharField(max_length=255)),
                ('resource_url', models.URLField()),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Admin Resource Uploads',
            },
        ),
        migrations.CreateModel(
            name='AdminTutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_type', models.CharField(choices=[('vids', 'Hot Videos'), ('pdfs', 'Free Pdfs'), ('link', 'Direct Link')], max_length=4)),
                ('tutorial_name', models.CharField(max_length=255)),
                ('tutorial_url', models.URLField()),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Admin Tutorial Uploads',
            },
        ),
        migrations.CreateModel(
            name='DeptUnit',
            fields=[
                ('unit_code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('unit_name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Units',
            },
        ),
        migrations.CreateModel(
            name='LectureResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(choices=[('notes', 'Lecture Notes'), ('assig', 'Assignment'), ('TAcat', 'Take Away CAT')], max_length=5)),
                ('resource_url', models.URLField()),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Lecture Uploads',
            },
        ),
        migrations.CreateModel(
            name='LibrarianResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pastpaper_name', models.CharField(max_length=255)),
                ('academic_year', models.CharField(max_length=20)),
                ('pastpaper_url', models.URLField()),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Librarian Uploads',
            },
        ),
        migrations.CreateModel(
            name='MsuDepartmentList',
            fields=[
                ('dept_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Department',
            },
        ),
        migrations.CreateModel(
            name='MsuFacultyList',
            fields=[
                ('faculty_code', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('faculty_name', models.CharField(max_length=255)),
                ('faculty_dean', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Faculty',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_code', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('person_role', models.CharField(choices=[('adm', 'Administrator'), ('lec', 'Lecturer'), ('lib', 'Librarian')], max_length=3)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Person',
            },
        ),
        migrations.CreateModel(
            name='StudySemester',
            fields=[
                ('semester_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('semester', models.CharField(choices=[('SEM1', 'Semester I'), ('SEM2', 'Semester II')], max_length=4)),
                ('academic_year', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Semester',
            },
        ),
        migrations.AddField(
            model_name='msudepartmentlist',
            name='faculty_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msuhotlib.MsuFacultyList'),
        ),
        migrations.AddField(
            model_name='librarianresource',
            name='course_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_fk', to='msuhotlib.MsuDepartmentList'),
        ),
        migrations.AddField(
            model_name='librarianresource',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='librarian_fk', to='msuhotlib.Person'),
        ),
        migrations.AddField(
            model_name='lectureresource',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_fk', to='msuhotlib.StudySemester'),
        ),
        migrations.AddField(
            model_name='lectureresource',
            name='unit_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_fk', to='msuhotlib.DeptUnit'),
        ),
        migrations.AddField(
            model_name='lectureresource',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_fk', to='msuhotlib.Person'),
        ),
        migrations.AddField(
            model_name='deptunit',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dept_name_fk', to='msuhotlib.MsuDepartmentList'),
        ),
        migrations.AddField(
            model_name='deptunit',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semester_fk', to='msuhotlib.StudySemester'),
        ),
        migrations.AddField(
            model_name='admintutorial',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_name_fk', to='msuhotlib.Person'),
        ),
        migrations.AddField(
            model_name='adminresource',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msuhotlib.Person'),
        ),
        migrations.AddField(
            model_name='adminchallenge',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msuhotlib.Person'),
        ),
    ]
