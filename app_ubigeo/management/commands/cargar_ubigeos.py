import csv
from django.core.management.base import BaseCommand
from django.db import IntegrityError

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
        file = open(options['ruta_del_archivo'], mode='r', encoding="utf-8")
        INPUT_HEAD = ['UBIGEO', 'DISTRITO', 'PROVINCIA', 'DEPARTAMENTO']
        reader = csv.DictReader(file, INPUT_HEAD, delimiter=options["delimitador"])
        next(reader)
        for line in reader:
            print('.', end='', flush = True)
            for k, v in line.items():
                line[k] = v.lower().strip()
            try:
                depar = Departamento.objects.create(nombre=line['DEPARTAMENTO'])
            except IntegrityError:
                depar = Departamento.objects.get(nombre=line['DEPARTAMENTO'])
            except:
                # print(e)
                print("*-*-*-*-*-*-*" + line)

            try:
                prov = Provincia.objects.create(nombre=line['PROVINCIA'], departamento_id=depar.id)
            except IntegrityError:
                prov = Provincia.objects.get(nombre=line['PROVINCIA'], departamento_id=depar.id)
            except:
                # print(e)
                print("*-*-*-*-*-*-*" + line)

            try:
                Distrito.objects.create(nombre=line['DISTRITO'], ubigeo=line['UBIGEO'], provincia_id=prov.id)
            except:
                print(line)
