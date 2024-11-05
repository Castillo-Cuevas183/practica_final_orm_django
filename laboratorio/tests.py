from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Configuración inicial para las pruebas
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio de Prueba",
            ciudad="Ciudad de Prueba",
            pais="País de Prueba"
        )

    def test_laboratorio_data(self):
        # Verifica que los datos en Laboratorio coinciden con los creados en setUpTestData
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, "Laboratorio de Prueba")
        self.assertEqual(laboratorio.ciudad, "Ciudad de Prueba")
        self.assertEqual(laboratorio.pais, "País de Prueba")

    def test_listar_laboratorios_status_code(self):
        # Verifica que la URL de listado devuelva un HTTP 200
        url = reverse('listar_laboratorios')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_listar_laboratorios_usa_plantilla_correcta(self):
        # Verifica que la plantilla correcta se use y el contenido HTML sea el esperado
        url = reverse('listar_laboratorios')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'laboratorio/listar.html')
        self.assertContains(response, "Laboratorio de Prueba")
        self.assertContains(response, "Ciudad de Prueba")
        self.assertContains(response, "País de Prueba")
