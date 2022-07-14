from django.db import models

# Create your models here.

class Asignatura(models.Model):
    asignatura = models.CharField(max_length=100)
    
    def __str__(self):
        return self.asignatura

class Alumno(models.Model):
    rut = models.CharField(max_length=11)
    nombres = models.CharField(max_length=60)
    apPaterno = models.CharField(max_length=50)
    apMaterno = models.CharField(max_length=50)
    fNacimiento = models.DateField()
    sexos = [
        ('N', 'Sin especificación'),
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='N')
    imagen = models.ImageField(upload_to="alumnos", null=True)
    
    def __str__(self):
        return self.nombres


class Profesor(models.Model):
    rut = models.CharField(max_length=11)
    nombres = models.CharField(max_length=60)
    apPaterno = models.CharField(max_length=50)
    apMaterno = models.CharField(max_length=50)
    fNacimiento = models.DateField()
    sexos = [
        ('N', 'Sin especificación'),
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='N')

    def __str__(self):
        return self.nombres

class Curso(models.Model):
    curso = models.CharField(max_length=20)
    alumnos = models.ForeignKey(Alumno, null = False, blank = False, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, null = False, blank = False, on_delete=models.CASCADE)

    def __str__(self):
        return self.curso

class AulaComun(models.Model):
    asuntoAulaComun = models.CharField(max_length=250)
    fecha_aula= models.DateField(null=True)
    registroAula = models.TextField()

    def __str__(self):
        return self.registroAula

class ControlAsignatura(models.Model):
    asuntoControlasig= models.CharField(max_length=250)
    fecha_control= models.DateField(null=True)
    asignatura = models.ForeignKey(Asignatura, null = False, blank = False, on_delete=models.CASCADE)
    tareaAsignatura = models.TextField()

    def __str__(self):
        return self.tareaAsignatura

class Anotacion(models.Model):

    tipo_anotacion_choices=(
        ('Positiva',"Positiva"), ('Negativa', "Negativa")
    )

    alumnos = models.ForeignKey(Alumno, null = False, blank= False, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, null= False, blank= False, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, null= False, blank= False, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    tipo = models.CharField(max_length=20, choices=tipo_anotacion_choices, default='Positiva')
    anotacion = models.TextField()

    def __str__(self):
        return self.anotacion

    class Meta:
        ordering = ('-fecha',)

class Apoderado(models.Model):
    rut= models.CharField(max_length=11)
    nombres = models.CharField(max_length=60)
    apPaterno = models.CharField(max_length=50)
    apMaterno = models.CharField(max_length=50)
    fNacimiento = models.DateField()
    sexos = [
        ('N', 'Sin especificación'),
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ] 
    alumno = models.ForeignKey(Alumno, null = False, blank=False, on_delete=models.CASCADE)
    sexo = models.CharField(max_length=1, choices=sexos, default='N')
    correo = models.EmailField(null= False, unique=True)

    def __str__(self):
        return self.correo

class Comunicacion(models.Model):

    correo_status_choices=(
        ('N', "------------"),
        ('Editando', "Editando"),
        ('Publicado', "Publicado")
    )

    name=models.CharField(max_length=250)
    subject=models.CharField(max_length=250)
    body=models.TextField(blank=True, null=True)
    correo= models.ManyToManyField(Apoderado)
    created = models.DateTimeField(auto_now_add=True)

    status= models.CharField(max_length=10, choices=correo_status_choices, default='N')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created',)

class Calificaciones(models.Model):

    notas_choices=(
        ('-', "-----"),('N°1', "N°1"),('N°2', "N°2"),('N°3', "N°3"),
        ('N°4', "N°4"),('N°5', "N°5"),('N°6', "N°6"),('N°7', "N°7")
    )
    alumno = models.ForeignKey(Alumno, null = False, blank=False, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, null = False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    tipo=models.CharField(max_length=15, choices=notas_choices, default='-')
    nota= models.CharField(max_length=15)

    def __str__(self):
        return self.nota

    class Meta:
        ordering = ('-fecha',)

class asistencia(models.Model):
    estado_choices=(
        ('Presente', "Presente"), ('Ausente', "Ausente"),('Justificado', 'Justificado')
    )
    alumnos = models.ForeignKey(Alumno, null = False, blank=False, on_delete=models.CASCADE)
    fecha_asistencia = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=13, choices=estado_choices, default='Presente')
    justificacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.estado

    class Meta:
        ordering = ('-fecha_asistencia',)

