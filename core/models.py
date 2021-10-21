# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acucares(models.Model):
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'acucares'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Nacionalidades(models.Model):
    NACIONALIDADES_CHOICES = (
        ('BRA', 'Brasil'),
        ('ARG', 'Argentina'),
        ('URU', 'Uruguai'),
        ('PAR', 'Paraguai'),
        ('CHI', 'Chile'),
        ('POR', 'Portugal'),
        ('ESP', 'Espanha'),
        ('FRA', 'França'),
        ('ITA', 'Itália'),
        ('AFS', 'África do Sul'),
        ('EUA', 'Estados Unidos'),
        ('AUS', 'Austrália'),
    )

    nome = models.CharField('nacionalidade', max_length=45, choices=NACIONALIDADES_CHOICES)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'nacionalidades'


class Tipos(models.Model):
    TIPOS_CHOICES = (
        ('TIN', 'Tinto'),
        ('ROS', 'Rose'),
        ('BRA', 'Branco'),
    )

    nome = models.CharField('tipo', max_length=45, choices=TIPOS_CHOICES)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'tipos'


class Uvas(models.Model):
    UVAS_CHOICES = (
        ('CAB', 'Cabernet Sauvignon'),
        ('CAF', 'Cabernet Franc'),
        ('MER', 'Merlot'),
        ('MLB', 'Malbec'),
        ('TAN', 'Tannat'),
        ('PIN', 'Pinot Noir'),
        ('CHA', 'Chardonnay'),
        ('RIE', 'Riesling'),
    )

    nome = models.CharField('uvas', max_length=45, choices=UVAS_CHOICES)

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'uvas'


class UvasVinhos(models.Model):
    percentual_uva = models.IntegerField()
    id_vinho = models.ForeignKey('Vinhos', models.DO_NOTHING, db_column='id_vinho')
    id_uva = models.ForeignKey(Uvas, models.DO_NOTHING, db_column='id_uva')

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'uvas_vinhos'


class Vinhos(models.Model):
    nome = models.CharField(max_length=45)
    safra = models.IntegerField()
    vinicola = models.CharField(max_length=45)
    alcool = models.DecimalField(max_digits=2, decimal_places=1)
    temperatura = models.IntegerField()
    volume = models.IntegerField()
    guarda = models.IntegerField()
    amadurecimento = models.CharField(max_length=256)
    visual = models.CharField(max_length=45)
    olfativo = models.CharField(max_length=512)
    gustativo = models.CharField(max_length=512)
    destaque = models.IntegerField()
    promocao = models.IntegerField()
    avaliacao = models.DecimalField(max_digits=1, decimal_places=1)
    numero_avaliacoes = models.IntegerField()
    maior_avaliacao = models.DecimalField(max_digits=1, decimal_places=1)
    ativo = models.IntegerField()
    data_criacao = models.DateField()
    data_atualizacao = models.DateField()
    id_tipo = models.ForeignKey(Tipos, models.DO_NOTHING, db_column='id_tipo')
    id_acucar = models.ForeignKey(Acucares, models.DO_NOTHING, db_column='id_acucar')
    id_uvas = models.ForeignKey(UvasVinhos, models.DO_NOTHING, db_column='id_uvas')
    id_nacionalidade = models.ForeignKey(Nacionalidades, models.DO_NOTHING, db_column='id_nacionalidade')

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'vinhos'
