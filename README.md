# Sistema de Gestión de Vacaciones

## Descripción

Este proyecto consiste en un Sistema de Gestión de Vacaciones desarrollado en Python para automatizar el proceso de solicitud de vacaciones de los empleados de una clínica privada.

El sistema permite:

* Consultar días de vacaciones disponibles.
* Registrar solicitudes de vacaciones.
* Consultar el estado de una solicitud.
* Validar datos ingresados por el usuario.
* Simular una base de datos mediante un archivo CSV.

## Estructura del Proyecto

```
proyecto/
│
├── main.py
├── empleados.csv
└── README.md
```

## Base de Datos

El sistema utiliza el archivo `empleados.csv` para almacenar la información de los empleados.

## Funcionalidades

### Consultar saldo

Permite visualizar la cantidad de días de vacaciones disponibles para un empleado.

### Solicitar vacaciones

Permite registrar una solicitud verificando previamente que existan días disponibles.

### Consultar estado

Permite visualizar el estado actual de una solicitud.

## Manejo de Errores

El sistema contempla:

* Legajos inexistentes.
* Ingreso de texto cuando se espera un número.
* Solicitudes con cantidad de días menor o igual a cero.
* Solicitudes superiores al saldo disponible.

## Integrantes

* Micaela Natali Villanueva
* Pilar Abrate

## Materia

Organización Empresarial

Tecnicatura Universitaria en Programación a Distancia (TUPaD) - Universidad Tecnológica Nacional.

