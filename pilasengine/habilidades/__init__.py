# -*- encoding: utf-8 -*-
# pilas engine: un motor para hacer videojuegos
#
# Copyright 2010-2014 - Hugo Ruscitti
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)
#
# Website - http://www.pilas-engine.com.ar

from pilasengine.habilidades.habilidad import Habilidad
import difflib

class Habilidades(object):
    """Representa la forma de acceso y construcción de las habilidades.

    Esta clase representa el objeto creado por pilas que
    se puede acceder escribiendo ``pilas.habilidades``. Desde aquí
    se puede acceder a las habilidades pre-diseñadas de pilas y
    'enseñarselas' a los actores.

    Por ejemplo, para 'enseñar' una habilidad:

    >>> nave = pilas.actores.Nave()
    >>> nave.aprender(pilas.habilidades.Arrastrable)

    """

    def __init__(self):
        self.diccionario_de_habilidades = {
                "Arrastrable": self.Arrastrable,
                "SeMantieneEnPantalla": self.SeMantieneEnPantalla,
                "Habilidad": self.Habilidad,
                "SiempreEnElCentro": self.SiempreEnElCentro,
                "Arrastrable": self.Arrastrable,
                "AumentarConRueda": self.AumentarConRueda,
                "SeguirClicks": self.SeguirClicks,
                "SeguirAlMouse": self.SeguirAlMouse,
                "PuedeExplotar": self.PuedeExplotar,
                "PuedeExplotarConHumo": self.PuedeExplotarConHumo,
                "SeMantieneEnPantalla": self.SeMantieneEnPantalla,
                "RotarConMouse": self.RotarConMouse,
                "MirarAlActor": self.MirarAlActor,
                "MoverseConElTeclado": self.MoverseConElTeclado,
                "Imitar": self.Imitar,
                "RebotarComoCaja": self.RebotarComoCaja,
                "LimitadoABordesDePantalla": self.LimitadoABordesDePantalla,
                "RebotarComoPelota": self.RebotarComoPelota,
                "MoverseComoCoche": self.MoverseComoCoche,
                "EliminarseSiSaleDePantalla": self.EliminarseSiSaleDePantalla,
        }

        for k, v in self.diccionario_de_habilidades.items():
            self.diccionario_de_habilidades[k.lower()] = v

    def buscar_habilidad_por_nombre(self, nombre):
        nombre = nombre.lower()

        try:
            return self.diccionario_de_habilidades[nombre]
        except KeyError:
            posibilidades = self.diccionario_de_habilidades.keys()
            similar = difflib.get_close_matches(nombre, posibilidades)

            if similar:
                similar = similar[0]
                raise NameError("lo siento, no existe esa habilidad... quisiste decir '%s' ?" %(similar))
            else:
                raise NameError("li siento, no exista una habilidad con ese nombre...")

    @property
    def Habilidad(self):
        return self._referencia_habilidad('habilidad', 'Habilidad')

    @property
    def SiempreEnElCentro(self):
        return self._referencia_habilidad('siempre_en_el_centro',
                                          'SiempreEnElCentro')

    @property
    def Arrastrable(self):
        return self._referencia_habilidad('arrastrable', 'Arrastrable')

    @property
    def AumentarConRueda(self):
        return self._referencia_habilidad('aumentar_con_rueda',
                                          'AumentarConRueda')

    @property
    def SeguirClicks(self):
        return self._referencia_habilidad('seguir_clicks', 'SeguirClicks')

    @property
    def SeguirAlMouse(self):
        return self._referencia_habilidad('seguir_al_mouse', 'SeguirAlMouse')

    @property
    def PuedeExplotar(self):
        return self._referencia_habilidad('puede_explotar', 'PuedeExplotar')

    @property
    def PuedeExplotarConHumo(self):
        return self._referencia_habilidad('puede_explotar_con_humo',
                                          'PuedeExplotarConHumo')

    @property
    def SeMantieneEnPantalla(self):
        return self._referencia_habilidad('se_mantiene_en_pantalla',
                                          'SeMantieneEnPantalla')

    @property
    def RotarConMouse(self):
        return self._referencia_habilidad('rotar_con_mouse', 'RotarConMouse')

    @property
    def MirarAlActor(self):
        return self._referencia_habilidad('mirar_al_actor', 'MirarAlActor')

    @property
    def MoverseConElTeclado(self):
        return self._referencia_habilidad('moverse_con_el_teclado',
                                          'MoverseConElTeclado')

    @property
    def Imitar(self):
        return self._referencia_habilidad('imitar', 'Imitar')

    @property
    def RebotarComoCaja(self):
        return self._referencia_habilidad('rebotar_como_caja',
                                          'RebotarComoCaja')
    @property
    def LimitadoABordesDePantalla(self):
        return self._referencia_habilidad('limitado_a_bordes_de_pantalla',
                                          'LimitadoABordesDePantalla')

    @property
    def RebotarComoPelota(self):
        return self._referencia_habilidad('rebotar_como_pelota',
                                          'RebotarComoPelota')

    @property
    def MoverseComoCoche(self):
        return self._referencia_habilidad('moverse_como_coche',
                                          'MoverseComoCoche')

    @property
    def EliminarseSiSaleDePantalla(self):
        return self._referencia_habilidad('eliminarse_si_sale_de_pantalla',
                                          'EliminarseSiSaleDePantalla')

    @property
    def Disparar(self):
        return self._referencia_habilidad('disparar',
                                          'Disparar')

    def _referencia_habilidad(self, modulo, clase):
        import importlib
        referencia_a_modulo = importlib.import_module('pilasengine.habilidades.'
                                                      + modulo)
        referencia_a_clase = getattr(referencia_a_modulo, clase)
        return referencia_a_clase


class ProxyHabilidades(object):
    """Implementa un intermediario con todas las habilidades del Actor."""

    def __init__(self, habilidades):
        self.habilidades = habilidades

    def __getattr__(self, name):

        for habilidad in self.habilidades:
            if habilidad.__class__.__name__ == name:
                return habilidad

        raise Exception("El actor no tiene asignada la habilidad " +
                        name + ".\n No puede acceder mediante "
                        "actor.habilidades." + name)

    def __repr__(self):
        return '<Éste actor tiene {0} habilidades: {1}>'.format(
            str(len(self.habilidades)), str(self.habilidades))
