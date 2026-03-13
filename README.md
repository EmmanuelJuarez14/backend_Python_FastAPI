# **Tarea No. 3 - Backend de la practica 2**

## Nombres:
 - Gómez Tovar Yoshua Oziel🥇
 - Juarez Palma Emmanuel🥉
 - Zarco Sosa Kevin🥈
## Grupo:
 7CV4

# Backend Con Python y Fast-API

Este repositorio contiene la implementación de una aplicación móvil en Android (desarrollada en Kotlin) que consume una API REST local. El backend está construido con **Python y FastAPI**, y se encuentra dockerizado para facilitar su despliegue, cumpliendo con los requisitos del ciclo completo de comunicación HTTP.

##  Estructura del Proyecto

* **`Android/`**: Contiene el código fuente de la aplicación móvil (vistas, layouts y la capa de red configurada con Retrofit).
* **`Python_FastAPI/`**: Contiene la implementación del backend RESTful, la lógica de base de datos y el `Dockerfile`.

---

##  Requisitos Previos

Para compilar y ejecutar este proyecto necesitas:
1. **Docker Desktop** instalado y en ejecución.
2. **Android Studio** con un emulador configurado (API 24 o superior) o un dispositivo físico Android.
3. **Git** para clonar el proyecto.

---

## Instrucciones de Compilación y Ejecución

### 1. Levantar el Backend (FastAPI + Docker)

1. Abre una terminal y clona el repositorio:
   
   git clone [https://github.com/EmmanuelJuarez14/login_Android.git](https://github.com/EmmanuelJuarez14/login_Android.git)
   cd login_Android/Python_FastAPI
   
2.Construye la imagen y levanta el contenedor de Docker:
      docker build -t api-fastapi .
      docker run -p 8000:8000 api-fastapi

## 2. Ejecutar la Aplicación Android
1-.Abre Android Studio y selecciona Open.

2-.Navega y selecciona la carpeta Android/ de este repositorio.

3-.Espera a que Gradle sincronice las dependencias (Retrofit, Gson, etc.).

4-.Configuración de IP:

  -Si usas el Emulador de Android Studio: La URL base en el cliente Retrofit debe ser http://10.0.2.2:8000/.

  -Si usas un Dispositivo Físico: Asegúrate de estar en la misma red Wi-Fi y cambia la URL base a la IP de tu computadora.

5-.Presiona Run (Shift + F10) para compilar e instalar la app en tu emulador o dispositivo.

