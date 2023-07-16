# Generated by Django 4.1 on 2023-07-16 03:20

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "es_administrador",
                    models.BooleanField(default=False, verbose_name="Administrador"),
                ),
                (
                    "es_alumno",
                    models.BooleanField(default=False, verbose_name="Alumno"),
                ),
                (
                    "es_empresa",
                    models.BooleanField(default=False, verbose_name="Empresa"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Alumno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("matricula", models.IntegerField()),
                ("nombre", models.CharField(default="", max_length=50)),
                ("apellido_paterno", models.CharField(default="", max_length=50)),
                ("apellido_materno", models.CharField(default="", max_length=50)),
                ("sexo", models.CharField(default="", max_length=20)),
                ("correo_personal", models.EmailField(default="", max_length=80)),
                ("correo_institucional", models.EmailField(default="", max_length=80)),
                ("telefono", models.CharField(max_length=20)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="ConfiguracionPaginas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("estado_paginas_alumnos", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Empresa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("razon_social", models.CharField(max_length=100)),
                ("rfc", models.CharField(max_length=20)),
                ("telefono_empresa", models.CharField(max_length=20)),
                ("titular", models.CharField(max_length=100)),
                ("cargo", models.CharField(max_length=100)),
                ("nombre_enlace", models.CharField(max_length=100)),
                ("telefono_enlace", models.CharField(max_length=20)),
                ("correo_enlace", models.EmailField(max_length=100)),
                ("correo", models.EmailField(max_length=100)),
                ("is_active", models.BooleanField(default=True)),
                ("calle", models.CharField(max_length=100)),
                ("numero", models.CharField(max_length=10)),
                ("colonia", models.CharField(max_length=100)),
                ("ciudad", models.CharField(max_length=100)),
                ("codigo_postal", models.CharField(max_length=10)),
                ("entidad", models.CharField(max_length=100)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Proceso",
            fields=[
                ("id_proceso", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="ProgramaEducativo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Proyecto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "periodo",
                    models.CharField(
                        choices=[
                            ("Enero-Abril", "Enero-Abril"),
                            ("Mayo-Agosto", "Mayo-Agosto"),
                            ("Septiembre-Diciembre", "Septiembre-Diciembre"),
                        ],
                        max_length=25,
                    ),
                ),
                ("año", models.IntegerField()),
                ("vacantes", models.IntegerField()),
                ("vacantes_disponibles", models.IntegerField()),
                (
                    "modalidad",
                    models.CharField(
                        choices=[
                            ("Presencial", "Presencial"),
                            ("Remoto", "Remoto"),
                            ("Mixta", "Mixta"),
                        ],
                        max_length=10,
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("objetivo", models.TextField()),
                ("justificacion", models.TextField()),
                ("asesor", models.CharField(max_length=100)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProyectoAlumno",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "alumno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.alumno",
                    ),
                ),
                (
                    "proyecto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="usuarios.proyecto",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="proyecto",
            name="alumnos",
            field=models.ManyToManyField(
                through="usuarios.ProyectoAlumno", to="usuarios.alumno"
            ),
        ),
        migrations.AddField(
            model_name="proyecto",
            name="id_empresa",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="usuarios.empresa"
            ),
        ),
        migrations.AddField(
            model_name="proyecto",
            name="id_proceso",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="usuarios.proceso"
            ),
        ),
        migrations.AddField(
            model_name="proyecto",
            name="id_programa_educativo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="usuarios.programaeducativo",
            ),
        ),
        migrations.AddField(
            model_name="alumno",
            name="programa_educativo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="usuarios.programaeducativo",
            ),
        ),
        migrations.AddField(
            model_name="alumno",
            name="proyectos",
            field=models.ManyToManyField(
                through="usuarios.ProyectoAlumno", to="usuarios.proyecto"
            ),
        ),
        migrations.AddField(
            model_name="alumno",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="Administrador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]