import csv

from django.core.management.base import BaseCommand

from app_ubigeo.models import Departamento, Provincia, Distrito


class Command(BaseCommand):
    help = """
    parameters: delimitador, ruta_del_archivo
    
    Ejemplo:
    python manage.py cargar_data "<delimitador>" "<ruta_del_archivo>"

    El archivo debe ser un CSV
    Las cabeceras que debe posee su archivo son: ['UBIGEO', 'DISTRITO', 'PROVINCIA', 'DEPARTAMENTO']
    """

    def add_arguments(self, parser):
        parser.add_argument('delimitador', type=str)
        parser.add_argument('ruta_del_archivo', type=str)

    def handle(self, *args, **options):
        Distrito.objects.all().delete()
        Provincia.objects.all().delete()
        Departamento.objects.all().delete()

        file = open(options['ruta_del_archivo'], mode='r')
        INPUT_HEAD = ['UBIGEO', 'DISTRITO', 'PROVINCIA', 'DEPARTAMENTO']
        reader = csv.DictReader(file, INPUT_HEAD, delimiter=options["delimitador"])
        for line in reader:
            print('.', end='', flush=True)
            for k, v in line.items():
                line[k] = v.lower().strip()
            try:
                depar = Departamento.objects.create(nombre=line['DEPARTAMENTO'])
            except:
                depar = Departamento.objects.get(nombre=line['DEPARTAMENTO'])

            try:
                prov = Provincia.objects.create(nombre=line['PROVINCIA'], departamento_id=depar.id)
            except:
                prov = Provincia.objects.get(nombre=line['PROVINCIA'], departamento_id=depar.id)

            Distrito.objects.create(nombre=line['DISTRITO'], ubigeo=line['UBIGEO'], provincia_id=prov.id)
