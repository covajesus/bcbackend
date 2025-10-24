# Black Cat Hostal - Backend API

## 📋 Descripción

Backend/API REST desarrollado en Python con FastAPI para el sitio web **blackcathostal.com**. Este sistema proporciona servicios de autenticación, gestión de usuarios y control de roles para la plataforma del hostal.

## 🚀 Tecnologías Utilizadas

- **FastAPI** - Framework web moderno y de alto rendimiento para Python
- **SQLAlchemy** - ORM (Object-Relational Mapping) para Python
- **Pydantic** - Validación de datos usando anotaciones de tipos de Python
- **JWT (JSON Web Tokens)** - Para autenticación y autorización
- **BCrypt** - Para el hash seguro de contraseñas
- **Uvicorn** - Servidor ASGI de alto rendimiento
- **Python 3.12+** - Lenguaje de programación

## 📁 Estructura del Proyecto

```
bcbackend/
├── main.py                     # Punto de entrada principal de la aplicación
├── requirements.txt            # Dependencias del proyecto
├── README.md                   # Documentación del proyecto
└── app/
    └── backend/
        ├── auth/              # Módulos de autenticación
        │   ├── auth_user.py   # Lógica de autenticación de usuarios
        │   └── login_users.py # Procesamiento de login
        ├── classes/           # Clases de negocio
        │   ├── authentication_class.py  # Clase de autenticación
        │   ├── user_class.py           # Clase de usuario
        │   ├── rol_class.py            # Clase de roles
        │   ├── setting_class.py        # Clase de configuraciones
        │   └── helper_class.py         # Funciones auxiliares
        ├── db/               # Base de datos
        │   ├── database.py   # Configuración de la base de datos
        │   └── models.py     # Modelos de datos (User, Rol)
        ├── routers/          # Endpoints de la API
        │   ├── authentications.py  # Rutas de autenticación
        │   ├── users.py            # Rutas de usuarios
        │   └── rols.py             # Rutas de roles
        └── schemas.py        # Esquemas de validación Pydantic
```

## 🔧 Funcionalidades Principales

### 🔐 **Autenticación y Seguridad**
- Login con JWT tokens
- Hash seguro de contraseñas con BCrypt
- Recuperación de contraseñas
- Validación de tokens de acceso
- Control de sesiones

### 👥 **Gestión de Usuarios**
- Registro de nuevos usuarios
- Actualización de perfiles de usuario
- Listado y búsqueda de usuarios
- Supervisores y jerarquías
- Confirmación de email

### 🛡️ **Sistema de Roles**
- Creación y gestión de roles
- Asignación de roles a usuarios
- Control de permisos basado en roles
- Actualización de roles

## 🔌 API Endpoints

### **Autenticación** (`/api/authentications`)
- `POST /login` - Iniciar sesión
- `POST /recover_password` - Recuperar contraseña

### **Usuarios** (`/api/users`)
- `POST /` - Listar usuarios con filtros
- `POST /store` - Crear nuevo usuario
- `GET /edit/{id}` - Obtener usuario por ID
- `GET /refresh_password/{rut}` - Refrescar contraseña
- `POST /supervisors` - Obtener supervisores

### **Roles** (`/api/rols`)
- `GET /` - Listar todos los roles
- `POST /store` - Crear nuevo rol
- `GET /edit/{id}` - Obtener rol por ID
- `PATCH /update/{id}` - Actualizar rol
- `DELETE /delete/{id}` - Eliminar rol

## ⚙️ Instalación y Configuración

### **Prerrequisitos**
- Python 3.12 o superior
- pip (gestor de paquetes de Python)
- Base de datos compatible con SQLAlchemy

### **Instalación**

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/covajesus/bcbackend.git
   cd bcbackend
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # o
   venv\Scripts\activate     # Windows
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno**
   Las siguientes variables se configuran automáticamente en `main.py`:
   - `SECRET_KEY`: Clave secreta para JWT
   - `ALGORITHM`: Algoritmo de encriptación (HS256)

5. **Configurar base de datos**
   Editar `app/backend/db/database.py` con los datos de conexión a tu base de datos.

## 🚀 Ejecución

### **Desarrollo**
```bash
python main.py
```

### **Producción**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

La API estará disponible en:
- **Local**: `http://localhost:8000`
- **Documentación Swagger**: `http://localhost:8000/docs`
- **Documentación ReDoc**: `http://localhost:8000/redoc`

## 🔧 Configuración Avanzada

### **CORS (Cross-Origin Resource Sharing)**
Configurado para permitir conexiones desde:
- Todos los orígenes (`*`) en desarrollo
- `https://newerp-ghdegyc9cpcpc6gq.eastus-01.azurewebsites.net` en producción

### **Timeouts y Límites**
- **Keep-alive**: 30 minutos (1800 segundos)
- **Graceful shutdown**: 1 minuto (60 segundos)
- **Máximo de requests**: 500,000
- **Concurrencia máxima**: 500,000

## 🏗️ Arquitectura

Este backend sigue una arquitectura modular y escalable:

- **Routers**: Definen los endpoints y manejan las peticiones HTTP
- **Classes**: Contienen la lógica de negocio y operaciones con la base de datos
- **Schemas**: Validan y serializan los datos de entrada y salida
- **Models**: Definen la estructura de las tablas de la base de datos
- **Auth**: Manejan la autenticación y autorización

## 🔒 Seguridad

- **Contraseñas**: Hash con BCrypt (12 rounds)
- **JWT Tokens**: Firmados con HS256
- **CORS**: Configurado para orígenes específicos
- **Validación**: Pydantic para validación de datos de entrada
- **SQL Injection**: Protección a través de SQLAlchemy ORM

## 📝 Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto es privado y pertenece a Black Cat Hostal.

## 📞 Contacto

Para consultas sobre este backend, contactar al equipo de desarrollo de **blackcathostal.com**.

---

⚡ **Desarrollado con FastAPI para Black Cat Hostal** ⚡
