from django.db import models


class MsuFacultyList(models.Model):
    """ MSU FACULTY LIST model."""
    faculty_code = models.CharField(primary_key=True, max_length=8)
    faculty_name = models.CharField(max_length=255)
    faculty_dean = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return self.faculty_name

    class Meta:
        db_table = 'Faculty'


class MsuDepartmentList(models.Model):
    """Master MSU DEPARTMENT LIST model."""
    dept_id = models.CharField(primary_key=True, max_length=8)
    dept_name = models.CharField(max_length=255)
    faculty_name = models.ForeignKey(MsuFacultyList, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.dept_name, self.faculty_name)

    class Meta:
        db_table = 'Department'


class StudySemester(models.Model):
    """ MSU SEMESTER LIST model."""
    semester_id = models.CharField(primary_key=True, max_length=8)
    SEMESTER_TYPE = (
        ("SEM1", "Semester I"),
        ("SEM2", "Semester II"),
    )
    semester = models.CharField(max_length=4, choices=SEMESTER_TYPE)
    academic_year = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.semester, self.academic_year)

    class Meta:
        db_table = 'Semester'


class DeptUnit(models.Model):
    """ DEPT UNIT LIST model."""
    unit_code = models.CharField(primary_key=True, max_length=6)
    unit_name = models.CharField(max_length=255)
    department = models.ForeignKey(
        MsuDepartmentList, related_name='dept_name_fk',
        on_delete=models.CASCADE)
    semester = models.ForeignKey(
        StudySemester, related_name='semester_fk',
        on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.unit_name, self.semester)

    class Meta:
        db_table = 'Units'


class Person(models.Model):
    """MSU HOTLIB USERS model"""
    PERSON_ROLE = (
        ("adm", "Administrator"),
        ("lec", "Lecturer"),
        ("lib", "Librarian"),
    )
    user_code = models.CharField(primary_key=True, max_length=8)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    person_role = models.CharField(max_length=3, choices=PERSON_ROLE)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.username, self.person_role)

    class Meta:
        db_table = 'Person'


class LectureResource(models.Model):
    RESOURCE_CHOICE = (
        ("notes", "Lecture Notes"),
        ("assig", "Assignment"),
        ("TAcat", "Take Away CAT"),
    )
    resource_name = models.CharField(max_length=5, choices=RESOURCE_CHOICE)
    unit_name = models.ForeignKey(
        DeptUnit, related_name='unit_fk',
        on_delete=models.CASCADE)
    semester = models.ForeignKey(
        StudySemester, related_name='unit_fk',
        on_delete=models.CASCADE)
    resource_url = models.URLField()
    uploaded_by = models.ForeignKey(
        Person, related_name='person_fk',
        on_delete=models.CASCADE)
    uploaded_on = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.resource_name, self.resource_url)

    class Meta:
        db_table = 'Lecture Uploads'


class LibrarianResource(models.Model):
    pastpaper_name = models.CharField(max_length=255)
    academic_year = models.CharField(max_length=20)
    pastpaper_url = models.URLField()
    course_name = models.ForeignKey(
        MsuDepartmentList, related_name='course_fk',
        on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(
        Person, related_name='librarian_fk',
        on_delete=models.CASCADE)
    uploaded_on = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.pastpaper_name, self.pastpaper_url)

    class Meta:
        db_table = 'Librarian Uploads'


class AdminTutorial(models.Model):
    TUTORIAL_TYPE = (
        ("vids", "Hot Videos"),
        ("pdfs", "Free Pdfs"),
        ("link", "Direct Link"),
    )
    tutorial_type = models.CharField(max_length=4, choices=TUTORIAL_TYPE)
    tutorial_name = models.CharField(max_length=255)
    tutorial_url = models.URLField()
    uploaded_by = models.ForeignKey(
        Person, related_name='admin_name_fk', on_delete=models.CASCADE
    )
    uploaded_on = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.tutorial_name, self.tutorial_url)

    class Meta:
        db_table = 'Admin Tutorial Uploads'


class AdminResource(models.Model):
    RESOURCE_CAT = (
        ("prog", "Programming"),
        ("net", "Networking"),
        ("blockc", "Blockchain"),
        ("datasc", "Data Science"),
        ("webdev", "Web Development"),
        ("script", "Scripting"),
        ("intell", "Artificial Intelligence"),
    )
    resource_type = models.CharField(max_length=6, choices=RESOURCE_CAT)
    resource_name = models.CharField(max_length=255)
    resource_url = models.URLField()
    uploaded_by = models.ForeignKey(
        Person, on_delete=models.CASCADE
    )
    uploaded_on = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.resource_name, self.resource_url)

    class Meta:
        db_table = 'Admin Resource Uploads'


class AdminChallenge(models.Model):
    CHALLENGE_CAT = (
        ("prog", "Programming"),
        ("net", "Networking"),
        ("blockc", "Blockchain"),
        ("datasc", "Data Science"),
        ("webdev", "Web Development"),
        ("script", "Scripting"),
        ("intell", "Artificial Intelligence"),
    )
    CHALLENGE_LEVEL = (
        ("beginner", "Beginner Level"),
        ("intermediate", "Intermediate Level"),
        ("advanced", "Advanced Level"),
    )
    challenge_name = models.CharField(max_length=255)
    challenge_category = models.CharField(max_length=6, choices=CHALLENGE_CAT)
    challenge_level = models.CharField(max_length=12, choices=CHALLENGE_LEVEL)
    challenge_url = models.URLField()
    uploaded_by = models.ForeignKey(
        Person, on_delete=models.CASCADE
    )
    uploaded_on = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.challenge_name, self.challenge_url)

    class Meta:
        db_table = 'Admin Challenge Uploads'


class AdminHowToRepo(models.Model):
    howto_url = models.URLField()
    howto_description = models.TextField(max_length=255)
    uploaded_by = models.ForeignKey(
        Person, on_delete=models.CASCADE
    )
    uploaded_on = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return "%s %s" % (self.howto_url, self.howto_description)

    class Meta:
        db_table = 'Admin HowTO Uploads'
