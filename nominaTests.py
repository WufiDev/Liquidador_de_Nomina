import unittest
from calcular_nomina import calcular_nomina

class TestCalculoNomina(unittest.TestCase):

    # Casos de Prueba Normales

    def test_ingreso_horas_extras_sin_comisiones(self):
        resultado = calcular_nomina(sueldo=2000000, dias_trabajados=30, horas_trabajadas=8, comisiones=0, horas_extras=10)
        self.assertGreater(resultado["total_devengado"], 2000000)
        self.assertEqual(resultado["deducciones_salud"], resultado["total_devengado"] * 0.04)
    
    def test_ingreso_comisiones_sin_horas_extras(self):
        resultado = calcular_nomina(sueldo=2000000, dias_trabajados=30, horas_trabajadas=8, comisiones=2500000, horas_extras=0)
        self.assertAlmostEqual(resultado["total_devengado"], 4500000, places=2)
    
    def test_ingreso_dias_trabajados_parciales(self):
        resultado = calcular_nomina(sueldo=2000000, dias_trabajados=15, horas_trabajadas=8, comisiones=0, horas_extras=0)
        self.assertAlmostEqual(resultado["total_devengado"], 1000000, places=2)

    def test_ingreso_todas_las_variables_estandar(self):
        resultado = calcular_nomina(sueldo=2000000, dias_trabajados=30, horas_trabajadas=8, comisiones=100000, horas_extras=5)
        self.assertGreater(resultado["total_devengado"], 2000000)
        self.assertGreater(resultado["nomina_final"], 1840000)
    
    def test_ingreso_sueldo_horas_sin_dias_trabajados(self):
        with self.assertRaises(ValueError):
            calcular_nomina(sueldo=2000000, dias_trabajados=0, horas_trabajadas=8, comisiones=0, horas_extras=40)

    def test_ingreso_solo_sueldo_dias_trabajados(self):
        resultado = calcular_nomina(sueldo=2000000, dias_trabajados=30, horas_trabajadas=8, comisiones=0, horas_extras=0)
        self.assertAlmostEqual(resultado["total_devengado"], 2000000, places=2)

    # Casos de Prueba Extraordinarios

    def test_sueldo_igual_4_smlv(self):
        resultado = calcular_nomina(sueldo=5200000, dias_trabajados=30, horas_trabajadas=8, comisiones=0, horas_extras=0)
        self.assertEqual(resultado["total_devengado"], 5200000)
        self.assertEqual(resultado["deducciones_salud"], 208000)

    def test_sueldo_mayor_4_smlv(self):
        resultado = calcular_nomina(sueldo=6000000, dias_trabajados=30, horas_trabajadas=8, comisiones=1000000, horas_extras=20)
        self.assertGreater(resultado["total_devengado"], 6000000)
        self.assertGreater(resultado["nomina_final"], 5200000)

    def test_menos_15_dias_trabajados(self):
        resultado = calcular_nomina(sueldo=2000000, dias_trabajados=10, horas_trabajadas=8, comisiones=0, horas_extras=0)
        self.assertAlmostEqual(resultado["total_devengado"], 666666.67, places=2)
        self.assertAlmostEqual(resultado["nomina_final"], 613333.33, places=2)

    def test_menos_8_horas_trabajadas(self):
        resultado = calcular_nomina(sueldo=2000000, dias_trabajados=30, horas_trabajadas=4, comisiones=0, horas_extras=0)
        self.assertGreater(resultado["total_devengado"], 2000000)
        self.assertEqual(resultado["deducciones_salud"], resultado["total_devengado"] * 0.04)

    def test_sueldo_extremadamente_alto(self):
        resultado = calcular_nomina(sueldo=13000000, dias_trabajados=30, horas_trabajadas=8, comisiones=0, horas_extras=0)
        self.assertEqual(resultado["total_devengado"], 13000000)
        self.assertEqual(resultado["deducciones_salud"], 520000)

    def test_comisiones_significativas(self):
        resultado = calcular_nomina(sueldo=2000000, dias_trabajados=30, horas_trabajadas=8, comisiones=2000000, horas_extras=0)
        self.assertEqual(resultado["total_devengado"], 4000000)
        self.assertEqual(resultado["nomina_final"], 3680000)

    # Casos de Prueba de Error

    def test_salario_cero(self):
        with self.assertRaises(ValueError):
            calcular_nomina(sueldo=0, dias_trabajados=30, horas_trabajadas=8, comisiones=0, horas_extras=0)

    def test_salario_negativo(self):
        with self.assertRaises(ValueError):
            calcular_nomina(sueldo=-1000000, dias_trabajados=30, horas_trabajadas=8, comisiones=0, horas_extras=0)

    def test_dias_trabajados_cero(self):
        with self.assertRaises(ValueError):
            calcular_nomina(sueldo=2000000, dias_trabajados=0, horas_trabajadas=8, comisiones=0, horas_extras=0)

    def test_dias_trabajados_negativo(self):
        with self.assertRaises(ValueError):
            calcular_nomina(sueldo=2000000, dias_trabajados=-5, horas_trabajadas=8, comisiones=0, horas_extras=0)

    def test_horas_trabajadas_negativas(self):
        with self.assertRaises(ValueError):
            calcular_nomina(sueldo=2000000, dias_trabajados=30, horas_trabajadas=-8, comisiones=0, horas_extras=0)

    def test_comisiones_negativas(self):
        with self.assertRaises(ValueError):
            calcular_nomina(sueldo=2000000, dias_trabajados=30, horas_trabajadas=8, comisiones=-500000, horas_extras=0)


if __name__ == '__main__':
    unittest.main()
