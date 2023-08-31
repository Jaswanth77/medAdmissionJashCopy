from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import os
def image_path_and_rename(instance, filename):
    folder = str(instance.ar_number)
    upload_to = 'images'
    ext = filename.split('.')[-1]
    # get filename
    filename = '{}.{}'.format(instance.ar_number, ext)
    # return the whole path to the file
    return os.path.join(upload_to+'/'+folder+'/', filename)

def pdf_path_and_rename(instance, filename):
    folder = str(instance.ar_number)
    upload_to = 'files'
    ext = filename.split('.')[-1]
    # get filename
    filename = '{}.{}'.format(instance.ar_number, ext)
    # return the whole path to the file
    return os.path.join(upload_to+'/'+folder+'/', filename)

class ApplicationFormModel(models.Model):
    community_choices = [
        ("OC", "OC"),
        ("BC", "BC"),
        ("MBC", "MBC"),
        ("SC", "SC"),
        ("SCA", "SCA"),
        ("ST", "ST"),
    ] 
    status_choices = [
        ("applied","applied"),
        ("discontinued","discontinued"),
        ("admitted","admitted"),
    ]
    community_choices = [
        ("OC", "OC"),
        ("BC", "BC"),
        ("MBC", "MBc"),
        ("SC", "SC"),
        ("SCA", "SCA"),
        ("ST", "ST"),
    ]    
    status= models.CharField(choices=status_choices,max_length=100,blank=True,null=True)
    #if status is discontinue then reason should be entered
    reason_to_discontinue = models.CharField(max_length=500,default='',blank=True)
    ar_number = models.AutoField(primary_key=True)
    email = models.CharField(max_length=500,default='',blank=True)
    student_name = models.CharField(max_length=500, default="", blank=True)
    course = models.CharField(max_length=200, default="", blank=True)
    date_of_birth = models.DateField(default=None, null=True, blank=True)
    course_type = models.CharField(max_length=200, default="",blank=True,null=True)
    aadhar_no = models.CharField(max_length=12, default="",blank=True)
    academic_year_start = models.CharField(max_length=4,default="",null=True,blank=True)
    academic_year_end = models.CharField(max_length=4,default="",null=True,blank=True)
    gender = models.CharField(max_length=100, default="", blank=True)
    is_hostellite = models.CharField(default=False, blank=True,max_length=200)
    community = models.CharField(
        max_length=20, choices=community_choices, default="", blank=True
    )
    religion = models.CharField(max_length=300, default="", blank=True)
    native_place = models.CharField(max_length=500, default="", blank=True)
    blood_group = models.CharField(max_length=30, default="", blank=True)
    height = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0, blank=True
    )
   
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0, blank=True
    )
    caste = models.CharField(max_length=300, default="", blank=True)    
    address_for_communication = models.CharField(
        max_length=5000, default="", blank=True
    )
    student_contact_no = models.CharField(max_length=50, default="", blank=True)
    mobile_1 = models.CharField(max_length=30,default = "",blank=True)
    mobile_2 = models.CharField(max_length=30,default = "",blank=True)
    mobile_3 = models.CharField(max_length=30,default = "",blank=True)
    date_of_admission = models.DateField(default=None, null=True, blank=True)
    address_local_guardian = models.CharField(max_length=5000, default="", blank=True)
    guardian_mobile = models.CharField(max_length=20, default="", blank=True)
    nationality = models.CharField(max_length=200, default="", blank=True)
    mother_tongue = models.CharField(max_length=300, default="", blank=True)
    quota = models.CharField(
        max_length=20, default="", blank=True
    )
    # 
    father_name = models.CharField(max_length=500, default="", blank=True)
    father_occupation = models.CharField(max_length=500, default="", blank=True)
    father_occupation_address = models.CharField(max_length=500, default="", blank=True)
    father_phone_number = models.CharField(max_length=20, default="", blank=True)
    father_email = models.EmailField(max_length=200, default="", blank=True)
    mother_name = models.CharField(max_length=500, default="", blank=True)
    mother_occupation = models.CharField(max_length=500, default="", blank=True)
    mother_occupation_address = models.CharField(max_length=500, default="", blank=True)
    mother_phone_number = models.CharField(max_length=20, default="", blank=True)
    mother_email = models.EmailField(max_length=200, default="", blank=True)
    #    
    hsc_register_no = models.CharField(max_length=100, default="", blank=True)
    board_of_study = models.CharField(
        max_length=30, default="", blank=True
    )
    hsc_year_of_passing = models.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(3000)],
        default=0,
        blank=True,
    )
    hsc_physics_mark = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
        default=0.0,
        blank=True,
    )
    hsc_chemistry_mark = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
        default=0.0,
        blank=True,
    )
    hsc_biology_mark = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
        default=0.0,
        blank=True,
    )
    hsc_total_mark = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
        default=0.0,
        blank=True,
    )
    hsc_marks_maximum = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
        default=0.0,
        blank=True,
    )
    pcb_percentage = models.DecimalField(
        max_digits=7,
        decimal_places=4,
        validators=[MinValueValidator(0)],
        default=0.0,
        blank=True,
    )
    # 
    neet_roll_no = models.CharField(max_length=200, default="", blank=True)
    neet_year = models.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(3000)],
        default=0,
        blank=True,
    )
    neet_study_center_name = models.CharField(max_length=500, blank=True, default="")
    no_of_neet_attempts = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)], default=0, blank=True
    )

    neet_air = models.IntegerField(
        validators=[MinValueValidator(0)], default=0, blank=True
    )
    selection_committee_allotment_order_no = models.CharField(
        max_length=500, default="", blank=True
    )
    selection_committee_general_rank = models.CharField(
        max_length=500, default="", blank=True
    )
    allotment_order_date = models.DateField(default=None, null=True, blank=True)

    neet_total_mark = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(720)], default=0, blank=True
    )
    neet_physics_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.0,
        blank=True,
    )
    neet_chemistry_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.0,
        blank=True,
    )
    neet_biology_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.0,
        blank=True,
    )
    neet_total_percentile = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0.0,
        blank=True,
    )
    student_photo = models.ImageField(upload_to=image_path_and_rename,null=True,blank=True)
    neet_score_card = models.FileField(upload_to=pdf_path_and_rename,null=True,blank=True)
    conduct_certificate = models.FileField(upload_to=pdf_path_and_rename,null=True,blank=True)
    neet_admit_card = models.FileField(upload_to=pdf_path_and_rename,null=True,blank=True)
    allotment_order_sslc_certificate = models.FileField(upload_to=pdf_path_and_rename,null=True,blank=True)
    hsc_certificate = models.FileField(upload_to=pdf_path_and_rename,null=True,blank=True)
    transfer_certificate = models.FileField(upload_to=pdf_path_and_rename,null=True,blank=True)
    community_certificate = models.FileField(upload_to=pdf_path_and_rename,null=True,blank=True)
    aadhaar_card = models.FileField(upload_to=pdf_path_and_rename,null=True,blank=True)
    eligibility_migration_certificates = models.FileField(upload_to=pdf_path_and_rename,null=True,blank=True)
    nativity_certificate = models.FileField(upload_to=pdf_path_and_rename,null=True,blank=True)
    income_certificate = models.FileField(upload_to=pdf_path_and_rename,null=True,blank=True)
    physical_fitness_certificate = models.FileField(upload_to=pdf_path_and_rename,null=True,blank=True)
    declaration_form = models.FileField(upload_to=pdf_path_and_rename,null=True,blank=True)
    anti_ragging_bond = models.FileField(upload_to=pdf_path_and_rename,null=True,blank=True)
    physically_handicapped_certificate = models.FileField(upload_to=pdf_path_and_rename,null=True,blank=True)

    def __str__(self):
        return self.email

