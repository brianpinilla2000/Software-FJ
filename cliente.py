
# ============================================
# CLASE CLIENTE
# PROYECTO SOFTWARE FJ - UNAD
# ============================================

# Importamos la clase Entidad.
from entidades import Entidad

# Importamos las excepciones y funciones de registro.
from registros import (
    DatosInvalidosError,
    registrar_evento,
    registrar_error
)


class Cliente(Entidad):

    def __init__(self, identificador, nombre, correo, telefono):

        try:
            # Validamos el identificador.
            super().__init__(identificador)

            # Validamos el nombre.
            if not nombre or not nombre.strip():
                raise DatosInvalidosError(
                    "El nombre del cliente es obligatorio."
                )

            # Validamos el correo.
            if (
                not correo
                or "@" not in correo
                or "." not in correo
            ):
                raise DatosInvalidosError(
                    "El correo electrónico no es válido."
                )

            # Validamos el teléfono.
            if not telefono or not str(telefono).isdigit():
                raise DatosInvalidosError(
                    "El teléfono debe contener únicamente números."
                )

            # Encapsulamos los atributos.
            self._nombre = nombre
            self._correo = correo
            self._telefono = str(telefono)

            registrar_evento(
                f"Cliente registrado: {self._nombre}"
            )

        except DatosInvalidosError as error:
            registrar_error(
                f"Error al registrar cliente: {error}"
            )
            raise

        except Exception as error:
            registrar_error(
                f"Error inesperado al crear cliente: {error}"
            )
            raise

    # Propiedad del nombre.
    @property
    def nombre(self):
        return self._nombre

    # Propiedad del correo.
    @property
    def correo(self):
        return self._correo

    # Propiedad del teléfono.
    @property
    def telefono(self):
        return self._telefono

    # Método para describir el cliente.
    def describir(self):
        return (
            f"Cliente: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Telefono: {self.telefono}"
        )

