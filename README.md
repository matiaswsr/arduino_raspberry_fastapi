# 🔌 Raspberry Pi + Arduino UNO + FastAPI

## 📖 Descripción
Este proyecto fue desarrollado con el objetivo de demostrar el potencial del **hardware de bajo costo**, la integración entre sistemas embebidos y software moderno, y servir como punto de partida para que estudiantes, makers y desarrolladores se animen a experimentar, aprender e inventar soluciones reales.  

La solución integra un **Arduino UNO**, una **Raspberry Pi 3 Model B** y una **API REST desarrollada con FastAPI**, combinando electrónica, programación embebida y desarrollo backend profesional en una arquitectura clara, modular y extensible.  

El enfoque del proyecto no es únicamente funcional, sino también **didáctico y arquitectónico**, siguiendo buenas prácticas de desarrollo, separación de responsabilidades y escalabilidad.

---

## 🏗️ Arquitectura y concepto
La arquitectura se basa en una separación clara de roles:

- **Arduino UNO** ⚙️  
  - Lectura de sensores  
  - Control de actuadores  
  - Comunicación serial estructurada  

- **Raspberry Pi** 🖥️  
  - Ejecuta la API REST  
  - Gestiona la comunicación con Arduino  
  - Expone servicios al exterior  

- **FastAPI (Python)** 🐍  
  - Endpoints RESTful  
  - Manejo de errores centralizado  
  - CORS habilitado para frontend  
  - Arquitectura basada en routers y services  

Este diseño refleja una arquitectura similar a sistemas **IoT reales**, donde los dispositivos de bajo nivel no se exponen directamente a la red, sino que se integran a través de una capa intermedia segura y controlada.

---

## 🔧 Sensores y actuadores utilizados

### 💡 LED (Actuador)
Permite verificar:  
- Control remoto de hardware  
- Respuesta inmediata desde la API  
- Funcionamiento end-to-end (**API → Serial → Arduino → Hardware**)  

### 🌡️ Sensor DHT11 (Temperatura y Humedad)
Permite medir:  
- Temperatura ambiente  
- Humedad relativa  

Este sensor es ampliamente utilizado en proyectos IoT y domótica, y demuestra cómo exponer métricas físicas reales mediante una API HTTP.

### 📡 Sensor ultrasónico HC-SR04
Permite medir distancia mediante ultrasonido, útil en:  
- Detección de objetos  
- Sistemas de proximidad  
- Automatización y robótica básica  

La lectura de distancia es procesada en Arduino y expuesta por la API.

---

## 🔗 Importancia de la integración Arduino – Raspberry Pi – FastAPI
Este proyecto pone en evidencia un punto clave: **la integración es tan importante como el hardware o el software por separado**.

- Arduino es excelente para tiempo real y control directo de sensores.  
- Raspberry Pi permite ejecutar software complejo, redes y servicios.  
- FastAPI aporta estándares modernos de integración, escalabilidad y consumo por terceros.  

La combinación de estos tres elementos abre la puerta a:  
- Sistemas IoT reales  
- Prototipos industriales  
- Automatización  
- Integración con frontends web o móviles  
- Exposición de datos a la nube  

---

## 🖥️ Backend y APIs: una habilidad esencial hoy
En la actualidad, todo desarrollador backend debería ser capaz de diseñar e implementar APIs, incluso cuando el proyecto involucra hardware.  

Exponer dispositivos físicos a través de una API:  
- Permite desacoplar sistemas  
- Facilita la escalabilidad  
- Habilita múltiples consumidores (web, móvil, otros servicios)  
- Alinea proyectos embebidos con arquitecturas modernas  

Este proyecto demuestra cómo un sistema embebido puede convertirse en un servicio accesible, seguro y reutilizable.

---

## 🌍 Proyección hacia el mundo IoT
La arquitectura presentada es directamente extrapolable a escenarios IoT reales:  
- Sensores distribuidos  
- Gateways  
- APIs centralizadas  
- Integración con dashboards, alertas o machine learning  

A partir de esta base, es posible evolucionar hacia:  
- Autenticación y autorización  
- Persistencia de datos  
- Comunicación con la nube  
- Automatización avanzada  
- Control remoto en tiempo real  

---

## 🎯 Objetivo
El objetivo principal de este proyecto es motivar:  
- A aprender  
- A experimentar  
- A romper la barrera entre hardware y software  
- A construir soluciones propias  

No se trata solo de encender un LED o leer un sensor, sino de entender cómo todo se conecta, cómo se diseña una solución completa y cómo pequeñas ideas pueden escalar a sistemas reales.  

Este proyecto demuestra que, con herramientas accesibles, buenas prácticas y curiosidad, es posible construir sistemas potentes, profesionales y listos para el mundo real.

---

## 🛠️ Componentes involucrados
- Arduino UNO  
- Protoboard  
- LED estándar  
- Resistencia 220 Ω  
- Módulo con Sensor DHT11 (temperatura y humedad)  
- Sensor ultrasónico HC-SR04  
- Cables Dupont macho-macho

<img width="1569" height="753" alt="Diagrama" src="https://github.com/user-attachments/assets/3cf07e9e-cb96-4ef4-96eb-d6d1f112fcaa" />

![20260113_190944](https://github.com/user-attachments/assets/92332985-9095-448b-b623-e22e2cd41b6c)

![20260113_191000](https://github.com/user-attachments/assets/e34d0922-7336-43fd-9c54-8bb2019b2be1)

![conexiones](https://github.com/user-attachments/assets/5710ba0c-8183-4575-b521-d419e4022eca)

<img width="1041" height="615" alt="frontend_html" src="https://github.com/user-attachments/assets/51d34911-0656-4cf4-a9b8-72e23a5a0171" />






