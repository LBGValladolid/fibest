from django.db import models

from enum import Enum, unique

@unique
class Titulation(Enum):
    GRADO_ADE                               = (0, "Grado en Administración y Dirección de Empresas")
    GRADO_ARQUITECTURA                      = (1, "Grado en Arquitectura")
    GRADO_COMERCIO                          = (2, "Grado en Comercio")
    GRADO_CRIMINOLOGIA                      = (3, "Grado en Criminología")
    GRADO_DERECHO                           = (4, "Grado en Derecho")
    GRADO_ECONOMIA                          = (5, "Grado en Economía")
    GRADO_EDUCACION_INFANTIL                = (6, "Grado en Educación Infantil")
    GRADO_EDUCACION_PRIMARIA                = (7, "Grado en Educación Primaria")
    GRADO_EDUCACION_SOCIAL                  = (8, "Grado en Educación Social")
    GRADO_ENFERMERIA                        = (9, "Grado en Enfermería")
    GRADO_ENOLOGIA                          = (10, "Grado en Enología")
    GRADO_ESPAÑOL                           = (11, "Grado en Español: Lengua y literatura")
    GRADO_ESTADISTICA                       = (12, "Grado en Estadística")
    GRADO_ESTUDIOS_CLASICOS                 = (13, "Grado en Estudios Clásicos")
    GRADO_ESTUDIOS_INGLESES                 = (14, "Grado en Estudios Ingleses")
    GRADO_FILOSOFIA                         = (15, "Grado en Filosofía")
    GRADO_FINANZAS_BANCA_SEGUROS            = (16, "Grado en Finanzas, Banca y Seguros")
    GRADO_FISIOTERAPIA                      = (17, "Grado en Fisioterapia")
    GRADO_FUNDAMENTOS_ARQUITECTURA          = (18, "Grado en Fundamentos de Arquitectura")
    GRADO_FISICA                            = (19, "Grado en Física")
    GRADO_GEOGRAFIA_ORDENACION_TERRITORIO   = (20, "Grado en Geografía y Ordenación del Territorio")
    GRADO_HISTORIA                          = (21, "Grado en Historia")
    GRADO_HISTORIA_ARTE                     = (22, "Grado en Historia del Arte")
    GRADO_HISTORIA_CIENCIAS_MUSICA          = (23, "Grado en Historia y Ciencias de la Música")
    GRADO_INGENIERIA_AGRARIA_ENERGETICA     = (24, "Grado en Ingeniería Agraria y Energética")
    GRADO_INGENIERIA_AGRICOLA_MEDIO_RURAL   = (25, "Grado en Ingeniería Agrícola y del Medio Rural")
    GRADO_INGENIERIA_BIOMEDICA              = (26, "Grado en Ingeniería Biomédica")
    GRADO_INGENIERIA_ELECTRICA              = (27, "Grado en Ingeniería Eléctrica")
    GRADO_INGENIERIA_FORESTAL_MEDIO_NATURAL = (28, "Grado en Ingeniería Forestal y del Medio Natural")
    GRADO_INGENIERIA_FORESTAL_INDUSTRIAS    = (29, "Grado en Ingeniería Forestal: Industrias forestales")
    GRADO_INGENIERIA_INFORMATICA            = (30, "Grado en Ingeniería Informática")
    GRADO_INGENIERIA_MECANICA               = (31, "Grado en Ingeniería Mecánica")
    GRADO_INGENIERIA_QUIMICA                = (32, "Grado en Ingeniería Química")
    GRADO_INGENIERIA_ESPEC_TELECOMUNICACION = (33, "Grado en Ingeniería de Tecnologías Específicas de Telecomunicación")
    GRADO_INGENIERIA_TECNO_TELECOMUNICACION = (34, "Grado en Ingeniería de Tecnologías de Telecomunicación")
    GRADO_INGENIERIA_AGRARIAS_ALIMENTARIAS  = (35, "Grado en Ingeniería de las Industrias Agrarias y Alimentarias")
    GRADO_INGENIERIA_DISEÑO_INDUSTRIAL      = (36, "Grado en Ingeniería en Diseño Industrial y Desarrollo de Producto")
    GRADO_INGENIERIA_ELECTRONICA_INDUSTRIAL = (37, "Grado en Ingeniería en Electrónica Industrial y Automática")
    GRADO_INGENIERIA_ORGA_INDUSTRIAL        = (38, "Grado en Ingeniería en Organización Industrial")
    GRADO_INGENIERIA_TECNO_INDUSTRIALES     = (39, "Grado en Ingeniería en Tecnologías Industriales")
    GRADO_LENGUAS_MODERNAS_LITERATURA       = (40, "Grado en Lenguas Modernas y sus Literaturas")
    GRADO_LOGOPEDIA                         = (41, "Grado en Logopedia")
    GRADO_MARKETING_INVESTIGACION_MERCADOS  = (42, "Grado en Marketing e Investigación de Mercados")
    GRADO_MATEMATICAS                       = (43, "Grado en Matemáticas")
    GRADO_MEDICINA                          = (44, "Grado en Medicina")
    GRADO_NUTRICION_HUMANA_DIETETICA        = (45, "Grado en Nutrición Humana y Dietética")
    GRADO_OPTICA_OPTOMETRIA                 = (46, "Grado en Óptica y Optometría")
    GRADO_PERIODISMO                        = (47, "Grado en Periodismo")
    GRADO_PUBLICIDAD_RELACIONES_PUBLICAS    = (48, "Grado en Publicidad y Relaciones Públicas")
    GRADO_QUIMICA                           = (49, "Grado en Química")
    GRADO_RELACIONES_LABORALES_RR_HH        = (50, "Grado en Relaciones Laborales y Recursos Humanos")
    GRADO_TRABAJO_SOCIAL                    = (51, "Grado en Trabajo Social")
    GRADO_TRADUCCION_INTERPRETACION         = (52, "Grado en Traducción e Interpretación")
    GRADO_TURISMO                           = (53, "Grado en Turismo")
    PROGRAMA_CONJUNTO_AGRICOLA_FORESTAL     = (54, "Programa de Estudios Conjunto de Grado en Ingeniería Agrícola y del Medio Rural e Ingeniería Forestal y del Medio Natural")
    PROGRAMA_CONJUNTO_AGRICOLA_ALIMENTARIAS = (55, "Programa de Estudios Conjunto de Grado en Ingeniería Agrícola y del Medio Rural y Grado en Ingeniería de las Industrias Agrarias y Alimentarias")
    PROGRAMA_CONJUNTO_AGRARIAS_ENOLOGIA     = (56, "Programa de Estudios Conjunto de Grado en Ingeniería de las Industrias Agrarias y Alimentarias y Grado en Enología")
    PROGRAMA_CONJUNTO_DERECHO_ADE           = (57, "Programa de estudios conjunto de Grado en Derecho y Grado en Administración y Dirección de Empresas")
    PROGRAMA_CONJUNTO_INFANTIL_PRIMARIA     = (58, "Programa de estudios conjunto de Grado en Educación Infantil y Grado en Educación Primaria")
    PROGRAMA_CONJUNTO_ESTADISTICA_INFOR     = (59, "Programa de estudios conjunto de Grado en Estadística y Grado en Ingeniería Informática")
    PROGRAMA_CONJUNTO_FISICA_MATEMATICAS    = (60, "Programa de estudios conjunto de Grado en Física y Grado en Matemáticas")
    PROGRAMA_CONJUNTO_INFOR_MATEMATICAS     = (61, "Programa de estudios conjunto de Grado en Ingeniería Informática de Servicios y Aplicaciones y Grado en Matemáticas")
    PROGRAMA_CONJUNTO_TELECO_ADE            = (62, "Programa de estudios conjunto de Grado en Ingeniería de Tecnologías de Telecomunicación y Grado en Administración y Dirección de Empresas")
    PROGRAMA_CONJUNTO_PUBLICIDAD_TURISMO    = (63, "Programa de estudios conjunto de Grado en Publicidad y Relaciones Públicas y Grado en Turismo")
    PROGRAMA_CONJUNTO_RECURSOS_HUMANOS_ADE  = (64, "Programa de estudios conjunto de Grado en Relaciones Laborales y Recursos Humanos y Grado de Administración y Dirección de Empresas")

    @classmethod
    def get_titulations(en):
        return [(x.value[0],x.value[1]) for x in en]



class CV(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    dni = models.CharField(max_length=15)
    titulation = models.IntegerField(choices=Titulation.get_titulations())

    # TODO ACTIVIDADES

    cv = models.FileField()
    cover_letter = models.FileField()