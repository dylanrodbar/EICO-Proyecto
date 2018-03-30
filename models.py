# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Calificacionxpublicacion(models.Model):
    publicacion_fk = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='publicacion_fk', blank=True, null=True)
    calificacion_fk = models.ForeignKey('TipoCalificacion', models.DO_NOTHING, db_column='calificacion_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calificacionxpublicacion'


class Comentario(models.Model):
    descripcion = models.TextField(blank=True, null=True)
    usuario_fk = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_fk', blank=True, null=True)
    publicacion_fk = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='publicacion_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comentario'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Evento(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    usuario_fk = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento'


class Formacion(models.Model):
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    tipo_formacion_fk = models.ForeignKey('TipoFormacion', models.DO_NOTHING, db_column='tipo_formacion_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formacion'


class Formacionxusuario(models.Model):
    usuario_fk = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_fk', blank=True, null=True)
    formacion_fk = models.ForeignKey(Formacion, models.DO_NOTHING, db_column='formacion_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formacionxusuario'


class Media(models.Model):
    link = models.TextField(blank=True, null=True)
    tipo_media_fk = models.ForeignKey('TipoMedia', models.DO_NOTHING, db_column='tipo_media_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media'


class Mediaxpublicacion(models.Model):
    publicacion_fk = models.ForeignKey('Publicacion', models.DO_NOTHING, db_column='publicacion_fk', blank=True, null=True)
    media_fk = models.ForeignKey(Media, models.DO_NOTHING, db_column='media_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mediaxpublicacion'


class Publicacion(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    usuario_fk = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publicacion'


class Servicio(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio'


class SitioInteres(models.Model):
    titulo = models.CharField(max_length=100, blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sitio_interes'


class TipoCalificacion(models.Model):
    nombre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_calificacion'


class TipoFormacion(models.Model):
    nombre = models.CharField(max_length=9, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_formacion'


class TipoMedia(models.Model):
    nombre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_media'


class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50, blank=True, null=True)
    contrasena = models.CharField(max_length=50, blank=True, null=True)
    tipo_usuario_fk = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='tipo_usuario_fk', blank=True, null=True)
    correo_electronico = models.CharField(max_length=40, blank=True, null=True)
    media_fk = models.ForeignKey(Media, models.DO_NOTHING, db_column='media_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
